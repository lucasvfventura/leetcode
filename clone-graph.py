"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        stack = [node]
        visited = {}
        while stack:
            n = stack.pop()
            visited[n.val] = [nb.val for nb in n.neighbors]
            for nb in n.neighbors:
                if visited.get(nb.val) == None:
                    stack.append(nb)

        nodes = {i: Node(i) for i in range(1, len(visited) + 1)}
        for i in range(1, len(visited)+1):
            n = nodes[i]
            n.neighbors = [nodes[j] for j in visited[i]]

        return nodes[node.val]