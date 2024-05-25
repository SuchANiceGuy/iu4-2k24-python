import argparse
from write_SMD_to_file import printSmd
from parser import parse_file
from modification import modificationFile
import extras


def main() -> None:
    parser = argparse.ArgumentParser(description='Command for modified smd file')
    parser.add_argument('file', type=str,
                        help='SMD file which will be modified')

    args = parser.parse_args()
    printSmd(modificationFile(parse_file(args.file)))


if __name__ == '__main__':
    main()
