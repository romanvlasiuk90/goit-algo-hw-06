import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

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

# Реалізація алгоритму DFS
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for node in graph.neighbors(start):
        if node not in path:
            new_path = dfs(graph, node, goal, path)
            if new_path:
                return new_path
    return None

# Реалізація алгоритму BFS
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next_node in graph.neighbors(vertex):
            if next_node not in path:
                if next_node == goal:
                    return path + [next_node]
                else:
                    queue.append((next_node, path + [next_node]))
    return None

# Виконання алгоритмів DFS та BFS
start_node = 'Station A'
goal_node = 'Station F'

dfs_path = dfs(G, start_node, goal_node)
bfs_path = bfs(G, start_node, goal_node)

print(f"DFS шлях від {start_node} до {goal_node}: {dfs_path}")
print(f"BFS шлях від {start_node} до {goal_node}: {bfs_path}")

# Аналіз результатів
conclusions = f"""
# Висновки

## Шляхи, знайдені алгоритмами
- **DFS шлях від {start_node} до {goal_node}**: {dfs_path}
- **BFS шлях від {start_node} до {goal_node}**: {bfs_path}

## Аналіз різниці в шляхах
- **DFS (глибокий пошук)**: DFS йде якомога глибше в одному напрямку, перш ніж вертатися назад і шукати інші шляхи. Тому шлях може бути довшим або не оптимальним.
- **BFS (широкий пошук)**: BFS перевіряє всі сусідні вузли перш, ніж переходити на наступний рівень. Це гарантує знаходження найкоротшого шляху в ненагружених графах.

## Висновки
- Для цього графа алгоритм BFS знайшов найкоротший шлях, тоді як DFS може знайти довший шлях через природу свого пошуку. Вибір алгоритму залежить від потреб: якщо потрібен найкоротший шлях, варто використовувати BFS.
"""

# Збереження висновків у файл readme.md
with open('readme.md', 'w', encoding='utf-8') as f:
    f.write(conclusions)

print(conclusions)