input = 265149

def part1(src):
    num = 1
    exp = 1
    dir = 0
    move = [ [ 1, 0 ], [ 0, -1 ], [ -1, 0 ], [ 0, 1 ] ]
    coord = [ 0, 0 ]
    while num < src:
        
        for i in range(exp):
            coord = [ coord[0] + move[dir][0], coord[1] + move[dir][1] ]
            num += 1
            if (num == src):
                break
        dir = (dir + 1) % 4
        if dir % 2 == 0:
            exp += 1
    return abs(coord[1] - 0) + abs(coord[0] - 0)
    
print(part1(input))