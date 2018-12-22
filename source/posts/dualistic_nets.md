Dualistic PetriNets
===================

In this post we explore an extention to the previous vector state machine design.

Fuzzy Logic
-----------

As a reminder - the notation use here is known as a VASS - a Vector addition system with states.

Previously we have shown how a Petri-Net can be transformed into a set of vector transformations.
This system had a rule that state is persisted only if its output results in a valid state (no negative numbers).

Dualistic Petri-Nets provide a way to connect two Petri-Nets that have states in common.
This adds additional dimentionality to the system allowing for the behavior of one net to affect another.

We can introduce this concept as an extension to the VASS design with the introduction of
a new type of vector transformation called a Guard.

Guards
------

Vectors transforms we term as 'guards' can be used to inhibit the action of a state transition.

This works by evaluting the guard ahead of the transition using a parallel-but-identical petri net.

This allows the net to contain conditional statements that assert a condition about the
overall network before applying state change.


Demo
----

Let's examine a simple net that describes a system that requires turn taking 

:TODO: finish this post! adding a digram for a game of nim
https://en.wikipedia.org/wiki/Nim
