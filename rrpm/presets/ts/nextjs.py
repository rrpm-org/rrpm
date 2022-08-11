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
    console.print("[green]Creating project with create-next-app, TypeScript and NPM[/]")
    if config.config["cli"]["display_output"]:
        subprocess.run(
            ["npx", "create-next-app@latest", name, "--ts"],
            shell=True,
        )
    else:
        subprocess.run(
            ["npx", "create-next-app@latest", name, "--ts"],
            shell=True,
            capture_output=True,
        )
    return


def yarn(repository: str, name: str):
    if os.path.exists(os.path.join(home, repository, name)):
        console.print("[red]Project already exists![/]")
        return
    os.mkdir(os.path.join(home, repository, name))
    console.print(
        "[green]Creating project with create-next-app, TypeScript and Yarn[/]"
    )
    if config.config["cli"]["display_output"]:
        subprocess.run(
            ["yarn", "create", "next-app", name, "--typescript"],
            shell=True,
        )
    else:
        subprocess.run(
            ["yarn", "create", "next-app", name, "--typescript"],
            shell=True,
            capture_output=True,
        )
    return


def pnpm(repository: str, name: str):
    if os.path.exists(os.path.join(home, repository, name)):
        console.print("[red]Project already exists![/]")
        return
    os.mkdir(os.path.join(home, repository, name))
    console.print(
        "[green]Creating project with create-next-app, TypeScript and Pnpm[/]"
    )
    if config.config["cli"]["display_output"]:
        subprocess.run(
            ["pnpm", "create", "next-app", name, "--", "--ts"],
            shell=True,
        )
    else:
        subprocess.run(
            ["pnpm", "create", "next-app", name, "--", "--ts"],
            shell=True,
            capture_output=True,
        )
    return
