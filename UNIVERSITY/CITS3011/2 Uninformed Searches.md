## Reflex Agents
- Choose action based on current precept
## Formulation of Search
- A state space
- A successor function (actions and costs)
- A start state
- A goal state and test
## State Space Graph
- A formal representation of a search problem
	- Nodes are states, edges are successor functions
	- In the graph, each state only occurs once
## Search Tree
- Search is to find the best path from the start to the goal on the state space graph
- A search tree is a tree of plans, searching on the state space graph
- The search tree represents paths in the partial state space graph
- Nodes represent states
	- Start is the root
	- Children are from the successor function
- Expending a node means applying the successor function, generating new states
- Path cost is the accumulative cost along the path
- Usually, the whole tree is too large to fully build
- In the tree, each state can occur many times
- The fundamental idea is:
	- At any given moment we are in some state `s`
	- `s` will usually offer several possible actions
	- Choose one action to explore first
	- Keep `s` and the other actions to explore later, in case the first one doesn't deliver
- Action selection determined by search strategy
``` python
function TREE-SEARCH(problem, fringe) return solution or failure
	fringe <- INSERT(MAKE-NODE(INITIAL-STATE[problem]), fringe)
	loop do
		if EMPTY(fringe) then return failure
		node <- REMOVE-FIRST(fringe)
		if GOAL-TEST[problem] applied to STATE[node] succeeds:
			then return SOLUTION(node)
		fringe <- INSERT-ALL(EXPEND(node, problem), fringe)
```
- The search strategy solely depends on the fringe strategy
	- All fringes are priority queues, each element in the fringe is a current leaf node
	- Different methods setting the priority lead to different search algorithm
## Comparing Search Strategies
- The performance of search strategies is generally compared in four ways
	- Completeness
	- Optimality
	- Time complexity
	- Space complexity
		- `b` maximum branching factor
		- `m` maximum depth 
		- `d` depth of least cost solution
### Uninformed Search Strategies
- Breadth-first search
	- Expand the shallowest node next
	- Complete: yes if `b` is finite
	- Optimal: Yes if all costs are equal
	- Time: `O(1+b+b^2+...+b^d)=O(b^d)`
	- Space: `O(b^d)`, all nodes at one level have to be stored simultaneously
- Uniform-cost search
	- Expand the lowest cost node next
	- Complete: yes if all step-costs >= 0
	- Optimal: As above
	- Time: `O(n)` where `n` is the number of nodes with cost less than the optimum
	- Space: as above
- Depth-first search
	- Expand deepest node next
	- Complete: no, fails in infinite-depth spaces
	- Optimal: no, could hit any solution first
	- Time: `O(b^m)`, follows paths "all the way down"
	- Space: `O(bm)`, it only needs to store the current path plus untried alternatives
- Depth-limited search
	- Depth-first but with cut-off depth
- Iterative deepening depth-first search
	- Depth-limited repeated, with increasing cut-offs
	- Complete: yes 
	- Optimal: Yes for constant step-costs
	- Time: `O(1+b+b^2+...+b^d)=O(b^d)`
	- Space: `O(bd)`
- Bidirectional search
	- Search from both ends concurrently
