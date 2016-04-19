def _integers_from_file(path):
    integers = []
    with open(path) as ints_file:
        lines = ints_file.readlines()
        for line in lines:
            line_ints = []
            for n in line.split(','):
                try:
                    line_ints.append(int(n))
                except ValueError:
                    continue
            integers.append(line_ints)
    return integers

def num_ints_from_file(path):
    """
    Calculates the number of integers in a given file
    """
    lines = _integers_from_file(path)
    length = 0
    for line in lines:
        length += len(line)
    return length

def longest_line_from_file(path):
    """
    Calculates the length of the longest line.
    """
    lines = _integers_from_file(path)
    longest = len(lines[0])
    for line in lines[1:]:
        if len(line) > longest:
            longest = len(line)
    return longest

def most_common_from_file(path):
    """
    Calculates the most common integer or integers in a given file
    """
    lines = _integers_from_file(path)
    most_common_map = {}
    for line in lines:
        for n in line:
            if most_common_map.get(n) is None:
                most_common_map[n] = 1
            else:
                most_common_map[n] += 1
    count_list =  most_common_map.keys()
    most_common = [count_list[0]]
    for value in count_list[1:]:
        if most_common_map[value] > most_common_map[most_common[0]]:
            most_common = [value]
        elif most_common_map[value] == most_common_map[most_common[0]]:
            most_common.append(value)
    return most_common

def mean_from_file(path):
    lines = _integers_from_file(path)
    integers = []
    total = 0
    for line in lines:
        for n in line:
            total += n
        integers.extend(line)
    try:
        mean = float('{0:.3f}'.format(
            float(total) / float(len(integers))
        ))
    except ZeroDivisionError:
        return None
    return mean
