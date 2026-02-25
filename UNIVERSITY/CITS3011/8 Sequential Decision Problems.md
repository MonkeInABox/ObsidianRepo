- A problem where the utility obtained by an agent depends on a sequence of decisions
- SDPs generalise the searching problems that we have seen:
	- Search algorithms aim to find a sequence of actions for one start state
	- SDPs aim to find a policy for how to act from any possible state
- A policy is a set of state-action rules
	- For each state which action to take
	- Turns a utility-based agent into a simple reflex agent
# Markov Decision Process
- Fully observable, stochastic environment with a Markovian transition model and additive reward
	- Given the present state, the future and the past are independent
- Components of MDP:
	- Set of states
	- Actions in each state
	- Transition model (world model) $P(s'|s, a)$
	- Reward function
## Optimal Policy $\pi*$ 
- Specifies what the agent should do for any state
- Depends on many factors
	- Transition model
	- Terminal utilities
	- Step-cost
## Discounted Reward
- It is reasonable to maximise the sum of rewards
- Therefore, it is reasonable to have additive discounted rewards
- $\gamma$ is the discount factor, between $0-1$ 
	- $\gamma \approx 0$ prefer short term rewards, opposite for $\gamma \approx 1$

## Infinite Horizon
- Finite horizon means that there is a fixed time limit after which the game is over, optimal action in a given state may also depend on time left, this is nonstationary
- With discounted rewards, the utility on an infinite horizon will converge on a finite number
- Given a policy $\pi$ we can determine agents expected utilities if it follows that policy starting in state $s$ $$U^{\pi}(s) = E[\sum\limits^{\infty}_{t=0}\gamma^{t}R(s_{t},\pi(s_{t}),s_{t+1})]$$
- True utility: $$U(s) = E[\sum\limits^{\infty}_{t=0}\gamma^{t}R(s_{t},\pi^{*}(s_{t}),s_{t+1})]$$
- Given a utility for each state, we can determine the optimal policy for the agent (action determination): $$\pi^{*}(s) = argmax_{a\epsilon Actions(s)}\sum\limits_{s'}P(s'|s,a)[R(s,a,s')+\gamma U(s')]$$
# Bellman Equation
- Combining previous two determination, we can have a direct relationship between the utility of a state and the utilities of its neighbours $$U(s) = max_{a\epsilon Actions(s)}\sum\limits_{s'}P(s'|s,a)[R(s,a,s')+\gamma U(s')]$$
## Q-Function
- Another important quantity is the action-utility function or Q-function which is the expected utility of taking a given action in a state
$$U(s) = max_{a\epsilon Actions(s)} Q(s, a)$$
- The optimal policy can also be extracted from the Q-function: $$\pi^{*}(s) = max_{a\epsilon Actions(s)} Q(s, a)$$
# Solving SDP
## Value Iteration
- Basic Idea:
	- Determine the true utility of each state
	- Then determine the optimal action in each state, by action determination
- To determine the utility of each state, use iterative approximation:
	- Start with arbitrary utilities $U$
	- Update $U$ to make them locally consistent with Bellman Equation
	- Repeat until $U$ is "close enough"
- This has been proved to converge under reasonable assumptions
``` python
function Value_Iteration(MDP, $\epsilon$) returns utility_func:
	loop:
		U <- U'
		$\delta$ <- 0
		for each state s in S:
			U'[s] <- R(s) + $\gamma$ max\sum P(s'|s, a) U[s']
			if |U'[s]-U[s]| > $\delta$:
				$\delta$ <- |U'[s] - U[s]|
	until $\delta$ < $\epsilon$(1-$\gamma$)/$\gamma$ 
	return U
```
## Policy Iteration vs. Value Iteration
- Both compute the same thing
- Value iteration repeatedly applies Bellman update on the utility
- Policy iteration alternates between policy evaluation and improvement
- Computational Trade-Off:
	- Value Iteration:
		- Each iteration is cheaper 
		- But may require more iterations to converge
	- Policy Iteration:
		- Each iteration more expensive
		- Usually converges in fewer iterations
