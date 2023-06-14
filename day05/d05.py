input = [int(i) for i in open('input', 'r').read().splitlines()]

def part1():
    steps = 0
    idxa = 0
    while idxa < len(input):
        idxb = idxa + input[idxa]
        input[idxa] += 1
        idxa = idxb
        steps += 1
    return steps

print(part1())