- Sources of incompletedness include:
	- Sensor limitations (may be impossible to perceive the entire state)
	- Intractability (full state description too large to store/compute)
- Sources of non-determinism everywhere, such as human interference, dice, mechanical failure, weather
## Adversarial Search
- Different players get to choose actions at various points
- Need new algorithms taking other player's actions into consideration
- Initial state and set of actions define a game tree

## Formulation of Game
- `S_0` = initial state
- `toMove(S)` the player whose turn it is to move in state `s`
- `Actions(s)` the set of legal moves in state `s`
- `Results(s, a)` the transition model, defining the state resulting from taking an action
- `isTerminal(s)` which is true if the game is over
- `Utility(s, p)` defining the numeric value to player `p` at the end 

## Single Agent Search Tree
- One agent moves
	- Mario moves, each action is -1 utility, get coin = +10 utility and terminate
### Value of a State
- The best achievable outcome from that state
- `V(s) = max_{s'children(s)}V(s') if not isTerminal(s);`
- `V(s) = Utility(s) if isTerminal(s)`

## Adversarial Game Tree
- Two agents move in turn (Mario and Goomba)
	- If Mario killed by Goomba, `Utility(s) = -inf` and terminates
	- Assuming Mario can jump only when getting coin (cannot jump kill or around Goomba)

## Perfect Play: Minimax Algorithm
- A zero-sum two player game between MAX and MIN
	- Moves alternate
- Assume we have a utility/value that we can apply for any game position
	- positive s is good for MAX
	- negative for MIN
- Whenever MAX has more move in the position s, they choose the move that maximises the value of utility, assuming that MIN chooses optimally
- Whenever MIN has the move in position s, they choose the move that minimises the value of utility, assuming MAX chooses optimally
```python
MINIMAX(s):
	= Utility(s, MAX), if isTerminal(s)
	= max_{a for all actions(s)}MINIMAX(Results(s,a)), if toMove(s) = MAX
	= min_{a for all actions(s)}MINIMAX(Results(s,a)), if toMove(s) = MIN
```
- The tree is generated top-down, starting from the current position to the leaves
- Then Minimax is applied bottom-up, from leaves to current
- A ply means one move by player, bringing us one level deeper
```
Complete = yes, for finite
Optimal = yes, against optimal opponent
Time = O(b^m), all nodes
Space = O(bm), depth first search
```
- For a big game like chess, expanding to terminals is unfeasible
- Standard approaches:
	- Cut off test
	- Evaluation function
		- Still perfect play ***if*** we have a perfect evaluation function
```python
def MINIMAX(state) -> action:
	inputs = current state
	v = MAXVALUE(state)
	return action #in successors state with value v


# the following functions call each other recursively
def MAXVALUE(state) -> Utility:
	if isTerminal(state):
		return Utility(state)
	v = -inf
	for a, s in successors(state):
		v = MAX(v, MINVALUE(s))
	return v

def MINVALUE(state) -> Utility:
	if isTerminal(state):
		return Utility(state)
	v = +inf
	for a, s in successors(state):
		v = MIN(v, MAXVALUE(s))
	return v
```

## Cutting Off Search
- We can cut off at a fixed depth
	- Works well for simple games
	- Depth-limited search
- Often required to manage time taken per move
	- Can be hard to turn time into a cut off depth
	- Iterative deepening

## Evaluation Functions
- We expand as far as we can, and apply some judgement to decide which positions are best
- Define a linear weighted sum of relevant features
- `eval_func(s) = w1 * f1(s) + w2 * f2(s)...`
	- where w's are weightings of a function, i.e. w1 = 9 and f1 = no. white vs black queens
- The quality of the player depends critically on the quality of the evaluation function
- Should:
	- Agree with the utility function on terminal states
	- Reflect the probability of winning
	- Be time efficient
- Only ordering, not exact values matter
	- Measure of certainty required

## Alpha-Beta Pruning
- Identify nodes that cannot be better than those that we have already seen
- Keep track of possible values for each internal node