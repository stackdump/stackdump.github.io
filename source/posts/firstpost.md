Blockchains & State Machines 
============================

In this post we examine some deterministic state machines
and explore possible application to blockchain technology.

Vector Addition Systems are Petri-Net Equivilant
------------------------------------------------

A [Vector Addition System (with States) VASS](https://en.wikipedia.org/wiki/Vector_addition_system)


    A vector addition system consists of a finite set of integer vectors.
    An initial vector is seen as the initial values of multiple counters,
    and the vectors of the VAS are seen as updates.
    These counters may never drop below zero.

    More precisely, given an initial vector with non negative values,
    the vectors of the VAS can be added componentwise,
    given that every intermediate vector has non negative values.


Introducing Bitwrap Machines 
----------------------------

#### Program code expressed as a counter machine

A Bitwrap machine can be explained as follows:

    1. It declares a single 'state-vector' of size 'n'
       * the machine is said to have 'n' places
       * each place(n) has a pre-defined inital value.
    2. 'transitions' are defined as a set of delta vectors
       * of size 'n' 
       * containing positive or negative integers.
    3. Transactions are applied to the current state vector using vector addition.
    4. The 'state-vector' is stored after each valid transaction.
    5. No place(n) may store a negative value.
       * only valid output states are stored

#### Using a Petri-Net to design a bitwrap machine

![tic-tac-toe state machine](http://www.blahchain.com/image/octoe.png)

The state machine above models a game of tic-tac-toe.

    NEW[1] turn_x[0] turn_o[0] M00[1] M01[1] M02[1] M10[1] M11[1] M12[1] M20[1] M21[1] M22[1]

    => [ 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

Notice that we can map each 'Place' from the diagram to a position in a vector below:

    # inital state:
    => [ 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    # Begin:
    +  [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    => [ 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    # Move X11:
    +  [ 0,-1, 1, 0, 0, 0, 0,-1, 0, 0, 0, 0]
    => [ 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]

    # Move O11:
    +  [ 0, 1,-1, 0, 0, 0, 0,-1, 0, 0, 0, 0]
    => [ 0, 1, 0, 1, 1, 1, 1,-1, 1, 1, 1, 1] # INVALID!

    # Move X00:
    +  [ 0,-1, 1,-1, 0, 0, 0, 0, 0, 0, 0, 0]
    => [ 0,-1, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1] # INVALID!

    # Move O00:
    +  [ 0, 1,-1,-1, 0, 0, 0,-1, 0, 0, 0, 0]
    => [ 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1]

This is this Turing complete?
-----------------------------

Definitively *NO* - elementary Petri-Nets are only made turing complete by extending the rules to add conditionals called 'Inhibitor Arcs'.

However - Bitwrap does allow for Inhibitor Arcs as a useful way of declaring a role.
* The role feature is still a [work in progess](https://github.com/bitwrap/bitwrap-machine/blob/master/bitwrap_machine/dsl.py#L10).

### Application to Blockchains

By combining this deterministic model with an event store,
we can now reliably architect applications and services designed to span multiple blockchain providers and notations.

Conclusion
----------

The bitwrap state machine algorithm relies only on mathematical primitives.
Each transaction is modeled by deterministic operations represented as vector addition.

This determinism makes Bitwrap machines ideally suited as a method of
modeling event data using an eventstore, ledger, or a blockchain database.


Read [More Articles](?post=articles)
