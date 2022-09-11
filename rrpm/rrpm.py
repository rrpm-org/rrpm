import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import questionary
from typer import Typer
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

from .presets.py import default_questions as py_q
from .presets.py.poetry import poetry
from .presets.py.pip import pip
from .presets.py.venv import venv
from .presets.js import React, NextJS, Vanilla
from .presets.js import React as ReactTS, NextJS as NextTS, Vanilla as VanillaTS
from .utils import (
    get_home_dir,
    get_domain,
    get_user_repo,
    is_domain,
    is_shorthand,
    get_all_dirs,
)
from .ext.loader import load_extension
from .config import Config

console = Console()
config = Config()
cli = Typer()

DOMAIN_REGEX = re.compile(r"([a-zA-Z0-9_-]+\.)?(.*)\.([a-zA-Z]+)")


@cli.command(help="Clone a remote repository to directory specified in config")
def get(url: str):
    if not is_domain(url) and not is_shorthand(url):
        console.print("[red]Invalid domain or shorthand![/]")
        return

    if is_domain(url):
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

    home_dir = get_home_dir()
    try:
        domain = get_domain(url)
    except IndexError:
        pass

    if is_shorthand(url):
        domain = "github.com"

    if not os.path.exists(home_dir):
        os.mkdir(home_dir)

    if not os.path.exists(os.path.join(home_dir, domain)):
        os.mkdir(os.path.join(home_dir, domain))

    for ext in config.config["extensions"]["hooks"]:
        try:
            load_extension(
                os.path.expandvars(
                    os.path.expanduser(config.config["root"]["ext_dir"])
                ),
                ext,
            ).pre_fetch(url)
        except Exception:
            console.print(f"[red]Exception occured in extension: {ext}[/]")
            console.print_exception()
            return
    if is_shorthand(url):
        url = "https://github.com/" + url

    try:
        user, repo = get_user_repo(url)
    except IndexError:
        console.print("[red]Cannot determine user/repository from given URL![/]")
        return

    user_dir = os.path.join(home_dir, domain, user)
    repo_dir = os.path.join(home_dir, domain, user, repo)

    if not os.path.exists(user_dir):
        os.mkdir(user_dir)

    if os.path.exists(repo_dir):
        console.print("[yellow]Repository is already cloned![/]")
        pull = questionary.confirm("Pull new commits instead?").ask()
        if pull:
            os.chdir(repo_dir)
            out = subprocess.run(["git", "pull"], capture_output=True, shell=True)
            if out.returncode == 0:
                console.print("[green]Successfully pulled new commits![/]")
                return
            else:
                console.print(
                    f"[red]Failed to pull updates with exit status {out.returncode}![/]"
                )
                return

    console.print(f"[green]Fetching repository from {url}[/]")
    out = subprocess.run(
        ["git", "clone", url, repo_dir], capture_output=True, shell=True
    )
    if out.returncode == 0:
        console.print(
            f"[green]Successfully cloned repository in github.com/{user}/{repo}[/]"
        )
    else:
        console.print(f"[red]Failed to clone with exit status {out.returncode}[/]")

    for ext in config.config["extensions"]["hooks"]:
        try:
            load_extension(
                os.path.expandvars(
                    os.path.expanduser(config.config["root"]["ext_dir"])
                ),
                ext,
            ).post_fetch(url)
        except Exception:
            console.print(f"[red]Exception occured in extension: {ext}[/]")
            console.print_exception()
            return


@cli.command(name="remove", help="Remove a cloned repository")
def remove(shorthand: str):
    if not is_shorthand(shorthand):
        console.print("[red]Invalid shorthand![/]")
        return

    home_dir = get_home_dir()

    if not os.path.exists(home_dir):
        os.mkdir(home_dir)
        console.print("[red]Repository does not exist![/]")
        return

    matches = []

    for domain in os.listdir(home_dir):
        if os.path.isdir(os.path.join(home_dir, domain)):
            for user in os.listdir(os.path.join(home_dir, domain)):
                if os.path.isdir(os.path.join(home_dir, domain, user)):
                    for repo in os.listdir(os.path.join(home_dir, domain, user)):
                        if repo == shorthand.split("/")[1] and os.path.isdir(
                            os.path.join(home_dir, domain, user, repo)
                        ):
                            matches.append(domain + "/" + user + "/" + repo)

    if matches != []:
        repo = questionary.select("Select Repository", choices=matches).ask()
        console.print(f"[yellow]Removing repository: '{repo}'[/]")
        try:
            shutil.rmtree(os.path.realpath(os.path.join(home_dir, repo)))
        except PermissionError as e:
            console.print("[red]Failed to remove repository: '{repo}'[/]")
            file = str(e).split("'")
            console.print(f"[red]Access denied to file: {file[1]}[/]")
            return
        console.print(f"[green]Successfully removed repository: '{repo}'[/]")
    else:
        console.print("[red]No matching repositories found![/]")


@cli.command(name="tree", help="List all cloned repositories and generated projects")
def tree():
    home_dir = get_home_dir()
    if os.path.exists(home_dir):
        console.print(f"[red]{home_dir}[/]")
        for host in os.listdir(home_dir):
            if not host == "." and not host == "..":
                console.print(f"  |- [blue]{host}[/]")
                if len(os.listdir(os.path.join(home_dir, host))) != 0:
                    if host == "github.com":
                        for user in os.listdir(os.path.join(home_dir, host)):
                            console.print(f"      |- [green]{user}[/]")
                            if len(os.listdir(os.path.join(home_dir, host, user))) != 0:
                                for repo in os.listdir(
                                    os.path.join(home_dir, host, user)
                                ):
                                    console.print(f"          |- [magenta]{repo}[/]")
                    else:
                        for repo in os.listdir(os.path.join(home_dir, host)):
                            console.print(f"      |- [green]{repo}[/]")


@cli.command(name="list")
def list_():
    total = 0
    table = Table(title="[green]List of Repositories[/]")
    table.add_column("[red]Site")
    table.add_column("[green]Repository")
    table.add_column("[blue]Owner")
    table.add_column("[magenta]Shorthand")
    for i in os.listdir(os.path.realpath(get_home_dir())):
        if os.path.isdir(os.path.realpath(os.path.join(get_home_dir(), i))):
            for j in os.listdir(os.path.realpath(os.path.join(get_home_dir(), i))):
                if os.path.isdir(os.path.realpath(os.path.join(get_home_dir(), i, j))):
                    for k in os.listdir(
                        os.path.realpath(os.path.join(get_home_dir(), i, j))
                    ):
                        if os.path.isdir(
                            os.path.realpath(os.path.join(get_home_dir(), i, j, k))
                        ):
                            table.add_row(
                                f"[red]{i}",
                                f"[green]{k}",
                                f"[blue]{j}",
                                f"[magenta]{j}/{k}[/]",
                            )
                            total += 1
    console.print(table)
    console.print(f"[green]Total Repositories: [/][blue]{total}[/]")


@cli.command(
    name="migrate", help="Migrate and import all repositories from another directory"
)
def migrate(path: Path):
    if not path.exists():
        console.print(f"[red]Directory: '{path}' doesn't exist![/]")
        return

    if not path.is_dir():
        console.print(f"[red]Path: '{path}' is not a directory![/]")
        return

    console.print(f"Importing projects from '{path}'...")
    console.print("[red]Warning: All your uncommited changes will be lost!")
    ignore = questionary.confirm("Continue").ask()
    if not ignore:
        return
    dirs = get_all_dirs(path)
    repos_filtered = []
    remotes = []
    for dir in dirs:
        if ".git" in str(dir).split("\\"):
            repo_list = str(dir).split("\\")
            repo_name = "\\".join(repo_list[: repo_list.index(".git")])
            if repo_name not in repos_filtered:
                repos_filtered.append(repo_name)
                console.print(f"[green]Found Repository in: {repo_name}")

    console.print(f"Total Repositories Found: {len(repos_filtered)}")
    for repo in repos_filtered:
        os.chdir(repo)
        out = subprocess.run(["git", "remote", "-v"], capture_output=True)
        if not out.stdout:
            repos_filtered.remove(repo)
            console.print(
                f"[red]Ignoring repository: {repo} as no remote is present[/]"
            )
        else:
            remote = out.stdout.decode().split("\n")[0].split("\t")[1].split(" ")[0]
            remotes.append(remote)
            repo_name = repo.split("\\")[-1]
            console.print(f"[green]Using remote: {remote} for repository: {repo_name}")

    for remote in remotes:
        get(remote)
        repo_name = repos_filtered[remotes.index(remote)].split("\\")[-1]
        console.print(f"[red]Deleting project: {repo_name}")
        try:
            shutil.rmtree(os.path.realpath(repos_filtered[remotes.index(remote)]))
        except PermissionError:
            console.print(
                f"[red]Warning: Failed to delete repository: {repo_name}: access denied![/]"
            )


@cli.command(help="Generate a project from any of the presets and/or its variations")
def create(name: str, src: bool = False):
    home = get_home_dir()
    exts = []
    base_choices = ["Python", "FastAPI", "Flask", "NodeJS", "React", "NextJS"]
    for ext in config.config["extensions"]["presets"]:
        try:
            ext_ = (
                load_extension(
                    os.path.expandvars(
                        os.path.expanduser(config.config["root"]["ext_dir"])
                    ),
                    ext,
                )
                .Preset()
                .name
            )
            exts.append({ext_: load_extension(config.config["root"]["ext_dir"], ext)})
            base_choices += [ext_]
        except Exception:
            try:
                if config.config["extensions"]["ignore_extension_load_error"] is True:
                    console.print(f"[red]Failed to load extension {ext}[/]")
                else:
                    console.print(f"[red]Failed to load extension {ext}[/]")
                    console.print_exception()
                    console.print(
                        "[red]To disable exitting the program, consider adding ignore_extension_load_error = true to your config file.[/]"
                    )
                    return
            except KeyError:
                console.print(f"[red]Failed to load extension {ext}[/]")
                console.print_exception()
                console.print(
                    "[red]To disable exitting the program, consider adding ignore_extension_load_error = true to your config file.[/]"
                )
                return
    prj_type = questionary.select(
        "Project Preset",
        choices=base_choices,
    ).ask()
    try:
        repository = questionary.select(
            "Repository", choices=os.listdir(home) + ["Other"]
        ).ask()
    except FileNotFoundError:
        console.print("Invalid directory specified in config")
        return
    if repository == "Other":
        repository = questionary.text("Enter Domain(without 'https://'): ").ask()
        if DOMAIN_REGEX.match(repository) is None:
            console.print("[red]Invalid repository![/]")
            return
        os.mkdir(os.path.join(home, repository))
    if repository == "github.com":
        if not os.path.exists(os.path.join(home, repository)):
            os.mkdir(os.path.join(home, repository))
        user = questionary.select(
            "GitHub Username",
            choices=os.listdir(os.path.join(home, "github.com")) + ["Other"],
        ).ask()
        if user == "Other":
            user = questionary.text("Enter Username: ").ask()
        repository = os.path.join(repository, user)
    if prj_type in ["Python", "FastAPI", "Flask"]:
        env = py_q()
        if env == "Poetry":
            poetry(repository, name, src)
        elif env == "Pip":
            pip(repository, name)
        elif env == "Virtual Environment":
            venv(repository, name)
        else:
            console.print("[red]Invalid package manager selected[/]")
    elif prj_type in ["NodeJS", "React", "NextJS"]:
        ts = questionary.confirm("Use TypeScript").ask()
        if ts:
            if prj_type == "NodeJS":
                preset = VanillaTS(repository, name)
                pms = {man.name: man for man in preset.package_managers}
                pm = questionary.select("Package Manager", choices=pms.keys()).ask()
                if not pm or not repository or not name:
                    return
                preset.generate(pms.get(pm))
            elif prj_type == "React":
                preset = ReactTS(repository, name)
                pms = {man.name: man for man in preset.package_managers}
                pm = questionary.select("Package Manager", choices=pms.keys()).ask()
                if not pm or not repository or not name:
                    return
                preset.generate(pms.get(pm))
            elif prj_type == "NodeJS":
                preset = NextTS(repository, name)
                pms = {man.name: man for man in preset.package_managers}
                pm = questionary.select("Package Manager", choices=pms.keys()).ask()
                if not pm or not repository or not name:
                    return
                preset.generate(pms.get(pm))
        else:
            if prj_type == "NodeJS":
                preset = Vanilla(repository, name)
                pms = {man.name: man for man in preset.package_managers}
                pm = questionary.select("Package Manager", choices=pms.keys()).ask()
                if not pm or not repository or not name:
                    return
                preset.generate(pms.get(pm))
            elif prj_type == "React":
                preset = React(repository, name)
                pms = {man.name: man for man in preset.package_managers}
                pm = questionary.select("Package Manager", choices=pms.keys()).ask()
                if not pm or not repository or not name:
                    return
                preset.generate(pms.get(pm))
            elif prj_type == "NodeJS":
                preset = NextJS(repository, name)
                pms = {man.name: man for man in preset.package_managers}
                pm = questionary.select("Package Manager", choices=pms.keys()).ask()
                if not pm or not repository or not name:
                    return
                preset.generate(pms.get(pm))
    else:
        for ext in exts:
            if ext.get(prj_type) is not None:
                try:
                    ext[prj_type].Preset().on_select(repository, name)
                except Exception:
                    console.print(
                        f"[red]Exception occured in extension: {ext[prj_type].__file__}[/]"
                    )
                    console.print_exception()
                    return
                break


@cli.command(name="config", help="View current config file or regenerate config file")
def view_config(regenerate: bool = False, generate: bool = False):
    if generate is True:
        if sys.platform.lower().startswith("win"):
            CONFIG = {
                "root": {
                    "dir": "%USERPROFILE%\\Projects",
                    "ext_dir": "%LOCALAPPDATA%\\rrpm\\extensions",
                },
                "cli": {
                    "display_output": False,
                    "ignore_extension_load_error": False,
                },
                "extensions": {"presets": [], "hooks": []},
            }
        else:
            CONFIG = {
                "root": {
                    "dir": "~/Projects",
                    "exts_dir": "~/.config/rrpm/extensions",
                },
                "cli": {
                    "display_output": False,
                    "ignore_extension_load_error": False,
                },
                "extensions": {"presets": [], "hooks": []},
            }
        root_dir = questionary.path(
            "Root Project Directory", CONFIG["root"]["dir"]
        ).ask()
        ext_dir = questionary.path(
            "Extensions Directory", CONFIG["root"]["ext_dir"]
        ).ask()
        output = questionary.confirm(
            "Display raw git command output", CONFIG["cli"]["display_output"]
        ).ask()
        ignore_error = questionary.confirm(
            "Ignore extension load errors", CONFIG["cli"]["ignore_extension_load_error"]
        ).ask()
        CONFIG["root"]["dir"] = os.path.realpath(
            os.path.expandvars(os.path.expanduser(root_dir))
        )
        CONFIG["root"]["ext_dir"] = os.path.realpath(
            os.path.expandvars(os.path.expanduser(ext_dir))
        )
        CONFIG["cli"]["display_output"] = output
        CONFIG["cli"]["ignore_extension_load_error"] = ignore_error
        config.generate(CONFIG)
        console.print("[green]Successfully saved new config![/]")
        return

    if regenerate is True:
        config.regenerate()
        console.print("[green]Config file regenerated successfully![/]")
    else:
        configstring = json.dumps(config.config, indent=2)
        md = f"```json\n{configstring}\n```"
        console.print(Markdown(md))


if __name__ == "__main__":
    cli()
