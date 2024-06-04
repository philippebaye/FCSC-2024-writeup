import json
from Crypto.Util.number import long_to_bytes

datas = json.load(open('output.txt', 'r'))

flag = 0
for data in datas:
    flag ^= data
flag = hex(flag)[2:]
print(f'flag = \'FCSC{{{flag}}}\'')
