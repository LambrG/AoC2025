from file import read_data
import re
from itertools import product
import z3


def parse_tuple_string(s):
    numbers = [int(x) for x in re.findall(r'\d+', s.strip())]
    return tuple(numbers)


def process_data(file):
    machines = []
    for line in file:
        p1_end = line.index(']')
        part_1 = line[1:p1_end]
        diagram = []
        for char in part_1:
            if char == '.':
                diagram.append(-1)
            elif char == '#':
                diagram.append(1)
        p3_start = line.index('{')
        joltage = [int(x) for x in line[p3_start + 1:-1].split(',')]
        buttons = [parse_tuple_string(x) for x in line[p1_end + 1: p3_start].split()]
        machines.append((diagram, buttons, joltage))
    return machines


def display_machines(machines):
    for machine in machines:
        diagram, buttons, joltage = machine
        print("Diagram:", diagram, end=' | ')
        print("Buttons:", buttons, end=' | ')
        print("Joltage:", joltage)


def find_min_presses_combinations(buttons, target):
    start = [-1] * len(target)
    num_presses = 0
    
    while True:
        for combo in product(range(len(buttons)), repeat=num_presses):
            current = start.copy()
            for button_idx in combo:
                for wire in buttons[button_idx]:
                    current[wire] *= -1
            
            if current == target:
                return num_presses
        
        num_presses += 1
    
    return -1


def can_reach_target_in_presses(buttons, target, num_presses):
    """Check if target is reachable in exactly num_presses by working backwards."""
    target = tuple(target)
    memo = {}


def solve1(data):
    machines = process_data(data)
    total = 0
    
    for diagram, buttons, joltage in machines:
        target = diagram.copy()
        
        presses = find_min_presses_combinations(buttons, target)
        total += presses
    
    return total


def solve2(data):

    machines = process_data(data)
    total = 0
    
    for i, machine in enumerate(machines):
        diagram, buttons, joltage = machine
        o = z3.Optimize()
        vars = z3.Ints(f"n{j}" for j in range(len(buttons)))
        for var in vars: o.add(var >= 0)
        for j, jolt in enumerate(joltage):
            equation = 0
            for b, button in enumerate(buttons):
                if j in button:
                    equation += vars[b]
            o.add(equation == jolt)
        o.minimize(sum(vars))
        o.check()
        total += o.model().eval(sum(vars)).as_long()
    return total


def main():
    test = read_data('inputs/10test.txt')
    actual = read_data('inputs/day10.txt')

    test_result = solve1(test)
    assert test_result == 7, f"Expected 7 but got {test_result}"
    actual_result = solve1(actual)
    print(actual_result)

    test_result2 = solve2(test)
    assert test_result2 == 33, f"Expected 33 but got {test_result2}"
    print(test_result2)
    actual_result2 = solve2(actual)
    print(actual_result2)


if __name__ == "__main__":
    main()
