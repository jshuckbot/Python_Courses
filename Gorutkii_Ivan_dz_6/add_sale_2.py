import sys

with open('bakery_2.csv', 'a', encoding='utf-8') as f:
    f.write(f'{sys.argv[-1]}\n')
