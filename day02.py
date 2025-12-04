def process_ranges(file_path):
    with open(file_path, "r") as f:
        ranges_text = f.read()
    
    ranges = ranges_text.split(",")
    total = 0
    total2 = 0
    
    for range_pair in ranges:
        start, end = range_pair.split("-")
        
        for number in range(int(start), int(end) + 1):
            code = str(number)
            code_length = len(code)            
            middle = code_length // 2

            first_half = code[:middle]
            second_half = code[middle:]
            if first_half == second_half:
                total += number
            
            for pattern_length in range(1, middle + 1):
                pattern = code[:pattern_length]
                repetitions = code_length // pattern_length
                
                if pattern * repetitions == code:
                    total2 += number
                    break
    
    return total, total2


test_total, test_total2 = process_ranges("inputs/02test.txt")
assert test_total == 1227775554, f"Test part 1 failed: got {test_total}, expected 1227775554"
assert test_total2 == 4174379265, f"Test part 2 failed: got {test_total2}, expected 4174379265"
print("All assertions passed!")

result_total, result_total2 = process_ranges("inputs/day02.txt")
print(result_total)
print(result_total2)