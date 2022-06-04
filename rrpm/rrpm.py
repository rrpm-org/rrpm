import getpass
import os
import re
import subprocess
import shutil
import sys
import time

import questionary
from typer import Typer
from rich.console import Console
from rich.progress import Progress
from utils import get_home_dir, get_domain, is_github_url, get_github_user_repo
from config import Config

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
    "react": {
        "TypeScript": {
            "NPM": ["npx", "create-react-app", "--template", "typescript"],
            "Yarn": ["yarn", "create", "react-app", "--template", "typescript"],
        },
        "JavaScript": {
            "NPM": ["npx", "create-react-app@latest"],
            "Yarn": ["yarn", "create", "react-app"],
        },
    },
    "vite": {
        "react": {
            "TypeScript": {
                "NPM": ["npm", "create", "vite@latest", "--", "--template", "react-ts"],
                "Yarn": ["yarn", "create", "vite", "--template", "react-ts"],
                "Pnpm": ["yarn", "create", "vite", "--", "--template", "react-ts"]
            },
            "JavaScript": {
                "NPM": ["npm", "create", "vite@latest", "--", "--template", "react"],
                "Yarn": ["yarn", "create", "vite", "--template", "react"],
                "Pnpm": ["yarn", "create", "vite", "--", "--template", "react"]
            },
        }
    }
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
            if config.config['cli']['displayOutput'] is True:
                out = subprocess.run(["git", "clone", url, repo_dir])
            else:
                out = subprocess.run(["git", "clone", url, repo_dir], capture_output=True)
            if out.returncode == 0:
                console.print(f"[green]Successfully cloned repository in github.com/{username}/{reponame}[/]")
            else:
                console.print(f"[red]Failed to clone with exit status {out.returncode}[/]")
        else:
            console.print(f"[green]Fetching GitHub Repository[/]")
            if config.config['cli']['displayOutput'] is True:
                out = subprocess.run(["git", "clone", url, repo_dir])
            else:
                out = subprocess.run(["git", "clone", url, repo_dir], capture_output=True)
            if out.returncode == 0:
                console.print(f"[green]Successfully cloned repository in github.com/{username}/{reponame}[/]")
            else:
                console.print(f"[red]Failed to clone with exit status {out.returncode}[/]")
    else:
        console.print(f"[green]Fetching {domain}[/]")
        if config.config['cli']['displayOutput'] is True:
            out = subprocess.run(["git", "clone", url, os.path.join(home_dir, domain)])
        else:
            out = subprocess.run(["git", "clone", url, os.path.join(home_dir, domain)], capture_output=True)
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
                                for repo in os.listdir(os.path.join(home_dir, host, user)):
                                    console.print(f"          |- [magenta]{repo}[/]")
                    else:
                        for repo in os.listdir(os.path.join(home_dir, host)):
                            console.print(f"      |- [green]{repo}[/]")


@cli.command(help="Generate a project from any of the presets and/or its variations")
def create(name: str, src: bool = False):
    prj_type = questionary.select(
        "Project Preset",
        choices=[
            "Python",
            "FastAPI",
            "Flask",
            "NodeJS",
            "React",
            "NextJS"
        ]
    ).ask()
    if prj_type in ["React", "NextJS", "NodeJS"]:
        ts = questionary.select(
            "Select Type",
            choices=[
                "JavaScript",
                "TypeScript"
            ]
        ).ask()
        package_man = questionary.select(
            "Select Package Manager",
            choices=[
                "NPM",
                "Yarn",
                "Pnpm"
            ]
        ).ask()
        if shutil.which(package_man) is None:
            console.print(f"[red]Package manager {package_man} not found![/]")
            return
        if shutil.which("npx") is None:
            console.print(f"[red]NPX not found![/]")
            return
        if prj_type == "React":
            if package_man == "Pnpm":
                console.print("[red]Pnpm is not supported for React projects yet![/]")
            bundler = questionary.select(
                "Bundler",
                choices=["Vite", "create-react-app"]
            ).ask()
            domain = questionary.select(
                "Repository",
                choices=os.listdir(get_home_dir()) + ["Other"]
            ).ask()
            if domain == "Other":
                domain = questionary.text("Enter Domain(without 'https://'): ").ask()
                if DOMAIN_REGEX.match(domain) is None:
                    console.print(f"[red]Invalid domain![/]")
                    return
                os.mkdir(os.path.join(get_home_dir(), domain))
            if domain == "github.com":
                if not os.path.exists(os.path.join(get_home_dir(), domain)):
                    os.mkdir(os.path.join(get_home_dir(), domain))
                user = questionary.select("GitHub Username",
                                          choices=os.listdir(os.path.join(get_home_dir(), "github.com")) + [
                                              "Other"]).ask()
                if user == "Other":
                    user = questionary.text("Enter Username: ").ask()
                domain = os.path.join(domain, user)
                if not os.path.exists(os.path.join(get_home_dir(), "github.com")):
                    os.mkdir(os.path.join(get_home_dir(), "github.com"))
                if not os.path.exists(os.path.join(get_home_dir(), domain)):
                    os.mkdir(os.path.join(get_home_dir(), domain))
            if os.path.exists(os.path.join(get_home_dir(), domain, name)):
                console.print(f"[red]Project already exists![/]")
                return
            if bundler == "Vite":
                os.chdir(os.path.join(get_home_dir(), domain))
                console.print(f"[green]Creating project with Vite, {ts} and {package_man}[/]")
                if config.config['cli']['displayOutput']:
                    subprocess.run(
                        pm_cmd["vite"]["react"][ts][package_man],
                        shell=True)
                else:
                    subprocess.run(
                        pm_cmd["vite"]["react"][ts][package_man],
                        shell=True, capture_output=True)
                return
            elif bundler == "create-react-app":
                os.mkdir(os.path.join(get_home_dir(), domain, name))
                console.print(f"[green]Creating project with create-react-app, {ts} and {package_man}[/]")
                if config.config['cli']['displayOutput']:
                    subprocess.run(pm_cmd["react"][ts][package_man] + [os.path.join(get_home_dir(), domain, name)],
                                   shell=True)
                else:
                    subprocess.run(pm_cmd["react"][ts][package_man] + [os.path.join(get_home_dir(), domain, name)],
                                   shell=True, capture_output=True)
                return
        elif prj_type == "NextJS":
            domain = questionary.select(
                "Repository",
                choices=os.listdir(get_home_dir()) + ["Other"]
            ).ask()
            if domain == "Other":
                domain = questionary.text("Enter Domain(without 'https://'): ").ask()
                if DOMAIN_REGEX.match(domain) is None:
                    console.print(f"[red]Invalid domain![/]")
                    return
                os.mkdir(os.path.join(get_home_dir(), domain))
            if domain == "github.com":
                if not os.path.exists(os.path.join(get_home_dir(), domain)):
                    os.mkdir(os.path.join(get_home_dir(), domain))
                user = questionary.select("GitHub Username",
                                          choices=os.listdir(os.path.join(get_home_dir(), "github.com")) + [
                                              "Other"]).ask()
                if user == "Other":
                    user = questionary.text("Enter Username: ").ask()
                domain = os.path.join(domain, user)
                if not os.path.exists(os.path.join(get_home_dir(), "github.com")):
                    os.mkdir(os.path.join(get_home_dir(), "github.com"))
                if not os.path.exists(os.path.join(get_home_dir(), domain)):
                    os.mkdir(os.path.join(get_home_dir(), domain))
            if os.path.exists(os.path.join(get_home_dir(), domain, name)):
                console.print(f"[red]Project already exists![/]")
                return
            os.mkdir(os.path.join(get_home_dir(), domain, name))
            console.print(f"[green]Creating project with create-next-app, {ts} and {package_man}[/]")
            if config.config['cli']['displayOutput']:
                out = subprocess.run(pm_cmd["nextjs"][ts][package_man]+[os.path.join(get_home_dir(), domain, name)], shell=True)
            else:
                out = subprocess.run(pm_cmd["nextjs"][ts][package_man]+[os.path.join(get_home_dir(), domain, name)], shell=True, capture_output=True)
            return
        elif prj_type == "NodeJS":
            console.print(f"[green]Creating project with NodeJS[/]")
            return
    else:
        env = questionary.select(
            "Package Manager",
            choices=[
                "Poetry",
                "Pip",
                "Virtual Environment"
            ]
        ).ask()
        if env == "Poetry":
            if shutil.which("poetry") is None:
                console.print(f"[red]Poetry not found![/]")
                return

            console.print(f"[green]Creating project with Poetry[/]")
            if not os.path.exists(get_home_dir()):
                os.mkdir(get_home_dir())

            domain = questionary.select(
                "Repository",
                choices=os.listdir(get_home_dir()) + ["Other"]
            ).ask()
            if domain == "Other":
                domain = questionary.text("Enter Domain(without 'https://'): ").ask()
                if DOMAIN_REGEX.match(domain) is None:
                    console.print(f"[red]Invalid domain![/]")
                    return
                os.mkdir(os.path.join(get_home_dir(), domain))
            if domain == "github.com":
                if not os.path.exists(os.path.join(get_home_dir(), domain)):
                    os.mkdir(os.path.join(get_home_dir(), domain))
                user = questionary.select("GitHub Username",
                                          choices=os.listdir(os.path.join(get_home_dir(), "github.com")) + [
                                              "Other"]).ask()
                if user == "Other":
                    user = questionary.text("Enter Username: ").ask()
                domain = os.path.join(domain, user)
                if not os.path.exists(os.path.join(get_home_dir(), "github.com")):
                    os.mkdir(os.path.join(get_home_dir(), "github.com"))
                if not os.path.exists(os.path.join(get_home_dir(), domain)):
                    os.mkdir(os.path.join(get_home_dir(), domain))
            if os.path.exists(os.path.join(get_home_dir(), domain, name)):
                console.print(f"[red]Project already exists![/]")
                return

            os.chdir(os.path.join(get_home_dir(), domain))
            if src:
                subprocess.run(
                    ["poetry", "new", os.path.join(get_home_dir(), domain, name), "--name", name, "--src"], shell=True)
            else:
                subprocess.run(["poetry", "new", os.path.join(get_home_dir(), domain, name), "--name", name],
                               shell=True)
            return
        elif env == "Pip":
            if shutil.which("pip") is None:
                console.print(f"[red]Pip not found![/]")
                return
            console.print(f"[green]Creating project with Pip[/]")
            if not os.path.exists(get_home_dir()):
                os.mkdir(get_home_dir())

            os.chdir(get_home_dir())
            domain = questionary.select(
                "Repository",
                choices=os.listdir(get_home_dir()) + ["Other"]
            ).ask()
            if domain == "Other":
                domain = questionary.text("Enter Domain(without 'https://'): ").ask()
                if DOMAIN_REGEX.match(domain) is None:
                    console.print(f"[red]Invalid domain![/]")
                    return
                os.mkdir(os.path.join(get_home_dir(), domain))
            if domain == "github.com":
                user = questionary.text("Enter GitHub Username: ").ask()
                domain = os.path.join(domain, user)
                if not os.path.exists(os.path.join(get_home_dir(), "github.com")):
                    os.mkdir(os.path.join(get_home_dir(), "github.com"))
                if not os.path.exists(os.path.join(get_home_dir(), domain)):
                    os.mkdir(os.path.join(get_home_dir(), domain))
            if os.path.exists(os.path.join(get_home_dir(), domain, name)):
                console.print(f"[red]Project already exists![/]")
                return
            os.chdir(os.path.join(get_home_dir(), domain))
            deps = questionary.text("Enter comma separated list of dependencies: ").ask().split(",")
            dep_progress = 50 / len(deps)
            with Progress() as progress:
                create_task = progress.add_task("[green]Creating files", total=100)
                write_task = progress.add_task("[green]Writing data", total=100)

                os.mkdir(os.path.join(get_home_dir(), domain, name))
                progress.update(create_task, advance=5)
                time.sleep(1)
                os.mkdir(os.path.join(get_home_dir(), domain, name, "src"))
                progress.update(create_task, advance=5)
                time.sleep(1)
                os.mkdir(os.path.join(get_home_dir(), domain, name, "src", name))
                progress.update(create_task, advance=5)
                time.sleep(1)
                os.mkdir(os.path.join(get_home_dir(), domain, name, "tests"))
                progress.update(create_task, advance=5)
                time.sleep(1)
                with open(os.path.join(get_home_dir(), domain, name, "requirements.txt"), "w") as f:
                    f.write("")
                progress.update(create_task, advance=10)
                time.sleep(1)
                with open(os.path.join(get_home_dir(), domain, name, "setup.py"), "w") as f:
                    f.write("")
                progress.update(create_task, advance=10)
                time.sleep(1)
                with open(os.path.join(get_home_dir(), domain, name, "src", name, "__init__.py"), "w") as f:
                    f.write("")
                progress.update(create_task, advance=10)
                time.sleep(1)
                with open(os.path.join(get_home_dir(), domain, name, "src", name, f"{name}.py"), "w") as f:
                    f.write("")
                progress.update(create_task, advance=10)
                time.sleep(1)
                with open(os.path.join(get_home_dir(), domain, name, "README.md"), "w") as f:
                    f.write("")
                progress.update(create_task, advance=10)
                time.sleep(1)
                with open(os.path.join(get_home_dir(), domain, name, "LICENSE"), "w") as f:
                    f.write("")
                progress.update(create_task, advance=10)
                time.sleep(1)
                with open(os.path.join(get_home_dir(), domain, name, "tests", "__init__.py"), "w") as f:
                    f.write("")
                progress.update(create_task, advance=10)
                time.sleep(1)
                with open(os.path.join(get_home_dir(), domain, name, "tests", f"test_{name}.py"), "w") as f:
                    f.write("")
                progress.update(create_task, advance=10)
                time.sleep(1)
                progress.console.print(f"[green]Files created successfully![/]")
                for dep in deps:
                    out = subprocess.run(["pip", "install", dep], capture_output=True)
                    if out.returncode != 0:
                        progress.console.print(f"[red]Failed to install dependency: {dep}[/]")
                    else:
                        progress.console.print(f"[green]Dependency: {dep.lstrip().rstrip()} installed successfully![/]")
                    progress.update(write_task, advance=dep_progress)
                progress.console.print("[green]All dependencies installed successfully![/]")
                progress.console.print("[green]Writing dependencies to files[/]")
                with open(os.path.join(get_home_dir(), domain, name, "requirements.txt"), "w") as f:
                    for dep in deps:
                        f.write(f"{dep.lstrip().rstrip()}\n")
                progress.update(write_task, advance=20)
                time.sleep(1)
                progress.console.print("[green]Writing setup.py[/]")
                with open(os.path.join(get_home_dir(), domain, name, "setup.py"), "w") as f:
                    f.write(f"""from setuptools import setup
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
)""")
                    f.close()
                progress.update(write_task, advance=20)
                time.sleep(1)
                progress.console.print("[green]Writing pyproject.toml[/]")
                with open(os.path.join(get_home_dir(), domain, name, "pyproject.toml"), "w") as f:
                    f.write(f"[build-system]\n"
                            f"requires = ['setuptools>=42']\n"
                            f"build-backend = 'setuptools.build_meta'\n")
                    f.close()
                progress.update(write_task, advance=5)
                time.sleep(1)
                progress.console.print("[green]Data written to files successfully![/]")
                progress.console.print("[green]Initializing Git Repo[/]")
                out = subprocess.run(["git", "init"], cwd=os.path.join(get_home_dir(), domain, name),
                                     capture_output=True)
                if out.returncode != 0:
                    progress.console.print(f"[red]Failed to initialize git repo![/]")
                else:
                    progress.console.print("[green]Git repo initialized successfully![/]")
                    progress.update(write_task, advance=1)
                    progress.console.print("[green]Adding files to git repo[/]")
                    out = subprocess.run(["git", "add", "."], cwd=os.path.join(get_home_dir(), domain, name),
                                         capture_output=True)
                    if out.returncode != 0:
                        progress.console.print(f"[red]Failed to add files to git repo![/]")
                    else:
                        progress.console.print("[green]Files added to git repo successfully![/]")
                        progress.update(write_task, advance=2)
                        progress.console.print("[green]Committing files to git repo[/]")
                        out = subprocess.run(["git", "commit", "-m", "Initial Commit from rrpm"],
                                             cwd=os.path.join(get_home_dir(), domain, name), capture_output=True)
                        if out.returncode != 0:
                            progress.console.print(f"[red]Failed to commit files to git repo![/]")
                        else:
                            progress.console.print("[green]Files committed to git repo successfully![/]")
                            progress.update(write_task, advance=2)
            console.print("[green]Package created successfully![/]")
            return
        elif env == "Virtual Environment":
            console.print(f"[green]Work in Progress![/]")
            return


if __name__ == "__main__":
    cli()
