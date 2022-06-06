import os
import platform
import toml

WIN_DEFAULT_CONFIG = {
    "root": {
        "dir": "%USERPROFILE%\\Projects",
        "ext_dir": "%LOCALAPPDATA%\\rrpm\\extensions",
    },
    "cli": {
        "display_output": False,
        "extensions": [],
    },
    "extensions": {
        "ignore_extension_load_error": False,
    },
}

UNIX_DEFAULT_CONFIG = {
    "root": {
        "dir": "~/Projects",
        "exts_dir": "~/.config/rrpm/extensions",
    },
    "cli": {
        "display_output": False,
        "extensions": [],
    },
    "extensions": {
        "ignore_extension_load_error": False,
    },
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
        if (
            not os.path.exists(os.path.join(self.base_path, "config.toml"))
            or open(os.path.join(self.base_path, "config.toml")).read() == ""
        ):
            with open(os.path.join(self.base_path, "config.toml"), "w") as f:
                if platform.system().lower().startswith("win"):
                    toml.dump(WIN_DEFAULT_CONFIG, f)
                    if not os.path.exists(WIN_DEFAULT_CONFIG["root"]["ext_dir"]):
                        os.mkdir(
                            os.path.expandvars(
                                os.path.expanduser(
                                    WIN_DEFAULT_CONFIG["root"]["ext_dir"]
                                )
                            )
                        )
                else:
                    toml.dump(UNIX_DEFAULT_CONFIG, f)
                    if not os.path.exists(UNIX_DEFAULT_CONFIG["root"]["ext_dir"]):
                        os.mkdir(
                            os.path.expandvars(
                                os.path.expanduser(
                                    UNIX_DEFAULT_CONFIG["root"]["ext_dir"]
                                )
                            )
                        )

    def regenerate(self):
        if not os.path.exists(self.base_path):
            os.mkdir(self.base_path)
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
