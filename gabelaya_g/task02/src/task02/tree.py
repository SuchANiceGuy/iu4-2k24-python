import os
import argparse
from colorama import Fore, Style


ANGLE = '└──'
TEE = '├──'
LINE = '│    '
BLANK = '     '


def build_tree(path: str, counter: dict, depth: int = 1, prefix: str = "") -> str:
    result = ""
    for item in sorted(os.listdir(path)):  # for item in sorted(os.listdir(path))
        is_last = item == sorted(os.listdir(path))[-1]  # is_last = True if item == items_list[-1] else False
        item_path = os.path.join(path, item)
        name_with_color = get_string(item_path, is_last, item, counter)
        result = f"{result}{prefix}{name_with_color}\n\r"
        if depth > 1:
            if os.path.isdir(item_path):
                extender = f"{prefix}{BLANK if is_last else LINE}"
                addon = build_tree(item_path, counter, depth - 1, extender)
                result = f"{result}{addon}"
    return result


def get_string(path: str, is_last: bool, name: str, counter: dict) -> str:
    if os.path.isdir(path):
        style = Fore.BLUE
        counter['dirs'] += 1
    if os.path.isfile(path):
        style = Fore.GREEN
        counter['files'] += 1
    string = f"{ANGLE if is_last else TEE} {style}{name}{Style.RESET_ALL}"
    return string


def start_tree(path: str, counter: dict, depth: int = 1) -> str:
    print(f"{Fore.BLUE}{os.path.abspath(path)}{Style.RESET_ALL}")
    return build_tree(path, counter, depth)
