## Product Rule
$$P(a|b) = \frac{P(a,b)}{P(b)}$$ $$P(x_{1}, x_{2}, x_{3})=P(x_{1})P(x_{2}|x_{1})P(x_{3}|x_{1},x_{2})$$
## Bayes' Rule
$$P(a)P(b|a)=P(b)P(a|b)$$ $$P(cause|effect) = \frac{P(cause)P(effect|cause)}{P(effect)}$$
- Independent if probability of x given y is equal to x
- Bayesian nets: a technique for describing complex joint distributions using simple, local distributions
	- A directed, acyclic graph, including nodes and edges
	- A local conditional distribution for each node

## D Separation
- Answering conditional independence queries just from the graph
	- Study independence properties for triples
	- Analyse complex cases as composition of triples
```
L --> R --> T //triple type 1: causal chain
	//t not independent of l (active triple), t independent of l given r (inactive triple)
U <-- R --> T //triple type 2: common cause
	//t not independent of u, t independent of u given r
R --> T <-- F //triple type 3: common effect
	//r independent of f, r not independent of f given t
```
- A path is active if each overlapping triple is active
- Are X and Y D-separated given evidence variables {Z}?
	- Consider all paths from X to Y
	- If none are active, then X and Y are D-separated given Z
- X and Y are guaranteed conditionally independent given Z if X and Y are D-separated given Z
- 