def file_to_list(path):
    lines = []
    with open(path, 'r') as infile:
        for line in infile.readlines():
            lines.append(line.strip())
    return lines