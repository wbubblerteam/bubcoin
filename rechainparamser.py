#!/usr/bin/env python3.9

import random
import re
from pathlib import Path

CHAINPARAMS_CPP_PATH = Path('src/chainparams.cpp')
EMPLACE_RE = re.compile(
    # match any line which adds a seed dns url, other than the dummy one
    r'^\s*vSeeds\.emplace_back\("(?!dummySeed\.invalid).*"\);.*$',
    re.MULTILINE
)
CHECKPOINTS_RE = re.compile(
    r'checkpointData = \{\s*{(\s*\{.*\}\,)*\s*\}\s*\};'
)
EMPTY_CHECKPOINTS = """checkpointData = {{}};"""
REPLACES_PARAMS = {
    # genesis timestamp string
    'The Times 03/Jan/2009 Chancellor on '
    'brink of second bailout for banks':
    'The Wbubbler 17/Feb/2021 Hello, I am Wbubbler, your friend! '
    'Bub is cool.',
    # genesis transaction public key
    '04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1'
    'f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f':
    '04b370600b143e9e7db6206de8dbdefdf109e8fe44ac343f6e07da71d0a'
    '94bc4c7552aadab878c0bbfa8354d15efab72084951060df7a81087731c83037370551d',
    # genesis posix timestamp
    '1231006505': '1629119093',
    # genesis hash nonce
    '2083236893': '737906790',
    # genesis block hash
    '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f':
    '00000000e51e0da00b4542726acf5385ff14ec7378e7ebf641eedc976d851aa1',
    # genesis byteswapped merkle hash
    '3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a':
    'cd28bcbab1701dd8f32aec2a5f7b0c8ff4fcd56ac794ceb95a63751f67c5abd3',
}
# todo: implement replacement for these
REPLACES_PCHMS = {
    # main
    'f9beb4d9': 'ffdfdcfe',
    # testnet
    '0b110907': 'abd3bfa5',
    # signet
    'fabfb5da': 'a9cdccff',
}
PCHMS_FORMAT = 'pchMessageStart[{}] = 0x{:x};'


def validate_decodeable(
    message: bytes, encoding: str
) -> bool:
    try:
        message.decode(encoding=encoding)
    except UnicodeDecodeError:
        return False
    else:
        return True

def validate_pchmessagestart(
    pchms: bytes, lower_bound: int = (2**32)//2
) -> bool:
    # check that pchms is invalid ascii
    if validate_decodeable(pchms, 'ascii'):
        return False
    # check that pchms is valid latin_1
    if not validate_decodeable(pchms, 'latin_1'):
        return False
    # validate that pchms is invalid unicode
    if validate_decodeable(pchms, 'utf_8'):
        return False

    # check that pchms produces a large 32-bit integer with any alignment
    for byteorder in ['big', 'little']:
        if int.from_bytes(pchms, byteorder) < lower_bound:
            return False
    
    return True


def random_pchmessagestart() -> bytes:
    random.seed()
    
    while True:
        int_array = [random.randrange(128, 256) for i in range(4)]
        pchms_candidate = bytes(int_array)
        if validate_pchmessagestart(pchms_candidate):
            return pchms_candidate


def replace_pchms(chainparams: str) -> str:
    modified = chainparams
    mapping = REPLACES_PCHMS

    for key, value in mapping.items():
        old_bytes = bytes.fromhex(key)
        new_bytes = bytes.fromhex(value)

        for i in range(len(old_bytes)):
            old_declare = PCHMS_FORMAT.format(i, old_bytes[i])
            new_declare = PCHMS_FORMAT.format(i, new_bytes[i])
            modified = modified.replace(old_declare, new_declare)

    return modified
        


def replace_params(chainparams: str) -> str:
    modified = chainparams

    # remove seed dns servers
    modified = re.sub(EMPLACE_RE, '', modified)
    # remove chain checkpoints
    modified = re.sub(CHECKPOINTS_RE, EMPTY_CHECKPOINTS, modified)
    # replace genesis block stuff
    for key, value in REPLACES_PARAMS.items():
        modified = modified.replace(key, value)
    # replace message start strings
    modified = replace_pchms(modified)
    
    return modified


def main():
    with open(CHAINPARAMS_CPP_PATH) as chainparams_file:
        chainparams_source = chainparams_file.read()

    modified_chainparams_source = replace_params(chainparams_source)
    

    with open(CHAINPARAMS_CPP_PATH, 'w') as chainparams_file:
        chainparams_file.write(modified_chainparams_source)


if __name__ == '__main__':
    main()
