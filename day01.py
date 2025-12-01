from file import read_data

data = read_data('day01.txt')

#data = ['L68','L30','R48','L5','R60','L55','L1','L99','R14','L82']

position = 50
count = 0

for line in data:
    direction = line[0]
    num = int(line[1:])
    count += num // 100
    num %= 100
    if direction == 'L':
        if position == 0:
            position = 100 - num
        else:
            position -= num
            if position < 0:
                position += 100
                count += 1
    else:
        position += num
        if position > 100:
            position -= 100
            count += 1
        elif position == 100:
            position = 0
    if position == 0:
        count += 1

print(count)