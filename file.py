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