input = [row.split() for row in open('input', 'r').read().splitlines()]

for row in input:
    print(min(row), '\t&\t', max(row))


def part1(input):
    return sum(int(max(row)) - int(min(row)) for row in input)

# print(part1(input))