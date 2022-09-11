from rich.console import Console

from .base.managers import Pip, Poetry, Venv
from .base.base import Preset, PackageManager
from rrpm.utils import get_home_dir
from rrpm.config import Config

console = Console()
config = Config()
home = get_home_dir()


class Vanilla(Preset):
    package_managers = [Pip, Poetry, Venv]

    def generate(self, pkg: PackageManager):
        pkg.generate(self.repo, self.name, "vanilla")


class Flask(Preset):
    package_managers = [Pip, Poetry, Venv]

    def generate(self, pkg: PackageManager):
        pkg.generate(self.repo, self.name, "flask")


class FastAPI(Preset):
    package_managers = [Pip, Poetry, Venv]

    def generate(self, pkg: PackageManager):
        pkg.generate(self.repo, self.name, "fastapi")
