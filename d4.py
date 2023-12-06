lines: list[str] = []
with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

card_count = [1 for _ in range(len(lines))]

total1, total2 = 0, 0
for i, line in enumerate(lines):
    card, numbers = line.split(":")
    winning, mine = numbers.split("|")

    winning = set([int(x) for x in winning.strip().split(" ") if x])
    mine = set([int(x) for x in mine.strip().split(" ") if x])

    num_matches = len(mine.intersection(winning))
    total1 += pow(2, num_matches - 1) if num_matches > 0 else 0

    for j in range(num_matches):
        card_count[i + j + 1] += card_count[i]

    total2 += card_count[i]

print(total1, total2)
