#!/usr/bin/env python3

import string
import sys
import os

if len(sys.argv) != 2:
    print(f'{os.path.basename(__file__)} [ downloaded file path ]')
    sys.exit(1)

try:
    list = [ int(i) % 37 for i in open(sys.argv[1]).read().split() ]

except FileNotFoundError:
    print(f'\033[31;1mE:\033[0m No such file or directory \'{sys.argv[1]}\'')
    sys.exit(1)

flag_content = []

for data in list:
    if data in range(26):
        flag_content.append(string.ascii_uppercase[data])
    elif data in range(26,36):
        flag_content.append(string.digits[data - 26])
    else:
        flag_content.append('_')

print(f"\033[32mpicoCTF{{{''.join(flag_content)}}}\033[0m")
