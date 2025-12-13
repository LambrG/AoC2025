from file import read_data
import re
from itertools import product
import math


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


def find_min_presses_recursive(current, target, buttons, presses, memo=None):
    if memo is None:
        memo = {}
    
    current_tuple = tuple(current)
    if current_tuple in memo:
        return memo[current_tuple]
    
    if current == target:
        return presses
    
    min_result = float('inf')
    
    for button in buttons:
        next_state = current.copy()
        for wire in button:
            next_state[wire] *= -1
        
        result = find_min_presses_recursive(next_state, target, buttons, presses + 1, memo)
        if result != float('inf'):
            min_result = min(min_result, result)
    
    memo[current_tuple] = min_result
    return min_result


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
    
    def can_reach_zero(state, presses_left):
        state_key = (state, presses_left)
        if state_key in memo:
            return memo[state_key]
        
        # Base case: reached zero
        if all(x == 0 for x in state):
            result = presses_left == 0
            memo[state_key] = result
            return result
        
        # Base case: no presses left
        if presses_left == 0:
            memo[state_key] = False
            return False
        
        # Try each button in reverse (subtract)
        for button in buttons:
            new_state = list(state)
            valid = True
            for wire in button:
                new_state[wire] -= 1
                if new_state[wire] < 0:
                    valid = False
                    break
            
            if valid and can_reach_zero(tuple(new_state), presses_left - 1):
                memo[state_key] = True
                return True
        
        memo[state_key] = False
        return False
    
    return can_reach_zero(target, num_presses)


def find_min_presses_joltage(buttons, target):
    target = tuple(target)
    
    min_presses = min(target)
    max_presses = sum(target)
    
    # Binary search for minimum presses
    result = -1
    left, right = min_presses, max_presses
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_reach_target_in_presses(buttons, target, mid):
            result = mid
            right = mid - 1  # Try lower
        else:
            left = mid + 1   # Try higher
    
    return result



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
        target = joltage.copy()
        
        presses = find_min_presses_joltage(buttons, target)
        total += presses
    
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
