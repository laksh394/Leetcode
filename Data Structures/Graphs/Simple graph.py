# Graph Data Structure using Adjacency Matrix
# An adjacency matrix is a 2D array of size 𝑉×V, where 𝑉 is the number of vertices in the graph. Each cell 𝑀[𝑖][𝑗] in the 
# matrix represents the presence or absence of an edge between vertices 𝑖 and 𝑗.

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * self.V for _ in range(self.V)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def display_matrix(self):
        for row in self.graph:
            print(" ".join(map(str, row)))

# Graph Data Structure using Adjacency List
# An adjacency list represents a graph as an array of lists. The size of the array is equal to the number of vertices.
# Each element of the array is a list containing a vertex's neighbors.

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(self.V)]  # Adjacency list representation

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display_graph(self):
        for i in range(self.V):
            print(f"{i}: " + " ".join(map(str, self.graph[i])))

# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.display_graph()
