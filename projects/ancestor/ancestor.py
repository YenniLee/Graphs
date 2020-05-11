class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")
    

def earliest_ancestor(ancestors, starting_node):
    
    earliest_ancestor = -1
    # set variable for how far back an ancestor goes or len(path)
    depth = 0

    graph = Graph()
    for a in ancestors:
        if a[0] not in graph.vertices:
            graph.add_vertex(a[0])
        if a[1] not in graph.vertices:
            graph.add_vertex(a[1])
        graph.add_edge(a[1], a[0])

    qq = Queue()
    # enqueue starting vertex
    qq.enqueue([starting_node])
    # swhile queue not empty
    while qq.size() > 0:
        # dequeue first vertex
        path = qq.dequeue()
        current_node = path[-1]
        if current_node != starting_node:
            if len(path) > depth:
                earliest_ancestor = current_node
                depth = len(path)
            elif len(path) == depth and earliest_ancestor > current_node:
                earliest_ancestor = current_node
        for next_a in graph.vertices[current_node]:
            new_path = list(path)
            new_path.append(next_a)
            qq.enqueue(new_path)
    return earliest_ancestor


family_tree = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(family_tree, 8))
