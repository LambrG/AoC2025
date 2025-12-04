from file import read_data

def show(warehouse):
    for row in warehouse:
        print(row)
        
    
def check_around(row,col,warehouse):
    count = 0
    for r in range (-1,2,1):
        for c in range(-1,2,1):
            char = warehouse[row+r][col+c]
            count += char == '@'
    return count - 1


def adjust_warehouse(warehouse):
    l = len(warehouse[0])
    warehouse = ['.'*l] + warehouse + ['.'*l]    
    warehouse = ['.' + line + '.' for line in warehouse]
    return warehouse


def solve1(data):
    warehouse = data    
    new_warehouse = [line for line in warehouse]
    total = 0
    
    for row, line in enumerate(warehouse):
        for col, char in enumerate(line):
            
            if char == '@':
                count = check_around(row,col,warehouse)
                
                if count < 4:
                    total += 1
                    new_warehouse[row] = new_warehouse[row][:col] + '.' + new_warehouse[row][col+1:]
                    
    return total, new_warehouse


def solve2(data):
    total = 0
    count, warehouse = solve1(data)
    
    while count > 0:
        total += count
        count, warehouse = solve1(warehouse)
        
    return total
        

if __name__ == "__main__":
    test = adjust_warehouse(read_data('inputs/04test.txt'))
    actual = adjust_warehouse(read_data('inputs/day04.txt'))
                
    assert solve1(test)[0] == 13
    print(solve1(test)[0])
    print(solve1(actual)[0])
    
    assert solve2(test) == 43
    print(solve2(test))
    print(solve2(actual))