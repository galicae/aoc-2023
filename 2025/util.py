def file_to_list(path, raw=False):
    lines = []
    with open(path, 'r') as infile:
        for line in infile.readlines():
            if raw:
                lines.append(line[:-1])
            else:
                lines.append(line.strip())

    return lines