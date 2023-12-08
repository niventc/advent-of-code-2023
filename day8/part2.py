from __future__ import annotations
from math import lcm
from typing import Dict

class Node:

    def __init__(self, name, left: Node, right: Node):
        self.name = name
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.name}: ({self.left.name}, {self.right.name})"

nodes: Dict[str, Node] = {}

with open("input.txt") as file:
    path = file.readline().rstrip()
    file.readline()

    for line in file.readlines():
        (name, siblings) = line.split(" = ")
        (left, right) = siblings.rstrip()[1:-1].split(", ")

        left_node = nodes.get(left, None)
        if not left_node:
            left_node = Node(left, None, None)
            nodes[left] = left_node
        
        right_node = nodes.get(right, None)
        if not right_node:
            right_node = Node(right, None, None)
            nodes[right] = right_node

        node = nodes.get(name, None)
        if not node:
            node = Node(name, left_node, right_node)
        else:
            node.left = left_node
            node.right = right_node

        nodes[name] = node

for node in nodes.values():
    print(node)

print("---")

current_nodes = [node for name, node in nodes.items() if name[-1:] == "A"]
results = []

for node in current_nodes:
    found = False
    steps = 0

    while not found:
        for direction in path:
            found = node.name[-1:] == 'Z'
            if found:
                continue

            node = node.left if direction == 'L' else node.right

            steps += 1

    results.append(steps)

print(results)
print(lcm(*results))

# 13133452426987

# bit overkill on the structure... expecting some sort of graph traversal, could just be a dict[str, (str, str)]