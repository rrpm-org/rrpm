from rich.console import Console

from .base.managers import NPM, PNPM, Yarn
from .base.base import Preset, PackageManager
from .. import get_home_dir
from .. import Config

console = Console()
config = Config()
home = get_home_dir()


class React(Preset):
    package_managers = [NPM, Yarn, PNPM]

    def generate(self, pkg: PackageManager):
        pkg.generate(self.repo, self.name, "react", True)


class Vanilla(Preset):
    package_managers = [NPM, Yarn, PNPM]

    def generate(self, pkg: PackageManager):
        pkg.generate(self.repo, self.name, "vanilla", True)


class NextJS(Preset):
    package_managers = [NPM, Yarn, PNPM]

    def generate(self, pkg: PackageManager):
        pkg.generate(self.repo, self.name, "next", True)