import os
import subprocess
from rich.console import Console
from .. import get_home_dir
from .. import Config

console = Console()
config = Config()
home = get_home_dir()


def npm(repository: str, name: str):
    if os.path.exists(os.path.join(home, repository, name)):
        console.print("[red]Project already exists![/]")
        return
    os.mkdir(os.path.join(home, repository, name))
    os.chdir(os.path.join(home, repository, name))
    console.print(
        "[green]Creating project with NPM, and JavaScript[/]"
    )
    if config.config["cli"]["display_output"]:
        subprocess.run(
            ["npm", "init"],
            shell=True,
        )
    else:
        subprocess.run(
            ["npm", "init"],
            shell=True,
            capture_output=True,
        )
    return


def yarn(repository: str, name: str):
    if os.path.exists(os.path.join(home, repository, name)):
        console.print("[red]Project already exists![/]")
        return
    os.mkdir(os.path.join(home, repository, name))
    os.chdir(os.path.join(home, repository, name))
    console.print(
        "[green]Creating project with NPM, and JavaScript[/]"
    )
    if config.config["cli"]["display_output"]:
        subprocess.run(
            ["yarn", "init"],
            shell=True,
        )
    else:
        subprocess.run(
            ["yarn", "init"],
            shell=True,
            capture_output=True,
        )
    return


def pnpm(repository: str, name: str):
    if os.path.exists(os.path.join(home, repository, name)):
        console.print("[red]Project already exists![/]")
        return
    os.mkdir(os.path.join(home, repository, name))
    os.chdir(os.path.join(home, repository, name))
    console.print(
        "[green]Creating project with NPM, and JavaScript[/]"
    )
    if config.config["cli"]["display_output"]:
        subprocess.run(
            ["pnpm", "init"],
            shell=True,
        )
    else:
        subprocess.run(
            ["pnpm", "init"],
            shell=True,
            capture_output=True,
        )
    return
