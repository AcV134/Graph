# Graph
Ready-to-use graph module 

## Motivation

Never having a graph module like Tree,Linked List etc bothered me. Hence i decided to custom make a graph module.

## Installation

- Download `graph.py` and add it to the folder
- Import the Graph class to the required file

```python
from graph import Graph
```

## Functions available:

+ `insert_node(a,b,c = 0)` :- inserting node a,node b with connection a->b, length (if given) c
+ `lengthf(a,b)` :- Length between nodes a nd b 
+ `short(a,b,flag = False)` :- Finding shortest path between a and b if flag is `False` else finding the distance between all paths from a to b
+ `all_length(leng,a,b)` :- Called by `short` to display all the lengths between a and b
+ `spath(a,b,visited = None)` :- Called by `short` to find all the paths between a and b
+ `all_Traversal()` :- Prints all the travesal paths 
+ `path()` :- prints all connections between nodes 
+ `Traversal(a,visited = None,value = 0)` :- prints all the possible traversal from node a

## Credit

- https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm#:~:text=Breadth%20First%20Traversal&text=We%20implement%20BFS%20for%20a,left%20with%20no%20unvisited%20nodes.
- https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
