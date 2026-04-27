from heapq import heappop, heappush, heapify
from collections import defaultdict

def prim(vertices, edges, start_node):
   
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((w, u, v))
        adj[v].append((w, v, u))

    mst = []
    visited = {start_node}
    edges_heap = adj[start_node][:]
    heapify(edges_heap)
    total_weight = 0

    while edges_heap:
        weight, u, v = heappop(edges_heap)
        
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            for next_edge in adj[v]:
                if next_edge[2] not in visited:
                    heappush(edges_heap, next_edge)
                    
    return mst, total_weight

nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
aristas = [
    ('A', 'B', 7), ('A', 'D', 5), ('B', 'C', 8), ('B', 'D', 9), 
    ('B', 'E', 7), ('C', 'E', 5), ('D', 'E', 15), ('D', 'F', 6),
    ('E', 'F', 8), ('E', 'G', 9), ('F', 'G', 11)
]

resultado, peso = prim(nodos, aristas, start_node='A')
print("--- MST PRIM ---")
for u, v, w in resultado:
    print(f"{u} - {v}: {w}")
print(f"Peso Total: {peso}")