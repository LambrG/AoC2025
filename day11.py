from file import read_data
from functools import cache


def parse_connections(data):
    connections_dict = {}
    for line in data:
        key, values = line.split(': ')
        connections_dict[key] = values.split()
    return connections_dict


connections = None


def solve_1(conn):
    global connections
    find_route_between.cache_clear()
    connections = conn
    return find_route_between('you', 'out')


def solve_2(conn):
    global connections
    find_route_between.cache_clear()
    connections = conn
    # Calculate routes that pass through both fft and dac
    # Route 1: svr -> fft -> dac -> out
    svr_to_fft = find_route_between('svr', 'fft')
    fft_to_dac = find_route_between('fft', 'dac')
    dac_to_out = find_route_between('dac', 'out')
    
    # Route 2: svr -> dac -> fft -> out
    svr_to_dac = find_route_between('svr', 'dac')
    dac_to_fft = find_route_between('dac', 'fft')
    fft_to_out = find_route_between('fft', 'out')
    
    total = (svr_to_fft * fft_to_dac * dac_to_out) + (svr_to_dac * dac_to_fft * fft_to_out)
    return total

@cache
def find_route_between(start, end):
    """Find number of routes from start to end node"""
    if start == end:
        return 1
    total_routes = 0
    for neighbor in connections.get(start,[]):
        if neighbor == end:
            total_routes += 1
        else:
            total_routes += find_route_between(neighbor, end)
    return total_routes


test = read_data('inputs/11test.txt')
puzzle_input = read_data('inputs/day11.txt')
test2 = read_data('inputs/11test2.txt')

test_connections = parse_connections(test)
test2_connections = parse_connections(test2)
puzzle_connections = parse_connections(puzzle_input)

assert solve_1(test_connections) == 5, f"Test failed: {solve_1(test_connections)}"
print("Part 1 Test Passed")
print("Part 1:", solve_1(puzzle_connections))

assert solve_2(test2_connections) == 2, f"Test failed: {solve_2(test2_connections)}"
print("Part 2 Test Passed")
print("Part 2:", solve_2(puzzle_connections))