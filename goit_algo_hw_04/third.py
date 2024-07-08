from colorama import Fore
from pathlib import Path
import sys


def main():
    if len(sys.argv) < 2:
        user_input = ''
    else:
        user_input = sys.argv[1]
        path = Path(user_input)
        if path.exists():
            if path.is_dir():
                print(f'📂{Fore.RED}{path.name}')
                items = path.glob('**/*')
                for item in items:
                    both = str(item).replace(str(path.parent), '')
                    if item.is_dir():
                        print(f'\t📂{Fore.GREEN}{both}')
                        continue
                    elif item.suffix == ".png":
                        print(f'\t📦{Fore.BLUE}{both}')
                        continue
                    print(f'\t📜{Fore.YELLOW}{both}')
            else:
                print(f'{path} is a file.')
        else:
            print(f'{path.absolute()} is not exist')


if __name__ == "__main__":
    main()
