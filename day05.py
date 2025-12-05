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

#not this way, need to go by adjustin ovelapping ranges
def solve2(ranges):
    inventory = {}
    print(len(ranges))
    for i,limits in enumerate(ranges):
        print(i)
        for item in range(limits[0], limits[1] + 1):
            inventory[item] = 1
    return sum(inventory.values()) 




test = read_data('inputs/05test.txt')
test_ranges, test_inventory = process_data(test)
actual = read_data('inputs/day05.txt')
actual_ranges, actual_inventory = process_data(actual)

assert solve1(test_ranges, test_inventory) == 3
assert solve2(test_ranges) == 14

print(solve1(actual_ranges,actual_inventory))
print(solve2(actual_ranges))


