# Создать скрипт, который через параметр запуска получает имя исполняемого файла.
# И запускает этот файл через библиотеку subprocess.

import argparse
import subprocess


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='python file path to run', required=True)
    args = parser.parse_args()
    result = subprocess.run(["python", args.file], capture_output=True, text=True)
    print(result)
