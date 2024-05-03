import module_to_import
from cat.meow import meow

print(module_to_import)


def main():
    print("say something")
    print(__name__)
    meow()


if __name__ == '__main__':
    main()

