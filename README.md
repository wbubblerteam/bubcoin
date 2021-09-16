# Bubcoin Core integration/staging tree

http://bit.do/wbubblercore-org

## What is Bubcoin?

Bubcoin is

For an immediately usable, binary version of
the Bubcoin Core software, see https://github.com/wbubblerteam/bubcoin/releases, or read the
[original whitepaper](https://bubcoincore.org/bubcoin.pdf).

## Disclaimer

Cyrptocurrency sucks ass!!    
This is a joke    
It's worthless and low power consumption because it's got low proof of work difficulty    
Praise be to bub

What

## What is Bubcoin?

Bubcoin is a joke cryptocurrency for trading with your friends, and some scripts for automatically creating your own version with your own name, logo recolour, and genesis block message.

Forked from the bitcoin core software https://github.com/bitcoin/bitcoin/

NAME: Bubcoin    
CODE: BUB    
CODE ISO4217: XUB

## How to use Bubcoin?

Bubcoin is just bitcoin but renamed and restarted. This software is bubcoin core. You can use other software designed for bitcoin with this, by running it with custom parameters.

More info:

https://user-images.githubusercontent.com/26749912/131839369-d2c6ca76-62d8-46b5-b354-70668ac28b86.mp4


## License

Bubcoin Core is released under the terms of the MIT license. See [COPYING](COPYING) for more
information or see https://opensource.org/licenses/MIT.

## Development Process

Bubcoin core is a bitcoin core knockoff. The latest stable release tag is cloned from the upstream repo to a branch like upstream-release-0.21.1](https://github.com/wbubblerteam/bubcoin/tree/upstream-release-0.21.1). This is then merged into [upstream-release-latest](https://github.com/wbubblerteam/bubcoin/tree/upstream-release-latest).

From here the branching is a little convoluted:
### Scripts
- Scripts are written on the [scripts-latest](https://github.com/wbubblerteam/bubcoin/tree/scripts-latest). The reason is that I originally worked off the upstream master branch - see [scripts-master](https://github.com/wbubblerteam/bubcoin/tree/scripts-master) - before realising I needed to work off a stable release, and rebasing.
### Manual modifications
- Manual icon changes are made on the [manual-icons](https://github.com/wbubblerteam/bubcoin/tree/manual-icons) branch. These include the .icns file and the bitmap with altered text.
- Manual parameter changes are made on the [manual-chainparams](https://github.com/wbubblerteam/bubcoin/tree/manual-chainparams) branch. These include the proof of work difficulty and coin limit.
- Manual changes to information is made on the [manual-readme](https://github.com/wbubblerteam/bubcoin/tree/manual-readme) branch. Like this here.
- The [backporting](https://github.com/wbubblerteam/bubcoin/tree/backporting) branch is used for fixes to the release tag to make it buildable, like dead dependency download links.
### Automatic modifications
On these branches changes are made automatically using the scripts.
- [auto-icons](https://github.com/wbubblerteam/bubcoin/tree/auto-icons)
- [auto-chainparams](https://github.com/wbubblerteam/bubcoin/tree/auto-chainparams)
- [auto-rename](https://github.com/wbubblerteam/bubcoin/tree/auto-rename)

Finally, all of these branches are merged into [staging](https://github.com/wbubblerteam/bubcoin/tree/staging), and when staging is stable it's merged into the main branch.

In other words:
![branching](https://user-images.githubusercontent.com/26749912/133629533-27d2d4dd-c72b-4243-9cca-8dd2bf4d9726.png)


Scripts:
- [renamer](https://github.com/wbubblerteam/bubcoin/blob/main/renamer.py)
- [logo svg colour replacer](https://github.com/wbubblerteam/bubcoin/blob/main/relogoer.py)
- [logo renderer](https://github.com/wbubblerteam/bubcoin/blob/main/relogoer.sh)
- [chain parameter replacer](https://github.com/wbubblerteam/bubcoin/blob/main/rechainparamser.py)

The contribution workflow is described in [CONTRIBUTING.md](CONTRIBUTING.md)
and useful hints for developers can be found in [doc/developer-notes.md](doc/developer-notes.md).
