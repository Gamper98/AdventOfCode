import os
from config.definitions import ROOT_DIR
import numpy as np
from collections import defaultdict

def read(text):
    with open(text, 'r') as f:
        risk = [[int(digit) for digit in row] for row in f.read().rstrip('\n').split('\n')]
        return np.array(risk, dtype=np.int8)

def dijkstra(graph, sr, dest):
    dist = defaultdict(lambda: np.iinfo(np.int32).max)
    visited = set()
    queue = {sr}
    dist[sr] = 0
    while queue:
        node = min(queue, key=dist.get)
        queue.remove(node)
        visited.add(node)
        neighb = [(node[0]-1,node[1]),(node[0]+1,node[1]),\
            (node[0],node[1]-1),(node[0],node[1]+1)]
        for x,y in neighb:
            if min(x,y) >= 0 and x < graph.shape[0] and \
                y < graph.shape[1] and (x,y) not in visited:
                queue.add((x,y))
                c_dist = dist[node] + graph[x,y]
                if c_dist < dist[(x,y)]:
                    dist[(x,y)] = c_dist
    return dist[dest]

def solution_A(risk):
    shortest_path = dijkstra(risk, (0,0), (risk.shape[0]-1,risk.shape[1]-1))
    return shortest_path

def make_bigger_risk(risk):
    bigger_risk = np.repeat(risk[None], repeats=5, axis=0)
    bigger_risk = np.repeat(bigger_risk[None], repeats=5, axis=0)
    a1 = np.arange(0,5, dtype=np.int8)
    add_matr = a1[:,None] + a1
    bigger_risk = (add_matr + bigger_risk.T).T
    bigger_risk = bigger_risk.swapaxes(1,2).reshape(risk.shape[0]*5, risk.shape[1]*5)
    bigger_risk[bigger_risk > 9] -= 9
    return bigger_risk

def solution_B(risk):
    bigger_risk = make_bigger_risk(risk)
    shortest_path = dijkstra(bigger_risk, (0,0), (bigger_risk.shape[0]-1,bigger_risk.shape[1]-1))
    return shortest_path

def main():
    risk = read(os.path.join(ROOT_DIR, '2021\Day_15\input', 'input.txt'))
    sol_A = solution_A(risk)
    sol_B = solution_B(risk)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()