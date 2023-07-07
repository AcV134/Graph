# Graph
Ready-to-use graph module <br>

## Motivation

Never having a graph module like Tree,Linked List etc bothered me. Hence i decided to custom make a graph module.

## Installation

- Download graph.py and add it to the folder
- Import the Graph class to the required file

```python
from graph import Graph
```

## Functions available:

+ `insert_node(a,b,c = 0)` :- inserting node a,node b with connection a->b, length (if given) c <br>
+ `lengthf(a,b)` :- Length between nodes a nd b <br>
+ `path()` :- prints all connections between nodes <br>
+ `all_paths(start,visited = None,value = 0)` :- prints all the possible traversal from node 'start' <br>

## Credit

- https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm#:~:text=Breadth%20First%20Traversal&text=We%20implement%20BFS%20for%20a,left%20with%20no%20unvisited%20nodes.
- https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
