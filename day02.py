#ranges = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
with open("day02.txt", "r") as f:
    ranges = f.read()
brackets = ranges.split(",")

#print(brackets)
total = 0
total2 = 0

for bracket in brackets:
    
    start, end = bracket.split("-")

    for i in range(int(start), int(end)+1):
        
        code = str(i)
        middle = len(code) // 2
        first = code[:middle]
        second = code[middle:]
        
        if first == second:
            total += i
            
        lenght = len(code)
        
        for j in range(1, lenght+1):
            
            pattern = code[:j]
            count = lenght // j
            
            if pattern * count == code:
                total2 += i
                break
            
    
            
print(total)
print(total2)

