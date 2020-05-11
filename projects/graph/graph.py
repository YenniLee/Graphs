"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge 
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While q is not empty:
        while qq.size() > 0:
            # dequeue/pop first vertex
            path = qq.dequeue()
            # if not visited/not in traversed set of vertices
            if path[-1] not in visited:
                # DO THE THING!!!
                print(path[-1])
                # mark aas visited 
                visited.add(path[-1])
                # enqueuue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        ss = Stack()
        # Push starting vertex into stack
        ss.push(starting_vertex)
        # Create a set to store visited vertices 
        visited = set()
        # While stack is not empty
        while ss.size() > 0:
            # Pop the first vertex 
            v = ss.pop()
            # Check if it has already been visited
            if v not in visited:
                # Mark vertex as visited 
                visited.add(v)
                # DO THE THING !!!
                print(v)
                # Push all of its neighbors onto stack 
                for neighbor in self.get_neighbors(v):
                    ss.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
    
        # Check if node has been visited
        if starting_vertex not in visited:
            # Mark as visited
            visited.add(starting_vertex)
            # DO THE THING 
            print(starting_vertex)
            # Call dft_recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        qq = Queue()
        # enqueue starating vertex
        qq.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # while q is not empty
        while qq.size() > 0:
            # dequeue the first vertex
            path = qq.dequeue()
            # grab the vertex from the end of the path 
            last_vert = path[-1] 
            # Check to see if vertex has been visited
            if last_vert not in visited:
                # Mark as visited
                visited.add(last_vert)
                # Check to see if it is the target
                if last_vert == destination_vertex:
                    # Search found!
                    return path 
                # else keep looking/movee onto its neighbors
                # enqueue a path to all its neighbors
                for neighbor in self.get_neighbors(last_vert):
                    new_path = list(path)
                    new_path.append(neighbor)
                    qq.enqueue(new_path)
                    


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack
        ss = Stack()
        # push a path to starting vertex
        ss.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while stack is not empty
        while ss.size() > 0:
            # pop the first path
            path = ss.pop()
            # grab the vertex from the end of the path 
            last_vert = path[-1]
            # Check if it has been visited
            if last_vert not in visited:
                # Mark it as visited
                visited.add(last_vert)
                # Check if it is the target!s
                if last_vert == destination_vertex:
                    return path
                # if not destination target, move on to its neighbors
                for neighbor in self.get_neighbors(last_vert):
                    new_path = list(path)
                    new_path.append(neighbor)
                    ss.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # check if vertex has been visited
        if starting_vertex not in visited:
            # Mark as visisted 
            visited.add(starting_vertex)
            print(starting_vertex)
            # Check to see if vertex is destination target
            if starting_vertex == destination_vertex:
                # return starting path
                return [starting_vertex]
            # else call dfs_recursive on neighbors
            for neighbor in self.get_neighbors(starting_vertex):
                # Check to see if neighbor vertex has been visited
                if neighbor not in visited:
                    # call dfs_recursive on neighbor vertex
                    new_path = self.dfs_recursive(neighbor, destination_vertex, visited)
                    if new_path != None:
                        return [starting_vertex] + new_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
