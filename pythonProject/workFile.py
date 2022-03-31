import os

with open("numbers.txt", 'r') as num_file:
    min_ = max_ = float(num_file.readline())
    for line in num_file:
        num = float(line)
        if num > max_:
            max_ = num
        elif num < min_:
            min_ = num
    sum_ = min_ + max_

with open("input.txt", 'r', encoding="utf8") as student_file:
    for line in student_file:
        mark = int(line.split()[-1])
        if mark < 3:
            name = " ".join(line.split()[:-1])
            print(name)

with open("output.txt", 'w') as output_file:
    output_file.write(str(sum_))
    output_file.write('\n')

