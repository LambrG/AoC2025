from file import read_data, process_data_to_grid_points
from shapely.geometry import Polygon, box


def area_of_rectangle(row1, col1, row2, col2):
    width = max(row1, row2) - min(row1, row2) +1
    height = max(col1, col2) - min(col1, col2) +1
    return width * height


def solve1(grid):
    max_area = 0
    for i in range(len(grid)):
        row1, col1 = grid[i]
        for j in range(i + 1, len(grid)):
            row2, col2 = grid[j]
            area = area_of_rectangle(row1, col1, row2, col2)
            if area > max_area:
                max_area = area 
    return max_area    


def solve2(grid):
    max_area = 0
    polygon = Polygon(grid)
    for i in range(len(grid)):
        row1, col1 = grid[i]
        for j in range(i + 1, len(grid)):
            row2, col2 = grid[j]
            rectangle = box(min(row1, row2), min(col1,col2), max(row1,row2), max(col1, col2))
            if polygon.contains(rectangle):
                area = area_of_rectangle(row1, col1, row2, col2)
                if area > max_area:
                    max_area = area
    return max_area


def main():
    test = read_data('inputs/09test.txt')
    test_grid = process_data_to_grid_points(test)
    actual = read_data('inputs/day09.txt')
    actual_grid = process_data_to_grid_points(actual)

    assert solve1(test_grid) == 50, f"Expected 50 but got {solve1(test_grid)}"
    print(solve1(actual_grid))

    assert solve2(test_grid) == 24, f"Expected 24 but got {solve2(test_grid)}"
    print(solve2(actual_grid))


if __name__ == "__main__":
    main()