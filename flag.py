#!/usr/bin/env python

import string
import sys
import os

if len(sys.argv) != 2:
    print(f'{os.path.basename(__file__)} [ downloaded file path ]')
    sys.exit()

try:
    list = [ int(i) % 37 for i in open(sys.argv[1]).read().split() ]

except FileNotFoundError:
    print(f'\033[31;1mE:\033[0m No such file or directory \'{sys.argv[1]}\'')
    sys.exit()

flag_content = []
alphabets = string.ascii_uppercase
decimals = string.digits

for data in list:
    if data in range(26):
        flag_content.append(alphabets[data])
    elif data in range(26,36):
        flag_content.append(decimals[data - 26])
    else:
        flag_content.append('_')

print(f"\033[32mpicoCTF{{{''.join(flag_content)}}}\033[0m")