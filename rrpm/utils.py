import os
import sys
import re
from typing import Tuple

from .config import Config


config = Config()
GH_REGEX = re.compile(r"(https://)?(www\.)?github\.com/[A-Za-z0-9_-]+/?")
SHORTHAND_REGEX = re.compile(r"^[a-zA-Z-0-9]+\/[a-zA-Z-0-9_\.]+$")
DOMAIN_REGEX = re.compile(
    r"^(http:\/\/|https:\/\/)?([a-zA-Z0-9-_]+\.)?([a-zA-Z0-9-_]+\.)([a-zA-Z0-9-_]+)"
)


def get_home_dir():
    if sys.platform.lower().startswith("win"):
        return os.path.realpath(os.path.expandvars(config.config["root"]["dir"]))
    return os.path.realpath(os.path.expanduser(config.config["root"]["dir"]))


def is_shorthand(url: str) -> bool:
    if SHORTHAND_REGEX.match(url) is not None:
        return True
    return False


def is_domain(url: str) -> bool:
    if DOMAIN_REGEX.match(url) is not None:
        return True
    return False


def get_domain(url: str) -> str:
    return url.split("/")[2]


def get_user_repo(url: str) -> Tuple[str, str]:
    return url.replace("https://", "").replace("http://", "").split("/")[
        1
    ], url.replace("https://", "").replace("http://", "").split("/")[2].replace(
        ".git", ""
    )
