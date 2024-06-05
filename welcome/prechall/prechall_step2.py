from hashlib import sha256

CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?€$*"
L1 = "$ABFIZht!HPUYhirKOXdhjxy?DGJSWehCENahklo*cghmpu€MQRVfhvzLTbhnqsw"
L2 = "!FOWamwzFRSTUdlp*EFVXbei?FMNPgjsCDFHcnvxFJQYkqy€FGKLforu"
L3 = "!FOWamwz$RcejkrwDIKNVYpwGHMXltw€*APSovwy?BCQdiuwEJUZfgwx"

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

s = input(">>> ")

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
