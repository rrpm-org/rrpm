from rich.console import Console

from .base.managers import NPM, PNPM, Yarn
from .base.base import Preset, PackageManager
from rrpm.utils import get_home_dir
from rrpm.config import Config

console = Console()
config = Config()
home = get_home_dir()


class React(Preset):
    package_managers = [NPM, Yarn, PNPM]

    def generate(self, pkg: PackageManager):
        pkg.generate(self.repo, self.name, "react", False)


class Vanilla(Preset):
    package_managers = [NPM, Yarn, PNPM]

    def generate(self, pkg: PackageManager):
        pkg.generate(self.repo, self.name, "vanilla", False)


class NextJS(Preset):
    package_managers = [NPM, Yarn, PNPM]

    def generate(self, pkg: PackageManager):
        pkg.generate(self.repo, self.name, "next", False)


class Astro(Preset):
    package_managers = [NPM, Yarn, PNPM]

    def generate(self, pkg: PackageManager):
        pkg.generate(self.repo, self.name, "astro", False)


class Svelte(Preset):
    package_managers = [NPM, Yarn, PNPM]

    def generate(self, pkg: PackageManager):
        pkg.generate(self.repo, self.name, "svelte", False)

        
class SvelteKit(Preset):
    package_managers = [NPM, Yarn, PNPM]

    def generate(self, pkg: PackageManager):
        pkg.generate(self.repo, self.name, "sveltekit", False)


class Vue(Preset):
    package_managers = [NPM, Yarn, PNPM]

    def generate(self, pkg: PackageManager):
        pkg.generate(self.repo, self.name, "vue", False)
