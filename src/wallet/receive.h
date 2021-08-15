// Copyright (c) 2021 The Bubcoin Core developers
// Distributed under the MIT software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

#ifndef BUBCOIN_WALLET_RECEIVE_H
#define BUBCOIN_WALLET_RECEIVE_H

#include <amount.h>
#include <wallet/ismine.h>
#include <wallet/transaction.h>
#include <wallet/wallet.h>

struct COutputEntry
{
    CTxDestination destination;
    CAmount amount;
    int vout;
};

#endif // BUBCOIN_WALLET_RECEIVE_H
