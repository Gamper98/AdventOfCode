import os
from config.definitions import ROOT_DIR
from collections import defaultdict

def read(text):
    with open(text, 'r') as f:
        raw_data = f.read().rstrip('\n').split('\n')
        graph = defaultdict(lambda: {'cons' : [], 'is_big':False})
        for connection in raw_data:
            n_1, n_2 = connection.split('-')
            if n_2 != 'start':
                graph[n_1]['cons'].append(n_2)
            if n_1 != 'start':
                graph[n_2]['cons'].append(n_1) 
            if n_1.isupper():
                graph[n_1]['is_big'] = True
            if n_2.isupper():
                graph[n_2]['is_big'] = True
        return graph

def depth_first_traversal_A(graph, current_node, path, all_path):
    path.append(current_node)
    if current_node == 'end':
        all_path.append(path)
        return
    for node in graph[current_node]['cons']:
        if node not in path or graph[node]['is_big']:
            depth_first_traversal_A(graph, node, path.copy(), all_path)

def depth_first_traversal_B(graph, current_node, path, all_path, is_two):
    if current_node in path and not graph[current_node]['is_big']:
        is_two = True
    path.append(current_node)
    if current_node == 'end':
        all_path.append(path)
        return
    for node in graph[current_node]['cons']:
        if node not in path or graph[node]['is_big'] or not is_two:
            depth_first_traversal_B(graph, node, path.copy(), all_path, is_two)

def solution_A(graph):
    all_path = []
    depth_first_traversal_A(graph, 'start', [], all_path)
    return len(all_path)

def solution_B(graph):
    all_path = []
    depth_first_traversal_B(graph, 'start', [], all_path, False)
    return len(all_path)

def main():
    graph = read(os.path.join(ROOT_DIR, '2021\Day_12\input', 'input.txt'))
    sol_A = solution_A(graph)
    sol_B = solution_B(graph)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()