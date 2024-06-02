# AdveRSArial Crypto (Baby)

<img alt="énoncé du challenge" src="enonce.png" width=300>

Les fichiers fournis :
- [output.txt](output.txt)

----

On est dans un contexte de chiffrement RSA, par conséquent le fichier `output.txt` contient :
- `c` : le flag chiffré
- `n` : le module de chiffrement
- `e` : le classique exposant de chiffrement

Sans autre information, pour pouvoir effectuer le déchiffrement de `c` (et donc retrouver le flag en clair), il semble nécessaire de retrouver les 2 facteurs premiers `p` et `q` constituant `n`

Le type de génération de `n` indiqué dans l'énoncé nous incite à l'examiner sous tous ses angles, et notamment regarder sa représentation en binaire :

```
10000000000000000100000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000010000000000000000100010000100000000100100000000000001000000000000010000000000000000000010000000000010100000000000000100000000000000000001000000000000000110000000000010000000100000000000001000100000000001000000000100000000000001000000000000000000000000100000000000000000000000000000000000010100000010000000000000000000000000000010000000000000000001010000000000000000100000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000010000000000000000000010000000000000100100000000001000000000000000000001000000100000010000000000000010000000000000000000000000000000000001000000000001000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000001
```

On constate alors qu'il est essentiellement composé de `0` (i.e. de "trous")

Par conséquent, on va transformer le problème de factorisation de `n` en un problème de factorisation de polynôme, la factorisation polynomiale étant en général un problème plus simple.

Pour cela on va commencer par déterminer le polynôme $N(X)$ de sorte qu'on ait $N(2) = n$ : les `1` de la représentation binaire de `n` correspondent aux différents coefficients non nuls de ce polynôme.

Le polynôme obtenu possède ainsi très peu de coefficients (49) malgré son degré élevé (1024) :

$$
N(X) = X^{1024} + X^{1007} + X^{958} + X^{872} + X^{859} + X^{842} + X^{838} + X^{833} + X^{824} + X^{821} + X^{807} + X^{793} + X^{772} + X^{760} + X^{758} + X^{743} + X^{723} + X^{707} + X^{706} + X^{694} + X^{686} + X^{672} + X^{668} + X^{657} + X^{647} + X^{633} + X^{608} + X^{571} + X^{569} + X^{562} + X^{532} + X^{513} + X^{511} + X^{494} + X^{445} + X^{397} + X^{376} + X^{362} + X^{359} + X^{348} + X^{327} + X^{320} + X^{313} + X^{298} + X^{261} + X^{249} + X^{212} + X^{49} + 1
$$

Celui-ci se factorise en 2 polynômes $P(X)$ et $Q(X)$ :

$$
N(X) = (X^{511} + X^{494} + X^{445} + X^{359} + X^{320} + X^{49} + 1) \cdot (X^{513} + X^{348} + X^{327} + X^{313} + X^{249} + X^{212} + 1)
\\
\Rightarrow
N(X) = P(X) \cdot Q(X)
\\
avec
\left\lbrace
    \begin{array}{ll}
        P(X) = X^{511} + X^{494} + X^{445} + X^{359} + X^{320} + X^{49} + 1
        \\
        Q(X) = X^{513} + X^{348} + X^{327} + X^{313} + X^{249} + X^{212} + 1
    \end{array}
\right.
$$

Les 2 facteurs de `n` sont donc `p` et `q` tels que $p = P(2)$ et $q = Q(2)$

Maintenant que `p` et `q` sont connus, on peut retrouver `d` (l'exposant de déchiffrement), puis déchiffrer `c` pour obtenir le flag :

$$
\begin{array}{ll}
\phi(n) = (p - 1) \cdot (q - 1)
\\
d \equiv e^{-1} \pmod{\phi(n)}
\\
flag \equiv c^{d} \pmod{n}
\end{array}
$$

Cette logique est implémentée dans le sage [adveRSArial-crypto-baby-solve.sage](./adveRSArial-crypto-baby-solve.sage) lancé avec Sage.
