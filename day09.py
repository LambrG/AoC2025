from file import read_data, process_data_to_grid_points
from shapely.geometry import Polygon, box


def area_of_rectangle(row1, col1, row2, col2):
    width = max(row1, row2) - min(row1, row2) +1
    height = max(col1, col2) - min(col1, col2) +1
    return width * height


def solve(grid):
    max_area_1 = 0
    max_area_2 = 0
    polygon = Polygon(grid)
    for i in range(len(grid)):
        row1, col1 = grid[i]
        for j in range(i + 1, len(grid)):
            row2, col2 = grid[j]
            area = area_of_rectangle(row1, col1, row2, col2)
            max_area_1 = max(max_area_1, area)
            rectangle = box(min(row1, row2), min(col1,col2), max(row1,row2), max(col1, col2))
            if polygon.contains(rectangle):
                max_area_2 = max(max_area_2, area)
    return max_area_1, max_area_2


def main():
    test = read_data('inputs/09test.txt')
    test_grid = process_data_to_grid_points(test)
    actual = read_data('inputs/day09.txt')
    actual_grid = process_data_to_grid_points(actual)

    test_result1, test_result2 = solve(test_grid)
    actual_result1, actual_result2 = solve(actual_grid)

    assert test_result1 == 50, f"Expected 50 but got {test_result1}"
    print(actual_result1)

    assert test_result2 == 24, f"Expected 24 but got {test_result2}"
    print(actual_result2)


if __name__ == "__main__":
    main()