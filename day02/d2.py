input = [list(map(int, num)) for num in[row.split() for row in open('input', 'r').read().splitlines()]]

def part1(input):
    return sum(int(max(row)) - int(min(row)) for row in input)

print(part1(input))