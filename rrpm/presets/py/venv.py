import getpass
import os
import shutil
import subprocess
import sys
import time

import questionary
from rich.console import Console
from rich.progress import Progress
from .. import Config, get_home_dir

console = Console()
config = Config()
home = get_home_dir()


def venv(repository, name):
    if os.path.exists(os.path.join(home, repository, name)):
        console.print("[red]Project already exists![/]")
        return
    if shutil.which("virtualenv") is None:
        console.print("[red]virtualenv is not installed![/]")
        install = questionary.confirm(
            "Install virtualenv? Select No if it is accessible as python -m virtualenv"
        ).ask()
        if install:
            console.print("[green]Installing virtualenv...[/]")
            if config.config["cli"]["dispay_output"]:
                out = subprocess.run(["pip", "install", "virtualenv"])
            else:
                out = subprocess.run(
                    ["pip", "install", "virtualenv"], capture_output=True
                )
            if out.returncode == 0:
                console.print("[green]virtualenv installed succesfully![/]")
            else:
                console.print("[red]virtualenv installation failed![/]")

    if not os.path.exists(os.path.join(home, repository)):
        os.mkdir(os.path.join(home, repository))

    if config.config["cli"]["display_output"]:
        subprocess.run(
            [
                "python",
                "-m",
                "virtualenv",
                os.path.join(get_home_dir(), repository, name),
            ]
        )
    else:
        subprocess.run(
            [
                "python",
                "-m",
                "virtualenv",
                os.path.join(get_home_dir(), repository, name),
            ],
            capture_output=True,
        )

    deps = (
        questionary.text("Enter comma separated list of dependencies: ")
        .ask()
        .split(",")
    )
    dep_progress = 50 / len(deps)
    with Progress() as progress:
        create_task = progress.add_task("[green]Creating files", total=100)
        write_task = progress.add_task("[green]Writing data", total=100)

        progress.update(create_task, advance=5)
        time.sleep(1)
        os.mkdir(os.path.join(home, repository, name, "src"))
        progress.update(create_task, advance=5)
        time.sleep(1)
        os.mkdir(os.path.join(home, repository, name, "src", name))
        progress.update(create_task, advance=5)
        time.sleep(1)
        os.mkdir(os.path.join(home, repository, name, "tests"))
        progress.update(create_task, advance=5)
        time.sleep(1)
        with open(os.path.join(home, repository, name, "requirements.txt"), "w") as f:
            f.write("")
        progress.update(create_task, advance=10)
        time.sleep(1)
        with open(os.path.join(home, repository, name, "setup.py"), "w") as f:
            f.write("")
        progress.update(create_task, advance=10)
        time.sleep(1)
        with open(
            os.path.join(home, repository, name, "src", name, "__init__.py"),
            "w",
        ) as f:
            f.write("")
        progress.update(create_task, advance=10)
        time.sleep(1)
        with open(
            os.path.join(home, repository, name, "src", name, f"{name}.py"),
            "w",
        ) as f:
            f.write("")
        progress.update(create_task, advance=10)
        time.sleep(1)
        with open(os.path.join(home, repository, name, "README.md"), "w") as f:
            f.write("")
        progress.update(create_task, advance=10)
        time.sleep(1)
        with open(os.path.join(home, repository, name, "LICENSE"), "w") as f:
            f.write("")
        progress.update(create_task, advance=10)
        time.sleep(1)
        with open(
            os.path.join(home, repository, name, "tests", "__init__.py"),
            "w",
        ) as f:
            f.write("")
        progress.update(create_task, advance=10)
        time.sleep(1)
        with open(
            os.path.join(home, repository, name, "tests", f"test_{name}.py"),
            "w",
        ) as f:
            f.write("")
        progress.update(create_task, advance=10)
        time.sleep(1)
        progress.console.print("[green]Files created successfully![/]")
        for dep in deps:
            out = subprocess.run(["pip", "install", dep], capture_output=True)
            if out.returncode != 0:
                progress.console.print(f"[red]Failed to install dependency: {dep}[/]")
            else:
                progress.console.print(
                    f"[green]Dependency: {dep.lstrip().rstrip()} installed successfully![/]"
                )
            progress.update(write_task, advance=dep_progress)
        progress.console.print("[green]All dependencies installed successfully![/]")
        progress.console.print("[green]Writing dependencies to files[/]")
        with open(os.path.join(home, repository, name, "requirements.txt"), "w") as f:
            for dep in deps:
                f.write(f"{dep.lstrip().rstrip()}\n")
        progress.update(write_task, advance=20)
        time.sleep(1)
        progress.console.print("[green]Writing setup.py[/]")
        with open(os.path.join(home, repository, name, "setup.py"), "w") as f:
            f.write(
                f"""from setuptools import setup
    setup(name='{name}',
    version='0.0.1',
    description='Package Description',
    author={getpass.getuser()},
    author_email='',
    url='',
    package_dir={{"":"src"}},
    packages=setuptools.find_packages(where="src"),
    python_requires='>={sys.version_info.major}.{sys.version_info.minor}',
    install_requires={[dep.lstrip().rstrip() for dep in deps]},
    classifiers=[]
    )"""
            )
        progress.update(write_task, advance=20)
        time.sleep(1)
        progress.console.print("[green]Writing pyproject.toml[/]")
        with open(os.path.join(home, repository, name, "pyproject.toml"), "w") as f:
            f.write(
                "[build-system]\n"
                f"requires = ['setuptools>=42']\n"
                f"build-backend = 'setuptools.build_meta'\n"
            )
        progress.update(write_task, advance=5)
        time.sleep(1)
        progress.console.print("[green]Data written to files successfully![/]")
        progress.console.print("[green]Initializing Git Repo[/]")
        out = subprocess.run(
            ["git", "init"],
            cwd=os.path.join(home, repository, name),
            capture_output=True,
        )
        if out.returncode != 0:
            progress.console.print("[red]Failed to initialize git repo![/]")
        else:
            progress.console.print("[green]Git repo initialized successfully![/]")
            progress.update(write_task, advance=1)
            progress.console.print("[green]Adding files to git repo[/]")
            out = subprocess.run(
                ["git", "add", "."],
                cwd=os.path.join(home, repository, name),
                capture_output=True,
            )
            if out.returncode != 0:
                progress.console.print("[red]Failed to add files to git repo![/]")
            else:
                progress.console.print(
                    "[green]Files added to git repo successfully![/]"
                )
                progress.update(write_task, advance=2)
                progress.console.print("[green]Committing files to git repo[/]")
                out = subprocess.run(
                    ["git", "commit", "-m", "Initial Commit from rrpm"],
                    cwd=os.path.join(home, repository, name),
                    capture_output=True,
                )
                if out.returncode != 0:
                    progress.console.print(
                        "[red]Failed to commit files to git repo![/]"
                    )
                else:
                    progress.console.print(
                        "[green]Files committed to git repo successfully![/]"
                    )
                    progress.update(write_task, advance=2)
    console.print("[green]Package created successfully![/]")
