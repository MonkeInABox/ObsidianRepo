- MergeSort Algorithm
    Divides the array into smaller arrays, until they are arrays of one and then sorts them back by merging each of the smaller arrays together. O(nlogn) 
- Quick-Sort Algorithm
    Pick a pivot node, all less to the left, all more to the right. Repeat until sorted. O(nlogn) or O(n^2)
- Heap
    Min-heap: the parent node is less than the child node. Max-heap is the opposite. If a node is removed, it takes O(logn) to re-order (heapify function)
- Depth-First Search
    From root to left branch, to left, until there are no more leaves, then right branch. O(V+E)
- Breadth-First Search
    Level-order. Top, second row, etc
- Post-Order Search
    Left, right, root
- In-Order Search
    Left, root, right
- Pre-Order Search
    Root, left, right
- Dijkstra’s Algorithm
    Creates a priority search tree through an initial pass, uses this tree with weights to find the shortest path. O(V^2)
- Floyd-Warshall Algorithm
    For weighted directed graphs. Dynamic as it uses the previous results (is A > B + B > C better than A > C?)
- Kruskal’s Algorithm
    Minimum spanning tree algorithm. Builds a forest, takes least weighted edges first. Avoids cycles by checking if the final vertex has been previously visited. Combines forests together once all the vertices has been found, making sure that these joining edges are from different subsets. O(ElogE)
- Prim’s Algorithm
    Minimum Spanning tree algorithm. Start from a vertex, follow shortest edge to vertex not already in searched list. Each edge is inserted into a priority queue once and takes log time. O(ElogV) for adjacency list, O(V^2) for adjacency matrix