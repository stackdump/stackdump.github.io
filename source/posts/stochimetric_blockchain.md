Blockchain Design Fundamentals
==============================


Truth is in the eye of the TokenHolder
--------------------------------------

There have been several blockchain implemenations where a good portion of the
protocol depended on the proper calculations made by the Wallet application.

Most recently I was involved with the launch of PegNet.
PegNet utilizes the Factom Blockchain to store chain entries and 
guarentee the order of execution for valid entries.

One main benefit of this design is that changes can be rapidly deployed
without having to update blockchain nodes.

The principle of this design conforms to the fundamental aspects
of CQRS and Domain Driven Design. While anyone can write events to the blockchain,
only valid event data is processed to calculate current balances.

This pushes most of the rules of the chain out to the wallets.

Factom uses consensus to agree on the state of the chain but is not
involved in the execution or finality of each transaction.

Blocks are minted every 10 min, and so PegNet uses this boundary as a sync point.

After each block as been created, a transaction is finalized.

Depending on the intended use case, it could be considered that
any valid entry broadcast to MainNet is final as soon as it's been Ack'd

Tokens Can do Anything
----------------------

Recall that one of the original applications of Petri-Nets was to
model chemical reactions.

As we can design tokens in a theoretical ideal gas.

With complete certainty, we can fully describe the behavior of any given token.

We're still in the phase of adoption where blockchains are being used for things experimentally.

On the technical side such a wide variety of solutions being engineered.

On the market side, we've see again a huge variety.
Here companies and organizations are attempting to achieve multiple goals:
#. mooning ride the bubble to get rich quick
#. build & brand some cause or idea
#. connect existing enterprise infrastructure
#. study new techniques and use cases


What's the Limiting Factor
--------------------------

Using tokens for analysis. After crafting such a careful mathematical model we put it to work.

Future: Event Modeling on Blockchains
-------------------------------------

could be a state channel
part of an oracle
like pegnet it could represent a social contract to execute 
some domain rules
