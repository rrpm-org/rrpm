import os
import subprocess
import questionary
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
    console.print("[green]Creating project with NPM, and JavaScript[/]")
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
    ts = questionary.confirm("Install TypeScript Globally?")
    ts_node = questionary.confirm("Install ts-node?")
    if config.config["cli"]["display_output"]:
        if ts:
            subprocess.run(["npm", "install", "--global", "typescript"], shell=True)
        else:
            subprocess.run(["npm", "install", "--save-dev", "typescript"], shell=True)
        if ts_node:
            subprocess.run(["npm", "install", "--global", "ts-node"], shell=True)
    else:
        if ts:
            subprocess.run(
                ["npm", "install", "--global", "typescript"],
                shell=True,
                capture_output=True,
            )
        else:
            subprocess.run(
                ["npm", "install", "--save-dev", "typescript"],
                shell=True,
                capture_output=True,
            )
        if ts_node:
            subprocess.run(["npm", "install", "--global", "ts-node"], shell=True)
    return


def yarn(repository: str, name: str):
    if os.path.exists(os.path.join(home, repository, name)):
        console.print("[red]Project already exists![/]")
        return
    os.mkdir(os.path.join(home, repository, name))
    os.chdir(os.path.join(home, repository, name))
    console.print("[green]Creating project with NPM, and JavaScript[/]")
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
    ts = questionary.confirm("Install TypeScript Globally?")
    ts_node = questionary.confirm("Install ts-node?")
    if config.config["cli"]["display_output"]:
        if ts:
            subprocess.run(["yarn", "global", "add", "typescript"], shell=True)
        else:
            subprocess.run(["yarn", "add", "--dev", "typescript"], shell=True)
        if ts_node:
            subprocess.run(["yarn", "global", "add", "ts-node"], shell=True)
    else:
        if ts:
            subprocess.run(
                ["yarn", "global", "add", "typescript"], shell=True, capture_output=True
            )
        else:
            subprocess.run(
                ["yarn", "add", "--dev", "typescript"], shell=True, capture_output=True
            )
        if ts_node:
            subprocess.run(["yarn", "global", "add", "ts-node"], shell=True)
    return


def pnpm(repository: str, name: str):
    if os.path.exists(os.path.join(home, repository, name)):
        console.print("[red]Project already exists![/]")
        return
    os.mkdir(os.path.join(home, repository, name))
    os.chdir(os.path.join(home, repository, name))
    console.print("[green]Creating project with NPM, and JavaScript[/]")
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
    ts = questionary.confirm("Install TypeScript Globally?")
    ts_node = questionary.confirm("Install ts-node?")
    if config.config["cli"]["display_output"]:
        if ts:
            subprocess.run(["pnpm", "add", "--global", "typescript"], shell=True)
        else:
            subprocess.run(["pnpm", "add", "--save-dev", "typescript"], shell=True)
        if ts_node:
            subprocess.run(["pnpm", "add", "--global", "ts-node"], shell=True)
    else:
        if ts:
            subprocess.run(
                ["pnpm", "add", "--global", "typescript"],
                shell=True,
                capture_output=True,
            )
        else:
            subprocess.run(
                ["pnpm", "add", "--save-dev", "typescript"],
                shell=True,
                capture_output=True,
            )
        if ts_node:
            subprocess.run(["pnpm", "add", "--global", "ts-node"], shell=True)
    return
