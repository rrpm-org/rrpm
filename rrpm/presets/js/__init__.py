import shutil
import sys
from rich.console import Console
import questionary

console = Console()


def default_questions():
    lang = questionary.select("Select Type", choices=["JavaScript", "TypeScript"]).ask()
    pkg_man = questionary.select(
        "Select Package Manager", choices=["NPM", "Yarn", "Pnpm"]
    ).ask()
    if shutil.which(pkg_man) is None:
        console.print(f"[red]Package manager {pkg_man} not found![/]")
        sys.exit(1)
    return lang, pkg_man
