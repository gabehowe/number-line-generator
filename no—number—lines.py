import re
from math import floor
from typing import Optional

while True:
    while True:
        inp = input("Equation (x >= z): ")
        if re.match('^[a-z0-9]{1,4}[\s]?(>=|<=|<|>)[\s]?[-]?.*[\s]?((>=|<=|<|>)[\s]?.*)?$', inp):
            break

    first_var = re.findall('^\w', inp)[0]
    second_var = int(re.findall('[-]?[\d]*$', inp)[0])
    operand: str = re.findall('(>=|<=|<|>)', inp)[0]
    # second_operand: str = Optional[re.findall('(>=|<=|<|>)', inp)[1]]
    # third_var = re.findall('[-]?[\w]*', inp)[1]
    if first_var.isdigit():
        first_var = int(first_var)
    # if third_var.isdigit():
    #     third_var = int(third_var)
    normal_chars = {'start': '├', 'middle': '─', 'line': '┼', 'end': '┤', 'section': '─────┼'}
    full_chars = {'start': '╠', 'middle': '═', 'line': '╬', 'end': '╣', 'section': '═════╬'}
    space = {1: '     ', 2: '    ', 3: '   ', 4: '  ', 5: ' '}
    line_length = 14
    line = ''
    nums = ''
    for i in range(floor(second_var - line_length / 2), floor(second_var + line_length / 2) + 1):
        nums += (str(i) + space[len(str(i))])
    print(nums)
    if operand == '<=' or operand == '<':
        line += full_chars['start']
        for i in range(0, floor(line_length / 2)):
            line += full_chars['section']
        if operand == '<':
            line = line.removesuffix(full_chars['line'])
            line += normal_chars['line']
        for i in range(0, floor(line_length / 2)):
            line += normal_chars['section']
        line = line.removesuffix(normal_chars['line'])
        line += normal_chars['end']
    else:
        line += normal_chars['start']
        for i in range(0, floor(line_length / 2)):
            line += normal_chars['section']
        if operand == '>=':
            line = line.removesuffix(normal_chars['line'])
            line += full_chars['line']
        for i in range(0, floor(line_length / 2)):
            line += full_chars['section']
        line = line.removesuffix(full_chars['line'])
        line += full_chars['end']

    print(line)
