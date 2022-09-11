from rich.console import Console

class PackageManager:
    def __init__(self):
        pass

    @classmethod
    def generate(cls):
        pass

class Preset:
    package_managers = []

    def __init__(self, repo: str, name: str):
        self.repo = repo
        self.name = name

    def generate(self, pkg: PackageManager):
        pass

    def exception_handler(self, e: Exception):
        Console().print_exception()