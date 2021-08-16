// Copyright (c) 2011-2020 The Bubcoin Core developers
// Distributed under the MIT software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

#ifndef BUBCOIN_QT_BUBCOINADDRESSVALIDATOR_H
#define BUBCOIN_QT_BUBCOINADDRESSVALIDATOR_H

#include <QValidator>

/** Base58 entry widget validator, checks for valid characters and
 * removes some whitespace.
 */
class BubcoinAddressEntryValidator : public QValidator
{
    Q_OBJECT

public:
    explicit BubcoinAddressEntryValidator(QObject *parent);

    State validate(QString &input, int &pos) const override;
};

/** Bubcoin address widget validator, checks for a valid bubcoin address.
 */
class BubcoinAddressCheckValidator : public QValidator
{
    Q_OBJECT

public:
    explicit BubcoinAddressCheckValidator(QObject *parent);

    State validate(QString &input, int &pos) const override;
};

#endif // BUBCOIN_QT_BUBCOINADDRESSVALIDATOR_H
