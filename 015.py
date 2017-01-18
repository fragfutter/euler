#!/usr/bin/python


def pascal(line):
    result = [1, ]
    for i in range(1, len(line)):
        result.append(line[i - 1] + line[i])
    result.append(1)
    return result


line = [1]
for i in range(41):
    print(i, max(line))
    line = pascal(line)
