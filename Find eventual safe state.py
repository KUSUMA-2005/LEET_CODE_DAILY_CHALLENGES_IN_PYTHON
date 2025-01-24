'''There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).
Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.'''

class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # 0 = unvisited, 1 = visiting, 2 = safe
        n = len(graph)
        state = [0] * n  # State array for each node
        safe_nodes = []
        def dfs(node):
            if state[node]==1:
                return False
            elif state[node]==2:
                return True
            state[node]=1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2
            return True
        for i in range(n):
            if dfs(i):
                safe_nodes.append(i)
        return safe_nodes

'''Intuition
Nodes in a cycle cannot reach a terminal node, so they are not safe.
A safe node always leads to a terminal node or other safe nodes.
Detecting cycles helps us exclude unsafe nodes and find all safe ones.
Why Cycles?
Cycles cause infinite loops: Nodes in a cycle never reach a terminal node, making them unsafe.

If a node leads to a cycle, it also becomes unsafe because paths starting from it will never terminate.

By detecting cycles, we ensure that only nodes leading to terminal nodes or safe nodes are marked as safe.

Approach
Use DFS to mark nodes as:
0 (unvisited)
1 (visiting): Currently being explored.
2 (safe): Leads only to terminal or safe nodes.
Cycle Detection:
If a node is revisited while in the 1 (visiting) state, it’s part of a cycle and not safe.
Collect all nodes marked safe (2) and return them in ascending order.
Complexity
Time: (O(V + E)) — Each node and edge is processed once.
Space: (O(V)) — For state tracking and recursion stack.'''
