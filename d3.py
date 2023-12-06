from collections import defaultdict


lines: list[str] = []
with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
graph: list[list[str]] = [[c for c in line] for line in lines]
n, m = len(graph), len(graph[0])


def get_char_border(i, j) -> list[tuple[int, int]]:
    res = []
    for xx, yy in ((i + x, j + y) for x, y in directions):
        if 0 <= xx < n and 0 <= yy < m:
            res.append((xx, yy))
    return res


num_positions = {}
for i in range(n):
    num, positions = 0, []
    for j in range(m + 1):
        if j < m and graph[i][j].isdigit():
            positions.extend(get_char_border(i, j))
            num = num * 10 + int(graph[i][j])
        elif num > 0:
            num_positions[tuple(positions)] = num
            num, positions = 0, []


gears, total1, total2 = defaultdict(list), 0, 0
for positions, num in num_positions.items():
    is_valid = False
    for x, y in set(positions):
        if not graph[x][y].isdigit() and graph[x][y] != ".":
            is_valid = True
        if graph[x][y] == "*":
            gears[(x, y)].append(num)
            total2 += (
                (gears[(x, y)][0] * gears[(x, y)][1]) if len(gears[(x, y)]) == 2 else 0
            )

    total1 += num if is_valid else 0


print(total1, total2)
