import os
import sys
import shutil
import subprocess
from rich.console import Console
from .. import get_home_dir

console = Console()


def poetry(repository: str, name: str, src: bool = False):
    home = get_home_dir()
    if shutil.which("poetry") is None:
        console.print(f"[red]Poetry not found![/]")
        sys.exit(1)

    console.print(f"[green]Creating project with Poetry[/]")
    if not os.path.exists(home):
        os.mkdir(home)
    if os.path.exists(os.path.join(home, repository, name)):
        console.print(f"[red]Project already exists![/]")
        sys.exit(1)
    os.chdir(os.path.join(home, repository))
    if src:
        subprocess.run(
            [
                "poetry",
                "new",
                os.path.join(home, repository, name),
                "--name",
                name,
                "--src",
            ],
            shell=True,
        )
    else:
        subprocess.run(
            [
                "poetry",
                "new",
                os.path.join(home, repository, name),
                "--name",
                name,
            ],
            shell=True,
        )
