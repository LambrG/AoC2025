from file import read_data, read_data_no_eol


def process_data1(data):
    math_homework = list(map(list, zip(*[line.split() for line in data])))
    return math_homework


def process_data2(data):
    column = len(data[0]) - 1
    lrow = len(data)
    math_homework = []
    curr_problem = []

    while column >= 0:
        curr_number = ''

        for line in data:
            char = line[column]

            if char in ('+', '*'):
                curr_problem.append(curr_number)
                curr_number = lrow * ' '
                curr_problem.append(char)
                math_homework.append(curr_problem)
                curr_problem = []
            else:
                curr_number += char

        if curr_number == lrow * ' ':
            column -= 1
        else:
            curr_problem.append(curr_number)
            column -= 1
    
    return math_homework


def solve(math_homework):
    total = 0
    for problem in math_homework:
        operator = problem.pop()
        equation = operator.join(problem)
        result = eval(equation)
        total += result

    return total


def main():
    test = read_data('inputs/06test.txt')
    test1 = process_data1(test)
    actual = read_data('inputs/day06.txt')
    actual1 = process_data1(actual)
    assert solve(test1) == 4277556, f"Wrong, you got {solve(test1)}. Should be 4277556"

    print(solve(actual1))

    test2 = read_data_no_eol('inputs/06test.txt')
    test2 = process_data2(test2)
    assert solve(test2) == 3263827
    actual2 = read_data_no_eol('inputs/day06.txt')
    actual2 = process_data2(actual2)
    print(solve(actual2))


if __name__ == '__main__':
    main()
