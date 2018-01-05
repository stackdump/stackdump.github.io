DDD-Flow Graph
==============

Here we demonstrate a graph that resembles a Petri-Net
but represents Elements of Domain Driven Design
as they apply to Eventstorming

A Petri-Net inspired Graph Format
---------------------------------

.. graphviz::

   digraph G {
       subgraph cluster0{
           label="DDD-flow";

           subgraph ExternalSystem {
               node [shape=circle,style=filled,fillcolor=darkorchid1,fixwidth=true,width=1];
               "External";
           }

           subgraph Aggregate {
               node [shape=circle,style=filled,fillcolor=gray,fixwidth=true,width=1];
               "Aggregate";
           }

           subgraph Actor {
               node [shape=doublecircle,style=filled,fillcolor=yellow,width=1];
               "Actor";
           }

           subgraph TimerTrigger {
               node [shape=hexagon,style=filled,fillcolor=red,height=0.8];
               "Timer / Trigger";
           }

           subgraph Command {
               node [shape=rect,style=filled,fillcolor=orange,height=0.2];
               "Command";
           }

           subgraph DomainEvent {
               node [shape=rect,style=filled,fillcolor=green,height=0.2];
               "DomainEvent";
           }

           subgraph cluster2 {
               label="A Game of Tic-Tac-Toe";

               subgraph ExternalSystem {
                   node [shape=circle,style=filled,fillcolor=darkorchid1,fixwidth=true,width=1];
                   "GameMaker";
               }

               subgraph Aggregate {
                   node [shape=circle,style=filled,fillcolor=gray,fixwidth=true,width=1];
                   "Move History";
                   "Turn";
               }

               subgraph Actor {
                   node [shape=doublecircle,style=filled,fillcolor=yellow,width=1];
                   "PlayerX";
                   "PlayerO";
                   "Judge";
               }

               subgraph Trigger {
                   node [shape=hexagon,style=filled,fillcolor=red,height=0.8];
                   "WinnerFound";
                   "IsTurn";
               }

               subgraph Command {
                   node [shape=rect,style=filled,fillcolor=orange,height=0.2];
                   "new";
                   "next_turn";
                   "winner_x";
                   "winner_o";
               }

               subgraph DomainEvent {
                   node [shape=rect,style=filled,fillcolor=green,height=0.2];
                   "X";
                   "O";
               }

               "GameMaker" -> "new"
               "Judge" -> "new"
               "new" -> "Move History"
               "Judge" -> "winner_x"
               "Judge" -> "winner_o"
               "Move History" -> "winner_x"
               "Move History" -> "winner_o"
               "PlayerX" -> "X"
               "PlayerO" -> "O"
               "X" -> "Move History"
               "O" -> "Move History"
               "Move History" -> "next_turn"
               "next_turn" -> "Turn"
               "WinnerFound" -> "winner_x"
               "WinnerFound" -> "winner_o"
               "IsTurn" -> "X"
               "IsTurn" -> "O"
               "Turn" -> "X"
               "Turn" -> "O"
               "Judge" -> "next_turn"
           }

       }
       "External" -> "Command"
       "Command" -> "Aggregate"
       "DomainEvent" -> "Aggregate"
       "Aggregate" -> "DomainEvent"
       "Aggregate" -> "Command"
       "Actor" -> "Command"
       "Actor" -> "DomainEvent"
       "Timer / Trigger" -> "Command"
       "Timer / Trigger" -> "DomainEvent"

   }

