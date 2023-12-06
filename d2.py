lines = []
with open("input.txt") as f:
    lines = f.readlines()

COLOR_LIMITS = {"blue": 14, "red": 12, "green": 13}
total1, total2 = 0, 0

for log in lines:
    uid, game = log.split(":")
    uid = int(uid[5:])
    color_totals = {x: 0 for x in COLOR_LIMITS}
    min_colors_played = {x: 1 for x in COLOR_LIMITS}

    for round in game.split(";"):
        local_color_totals = {x: 0 for x in COLOR_LIMITS}
        for move in round.split(","):
            num_cubes = int("".join([x for x in move if x.isdigit()]))
            for color in COLOR_LIMITS:
                local_color_totals[color] += num_cubes if color in move else 0
                color_totals[color] = max(
                    color_totals[color], local_color_totals[color]
                )

                min_colors_played[color] = max(
                    min_colors_played[color], num_cubes if color in move else 1
                )

    valid = True
    for color in COLOR_LIMITS:
        valid = False if color_totals[color] > COLOR_LIMITS[color] else True
    total1 += uid if valid else 0

    sub = 1
    for x in min_colors_played.values():
        sub *= x
    total2 += sub

print(total1, total2)
