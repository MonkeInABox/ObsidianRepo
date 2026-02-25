# Two Systems for Thinking
- System 1: Intuition and instinct (unconscious, fast, associative)
- System 2: Rational thinking (effort, slow, logical)

# Why Reinforcement Learning
- Supervised learning is where a learning agent is provided with input-output pairs (state-action pairs) on which to base its learning
- However, learning is sometimes needed in less generous settings
	- No ground truth, otherwise no need to learn
	- No model of environment
	- No utility function
- An alternative is that the agent interacts with the world and periodically receives feedback about its performance
- Use rewards to learn a successful agent function
	- Usually easier than providing labelled examples on how to behave

# RL vs. Solving MDPs
- RL still formulates the problem as a Markov Decision Process
	- Set of states
	- Set of actions
	- Transition model
	- Reward function
- RL shares the same goal as MDPs, which is to find the optimal policy $\pi ^{*}$ that maximises the expected sum of rewards
- However, in RL, the transition model and reward function are unknown

# Passive Learning vs. Active Learning
- Passive is given a fixed policy, learns utilities of that policy in the unknown environment
- Active is no fixed policy, the agent must select actions and actively improve its policy to maximise the return

# Model-Based vs. Model-Free
- Model based: the agent explicitly builds a transition model of the world to help interpret the rewards and make decisions about how to act
	- The model may be initially unknown and the agent learns the model from observing the effects of its actions
	- Learn the rules and solve it
	1. Learn empirical model for the MDP: use observed states, actions and rewards $s_{0}, a_{0}, r_{0}, s_{1}, a_{1}, ...$ to give an estimate of the transition model
	2. Solved the learned empirical MDP: use value iteration or policy iteration as in the previous lecture
	3. Run the learned policy: if not good enough, add the new data and go to step 1
- Model free: the agent neither knows nor explicitly learns a transition model 
	- Instead the agent learns a more direct representation of how to act such as the action-utility functions
	- Play the game and learn from the experience

# RL Algorithms
## Passive
### Direct Utility Estimation
- Given fixed policy $\pi$ the goal is to learn the expected utility for each state
![[Pasted image 20251007140640.png]]
- Suppose the agent executes a set of trials in the grid-world example using the fixed policy $\pi$ we can gather this data:
![[Pasted image 20251007140630.png]]
- The idea is to estimate the utility from samples
- Calculate the reward-to-go, the total expected reward from each state onward
- For a new trial, repeat again and keep a running average for each state
- In the limit of infinite trials, the sample average will converge to the true value
	- However, all states are treated as independent, which limits usefulness, no transition model is used (model-free)
- Estimate is simple but not efficient
	- Ignores relation between successor states (Bellman Equation)
	- The agent misses opportunities to learn
### Adaptive Dynamic Programming (ADP)
- Takes such advantages by learning the transition model
1. Learn the transition model $P(s'|s,a)$ by counting samples
![[Pasted image 20251007141310.png]]
2. Plug the learned transition model into Bellman to estimate utilities
![[Pasted image 20251007141437.png]]
![[Pasted image 20251007142101.png]]
### Temporal Difference Learning
- Solving the underlying MDP is not the only way to bring the Bellman equations to bear on the learning problem
- Another way is to use the observed transitions to adjust the utilities so that they agree with the Bellman equations
	- The first probability part of the Bellman equation is unknown so we cannot compute the expectation
	- The second part, we can collect samples for this part to estimate the expectation
- Averaging the samples will give an approximation to the true utility
	- However, we only have one sample per observed transition
	- Therefore, we take a running average instead:
		- $U^{\pi}(s) =(1-\alpha)U^{\pi}(s) + \alpha(sample)$ 
- We have the temporal difference update, as above
- If  temporal difference term is 0, utilities have converged
- $\alpha$ is the learning rate
- Model free
![[Pasted image 20251007143749.png]]
### TD Q Learning
- Apply TD method to the action-utility function $Q(s,a)$ instead of the utility function $U(s)$ 
	- $Q(s,a)$ is the expected utility of taking a given action in a state
	- The optimal action can be easily extracted as the maximum value for all actions
 ![[Pasted image 20251007144415.png]]

### SARSA (State, action, reward, state, action)
- SARSA updates with action $a'$ that is actually taken
![[Pasted image 20251007144533.png]]

# On-Policy vs. Off-Policy
- TDQL is off-policy as it learns about a different policy than the one currently executing
- SARSA is on-policy as it learns about the same policy that it is currently executing

# Active Reinforcement Learning
- Always taking the current best action, may lead us to a sub-optimal policy, we also need to explore..................;............
- Gets to decide what actions to take
- The key is to enable exploration
- We can have the exploratory versions of the previous algorithms
- This is about the exploration vs. exploitation trade-off
	- Try unknowns to gain information vs. choose current best actions
- We should not be greedy in terms of the immediate next move
- We should be greedy in the limit of infinite exploration, or **GLIE**
- Several GLIE schemes:
	- Simplest is to choose a random action at time step $t$ with probability $1/t$ and to follow the greedy policy otherwise
	- A better one is to give higher weights to actions that re promising or uncertain
	- It can be implemented as an exploration function
- We should also ensure safe exploration, avoiding: states with negative rewards, state from which there is no escape, states that permanently limit future rewards
![[Pasted image 20251007150148.png]]

## Generalisation in Learning
- Ultimately, neither supervised learning nor reinforcement learning can expose an agent to all of the states it will ever need to deal with:
	- We need to generalise from what we learn about seen states to cope with unseen states
- Agents require implicit, compact representation
	- Weighted linear sum or features or evaluation function
	- Function approximation
	- Relating states to each other
- The hypothesis space for the representation must be rich enough to allow for the correct answer