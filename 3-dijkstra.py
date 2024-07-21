import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створення графа
G = nx.Graph()

# Додавання вузлів (станції метро)
stations = [
    'Station A', 'Station B', 'Station C', 'Station D', 'Station E',
    'Station F', 'Station G', 'Station H', 'Station I', 'Station J'
]

G.add_nodes_from(stations)

# Додавання ребер з вагами (шляхи між станціями)
edges = [
    ('Station A', 'Station B', 5), ('Station A', 'Station C', 2), ('Station B', 'Station D', 4),
    ('Station C', 'Station D', 7), ('Station D', 'Station E', 3), ('Station E', 'Station F', 8),
    ('Station F', 'Station G', 6), ('Station G', 'Station H', 1), ('Station H', 'Station I', 3),
    ('Station I', 'Station J', 4), ('Station J', 'Station A', 7)
]

G.add_weighted_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)  # Розташування вузлів
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, edge_color='gray', font_size=15, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Транспортна мережа міста з вагами', size=20)
plt.show()

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, edge_data in graph[current_node].items():
            weight = edge_data['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Знаходження найкоротших шляхів для всіх вершин
shortest_paths = {}
for station in stations:
    shortest_paths[station] = dijkstra(G, station)

# Виведення результатів
for start_station, paths in shortest_paths.items():
    print(f"\nНайкоротші шляхи від {start_station}:")
    for end_station, distance in paths.items():
        print(f"  до {end_station}: {distance} одиниць")

# Висновки у форматі markdown
markdown_output = "# Висновки\n\n## Найкоротші шляхи для всіх вершин\n"
for start_station, paths in shortest_paths.items():
    markdown_output += f"\n### Найкоротші шляхи від {start_station}:\n"
    for end_station, distance in paths.items():
        markdown_output += f"- до {end_station}: {distance} одиниць\n"

with open('dijkstra_results.md', 'w', encoding='utf-8') as f:
    f.write(markdown_output)