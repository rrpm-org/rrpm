import os
import re
import subprocess

import questionary
from typer import Typer
from rich.console import Console

from .presets.py import default_questions as py_q
from .presets.py.poetry import poetry
from .presets.py.pip import pip
from .presets.py.venv import venv
from .presets.js import default_questions as js_q
from .presets.js.react import npm as rjnpm, yarn as rjyarn, pnpm as rjpnpm
from .presets.ts.react import npm as rtnpm, yarn as rtyarn, pnpm as rtpnpm
from .presets.js.nextjs import npm as njjnpm, yarn as njjyarn, pnpm as njjpnpm
from .presets.ts.nextjs import npm as njtnpm, yarn as njtyarn, pnpm as njtpnpm
from .presets.js.node import npm as njnpm, yarn as njyarn, pnpm as njpnpm
from .presets.ts.node import npm as ntnpm, yarn as ntyarn, pnpm as ntpnpm
from .utils import get_home_dir, get_domain, is_github_url, get_github_user_repo
from .config import Config

console = Console()
config = Config()
cli = Typer()

DOMAIN_REGEX = re.compile(r"([a-zA-Z0-9_-]+\.)?(.*)\.([a-zA-Z]+)")

pm_cmd = {
    "nextjs": {
        "TypeScript": {
            "NPM": ["npx", "create-next-app@latest", "--ts"],
            "Yarn": ["yarn", "create", "next-app", "--typescript"],
            "Pnpm": ["pnpm", "create", "next-app", "--", "--ts"],
        },
        "JavaScript": {
            "NPM": ["npx", "create-next-app@latest"],
            "Yarn": ["yarn", "create", "next-app"],
            "Pnpm": ["pnpm", "create", "next-app"],
        },
    },
}


@cli.command(help="Clone a remote repository to directory specified in config")
def get(url: str):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    home_dir = get_home_dir()
    domain = get_domain(url)

    if not os.path.exists(home_dir):
        os.mkdir(home_dir)

    if not os.path.exists(os.path.join(home_dir, domain)):
        os.mkdir(os.path.join(home_dir, domain))

    if is_github_url(url):
        username, reponame = get_github_user_repo(url)
        user_dir = os.path.join(home_dir, "github.com", username)
        repo_dir = os.path.join(home_dir, "github.com", username, reponame)
        if os.path.exists(repo_dir):
            console.print("[red]Repo already exists[/]")
            return
        if not os.path.exists(user_dir):
            os.mkdir(user_dir)
            console.print(f"[green]Fetching GitHub Repository[/]")
            if config.config["cli"]["displayOutput"] is True:
                out = subprocess.run(["git", "clone", url, repo_dir])
            else:
                out = subprocess.run(
                    ["git", "clone", url, repo_dir], capture_output=True
                )
            if out.returncode == 0:
                console.print(
                    f"[green]Successfully cloned repository in github.com/{username}/{reponame}[/]"
                )
            else:
                console.print(
                    f"[red]Failed to clone with exit status {out.returncode}[/]"
                )
        else:
            console.print(f"[green]Fetching GitHub Repository[/]")
            if config.config["cli"]["displayOutput"] is True:
                out = subprocess.run(["git", "clone", url, repo_dir])
            else:
                out = subprocess.run(
                    ["git", "clone", url, repo_dir], capture_output=True
                )
            if out.returncode == 0:
                console.print(
                    f"[green]Successfully cloned repository in github.com/{username}/{reponame}[/]"
                )
            else:
                console.print(
                    f"[red]Failed to clone with exit status {out.returncode}[/]"
                )
    else:
        console.print(f"[green]Fetching {domain}[/]")
        if config.config["cli"]["displayOutput"] is True:
            out = subprocess.run(["git", "clone", url, os.path.join(home_dir, domain)])
        else:
            out = subprocess.run(
                ["git", "clone", url, os.path.join(home_dir, domain)],
                capture_output=True,
            )
        if out.returncode == 0:
            console.print(f"[green]Successfully cloned repository in {domain}[/]")
        elif out.returncode == 128:
            console.print(f"[red]Repository already exists[/]")
        else:
            console.print(f"[red]Failed to clone with exit status {out.returncode}[/]")


@cli.command(name="list", help="List all cloned repositories and generated projects")
def list_():
    home_dir = get_home_dir()
    if os.path.exists(home_dir):
        console.print(f"[red]{home_dir}[/]")
        for host in os.listdir(home_dir):
            if not host == "." and not host == "..":
                console.print(f"  |- [blue]{host}[/]")
                # console.log(os.listdir(os.path.join(home_dir, host)))
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


@cli.command(help="Generate a project from any of the presets and/or its variations")
def create(name: str, src: bool = False):
    home = get_home_dir()
    prj_type = questionary.select(
        "Project Preset",
        choices=["Python", "FastAPI", "Flask", "NodeJS", "React", "NextJS"],
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
            console.print(f"[red]Invalid repository![/]")
            return
        os.mkdir(os.path.join(home, repository))
    if repository == "github.com":
        if not os.path.exists(os.path.join(home, repository)):
            os.mkdir(os.path.join(home, repository))
        user = questionary.select(
            "GitHub Username",
            choices=os.listdir(os.path.join(home, "github.com"))
                    + ["Other"],
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
            venv()
        else:
            console.print("[red]Invalid package manager selected[/]")
    else:
        lang, pkg = js_q()
        if lang == "TypeScript":
            if prj_type == "React":
                if pkg == "NPM":
                    rtnpm(repository, name)
                elif pkg == "Yarn":
                    rtyarn(repository, name)
                else:
                    rtpnpm(repository, name)
            elif prj_type == "NextJS":
                if pkg == "NPM":
                    njtnpm(repository, name)
                elif pkg == "Yarn":
                    njtyarn(repository, name)
                else:
                    njtpnpm(repository, name)
            elif prj_type == "NodeJS":
                if pkg == "NPM":
                    ntnpm()
                elif pkg == "Yarn":
                    ntyarn()
                else:
                    ntpnpm()
        else:
            if prj_type == "React":
                if pkg == "NPM":
                    rjnpm(repository, name)
                elif pkg == "Yarn":
                    rjyarn(repository, name)
                else:
                    rjpnpm(repository, name)
            elif prj_type == "NextJS":
                if pkg == "NPM":
                    njjnpm(repository, name)
                elif pkg == "Yarn":
                    njjyarn(repository, name)
                else:
                    njjpnpm(repository, name)
            elif prj_type == "NodeJS":
                if pkg == "NPM":
                    njnpm()
                elif pkg == "Yarn":
                    njyarn()
                else:
                    njpnpm()


if __name__ == "__main__":
    cli()
