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

counter = {
    'dirs': 0,
    'files': 0
}


@pytest.mark.parametrize(
    "path, is_last, name, counter, expected",
    [
        ["extras/dir", False, "dir", counter, f"{TEE} {Fore.BLUE}dir{Style.RESET_ALL}"],
        ["extras/dir/life1.txt", True, "life1.txt", counter, f"{ANGLE} {Fore.GREEN}life1.txt{Style.RESET_ALL}"],
    ]
)
def test_generate_string(path: str, is_last: bool, name: str, counter: dict, expected: str) -> None:
    assert get_string(path, is_last, name, counter) == expected


@pytest.mark.parametrize(
    "path, counter, depth, prefix, expected",
    [
        ["extras/dir", [], 1, "", '{Fore.BLUE}"extras/dir"{Style.RESET_ALL}'],
        ["extras/dir/dir1_0", [], 1, f"{BLANK}{LINE}{ANGLE}", '{Fore.BLUE}{BLANK}{LINE}{ANGLE}"extras/dir/dir1_0"{'
                                                              'Style.RESET_ALL}'],
    ]
)
def test_build_tree(path: str, counter: dict, depth: int, prefix: str, expected: str) -> None:
    assert build_tree(path, counter, depth, prefix) == expected
