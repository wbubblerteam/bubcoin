// Copyright (c) 2015-2019 The Bitcoin Core developers
// Distributed under the MIT software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

/**
 * Functionality for communicating with Tor.
 */
#ifndef BUBCOIN_TORCONTROL_H
#define BUBCOIN_TORCONTROL_H

#include <string>

class CService;

extern const std::string DEFAULT_TOR_CONTROL;
static const bool DEFAULT_LISTEN_ONION = true;

void StartTorControl(CService onion_service_target);
void InterruptTorControl();
void StopTorControl();

CService DefaultOnionServiceTarget();

#endif /* BUBCOIN_TORCONTROL_H */
