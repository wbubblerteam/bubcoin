// Copyright (c) 2021 The Bubcoin Core developers
// Distributed under the MIT software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

#ifndef BUBCOIN_UTIL_THREAD_H
#define BUBCOIN_UTIL_THREAD_H

#include <functional>

namespace util {
/**
 * A wrapper for do-something-once thread functions.
 */
void TraceThread(const char* thread_name, std::function<void()> thread_func);

} // namespace util

#endif // BUBCOIN_UTIL_THREAD_H
