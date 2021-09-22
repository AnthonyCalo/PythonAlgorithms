class Vertex:
    def __init__(self, n):
        self.name=n
        self.neighbors=[]

        self.distance=9999
        self.visited=False
    def add_neighbor(self,v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()
        else:
            return

class Graph:
    vertices={}
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name]=vertex
            return True
        else:
            return False
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key==u:
                    value.add_neighbor(v)
                if key==v:
                    value.add_neighbor(u)
            return True
        else:
            return False
    def print_graph(self):
        for key in self.vertices.keys():
            print(key, str(self.vertices[key].neighbors))

    def bfs(self, vert):
        queue = list()
        vert.distance=0
        vert.visited=True
        for v in vert.neighbors:
            #direct neighbors of vert will have distance of 1 and be added to the queue
                self.vertices[v].distance=vert.distance+1
                queue.append(v)
            
        while len(queue)>0:
            u = queue.pop(0)
            node_u = self.vertices[u]

            node_u.visited=True

            for v in node_u.neighbors:
                node_v=self.vertices[v]
                if node_v.visited==False:
                    queue.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance=node_u.distance+1
            
g = Graph()
a = Vertex("A")
g.add_vertex(a)
g.add_vertex(Vertex("B"))
letters = ["C", "D", "E", "F", "G", "H"]
for i in letters:
    g.add_vertex(Vertex(i))

edges = ["AB", "AE", "BE", "BF", "CG", "DE", "DH", "EF", "FG", "FH", "FJ", "GJ", "HI"]
for edge in edges:
    g.add_edge(edge[:1], edge[1:])
farts = [['P', 'A', 'H', 'N'], ['A', 'P', 'L', 'S', 'I', 'I', 'G'], ['Y', 'I', 'R']]
