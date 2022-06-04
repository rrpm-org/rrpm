import os
import sys
import re
from typing import Tuple

from .config import Config


config = Config()
GH_REGEX = re.compile(r"(https://)?(www\.)?github\.com/[A-Za-z0-9_-]+/?")


def get_home_dir():
    if sys.platform.lower().startswith("win"):
        return os.path.realpath(
            os.path.expandvars(config.config['root']['dir'])
        )
    return os.path.realpath(os.path.expanduser(config.config['root']['dir']))


def get_domain(url: str) -> str:
    return url.split("/")[2]


def is_github_url(url: str) -> bool:
    if GH_REGEX.match(url) is not None:
        return True
    return False


def get_github_user_repo(url: str) -> Tuple[str, str]:
    return url.replace("https://", "").replace("http://", "").split("/")[
        1
    ], url.replace("https://", "").replace("http://", "").split("/")[2].replace(
        ".git", ""
    )
