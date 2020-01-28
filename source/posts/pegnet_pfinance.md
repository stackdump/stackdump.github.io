Case Study: PegNet
------------------

PegNet exists on top of the Factom Blockchain.

At it's core is a Distributed Oracle protocol that awards PEG to miners using LXRHash - a CPU mining algorithm.

One key point of design that's easy to overlook. PegNet's miners don't process transactions.

The two basic operations: conversion and transfer

Convertion: transforms one pAsset to annother at marker rates. taking effect after the FactomProtocol creates the next directory block.

Normally this is every 10 min.

Transfer: an end user just posts a signed message to the blockchain indicating a transfer - which can be calculated immediately, but is only
considered immutable after the block boundry.

Mining has reached an equilbrium between competing pools.
Even if a single entity mines - they are still incentivised to report the correct oracle data.

if it could be demonstrated that one party is altering the feed,
it would damage the value of the entire protocol.

Advanced PegNet: pFinance
-------------------------

Several PegNet Improvement Proposals describe ways to extend the types of economic behavior
from PegNet.

One such proposal suggests where should be a way to short tokens witout having a direct counterparty to the transaction.
Instead a user could transact against the PegNet Blockchain.

This can be thought of as a similar situation to playing a betting card game against the House.
The house plays by a static strategy to ensure that the player has a consistent chance to win.

PegNet could be extended in a similar way - where the protocol is playing by house rules.
The result of this play could mean that certain types of positions can only be opened
if the market is signalling in a certain way.

If these signals can be quantitized, they can also influnce the rate at which certain transactions are allowed to occur.
