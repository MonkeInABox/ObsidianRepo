## General Tree Search
```python
function TREE-SEARCH(problem, fringe) returns a solution, or failure
	fringe ← INSERT(MAKE-NODE(INITIAL-STATE[problem]), fringe)
	loop do
		if EMPTY(fringe) then return failure
		node ← REMOVE-FIRST(fringe)
		if GOAL-TEST[problem] applied to STATE[node] succeeds:
			then return SOLUTION(node)
		fringe ← INSERT-ALL(EXPEND(node, problem), fringe)
```
- The fringe strategy: all fringes are priority queues, each element in the fringe is a current leaf node
	- Different methods setting the priority lead to different search algorithms
## Uninformed vs. Informed 
- Uninformed:
	- Selects nodes for expansion on the basis of distance/cost from the start state
	- Uses only information contained in the graph
	- No indication of distance to go
	- Uniform Cost Search:
		- Expand lowest-cost node next: no information about goal is used, nodes ordered by `path cost g(n)`, backward cost (the cost from that node to the bottom)
- Informed
	- Selects nodes for expansion on the basis of some estimate of distance to the goal state
	- Requires additional information, e.g. heuristic rules or evaluation function
	- Selects "best" node
	- Search Heuristics:
		- An estimate of how close a state is to a goal, designed for a particular problem
## Greedy Search
- Expand the node that appears to be closest to the goal
	- The estimate is based on the heuristics
	- Nodes order by `forward cost h(n)`
- The evaluation function or heuristic `h(n)` is the estimate of the cost of getting from `n` to the goal
	- `h_SLD(n) = straight_line_dist_from_n_to_end;`
- Complete: not always (incomplete in infinite state spaces)
- Optimal: no, returns first goal found
- Time: $O(b^{m})$ worst case, highly dependent on heuristics quality
- Space: $O(b^{m})$ worst case, keeps all nodes in memory
- A* gives us best of both greedy and uniform (minimises estimated path-cost to goal and minimises path-cost from start)

## A* Search
- Expend nodes using the estimate of total path-cost as out heuristic
	- Estimated total cost from start to goal via n
- A search contour is a useful way to visualise the search
	- A* is stretching the contours to the goal
- A* visits nodes in order of increasing `f` 
- It creates contours of nodes "stretching" to the goal
- If `f*` is the actual cost of the optimal solution:
	- A* visits all nodes `n` with $f(n) = f*$
	- And it visits some nodes `n` with $f(n) = f*$
- If `x` is the number of nodes `n` with $f(n) \leq f*$ 
	- Complete: yes, unless `x` is infinite
	- Time: O(x)
	- Space: O(x)

## Graph Search
```python
function GRAPH-SEARCH(problem, fringe) returns a solution, or failure
	closed ← an empty set
	fringe ← INSERT(MAKE-NODE(INITIAL-STATE[problem]), fringe)
	loop do
		if EMPTY(fringe) then return failure
		node ← REMOVE-FIRST(fringe)
		if GOAL-TEST[problem] applied to STATE[node] succeeds:
			then return SOLUTION(node)
		if STATE[node] is not in closed then
			add STATE[node] to closed
			fringe ← INSERT-ALL(EXPEND(node, problem), fringe)
```
- Graph search uses a closed set to avoid repeated states and improves efficiency (maybe at cost of optimality)
## A* Optimality
- A* tree search is optimal if heuristic is admissible
- A* graph search is optimal if heuristic is consistent
- A heuristic `h` is admissible `iff h(n) =< h*(n)` for all `n`
	- `h*(n)` is the actual cost from n to goal
- Consistent `iff h(n) =< c(n, a, n') + h(n')` for all n, a, n'
	- n' is successor to n by action a
	- Basically triangle inequality
	- n to the goal directly should be no more than `n` to the goal via any successor n'
	- Every consistent heuristic is admissible but no vice versa
- Note optimal means finds a best path
## A* Proof of Optimality
- Sufficient to show that no sub-optimal goal is ever visited
## Deriving Heuristics
- Relaxed subproblem: removing some constraints
- Sub-problem: only achieving part of the goal
### Assessing Heuristics
- Its effective branching factor
- Assume A* visits N nodes, and finds a solution at depth d
- The effective branching factor b* is the branching factor of a perfect tree
## Variants of A*
- Weighted A* and Anytime A*
	- Run weighted, starting from a big value for W
	- Run again with smaller
- Beam Search
	- Limits size of fringe
	- Keep only the top-k nodes with the best f(n)
	- Or keep only nodes with f(n) smaller than a threshold
	- Make the search contour only a focused portion
	- Make the search incomplete, sub-optimal, but more efficient (time and space)
- Iterative Deepening A* 
	- Modified depth-first search algorithm
	- Cut off is on f(n) not on depth
	- Gradually increasing the cut off
	- Without keeping all reached states in the memory, at the cost of visiting some states multiple times
- Simplified Memory-Bounded A*
	- SMA* with memory bound, using all memory available
		- Expands most promising node until memory is full
	- SMA* drops least promising node to make space for new nodes
	- When a node `x` is dropped, the f-cost of `x` is backed up in `x`'s parent node
