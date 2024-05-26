# Graph Searching Algorithms
Allows you to search for a path between two nodes in a graph using different algorithms.

### Algorithms
- Breadth First Search
- Depth First Search
- Greedy Search
- A* Search
- Uniform Cost Search

### Install
```shell
pip3 install -r requirements.txt
```
You also need to install [Graphviz](https://graphviz.org/download/) to visualize the graph.

### Usage
```shell
python3 main.py
```

### Example Output
### Image
![Graph](https://github.com/Scot-Survivor/Graph-Searching/blob/master/docs/example.png?raw=true)
#### Print Output
```shell
Enter number of nodes: 4
Enter max cost: 5
Enter max heuristic: 5
Enter number of goals: 1
               GRAPH
        _______1(C: 0,H: 0)__________________      
       /                                     \     
2(T)(C: 2,H: 2)                   _____3(C: 5,H: 3)
                                 /                 
                           4(C: 5,H: 3)            
______________________________
Breadth First
1 2 
Depth First
1 2 
Greedy
1 2 
A Star
1 2 3 4 
Uniform
1 2 



BFS Visits:  2
DFS Visits:  2
Greedy Visits:  2
A* Visits:  4
Uniform Visits:  2




Number of Nodes:  4
Number of Goals:  1


Goal List: 2
```
