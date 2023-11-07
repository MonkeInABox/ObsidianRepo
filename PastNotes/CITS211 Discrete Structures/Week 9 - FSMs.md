[[CITS2211 Discrete Structures]]

|   |   |
|---|---|
|Created|@September 27, 2023 4:51 PM|
|Class|Discrete Structures|
|Reviewed||

## FSMs

- A computer takes stimuli (inputs) and outputs a response in terms of these inputs
    - These inputs are the alphabet set

- The machines memory is represented by a set of states

- The machine has transitions from one state to another depending on stimulus provided

- One step from Q (start) is identified as the starting state, zero or more states may be accepting states (denoted by a double circle) if it is a good place to stop

> FSM : (Q, qoq_oqo​﻿, Σ, F , δ) where Q → the finite set of states, qoq_oqo​﻿ → is the start state, Σ → is the finite alphabet of input symbols, F → is a set of accepting states (may be empty), δ : Q x Σ → Q (The state transition function).

****************Computations & Behaviour of an FSM****************

- A trace of FSM M is a finite sequence of states and transition labels, starting and ending with a state
    - s(0), i(1), s(1), i(2)….. i(n), s(n)

- We say an FSM accepts an input string if there is a trace for that input string which leaves the FSM in an accepting state (i.e. i(1)i(2)…)

**********************************************Languages & Recognisers**********************************************

- The set of strings that are accepted by an FSM is the language that is recognised by the FSM
    - L(M), some set of Σ∗Σ^*Σ∗﻿

******************************************************Nondeterministic FSM (NFSM)******************************************************

- Produces a SET of possible next states