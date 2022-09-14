import getpass
import os
import shutil
import subprocess
import sys
import time
import questionary
from .base import PackageManager
from rich.console import Console
from rich.progress import Progress
from rrpm.config import Config
from rrpm.utils import get_home_dir

presets = ["react", "next", "vanilla", "astro", "svelte", "sveltekit", "vue"]
presets_py = ["vanilla", "flask", "fastapi"]
console = Console()
config = Config()
home = get_home_dir()


class NPM(PackageManager):
    name = "NPM"
    cmd = "npm"

    @classmethod
    def generate(cls, repo: str, name: str, preset: str, ts: bool):
        if not cls.check():
            console.print("[red]npm is not installed![/]")
            return

        if preset not in presets:
            console.print(f"[red]Unknown preset: '{preset}'[/]")
            return

        if ts:
            if preset == "react":
                bundler = questionary.select(
                    "Bundler", choices=["Vite", "create-react-app"]
                ).ask()
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    sys.exit(1)
                if bundler == "Vite":
                    os.chdir(os.path.join(get_home_dir(), repo))
                    console.print(
                        "[green]Creating project with Vite, TypeScript and NPM[/]"
                    )
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            [
                                "npm",
                                "create",
                                "vite@latest",
                                name,
                                "--",
                                "--template",
                                "react-ts",
                            ],
                            shell=True,
                        )
                    else:
                        subprocess.run(
                            [
                                "npm",
                                "create",
                                "vite@latest",
                                name,
                                "--",
                                "--template",
                                "react-ts",
                            ],
                            shell=True,
                            capture_output=True,
                        )
                else:
                    os.chdir(os.path.join(home, repo))
                    console.print(
                        "[green]Creating project with create-react-app, TypeScript and NPM[/]"
                    )
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            [
                                "npx",
                                "create-react-app@latest",
                                name,
                                "--template",
                                "typescript",
                            ],
                            shell=True,
                        )
                    else:
                        subprocess.run(
                            [
                                "npx",
                                "create-react-app@latest",
                                name,
                                "--template",
                                "typescript",
                            ],
                            shell=True,
                            capture_output=True,
                        )
            elif preset == "next":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with create-next-app, TypeScript and NPM[/]"
                )
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
                ts = questionary.confirm("Install TypeScript Globally?")
                ts_node = questionary.confirm("Install ts-node?")
                if config.config["cli"]["display_output"]:
                    if ts:
                        subprocess.run(
                            ["npm", "install", "--global", "typescript"], shell=True
                        )
                    else:
                        subprocess.run(
                            ["npm", "install", "--save-dev", "typescript"], shell=True
                        )
                    if ts_node:
                        subprocess.run(
                            ["npm", "install", "--global", "ts-node"], shell=True
                        )
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
                        subprocess.run(
                            ["npm", "install", "--global", "ts-node"], shell=True
                        )
                return
            elif preset == "astro":
                console.log("[red]Astro with TypeScript is not availble![/]")
            elif preset == "svelte":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        [
                            "npm",
                            "create",
                            "vite@latest",
                            name,
                            "--",
                            "--temaplte",
                            "svelte-ts",
                        ],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        [
                            "npm",
                            "create",
                            "vite@latest",
                            name,
                            "--",
                            "--temaplte",
                            "svelte-ts",
                        ],
                        shell=True,
                        capture_output=True,
                    )
                return
            elif preset == "sveltekit":
                console.log("[red]SvelteKit with TypeScript is not availble![/]")
            elif preset == "vue":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        [
                            "npm",
                            "create",
                            "vite@latest",
                            name,
                            "--",
                            "--template",
                            "vue-ts",
                        ],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        [
                            "npm",
                            "create",
                            "vite@latest",
                            name,
                            "--",
                            "--template",
                            "vue-ts",
                        ],
                        shell=True,
                        capture_output=True,
                    )
                return
        else:
            if preset == "react":
                bundler = questionary.select(
                    "Bundler", choices=["Vite", "create-react-app"]
                ).ask()
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    sys.exit(1)
                if bundler == "Vite":
                    os.chdir(os.path.join(get_home_dir(), repo))
                    console.print(
                        "[green]Creating project with Vite, JavaScript and NPM[/]"
                    )
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            [
                                "npm",
                                "create",
                                "vite@latest",
                                name,
                                "--",
                                "--template",
                                "react",
                            ],
                            shell=True,
                        )
                    else:
                        subprocess.run(
                            [
                                "npm",
                                "create",
                                "vite@latest",
                                name,
                                "--",
                                "--template",
                                "react",
                            ],
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
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with create-next-app, JavaScript and NPM[/]"
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
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Astro, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        ["npm", "create", "astro@latest", name],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        ["npm", "create", "astro@latest", name],
                        shell=True,
                        capture_output=True,
                    )
                return
            elif preset == "svelte":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        [
                            "npm",
                            "create",
                            "vite@latest",
                            name,
                            "--",
                            "--temaplte",
                            "svelte",
                        ],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        [
                            "npm",
                            "create",
                            "vite@latest",
                            name,
                            "--",
                            "--temaplte",
                            "svelte",
                        ],
                        shell=True,
                        capture_output=True,
                    )
                return
            elif preset == "sveltekit":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        ["npm", "create", "svelte@latest", name],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        ["npm", "create", "svelte@latest", name],
                        shell=True,
                        capture_output=True,
                    )
                return
            elif preset == "vue":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        [
                            "npm",
                            "create",
                            "vite@latest",
                            name,
                            "--",
                            "--template",
                            "vue",
                        ],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        [
                            "npm",
                            "create",
                            "vite@latest",
                            name,
                            "--",
                            "--template",
                            "vue",
                        ],
                        shell=True,
                        capture_output=True,
                    )
                return


class Yarn(PackageManager):
    name = "Yarn"
    cmd = "yarn"

    @classmethod
    def generate(cls, repo: str, name: str, preset: str, ts: bool):
        if not cls.check():
            console.print("[red]yarn is not installed![/]")
            return

        if preset not in presets:
            console.print(f"[red]Unknown preset: '{preset}'[/]")
            return

        if ts:
            if preset == "react":
                bundler = questionary.select(
                    "Bundler", choices=["Vite", "create-react-app"]
                ).ask()
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    sys.exit(1)
                if bundler == "Vite":
                    os.chdir(os.path.join(home, repo))
                    console.print(
                        "[green]Creating project with Vite, TypeScript and Yarn[/]"
                    )
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            ["yarn", "create", "vite", name, "--template", "react-ts"],
                            shell=True,
                        )
                    else:
                        subprocess.run(
                            ["yarn", "create", "vite", name, "--template", "react-ts"],
                            shell=True,
                            capture_output=True,
                        )
                else:
                    os.chdir(os.path.join(home, repo))
                    console.print(
                        "[green]Creating project with create-react-app, TypeScript and Yarn[/]"
                    )
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            [
                                "yarn",
                                "create",
                                "react-app",
                                name,
                                "--template",
                                "typescript",
                            ],
                            shell=True,
                        )
                    else:
                        subprocess.run(
                            [
                                "yarn",
                                "create",
                                "react-app",
                                name,
                                "--template",
                                "typescript",
                            ],
                            shell=True,
                            capture_output=True,
                        )
            elif preset == "next":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
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
            elif preset == "vanilla":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                os.chdir(os.path.join(home, repo, name))
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
                        subprocess.run(
                            ["yarn", "global", "add", "typescript"], shell=True
                        )
                    else:
                        subprocess.run(
                            ["yarn", "add", "--dev", "typescript"], shell=True
                        )
                    if ts_node:
                        subprocess.run(["yarn", "global", "add", "ts-node"], shell=True)
                else:
                    if ts:
                        subprocess.run(
                            ["yarn", "global", "add", "typescript"],
                            shell=True,
                            capture_output=True,
                        )
                    else:
                        subprocess.run(
                            ["yarn", "add", "--dev", "typescript"],
                            shell=True,
                            capture_output=True,
                        )
                    if ts_node:
                        subprocess.run(["yarn", "global", "add", "ts-node"], shell=True)
                return
            elif preset == "astro":
                console.log("[red]Astro with TypeScript is not availble![/]")
            elif preset == "svelte":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        [
                            "yarn",
                            "create",
                            "vite",
                            name,
                            "--",
                            "--temaplte",
                            "svelte-ts",
                        ],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        [
                            "yarn",
                            "create",
                            "vite",
                            name,
                            "--",
                            "--temaplte",
                            "svelte-ts",
                        ],
                        shell=True,
                        capture_output=True,
                    )
                return
            elif preset == "sveltekit":
                console.log("[red]SvelteKit with TypeScript is not availble![/]")
            elif preset == "vue":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        ["yarn", "create", "vite", name, "--", "--template", "vue-ts"],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        ["yarn", "create", "vite", name, "--", "--template", "vue-ts"],
                        shell=True,
                        capture_output=True,
                    )
                return
        else:
            if preset == "react":
                bundler = questionary.select(
                    "Bundler", choices=["Vite", "create-react-app"]
                ).ask()
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    sys.exit(1)
                if bundler == "Vite":
                    os.chdir(os.path.join(home, repo))
                    console.print(
                        "[green]Creating project with Vite, JavaScript and Yarn[/]"
                    )
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            ["yarn", "create", "vite", name, "--template", "react"],
                            shell=True,
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
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Astro, JavaScript and Yarn[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        ["yarn", "create", "astro", name],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        ["yarn", "create", "astro", name],
                        shell=True,
                        capture_output=True,
                    )
                return
            elif preset == "svelte":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        ["yarn", "create", "vite", name, "--", "--temaplte", "svelte"],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        ["yarn", "create", "vite", name, "--", "--temaplte", "svelte"],
                        shell=True,
                        capture_output=True,
                    )
                return
            elif preset == "sveltekit":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        ["yarn", "create", "svelte", name],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        ["yarn", "create", "svelte", name],
                        shell=True,
                        capture_output=True,
                    )
                return
            elif preset == "vue":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        ["yarn", "create", "vite", name, "--", "--template", "vue"],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        ["yarn", "create", "vite", name, "--", "--template", "vue"],
                        shell=True,
                        capture_output=True,
                    )
                return


class PNPM(PackageManager):
    name = "PNPM"
    cmd = "pnpm"

    @classmethod
    def generate(cls, repo: str, name: str, preset: str, ts: bool):
        if not cls.check():
            console.print("[red]pnpm is not installed![/]")
            return

        if preset not in presets:
            console.print(f"[red]Unknown preset: '{preset}'[/]")
            return

        if ts:
            if preset == "react":
                bundler = questionary.select("Bundler", choices=["Vite"]).ask()
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    sys.exit(1)
                if bundler == "Vite":
                    os.chdir(os.path.join(home, repo))
                    console.print(
                        "[green]Creating project with Vite, TypeScript and Pnpm[/]"
                    )
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            [
                                "pnpm",
                                "create",
                                "vite",
                                name,
                                "--",
                                "--template",
                                "react-ts",
                            ],
                            shell=True,
                        )
                    else:
                        subprocess.run(
                            [
                                "pnpm",
                                "create",
                                "vite",
                                name,
                                "--",
                                "--template",
                                "react-ts",
                            ],
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
                ts = questionary.confirm("Install TypeScript Globally?")
                ts_node = questionary.confirm("Install ts-node?")
                if config.config["cli"]["display_output"]:
                    if ts:
                        subprocess.run(
                            ["pnpm", "add", "--global", "typescript"], shell=True
                        )
                    else:
                        subprocess.run(
                            ["pnpm", "add", "--save-dev", "typescript"], shell=True
                        )
                    if ts_node:
                        subprocess.run(
                            ["pnpm", "add", "--global", "ts-node"], shell=True
                        )
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
                        subprocess.run(
                            ["pnpm", "add", "--global", "ts-node"], shell=True
                        )
                return
            elif preset == "astro":
                console.log("[red]Astro with TypeScript is not availble![/]")
            elif preset == "svelte":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        [
                            "pnpm",
                            "create",
                            "vite",
                            name,
                            "--",
                            "--temaplte",
                            "svelte-ts",
                        ],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        [
                            "pnpm",
                            "create",
                            "vite",
                            name,
                            "--",
                            "--temaplte",
                            "svelte-ts",
                        ],
                        shell=True,
                        capture_output=True,
                    )
                return
            elif preset == "sveltekit":
                console.log("[red]SvelteKit with TypeScript is not availble![/]")
            elif preset == "vue":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        ["pnpm", "create", "vite", name, "--", "--template", "vue-ts"],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        ["pnpm", "create", "vite", name, "--", "--template", "vue-ts"],
                        shell=True,
                        capture_output=True,
                    )
                return
        else:
            if preset == "react":
                bundler = questionary.select(
                    "Bundler", choices=["Vite", "create-react-app"]
                ).ask()
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    sys.exit(1)
                if bundler == "Vite":
                    os.chdir(os.path.join(home, repo))
                    console.print(
                        "[green]Creating project with Vite, JavaScript and Pnpm[/]"
                    )
                    if config.config["cli"]["display_output"]:
                        subprocess.run(
                            [
                                "pnpm",
                                "create",
                                "vite",
                                name,
                                "--",
                                "--template",
                                "react",
                            ],
                            shell=True,
                        )
                    else:
                        subprocess.run(
                            [
                                "pnpm",
                                "create",
                                "vite",
                                name,
                                "--",
                                "--template",
                                "react",
                            ],
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
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Astro, JavaScript and Pnpm[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        ["pnpm", "create", "astro@latest", name],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        ["pnpm", "create", "astro@latest", name],
                        shell=True,
                        capture_output=True,
                    )
                return
            elif preset == "svelte":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        ["pnpm", "create", "vite", name, "--", "--temaplte", "svelte"],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        ["pnpm", "create", "vite", name, "--", "--temaplte", "svelte"],
                        shell=True,
                        capture_output=True,
                    )
                return
            elif preset == "sveltekit":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with SvelteKit, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        ["pnpm", "create", "svelte@latest", name],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        ["pnpm", "create", "svelte@latest", name],
                        shell=True,
                        capture_output=True,
                    )
                return
            elif preset == "vue":
                if os.path.exists(os.path.join(home, repo, name)):
                    console.print("[red]Project already exists![/]")
                    return
                os.mkdir(os.path.join(home, repo, name))
                console.print(
                    "[green]Creating project with Svelte, JavaScript and NPM[/]"
                )
                if config.config["cli"]["display_output"]:
                    subprocess.run(
                        ["pnpm", "create", "vite", name, "--", "--template", "vue"],
                        shell=True,
                    )
                else:
                    subprocess.run(
                        ["pnpm", "create", "vite", name, "--", "--template", "vue"],
                        shell=True,
                        capture_output=True,
                    )
                return


class Pip(PackageManager):
    name = "Pip"
    cmd = "pip"

    @classmethod
    def generate(cls, repo: str, name: str, preset: str):
        if not cls.check():
            console.print("[red]pip is not installed![/]")
            return

        if preset not in presets_py:
            console.print(f"[red]Unknown preset: '{preset}'[/]")
            return

        console.print("[green]Creating project with Pip[/]")
        if not os.path.exists(home):
            os.mkdir(home)

        os.chdir(home)
        if os.path.exists(os.path.join(home, repo, name)):
            console.print("[red]Project already exists![/]")
            return
        os.chdir(os.path.join(home, repo))
        deps = (
            questionary.text("Enter comma separated list of dependencies: ")
            .ask()
            .split(",")
        )
        dep_progress = 50 / len(deps)
        with Progress() as progress:
            create_task = progress.add_task("[green]Creating files", total=100)
            write_task = progress.add_task("[green]Writing data", total=100)

            os.mkdir(os.path.join(home, repo, name))
            progress.update(create_task, advance=5)
            time.sleep(1)
            os.mkdir(os.path.join(home, repo, name, "src"))
            progress.update(create_task, advance=5)
            time.sleep(1)
            os.mkdir(os.path.join(home, repo, name, "src", name))
            progress.update(create_task, advance=5)
            time.sleep(1)
            os.mkdir(os.path.join(home, repo, name, "tests"))
            progress.update(create_task, advance=5)
            time.sleep(1)
            with open(os.path.join(home, repo, name, "requirements.txt"), "w") as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(os.path.join(home, repo, name, "setup.py"), "w") as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(
                os.path.join(home, repo, name, "src", name, "__init__.py"),
                "w",
            ) as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(
                os.path.join(home, repo, name, "src", name, f"{name}.py"),
                "w",
            ) as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(os.path.join(home, repo, name, "README.md"), "w") as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(os.path.join(home, repo, name, "LICENSE"), "w") as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(
                os.path.join(home, repo, name, "tests", "__init__.py"),
                "w",
            ) as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(
                os.path.join(home, repo, name, "tests", f"test_{name}.py"),
                "w",
            ) as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            progress.console.print("[green]Files created successfully![/]")
            for dep in deps:
                out = subprocess.run(["pip", "install", dep], capture_output=True)
                if out.returncode != 0:
                    progress.console.print(
                        f"[red]Failed to install dependency: {dep}[/]"
                    )
                else:
                    progress.console.print(
                        f"[green]Dependency: {dep.lstrip().rstrip()} installed successfully![/]"
                    )
                progress.update(write_task, advance=dep_progress)
            progress.console.print("[green]All dependencies installed successfully![/]")
            progress.console.print("[green]Writing dependencies to files[/]")
            with open(os.path.join(home, repo, name, "requirements.txt"), "w") as f:
                for dep in deps:
                    f.write(f"{dep.lstrip().rstrip()}\n")
            progress.update(write_task, advance=20)
            time.sleep(1)
            progress.console.print("[green]Writing setup.py[/]")
            with open(os.path.join(home, repo, name, "setup.py"), "w") as f:
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
            with open(os.path.join(home, repo, name, "pyproject.toml"), "w") as f:
                f.write(
                    "[build-system]\n"
                    "requires = ['setuptools>=42']\n"
                    "build-backend = 'setuptools.build_meta'\n"
                )
            progress.update(write_task, advance=5)
            time.sleep(1)
            progress.console.print("[green]Data written to files successfully![/]")
            progress.console.print("[green]Initializing Git Repo[/]")
            out = subprocess.run(
                ["git", "init"],
                cwd=os.path.join(home, repo, name),
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
                    cwd=os.path.join(home, repo, name),
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
                        cwd=os.path.join(home, repo, name),
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
        return


class Poetry(PackageManager):
    name = "Poetry"
    cmd = "poetry"

    @classmethod
    def generate(cls, repo: str, name: str, preset: str):
        if not cls.check():
            console.print("[red]poetry is not installed![/]")
            return

        if preset not in presets_py:
            console.print(f"[red]Unknown preset: '{preset}'[/]")
            return

        console.print("[green]Creating project with Poetry[/]")
        if not os.path.exists(home):
            os.mkdir(home)
        if os.path.exists(os.path.join(home, repo, name)):
            console.print("[red]Project already exists![/]")
            sys.exit(1)
        os.chdir(os.path.join(home, repo))
        src = questionary.confirm("Use `src` layout?").ask()
        if src:
            subprocess.run(
                [
                    "poetry",
                    "new",
                    os.path.join(home, repo, name),
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
                    os.path.join(home, repo, name),
                    "--name",
                    name,
                ],
                shell=True,
            )


class Venv(PackageManager):
    name = "Virtual Environment"
    cmd = "virtualenv"

    @classmethod
    def generate(cls, repo: str, name: str, preset: str):
        if not cls.check():
            console.print("[red]virtualenv is not installed![/]")
            return

        if preset not in presets_py:
            console.print(f"[red]Unknown preset: '{preset}'[/]")
            return

        if not os.path.exists(os.path.join(home, repo)):
            os.mkdir(os.path.join(home, repo))

        if config.config["cli"]["display_output"]:
            subprocess.run(
                [
                    "python",
                    "-m",
                    "virtualenv",
                    os.path.join(get_home_dir(), repo, name),
                ]
            )
        else:
            subprocess.run(
                [
                    "python",
                    "-m",
                    "virtualenv",
                    os.path.join(get_home_dir(), repo, name),
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
            os.mkdir(os.path.join(home, repo, name, "src"))
            progress.update(create_task, advance=5)
            time.sleep(1)
            os.mkdir(os.path.join(home, repo, name, "src", name))
            progress.update(create_task, advance=5)
            time.sleep(1)
            os.mkdir(os.path.join(home, repo, name, "tests"))
            progress.update(create_task, advance=5)
            time.sleep(1)
            with open(os.path.join(home, repo, name, "requirements.txt"), "w") as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(os.path.join(home, repo, name, "setup.py"), "w") as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(
                os.path.join(home, repo, name, "src", name, "__init__.py"),
                "w",
            ) as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(
                os.path.join(home, repo, name, "src", name, f"{name}.py"),
                "w",
            ) as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(os.path.join(home, repo, name, "README.md"), "w") as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(os.path.join(home, repo, name, "LICENSE"), "w") as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(
                os.path.join(home, repo, name, "tests", "__init__.py"),
                "w",
            ) as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            with open(
                os.path.join(home, repo, name, "tests", f"test_{name}.py"),
                "w",
            ) as f:
                f.write("")
            progress.update(create_task, advance=10)
            time.sleep(1)
            progress.console.print("[green]Files created successfully![/]")
            for dep in deps:
                out = subprocess.run(["pip", "install", dep], capture_output=True)
                if out.returncode != 0:
                    progress.console.print(
                        f"[red]Failed to install dependency: {dep}[/]"
                    )
                else:
                    progress.console.print(
                        f"[green]Dependency: {dep.lstrip().rstrip()} installed successfully![/]"
                    )
                progress.update(write_task, advance=dep_progress)
            progress.console.print("[green]All dependencies installed successfully![/]")
            progress.console.print("[green]Writing dependencies to files[/]")
            with open(os.path.join(home, repo, name, "requirements.txt"), "w") as f:
                for dep in deps:
                    f.write(f"{dep.lstrip().rstrip()}\n")
            progress.update(write_task, advance=20)
            time.sleep(1)
            progress.console.print("[green]Writing setup.py[/]")
            with open(os.path.join(home, repo, name, "setup.py"), "w") as f:
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
            with open(os.path.join(home, repo, name, "pyproject.toml"), "w") as f:
                f.write(
                    "[build-system]\n"
                    "requires = ['setuptools>=42']\n"
                    "build-backend = 'setuptools.build_meta'\n"
                )
            progress.update(write_task, advance=5)
            time.sleep(1)
            progress.console.print("[green]Data written to files successfully![/]")
            progress.console.print("[green]Initializing Git Repo[/]")
            out = subprocess.run(
                ["git", "init"],
                cwd=os.path.join(home, repo, name),
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
                    cwd=os.path.join(home, repo, name),
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
                        cwd=os.path.join(home, repo, name),
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
