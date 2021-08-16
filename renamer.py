#!/usr/bin/env python3.9

import subprocess
import sys
import concurrent.futures
from pathlib import Path
from typing import List


REPLACES = {
        'bitcoin': 'bubcoin',
        'btc': 'bub',
    }


def casereplace(text: str, old: str, new: str) -> str:
    cases = [
        str.lower,
        str.upper,
        str.capitalize,
        str.title
    ]
    for case in cases:
        text = text.replace(case(old), case(new))
    return text


def multireplace(text: str, mapping: dict) -> str:
    for key, value in mapping.items():
        text = casereplace(text, key, value)
    return text


def filereplace(filepath: Path):
    with open(filepath, encoding='utf-8') as file:
        content = file.read()
    content_replaced = multireplace(content, REPLACES)
    if content != content_replaced:
        print(f'Content: {filepath}')
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content_replaced)


def pathrename(filepath: Path):
    filename_replaced = multireplace(filepath.stem, REPLACES)
    if filepath.stem != filename_replaced:
        print(f'Rename: {filepath}')
        filepath.rename(filepath.with_stem(filename_replaced))


def check_ignore(files: List[Path]) -> List[Path]:
    command = ' '.join(['git check-ignore'] + [str(f) for f in files])
    try:
        result = subprocess.check_output(
            command, shell=True, encoding='utf-8'
        )
    except subprocess.CalledProcessError as error:
        result = error.output
    ignored_files = result.splitlines()
    ignored_paths = [Path(f).resolve() for f in ignored_files]

    return ignored_paths


def recurse(
    directory: Path, threadpool: concurrent.futures.ThreadPoolExecutor,
    ignore: List[Path]
):
    iterdir_list = list(directory.iterdir())
    ignored_paths = check_ignore(iterdir_list) + ignore
    for path in iterdir_list:
        print(path)
        ignore = ['.git', __name__]
        if path.resolve() in ignored_paths:
            print(f'Ignore: {path}')
            continue
        
        pathrename(path)
        if path.is_dir():
            recurse(path, threadpool, ignore)
        else:
            threadpool.submit(filereplace, path)


def main():
    for i in range(1):
        if input('Are you sure? y/N\n') != 'y':
            sys.exit(1)
    
    threadpool = concurrent.futures.ThreadPoolExecutor()
    cwd = Path().resolve()
    # todo: ignore specific phrases like the name BtcDrak
    ignore_str = [
        __file__,
        '.git',
        'contrib/builder-keys/keys.txt',
        'test/functional/wallet_taproot.py',
        'test/functional/data',
    ]
    ignore_path = [Path(p).resolve() for p in ignore_str]
    # always do gitignore first
    filereplace(Path('.gitignore'))
    recurse(cwd, threadpool, ignore_path)


if __name__ == '__main__':
    main()
