def get_input(file_name, transform=None, delim='\n'):
    with open(file_name) as fh:
        lines = fh.read().split(delim)
        if transform:
            lines = [transform(line) for line in lines]
        return lines
