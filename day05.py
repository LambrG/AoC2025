from file import read_data


def process_data(file):
    ranges = []
    inventory = []
    idx_split = 0
    for i,line in enumerate(file):
        if line == '':
            idx_split = i
            break
        else:
            limits = line.split('-')
            ranges.append((int(limits[0]), int(limits[1])))
    for i, line in enumerate(file[idx_split+1:]):
        inventory.append(int(line))
    return ranges, inventory


def solve1(ranges, inventory):
    total = 0
    for item in inventory:
        item = item
        for range in ranges:
            if range[0] <= item <= range[1]:
                total += 1
                break
    return total


def solve2(ranges):
    sorted_ranges = sorted(ranges, key=lambda r: r[0])
    
    merged = [sorted_ranges[0]]
    
    for current in sorted_ranges[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    
    total = sum(end - start + 1 for start, end in merged)
    
    return total


test = read_data('inputs/05test.txt')
test_ranges, test_inventory = process_data(test)
actual = read_data('inputs/day05.txt')
actual_ranges, actual_inventory = process_data(actual)

print(solve1(test_ranges, test_inventory))
print(solve2(test_ranges))
assert solve1(test_ranges, test_inventory) == 3
assert solve2(test_ranges) == 14


print(solve1(actual_ranges,actual_inventory))
print(solve2(actual_ranges))