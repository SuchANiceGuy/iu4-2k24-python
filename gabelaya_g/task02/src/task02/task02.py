import os
import argparse
from tree import start_tree


def main():
    parser = argparse.ArgumentParser(description="Tree function")
    parser.add_argument("path", type=str, default=os.getcwd(),
                        nargs=1, help="Path to directory to start generate tree")
    parser.add_argument("-d", "--depth", type=int, default=-1,
                        nargs=1, help="Maximum depth")
    args = parser.parse_args()
    path = args.path[0]

    if not os.path.isdir(path):
        parser.error("input is not a valid path")

    counter = {
        'dirs': 0,
        'files': 0
    }

    print(start_tree(args.path, counter, args.depth))
    print(f"dirs: {counter['dirs']}")
    print(f"files: {counter['files']}")


if __name__ == '__main__':
    main()

