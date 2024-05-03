import argparse

import pytest
from colorama import Fore, Style

from task02.tree import (
    get_string,
    build_tree
)

ANGLE = '└──'
TEE = '├──'
LINE = '│    '
BLANK = '     '


@pytest.mark.parametrize(
    "path, is_last, name, expected",
    [
        ["extras/dir", False, "dir", f"{TEE} {Fore.BLUE}dir{Style.RESET_ALL}"],
        ["extras/dir/life1.txt", True, "life1.txt", f"{ANGLE} {Fore.GREEN}life1.txt{Style.RESET_ALL}"],
    ]
)
def test_generate_string(path: str, is_last: bool, name: str, expected: str) -> bool:
    assert get_string(path, is_last, name) == expected


@pytest.mark.parametrize(
    "path, counter, depth, prefix",
    [
        ["extras/dir", [], 2, """
        """],
        ["extras/dir/dir1_0", [], 1, f"{BLANK}{LINE}{ANGLE}", ],
    ]
)
def test_build_tree(path: str, counter: dict, depth, prefix, expected) -> bool:
    assert build_tree(path, counter, depth, prefix) == expected
