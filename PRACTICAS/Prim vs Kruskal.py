import time
from heapq import heappop, heappush, heapify
from collections import defaultdict


class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return False
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        return True

def kruskal(vertices, edges):
    start_time = time.perf_counter()
 
    sorted_edges = sorted(edges, key=lambda e: e[2])
    ds = DisjointSet(vertices)
    mst = []
    
    for u, v, w in sorted_edges:
        if ds.union(u, v):
            mst.append((u, v, w))
    
    end_time = time.perf_counter()
    return mst, (end_time - start_time) * 1000

def prim(vertices, edges, start_node):
    start_time = time.perf_counter()
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((w, u, v))
        adj[v].append((w, v, u))

    mst = []
    visited = {start_node}
    edges_heap = adj[start_node][:]
    heapify(edges_heap)

    while edges_heap:
        w, u, v = heappop(edges_heap)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, w))
            for next_edge in adj[v]:
                if next_edge[2] not in visited:
                    heappush(edges_heap, next_edge)
    
    end_time = time.perf_counter()
    return mst, (end_time - start_time) * 1000

nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
aristas = [
    ('A', 'B', 7), ('A', 'D', 5),
    ('B', 'C', 8), ('B', 'D', 9), ('B', 'E', 7),
    ('C', 'E', 5), ('D', 'E', 15), ('D', 'F', 6),
    ('E', 'F', 8), ('E', 'G', 9), ('F', 'G', 11)
]

print("=== COMPARATIVA DE RENDIMIENTO: PRIM VS KRUSKAL ===\n")


mst_kruskal, tiempo_kruskal = kruskal(nodos, aristas)
print(f"--- Kruskal ---")
print(f"Tiempo: {tiempo_kruskal:.6f} ms")
print(f"MST: {mst_kruskal}")

print("\n" + "-"*45 + "\n")


mst_prim, tiempo_prim = prim(nodos, aristas, start_node='A')
print(f"--- Prim ---")
print(f"Tiempo: {tiempo_prim:.6f} ms")
print(f"MST: {mst_prim}")


print("\n=== RESUMEN ===")
if tiempo_kruskal < tiempo_prim:
    print(f"Kruskal fue más rápido por {tiempo_prim - tiempo_kruskal:.6f} ms")
else:
    print(f"Prim fue más rápido por {tiempo_kruskal - tiempo_prim:.6f} ms")