import os
import shutil
import subprocess
import sys
import questionary
from .base import PackageManager
from rich.console import Console
from .. import Config
from .. import get_home_dir

presets = ["react", "next", "vanilla", "astro", "svelte", "sveltekit", "vue"]
console = Console()
config = Config()
home = get_home_dir()

class NPM(PackageManager):
    name = "NPM"

    @classmethod
    def generate(cls, repo: str, name: str, preset: str, ts: bool):
        if preset not in presets:
            console.print(f"[red]Unknown preset: '{preset}'[/]")
            return

        if ts:
            if preset == "react":
                pass
            elif preset == "next":
                pass
            elif preset == "vanilla":
                pass
            elif preset == "astro":
                pass
            elif preset == "svelte":
                pass
            elif preset == "sveltekit":
                pass
            elif preset == "vue":
                pass
        else:
            if preset == "react":
                bundler = questionary.select("Bundler", choices=["Vite", "create-react-app"]).ask()
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    sys.exit(1)
                if bundler == "Vite":
                    os.chdir(os.path.join(get_home_dir(), repo))
                    console.print("[green]Creating project with Vite, JavaScript and NPM[/]")
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            ["npm", "create", "vite@latest", name, "--", "--template", "react"],
                            shell=True,
                        )
                    else:
                        subprocess.run(
                            ["npm", "create", "vite@latest", name, "--", "--template", "react"],
                            shell=True,
                            capture_output=True,
                        )
                else:
                    os.chdir(os.path.join(home, repo))
                    console.print(
                        "[green]Creating project with create-react-app, JavaScript and NPM[/]"
                    )
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            ["npx", "create-react-app@latest", name],
                            shell=True,
                        )
                    else:
                        subprocess.run(
                            ["npx", "create-react-app@latest", name],
                            shell=True,
                            capture_output=True,
                        )
            elif preset == "next":
                if os.path.exists(os.path.join(home, repo   , name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print("[green]Creating project with create-next-app, JavaScript and NPM[/]")
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
            elif preset == "vanilla":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                os.chdir(os.path.join(home, repo, name))
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
                return
            elif preset == "astro":
                pass
            elif preset == "svelte":
                pass
            elif preset == "sveltekit":
                pass
            elif preset == "vue":
                pass


class Yarn(PackageManager):
    name = "Yarn"

    @classmethod
    def generate(cls, repo: str, name: str, preset: str, ts: bool):
        if preset not in presets:
            console.print(f"[red]Unknown preset: '{preset}'[/]")
            return

        if ts:
            if preset == "react":
                pass
            elif preset == "next":
                pass
            elif preset == "vanilla":
                pass
            elif preset == "astro":
                pass
            elif preset == "svelte":
                pass
            elif preset == "sveltekit":
                pass
            elif preset == "vue":
                pass
        else:
            if preset == "react":
                bundler = questionary.select("Bundler", choices=["Vite", "create-react-app"]).ask()
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    sys.exit(1)
                if bundler == "Vite":
                    os.chdir(os.path.join(home, repo))
                    console.print("[green]Creating project with Vite, JavaScript and Yarn[/]")
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            ["yarn", "create", "vite", name, "--template", "react"], shell=True
                        )
                    else:
                        subprocess.run(
                            ["yarn", "create", "vite", name, "--template", "react"],
                            shell=True,
                            capture_output=True,
                        )
                else:
                    os.chdir(os.path.join(home, repo))
                    console.print(
                        "[green]Creating project with create-react-app, JavaScript and Yarn[/]"
                    )
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            ["yarn", "create", "react-app", name],
                            shell=True,
                        )
                    else:
                        subprocess.run(
                            ["yarn", "create", "react-app", name],
                            shell=True,
                            capture_output=True,
                        )
            elif preset == "next":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with create-next-app, JavaScript and Yarn[/]"
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
            elif preset == "vanilla":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                os.chdir(os.path.join(home, repo, name))
                console.print("[green]Creating project with Yarn, and JavaScript[/]")
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
            elif preset == "astro":
                pass
            elif preset == "svelte":
                pass
            elif preset == "sveltekit":
                pass
            elif preset == "vue":
                pass


class PNPM(PackageManager):
    name = "PNPM"

    @classmethod
    def generate(cls, repo: str, name: str, preset: str, ts: bool):
        if preset not in presets:
            console.print(f"[red]Unknown preset: '{preset}'[/]")
            return

        if ts:
            if preset == "react":
                pass
            elif preset == "next":
                pass
            elif preset == "vanilla":
                pass
            elif preset == "astro":
                pass
            elif preset == "svelte":
                pass
            elif preset == "sveltekit":
                pass
            elif preset == "vue":
                pass
        else:
            if preset == "react":
                bundler = questionary.select("Bundler", choices=["Vite", "create-react-app"]).ask()
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    sys.exit(1)
                if bundler == "Vite":
                    os.chdir(os.path.join(home, repo))
                    console.print("[green]Creating project with Vite, JavaScript and Pnpm[/]")
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            ["pnpm", "create", "vite", name, "--", "--template", "react"],
                            shell=True,
                        )
                    else:
                        subprocess.run(
                            ["pnpm", "create", "vite", name, "--", "--template", "react"],
                            shell=True,
                            capture_output=True,
                        )
                else:
                    if shutil.which("pnpx") is None:
                        console.print("[red]Pnpx is not installed![/]")
                    os.chdir(os.path.join(home, repo))
                    console.print(
                        "[green]Creating project with create-react-app, JavaScript and Pnpm[/]"
                    )
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            ["pnpx", "create-react-app", name],
                            shell=True,
                        )
                    else:
                        subprocess.run(
                            ["pnpx", "create-react-app", name],
                            shell=True,
                            capture_output=True,
                        )
            elif preset == "next":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with create-next-app, JavaScript and Pnpm[/]"
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
            elif preset == "vanilla":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                os.chdir(os.path.join(home, repo, name))
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
                return
            elif preset == "astro":
                pass
            elif preset == "svelte":
                pass
            elif preset == "sveltekit":
                pass
            elif preset == "vue":
                pass


class Pip(PackageManager):
    name = "Pip"

    @classmethod
    def generate(cls, repo: str, name: str):
        pass


class Poetry(PackageManager):
    name = "Poetry"

    @classmethod
    def generate(cls, repo: str, name: str):
        pass


class Venv(PackageManager):
    name = "Venv"

    @classmethod
    def generate(cls, repo: str, name: str):
        pass