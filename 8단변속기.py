import sys

line = list(map(int, (input().split(' '))))

if sorted(line) == line:
        print('ascending')
elif sorted(line, reverse = True) == line:
        print('descending')
else: print('mixed')
