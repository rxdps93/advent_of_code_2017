input = [row.split() for row in open('input', 'r').read().splitlines()]

def part1():
    return [len(row[0]) == len(row[1]) for row in zip(input, [set(row) for row in input])].count(True)

def part2():
    srt = []
    lst = []
    for row in input:
        lst = []
        for word in row:
            lst.append(''.join(sorted(word)))
        srt += [list(set(lst))]
    return [len(row[0]) == len(row[1]) for row in zip(input, srt)].count(True)

print(part1())
print(part2())