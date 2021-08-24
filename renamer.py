#!/usr/bin/env python3.9

import hashlib
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


def filereplace(
    filepath: Path, ignore_content: dict, mapping: dict = REPLACES
):
    with open(filepath, encoding='utf-8') as file:
        content = file.read()

    content_replaced = multireplace(content, ignore_content)
    content_replaced = multireplace(content_replaced, mapping)
    # there's an issue with case here but whatever
    content_replaced = multireplace(
        content_replaced, {v: k for k, v in ignore_content.items()}
    )
    
    if content != content_replaced:
        print(f'Content: {filepath}')
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content_replaced)


def pathrename(filepath: Path, mapping: dict = REPLACES) -> Path:
    filename_replaced = multireplace(filepath.name, mapping)
    if filepath.name != filename_replaced:
        print(f'Rename: {filepath}')
        filepath = filepath.rename(filepath.with_name(filename_replaced))
    return filepath


def check_ignore(files: List[Path]) -> List[Path]:
    command = ' '.join(['git check-ignore'] + [str(f) for f in files])
    try:
        result = subprocess.check_output(
            command, shell=True, encoding='utf-8'
        )
    except subprocess.CalledProcessError as error:
        result = error.output
    ignored_files = result.splitlines()
    ignored_paths = [Path(f.strip('"')).resolve() for f in ignored_files]

    return ignored_paths


def recurse(
    directory: Path, threadpool: concurrent.futures.ThreadPoolExecutor,
    ignore: List[Path], ignore_content: dict
):
    iterdir_list = list(directory.iterdir())
    ignored_paths = check_ignore(iterdir_list) + ignore
    for path in iterdir_list:
        print(path)
        if path.resolve() in ignored_paths:
            print(f'Ignore: {path}')
            continue
        
        path = pathrename(path)
        if path.is_dir():
            recurse(path, threadpool, ignore, ignore_content)
        else:
            threadpool.submit(filereplace, path, ignore_content)


def main():
    for i in range(1):
        if input('Are you sure? y/N\n') != 'y':
            sys.exit(1)
    
    threadpool = concurrent.futures.ThreadPoolExecutor()
    cwd = Path().resolve()

    ignore_str = [
        __file__,
        '.git',
        'contrib/builder-keys/keys.txt',
        'test/functional/wallet_taproot.py',
    ]
    ignore_path = [Path(p).resolve() for p in ignore_str]
    
    ignore_content = [
        'The Bitcoin Core developers',
        'Bitcoin Developers',
        'BtcDrak'
    ]
    ignore_content_hashes = {}
    for i in ignore_content:
        h = hashlib.md5()
        h.update(i.encode('utf_8'))
        ignore_content_hashes[i] = h.digest().hex()
    
    # always do gitignore first
    filereplace(Path('.gitignore'), {})
    recurse(cwd, threadpool, ignore_path, ignore_content_hashes)

    threadpool.shutdown()


if __name__ == '__main__':
    main()
