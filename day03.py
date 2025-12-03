from file import read_data

def solve(data, range_size):
    total = 0
    for bank in data:
        result = ''
        current_index = 0
        
        for iteration in range(range_size):
            max_digit = '0'
            remaining_length = len(bank[current_index:]) - (range_size - 1 - iteration)
            search_range = bank[current_index:current_index + remaining_length]
            
            for position, digit in enumerate(search_range):
                if int(digit) > int(max_digit):
                    max_digit = digit
                    max_position = position
            
            result += max_digit
            current_index += max_position + 1
        
        total += int(result)
    
    return total

test = read_data('inputs/03test.txt')
puzzle_input = read_data('inputs/day03.txt')

# Test assertions
assert solve(test, 2) == 357, f"Part 1 test failed: got {solve(test, 2)}, expected 357"
assert solve(test, 12) == 3121910778619, f"Part 2 test failed: got {solve(test, 12)}, expected 3121910778619"
print("All assertions passed!")

# Part 1
print(solve(puzzle_input, 2))

# Part 2
print(solve(puzzle_input, 12))