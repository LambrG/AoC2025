from file import read_data

test = read_data('03test.txt')
actual = read_data('day03.txt')

batteries = actual
total = 0
for bank in batteries:
    cur_max = 0
    for i,left in enumerate(bank[:-1]):
        right_bank = bank[i+1:]
        for right in right_bank:
            bats = int(left + right)
            if bats > cur_max:
                cur_max = bats
    total += cur_max
    
print(total)
    
batteries = test
total = 0
for bank in batteries:
    seznam = list(bank)
    print(seznam)
    for i in range(3)