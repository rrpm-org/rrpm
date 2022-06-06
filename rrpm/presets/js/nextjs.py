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
        console.print(f"[red]Project already exists![/]")
        return
    os.mkdir(os.path.join(home, repository, name))
    console.print(
        f"[green]Creating project with create-next-app, JavaScript and NPM[/]"
    )
    if config.config["cli"]["display_output"]:
        subprocess.run(
            ["npx", "create-next-app@latest", name],
            shell=True,
        )
    else:
        subprocess.run(
            ["npx", "create-next-app@latest", name],
            shell=True,
            capture_output=True,
        )
    return


def yarn(repository: str, name: str):
    if os.path.exists(os.path.join(home, repository, name)):
        console.print(f"[red]Project already exists![/]")
        return
    os.mkdir(os.path.join(home, repository, name))
    console.print(
        f"[green]Creating project with create-next-app, JavaScript and Yarn[/]"
    )
    if config.config["cli"]["display_output"]:
        subprocess.run(
            ["yarn", "create", "next-app", name],
            shell=True,
        )
    else:
        subprocess.run(
            ["yarn", "create", "next-app", name],
            shell=True,
            capture_output=True,
        )
    return


def pnpm(repository: str, name: str):
    if os.path.exists(os.path.join(home, repository, name)):
        console.print(f"[red]Project already exists![/]")
        return
    os.mkdir(os.path.join(home, repository, name))
    console.print(
        f"[green]Creating project with create-next-app, JavaScript and Pnpm[/]"
    )
    if config.config["cli"]["display_output"]:
        subprocess.run(
            ["pnpm", "create", "next-app", name],
            shell=True,
        )
    else:
        subprocess.run(
            ["pnpm", "create", "next-app", name],
            shell=True,
            capture_output=True,
        )
    return
