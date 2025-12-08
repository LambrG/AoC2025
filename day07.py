from file import read_data


def solve1(schema):
    start = schema[0].index('S')
    beam_indexes = {start}
    splits_count = 0

    for row in range(2, len(schema), 2):
        new_beam_indexes = set()
        for idx in beam_indexes:
            if schema[row][idx] == '^':
                new_beam_indexes.add(idx - 1)
                new_beam_indexes.add(idx + 1)
                splits_count += 1
            else:
                new_beam_indexes.add(idx)
        beam_indexes = new_beam_indexes

    return splits_count


def solve2(schema):
    start = schema[0].index('S')
    beam_indexes = {start: 1}
    width = len(schema[0])

    for row in range(2, len(schema), 2):
        new_beam_indexes = {}
        for idx, count in beam_indexes.items():
            if schema[row][idx] == '^':
                if idx > 0:
                    new_beam_indexes[idx - 1] = new_beam_indexes.get(idx - 1, 0) + count
                if idx < width - 1:
                    new_beam_indexes[idx + 1] = new_beam_indexes.get(idx + 1, 0) + count
            else:
                new_beam_indexes[idx] = new_beam_indexes.get(idx, 0) + count
        beam_indexes = new_beam_indexes

    return sum(beam_indexes.values())


def main():
    test = read_data('inputs/07test.txt')
    actual = read_data('inputs/day07.txt')

    assert solve1(test) == 21, f"Wrong, you got {solve1(test)}. Should be 21"
    assert solve2(test) == 40, f"Wrong for part 2, you got {solve2(test)}, Should be 40"

    print(solve1(actual))
    print(solve2(actual))


if __name__ == '__main__':
    main()