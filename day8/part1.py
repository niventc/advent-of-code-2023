from __future__ import annotations
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


found = False
steps = 0
current_node = nodes['AAA']

while not found:
    for direction in path:
        if current_node.name == 'ZZZ':
            found = True
            continue

        print(f"{current_node} going {direction} - {steps}")
        if direction == 'L':
            current_node = current_node.left
        else:
            current_node = current_node.right
        steps += 1


print(steps)

# 12643