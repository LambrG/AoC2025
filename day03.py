from file import read_data

test = read_data('03test.txt')
actual = read_data('day03.txt')
"""
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
"""    
batteries = actual #['811384523523527']
total = 0
for bank in batteries:
    #print(len(bank), 'znaku')
    output = ''
    curr_i = 0
    #bank += '0'
    #print(bank)
    for idx in range(12):
        curr_num = '0'
        end = len(bank[curr_i:])-(11-idx)
        #print(curr_i,end)       
        test_string = bank[curr_i:curr_i+end] 
        #print(test_string)
        #input()
        for j,char in enumerate(test_string):
            if int(char)> int(curr_num):
                curr_num = char
                max_j = j
        output += curr_num
        curr_i += max_j + 1
        
        #print(';'.join([output,test_string]))
        #input()
    total += int(output)

print(total)


