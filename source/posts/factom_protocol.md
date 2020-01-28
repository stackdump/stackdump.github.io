# Factom Protocol

The Factom Protocol is run by a decentralized community of Federated Nodes
and hosts several interconnected layer 2 tokens.

Chains & Entries
----------------

The Base layer of the blockchain provides data storage that is 
made immutable via merkle hash and anchoring.

The Factom Blockchain produces a new Directory box every 10 min.
An index of entries to each chain is maintained by the network.


Dual Tokens
-----------

On the Factom Blockchain where are two types of tokens:

* *EntryCredits(ECs)*: non-transferable token
  * Are burned when a user stores data on the factom blockchain.

* *Factoids(FCT)*: fungible token
 * Can be converted into entry credits at a constant $.001/kb rate based on market oracle.
 * Can be burned into PegNet market

Second Layer Protocols
----------------------

FAT, PegNet, smart contracts etc... 

Maintenance to PegNet has shown that broad sweeping design changes
can be built and deployed iteratively.

This allows the protocol to adjust itself to evolving circumstances.
For example: PegNet has been connected via state channel to an ERC20 token.

Additionally, PegNet was intially injected with tokenized collateral from the Factom ecosystem.
This allowed users who have been steaked (officially or not) in the factom protocol to invest
in the new one being bootstrapped.

SideChain Anchoring
-------------------

One other design that is possible is to use a so called 'out-of-band' approach.

This means running some process off-chain, and then reporting the state back to the FactomProtocol.
Essentially this allows for arbitrary operations to be attached to the blockchain's immutability.

Not all approaches would necessarily rely soley on public blockchain data, but as in the
case of PegNet, it could be desirable to do so.

PegNet: Future Work
-------------------

The current protocol has tested to be stable under very high bursts of load,
in addition to over 90 Entries-per-Second (my personal test on a 5 node network).

I'm excited to see what else can evolve on top of PegNet.
I'm currently in the process of drafing a PIP to help design pFinance and will post more as it's available.

For now you can follow the progress on github https://github.com/stackdump/pfinance-primitives
