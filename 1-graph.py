import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів (станції метро)
stations = [
    'Station A', 'Station B', 'Station C', 'Station D', 'Station E',
    'Station F', 'Station G', 'Station H', 'Station I', 'Station J'
]

G.add_nodes_from(stations)

# Додавання ребер (шляхи між станціями)
edges = [
    ('Station A', 'Station B'), ('Station A', 'Station C'), ('Station B', 'Station D'),
    ('Station C', 'Station D'), ('Station D', 'Station E'), ('Station E', 'Station F'),
    ('Station F', 'Station G'), ('Station G', 'Station H'), ('Station H', 'Station I'),
    ('Station I', 'Station J'), ('Station J', 'Station A')
]

G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)  # Розташування вузлів
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, edge_color='gray', font_size=15, font_weight='bold')
plt.title('Транспортна мережа міста', size=20)
plt.show()

# Аналіз основних характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступінь вершин: {degrees}")

# Візуалізація розподілу ступенів вершин
plt.figure(figsize=(10, 7))
plt.bar(degrees.keys(), degrees.values(), color='skyblue')
plt.xlabel('Станції', size=15)
plt.ylabel('Ступінь', size=15)
plt.title('Розподіл ступенів вершин', size=20)
plt.xticks(rotation=45)
plt.show()