class Coor:
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y


def from_file(file_path):
    with open(file_path, 'r') as f:
        line = f.readline()
        output = []
        while line:
            line = line.replace('\n', '').split(' ')
            line = [float(x) if '.' in x else x for x in line]  # convert decimals
            line = [int(x) if type(x) is str and x.isdigit() else x for x in line]  # convert integers
            if type(line[0]) is int:
                output.append(Coor(line[0] - 1, line[2], line[1]))
            line = f.readline()
    return output