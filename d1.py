lines = []
with open("input.txt") as f:
    lines = f.readlines()

NUMBER_MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

total1, total2 = 0, 0

for code in lines:
    nums = [int(x) for x in code if x.isdigit()]
    total1 += nums[0] * 10 + nums[-1]

    for num_string in NUMBER_MAPPING:
        if num_string in code:
            code = code.replace(
                num_string,
                num_string + str(NUMBER_MAPPING[num_string]) + num_string,
            )

    nums = [int(x) for x in code if x.isdigit()]
    total2 += nums[0] * 10 + nums[-1]

print(total1, total2)
