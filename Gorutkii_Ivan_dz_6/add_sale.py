import sys

with open('bakery.csv', 'r+', encoding='utf-8') as f:
    line = f.readline().strip()
    num = 1
    while line:
        line = f.readline()
        num += 1
    f.write(f'{num} {sys.argv[-1]}\n')
