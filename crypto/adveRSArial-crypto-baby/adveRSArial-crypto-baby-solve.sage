n = 179770685017248789197537661565815269934203562120851089179122414399064734715990794430000078278988633398024403072323955508476586487162411822366599111412534539430740137196265242371128714558362082882520001747685222655863817125733693411058452743768818267918688593648334613756045157321491607233744902053478170361857
e = 65537
c = 0x000c307feca4371acecab2690800586b967909e12ec3e80184666ca161129f86c6cd87e276127a1f9b672b66ba3d715321b24f7d660a928d829c154dcdc0634b99f51e281c2e138f77a04694ff7aeec25c938cf769fbd7d3f2968f0b96fc5d38a8f742f6a46e70d7eae8280ed61f0328df36497f0cb6251b0e13a2bc5adce6344a

print(bin(n))

E = GF(2)

R.<X> = PolynomialRing(E)
n_acc = n
P = 0
i = 0
#On construit le polynôme P tel que P(2) = n
while n_acc > 0:
    #P += (n_acc % 2)*X^i
    P += (n_acc & 1)*X^i
    i += 1
    #n_acc = n_acc // 2
    n_acc = n_acc >> 1

RR.<X> = PolynomialRing(ZZ)
P = RR(P)
print(P)
#On vérifie que la construction n'a pas eu de problèmes
assert int(P(2)) == int(n)

#On essaye de factoriser et on prend une des racinnes évaluée en 2
print(P.factor())
print(P.factor()[1][0])
p = int(P.factor()[0][0](2))

#On s'assure qu'on a bien trouvé une racine non triviale (pas 1 ni n)
assert n % p == 0
assert 1 < p < n

q = n// p
d = pow(e, -1, (p-1) * (q-1))

pt = pow(c, d, n)

from Crypto.Util.number import long_to_bytes
print(long_to_bytes(int(pt)))

b"\x02mF\x03\xb9\xe6(s\xb5\xd0\x88\xdd\xdc|N\n\xbbr\xb8~\x0cI\xce\xea{'\xc8\x7f\x1eS\x8dz\xbcf\x87\xb0\n+\xf2\x19=\x0f3\xef\xa8M'\x8f\x02}\xb8\x07\xee\xe7\xb3\\\xbd\x00FCSC{0224e979da8a6069869ccfc040abb680ffd35e3ba61bcc0e0683662c33fa81c0}"

