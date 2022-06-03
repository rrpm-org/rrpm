import os
import sys
from typing import Tuple

from config import Config


config = Config()


def get_home_dir():
    if sys.platform.lower().startswith("win"):
        return os.path.realpath(os.path.expandvars(f"%USERPROFILE%/{config.config['root']['dir']}"))
    return os.path.realpath(os.path.expanduser(f"~/{config.config['root']['dir']}"))


def get_domain(url: str) -> str:
    return url.split("/")[2]


def is_github_url(url: str) -> bool:
    if url.replace("http://", "").replace("https://", "").split("/")[0] == "github.com":
        return True
    return False


def get_github_user_repo(url: str) -> Tuple[str, str]:
    return url.replace("https://", "").replace("http://", "").split("/")[1], url.replace("https://", "").replace("http://", "").split("/")[2].replace(".git", "")
