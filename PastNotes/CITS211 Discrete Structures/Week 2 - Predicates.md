

|   |   |
|---|---|
|Created|@August 2, 2023 10:33 AM|
|Class|Discrete Structures|
|Reviewed||

Predicates are an incomplete sentence that needs to be filled with one or more things to make a complete statement.

- needs terms to make a complete sentence

> Predicate: a statement whose truth depends on the value of one or more terms.

Predicate: ∀x. (P(x) → Q(x))

Propositional: P → Q

e.g. let b = this book, H = is heavy: therefore: H(b) = this book is heavy

the number of places that a predicate has is called its arity

We will now define the **formal language** of predicate logic.

1. The alphabet of predicate logic contains symbols for denoting predicates called predicate symbols, for example, P, Q and R, each one with a given fixed arity (number of arguments needed). It also includes constants (a, b, c etc), variables (x, y, z etc), function symbols (f , g, h), punctuation symbols (namely parentheses, ( ), and a dot), quantifiers (∀ and ∃), and the propositional connectives ¬, ∨, ∧, →, ↔.

2. The syntax of predicate logic is defined by the following rules for construction of formulas: A predicate with the right number of arguments is a formula. If φ and ψ are formulas, then so are ∀x.φ, ∃x.ψ, ¬ φ, φ ∧ ψ, etc. And build recursively.

3. A slightly complicated definition (which we will come to) tells us when a variable in a formula is free or bound. Formulas with no free variables are called sentences (or sometimes propositions or statements, the same as in propositional logic).

> Bound variables are an occurrence of a variable which has been introduced by a quantifier in that formula and lies within the scope. These can be replaced.

> Free variables in a formula is an occurrence of a variable which does not lie in the scope.

e.g. (∀x.child(x)) ∧ clever(x) The first x is bound and the second is free. That is, the x for clever is not the same as the x of child. (∀y.child(y)) ∧ clever(x) means the same.

**********************************************************************VALIDITY, SATISFIABILITY, EXAMPLES:**********************************************************************

Validity:

- a tautology evaluates to true no matter what truth values are assigned to individual propositional variables

- validity is if a formula evaluates to true no matter what value the propositional variables take, it is valid (and a tautology)

Satisfiable:

- is if some setting of the variables makes it true (i.e. not a contradiction)