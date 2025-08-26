## Expectimax Search
- The chance node calculates the expected utility. `P(s)` is that probability
```python
Expectimax(s):
	= Utility(s, MAX), if isTerminal(s)
	= max_{a for all actions(s)}Expectimax(Results(s,a)), if toMove(s) = MAX
	= min_{a for all actions(s)}Expectimax(Results(s,a)), if toMove(s) = MIN
	= sum_{a for all actions(s)}P(s)*Expectimax(Results(s,a)), if toMove(s) = CHANCE
```
- MIN nodes and MAX nodes are special cases of the CHANCE nodes
- How to set probability for the chance node:
	- For simple cases like dice, we calculate true probabilities
	- For complex cases, we may need to make assumptions

## Monte Carlo Tree Search
- Use simulations to approximate the true expected utility
	- Simulation: cheap strategy to roll-out game
	- Back-propagation: prop the outcome back up the path, updating estimated utility of each ancestor node
- The UCB1 formula (w is no. wins, n is no. simulations, N is number of sims of the parent, c is balancing factor. 1st term is how promising, 2nd term is how uncertain) $$\frac{w}{n}+c\sqrt{\frac{lnN}{n}} = \text{exploitation + exploration}$$
## Normalisation Trick
- A trick to get whole conditional distribution at once:
	- Select the joint probabilities matching the evidence
	- Normalise the selection (making it sum to one)