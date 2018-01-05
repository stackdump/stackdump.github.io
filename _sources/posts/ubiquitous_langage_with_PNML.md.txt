# Petri-Nets as Mental Model for Domain Driven Design

One of the goals of Domain Driven Design is attempt to construct an [UbiquitousLanguage](https://martinfowler.com/bliki/UbiquitousLanguage.html)
that thoroughly describes a system.

By using a Petri-Net as a mental model during an [Event Storming](https://en.wikipedia.org/wiki/Event_Storming) session
contributors can document event designs using a specification that is both verifiable and executable.

Here we describe a technique for directly applying Petri-Net Markup Language (PNML) as an executable specification for domain events,
but first we will briefly introduce some of the principles at play.

### Theory of Computation

* In simple terms an algorithm is [computable](https://en.wikipedia.org/wiki/Computability) if a person can sit down with pencil and paper to solve the problem
  * That is to say there exists a general method of defining and attacking the problem.

Petri-Nets are known to be a good method of defining a ['concurrency-based model'](https://en.wikipedia.org/wiki/Computability#Concurrency-based_models)
of computation.

Wielding PNML as a formal specification for a [domain model](https://martinfowler.com/eaaCatalog/domainModel.html)
lets us build systems that has have verifiable runtime output.

### Application

Simply put: the aim of this technique is to name PNML elements: 'states' and 'transitions' --
in a way that creates a Ubiquitous Language that describes domain events.

Any Petri-Net can be convertible into a [vector addition system (with state) VASS](https://en.wikipedia.org/wiki/Vector_addition_system).

This vector system is useful as a state-machine API whereby we can validate events flowing through the system.

Additionally, using PNML in this manner constricts the degrees of freedom we use to construct a language,
because of this limitation we can assure that the constructed language is a *Regular Language* that is [not Turing complete](https://en.wikipedia.org/wiki/Petri_net#cite_note-14).

Kleene's theorem illustrates how Regular Languages and State Machines are two sides of the same coin.

### [Kleene's theorem](https://en.wikipedia.org/wiki/Regular_language#cite_note-RozenbergSalomaa1997-3)
    
    A [regular language](https://en.wikipedia.org/wiki/Regular_language)
    can be defined as a language recognized by a finite automaton.

Another way of describing this technique is:

* PNML serves as an [action language](https://en.wikipedia.org/wiki/Action_language) for
  * defining a formal state-transition system
  * that resulting system and provides a method to express that logic as a finite automaton

### Conclusion - what's the payoff?

This technique complements Domain Driven Design principles and further refines the practice of event-storming into a formal method.

Using PNML defined algorithms as state machines allows for localized actors to draw very concise context boundaries around event handlers.

Furthermore, by reducing the 'statefullness' of an application to mere vector addition,
  we can construct large systems that are easier to understand and validate.
  
#### Learn more

 See example languages describing fizz-buzz & a game Tic-Tac-Toe: [Using Petri-Nets to construct a language](dsl_creation.html)

