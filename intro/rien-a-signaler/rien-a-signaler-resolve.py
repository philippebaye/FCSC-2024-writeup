import json
from Crypto.Util.number import long_to_bytes

with open('output.txt', 'r') as output_file:
    data = json.loads(output_file.read())
    print(f'{data=}')
    e = 2**16 + 1
    m = pow(data['c'], e, data['n'])
    m = long_to_bytes(m)
    print(f'{m=}')
