from file import read_data
from math import prod


def process_data(file):
    map_data = [(int(x), int(y), int(z)) for line in file for x, y, z in [line.split(',')]]
    return map_data


def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + 
            (p1[1] - p2[1]) ** 2 + 
            (p1[2] - p2[2]) ** 2)**0.5


def merge_circuits(circuits, circuit_members, circuit_id_1, circuit_id_2):
    for point in circuit_members[circuit_id_2]:
        circuits[point] = circuit_id_1
        circuit_members[circuit_id_1].add(point)
    del circuit_members[circuit_id_2]


def create_distance_pairs(data):
    distance_pairs = []
    for i, point in enumerate(data):
        for j, other in enumerate(data):
            if i < j:
                distance = euclidean_distance(point, other)
                distance_pairs.append((distance, point, other))
    distance_pairs.sort()
    return distance_pairs


def solve(data, iterations):
    distance_pairs = create_distance_pairs(data)
    
    circuits = {box: i for i, box in enumerate(data)}
    circuit_members = {i: {box} for i, box in enumerate(data)}
    
    for idx, (distance, p1, p2) in enumerate(distance_pairs):
        if idx >= iterations:
            break
        
        in_circuit_p1 = p1 in circuits
        in_circuit_p2 = p2 in circuits
        
        if in_circuit_p1 and in_circuit_p2:
            if circuits[p1] == circuits[p2]:
                continue
            else:
                circuit_id_1 = circuits[p1]
                circuit_id_2 = circuits[p2]
                merge_circuits(circuits, circuit_members, circuit_id_1, circuit_id_2)
                if len(circuit_members) == 1:
                    return p1[0] * p2[0]
        
        elif in_circuit_p1 and not in_circuit_p2:
            circuit_id = circuits[p1]
            circuits[p2] = circuit_id
            circuit_members[circuit_id].add(p2)
        
        elif in_circuit_p2 and not in_circuit_p1:
            circuit_id = circuits[p2]
            circuits[p1] = circuit_id
            circuit_members[circuit_id].add(p1)
    
    sizes = [len(members) for members in circuit_members.values()]
    sizes.sort(reverse=True)
    return prod(sizes[:3])


def main():
    test = read_data('inputs/08test.txt')
    test_data = process_data(test)
    actual = read_data('inputs/day08.txt')
    actual_data = process_data(actual)
    
    print(solve(test_data, 10))
    assert solve(test_data, 10) == 40
    print(solve(actual_data, 1000))
    
    print()
    print(solve(test_data, 1000000))
    assert solve(test_data, 1000000) == 25272
    print(solve(actual_data, 1000000))


if __name__ == "__main__":
    main()