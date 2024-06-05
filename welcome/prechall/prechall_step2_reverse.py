from hashlib import sha256

CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?€$*"
L1 = "$ABFIZht!HPUYhirKOXdhjxy?DGJSWehCENahklo*cghmpu€MQRVfhvzLTbhnqsw"
L2 = "!FOWamwzFRSTUdlp*EFVXbei?FMNPgjsCDFHcnvxFJQYkqy€FGKLforu"
L3 = "!FOWamwz$RcejkrwDIKNVYpwGHMXltw€*APSovwy?BCQdiuwEJUZfgwx"


# ================================================
#
# Reverse de la chaine de caractères à trouver
#
# ================================================
# Ajout de _ afin de pouvoir l'utiliser pour indiquer que le caractère de la chaine reste à trouver
CHARSET_SAV = CHARSET
CHARSET += "_"

# Initialisation de la chaine à trouver, de longueur correspondant à l'assertion correspondante : 
# assert len(s) == 8 * (8 * 7 + 1)
s = ['_'] * (8 * (8 * 7 + 1))

# Prise en compte de la contrainte sur le début de la chaine qui doit être identique à L1 :
# assert L1 == "".join(A)
for i in range(len(L1)):
    s[i] = L1[i]

# Prise en compte que la suite doit correspondre à L2 :
# assert L2 == "".join([ B[0][i] for i in range(7) ])    
for i in range(len(L2)):
    s[len(L1) + i] = L2[i]

# Le 1er élément de chaque ligne B[i][0] doit correspondre à L3[i*8:i*8+8]
# assert L3 == "".join([ B[i][0] for i in range(7) ])
for i in range(7):
    for j in range(8):
        s[len(L1) + j + 7*8*i] = L3[j + 8*i]

ss = s
s = "".join(s)
print(s)

# Calcul de A et B (à l'identique du code initial)
s1, s2 = s[:8 * 8], s[8 * 8:]
A = [ s1[j:j + 8] for j in range(0, 8 * 8, 8) ]
B = [ [s2[i:i + 8 * 7][j:j + 8] for j in range(0, 8 * 7, 8) ] for i in range(0, len(s2), 8 * 7)]

#----------------------------
# Reverse de check(A,B)
#----------------------------
# Dictionnaire permettant de construire petit à petit le contenu des B[y][x] restant à trouver (ie y!=0 et x!=0)
dict_B_y_x = {}

# Reverse de la 2ème partie de check(A, B)
# - on doit avoir, pour chaque "colonne" x : intersection 2 à 2 de tous les B[j][x] (pour j=0 à 6) et A[7] = 1 unique et même caractère
# - or comme on connait tous les B[0][x], on peut facilement identifier ce caracctère : c'est celui de l'intersetion entre B[0][x] et A[7]
for x in range(1, 7):
    S = set(A[7])
    S = S.intersection(set(B[0][x]))
    for y in range(1,7) :
        if (y, x) in dict_B_y_x :
            dict_B_y_x[( y,x)] |= S.copy()
        else:
            dict_B_y_x[( y,x)] = S.copy()

# Reverse de la 1ère partie de check(A, B)
# - cette fois on s'appuie sur le fait que l'on connait tous les B[y][0]
for a in range(7):
    for b in range(7):
        S = set(A[a])
        for x in range(7):
            y = (a * x + b) % 7
            if x == 0:
                S = S.intersection(set(B[y][0]))
            else:
                if (y, x) in dict_B_y_x :
                    dict_B_y_x[( y,x)] |= S.copy()
                else:
                    dict_B_y_x[( y,x)] = S.copy()

#----------------------------

# Tri des caractères dans chaque B[y][x]
# assert all([ sorted(B[i][j]) == list(B[i][j]) for i in range(7) for j in range(7) ])
for x in range(1,7):
    for y in range(1,7):
        dict_B_y_x[(y, x)] = "".join(sorted(dict_B_y_x[(y, x)]))
        print(f'B[{y}][{x}] = {dict_B_y_x[(y, x)]}')

# Remplissage de la chaine avec les données des B[y][x] non encore remplies (ie y!=0 et x!=0)
for (y,x), l in dict_B_y_x.items():
    if y == 0 or x == 0:
        continue
    #print(f'B[{y}][{x}] = {l}')
    for i in range(8):
        ss[len(L1) + 8 * 7 * y + 8 * x + i] = l[i]
    pass

s ="".join(ss)
print(s)
print("========================================================")

# Restauration de CHARSET
CHARSET = CHARSET_SAV


# ================================================
#
# Code initial
#
# ================================================
def check(A, B):
    res = True
    for a in range(7):
        for b in range(7):
            S = set(A[a])
            for x in range(7):
                y = (a * x + b) % 7
                S = S.intersection(set(B[y][x]))
            res &= (len(S) == 1)
    for x in range(7):
        S = set(A[7])
        for y in range(7):
            S = S.intersection(set(B[y][x]))
        res &= (len(S) == 1)
    return res

# s = input(">>> ")
print(">>>", s)

assert len(s) == 8 * (8 * 7 + 1)
assert all(x in CHARSET for x in s)

s1, s2 = s[:8 * 8], s[8 * 8:]
A = [ s1[j:j + 8] for j in range(0, 8 * 8, 8) ]
B = [ [s2[i:i + 8 * 7][j:j + 8] for j in range(0, 8 * 7, 8) ] for i in range(0, len(s2), 8 * 7)]

assert L1 == "".join(A)
assert L2 == "".join([ B[0][i] for i in range(7) ])
assert L3 == "".join([ B[i][0] for i in range(7) ])
assert all([ sorted(B[i][j]) == list(B[i][j]) for i in range(7) for j in range(7) ])
assert check(A, B)

h = sha256(s.encode()).hexdigest()
print(f"Congrats! You can now go here: https://france-cybersecurity-challenge.fr/{h}")
