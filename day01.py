from file import read_data

test = read_data('inputs/01test.txt')
puzzle_input = read_data('inputs/day01.txt')


def solve(data):
    position = 50
    part1 = 0
    part2 = 0
    
    for line in data:
        direction = line[0]
        num = int(line[1:])
        part2 += num // 100
        num %= 100
        if direction == 'L':
            if position == 0:
                position = 100 - num
            else:
                position -= num
                if position < 0:
                    position += 100
                    part2 += 1
        else:
            position += num
            if position > 100:
                position -= 100
                part2 += 1
            elif position == 100:
                position = 0
        if position == 0:
            part1 += 1
            part2 += 1
    
    return part1, part2


# Test
assert solve(test) == (3,6), f"Test failed: got {solve(test)}, expected (3,6)"
print("Test passed!")

# Puzzle input
print(solve(puzzle_input))