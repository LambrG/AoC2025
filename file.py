def read_data(file):
    data = []
    with open(file) as text_file:
        for line in text_file.readlines():
            line = line.strip()
            data.append(line)
    return data

def read_data_no_eol(file):
    data = []
    with open(file) as text_file:
        for line in text_file.readlines():
            line = line.strip('\n')
            data.append(line)
    return data

def process_data_to_grid_points(file):
    points = []
    for line in file:
        parts = line.strip().split(',')
        points.append((int(parts[0]), int(parts[1])))
    return points    