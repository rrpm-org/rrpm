import os
import platform
import toml

WIN_DEFAULT_CONFIG = {
    "root": {
        "dir": "%USERPROFILE%\\Projects",
    },
    "cli": {"displayOutput": False},
}

UNIX_DEFAULT_CONFIG = {
    "root": {
        "dir": "~/Projects",
    },
    "cli": {"displayOutput": False},
}


class Config:
    def __init__(self):
        self.base_path = (
            os.path.join(os.getenv("LOCALAPPDATA"), "rrpm")
            if platform.system().lower().startswith("win")
            else os.path.join(os.getenv("HOME"), ".config", "rrpm")
        )
        if not os.path.exists(self.base_path):
            os.mkdir(self.base_path)
            if not os.path.exists(os.path.join(self.base_path, "config.toml")):
                with open(os.path.join(self.base_path, "config.toml"), "w") as f:
                    if platform.system().lower().startswith("win"):
                        toml.dump(WIN_DEFAULT_CONFIG, f)
                    else:
                        toml.dump(UNIX_DEFAULT_CONFIG, f)

    @property
    def config_path(self):
        return os.path.join(self.base_path, "config.toml")

    @property
    def config(self):
        with open(os.path.join(self.base_path, "config.toml")) as f:
            return toml.load(f)
