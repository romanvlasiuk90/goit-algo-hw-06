# Висновки

## Шляхи, знайдені алгоритмами
- **DFS шлях від Station A до Station F**: ['Station A', 'Station B', 'Station D', 'Station E', 'Station F']
- **BFS шлях від Station A до Station F**: ['Station A', 'Station B', 'Station D', 'Station E', 'Station F']

## Аналіз різниці в шляхах
- **DFS (глибокий пошук)**: DFS йде якомога глибше в одному напрямку, перш ніж вертатися назад і шукати інші шляхи. Тому шлях може бути довшим або не оптимальним.
- **BFS (широкий пошук)**: BFS перевіряє всі сусідні вузли перш, ніж переходити на наступний рівень. Це гарантує знаходження найкоротшого шляху в ненагружених графах.

## Висновки
- Для цього графа алгоритм BFS знайшов найкоротший шлях, тоді як DFS може знайти довший шлях через природу свого пошуку. Вибір алгоритму залежить від потреб: якщо потрібен найкоротший шлях, варто використовувати BFS.