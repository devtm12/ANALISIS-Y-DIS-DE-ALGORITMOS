class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False

def kruskal(vertices, edges):

    sorted_edges = sorted(edges, key=lambda x: x[2])
    ds = DisjointSet(vertices)
    mst = []
    total_weight = 0

    for u, v, weight in sorted_edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            
    return mst, total_weight


nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
aristas = [
    ('A', 'B', 7), ('A', 'D', 5), ('B', 'C', 8), ('B', 'D', 9), 
    ('B', 'E', 7), ('C', 'E', 5), ('D', 'E', 15), ('D', 'F', 6),
    ('E', 'F', 8), ('E', 'G', 9), ('F', 'G', 11)
]

resultado, peso = kruskal(nodos, aristas)
print("--- MST KRUSKAL ---")
for u, v, w in resultado:
    print(f"{u} - {v}: {w}")
print(f"Peso Total: {peso}")
