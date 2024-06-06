from pwn import *

from hashlib import sha256
from uuid import uuid4
from base64 import b64encode, b64decode

# ==========================================
# Opérations sur le nom
# ==========================================
def convert_fragment_name_as_value(fragment:str) -> int:
    return (sum([ord(c) for c in fragment]) * 0x13 + 0x37) % 0x7f    

def convert_name_as_values(name:str)->int:
    return [convert_fragment_name_as_value(name[i::3]) for i in range(3)]

# ==========================================
# Opérations sur le N° de série
# ==========================================
def convert_hash_header_as_value(header:str)->int:
    header = int(header, 16)
    header = (55 * header + 19) % 127
    return header

def check_serial_match_name(serial:str, name_values:list) -> bool:
    h_serial = sha256(serial.encode()).hexdigest()
    for i in range(3):
        header_value = h_serial[2*i:2*i+2]
        header_value = convert_hash_header_as_value(header_value)
        if header_value != name_values[i]:
            return False
    return True      

def generate_serial_that_matches_name(name:str) -> str:
    name_values = convert_name_as_values(name)
    serial_matches_name = False
    while not serial_matches_name:
        serial = str(uuid4())
        serial_matches_name = check_serial_match_name(serial, name_values)
    return serial


# ==========================================
# Opérations sur formattage de la licence
# ==========================================
def generate_license(name:str, user_type:str) -> bytes:
    #serial = '1d117c5a-297d-4ce6-9186-d4b84fb7f230'
    serial = generate_serial_that_matches_name(name)
    license_payload = f'Name: {name}\nSerial: {serial}\nType: {user_type}\n'
    license_payload = b64encode(license_payload.encode())
    licence = b'----BEGIN WHITE LICENSE----\n' + license_payload + b'\n-----END WHITE LICENSE-----\n'
    return licence
'''
Walter White Junior

65d11a39-df04-4fe1-bb82-9bd791b7aea3
'''


host, port = "challenges.france-cybersecurity-challenge.fr", "2250"

if args.REMOTE:
  processus = remote(host,port)
else:
  processus = process(['python3', 'fifty-solve.py'])

# Welcome message

for question in range(51):
    data = processus.recvline().decode()
    log.info(data)
    while 'Give me a valid' not in data:
        data = processus.recvline().decode()
        log.info(data)
    type = '1337' if 'admin' in data else '1'
    name = data.split(':')[1].strip()
    log.info(f'{question=}, {name=}, {type=}')
    license = generate_license(name, type)
    processus.sendline(license)
    #processus.sendline()

processus.close()
