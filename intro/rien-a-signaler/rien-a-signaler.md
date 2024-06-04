# Rien à signaler

<img alt="énoncé du challenge" src="enonce.png" width=300>

Les fichiers fournis :
- [output.txt](output.txt)
- [rien-a-signaler.py](rien-a-signaler.py)

----

Le script `rien-a-signaler.py` effectue un chiffrement RSA du fichier `flag.txt` et fournit en sortie dans le fichier `output.txt` :
- `c` : le flag chiffré
- `n` : le module de chiffrement
- `e` : l'exposant de déchiffrement.

En effet, dans l'implémentation, il y a eu une inversion entre `pk` et `sk` lors de la récupération des clés :

```py
# Generate RSA keys
sk, pk = keygen()
```

Ainsi au lieu d'avoir l'exposant de chiffrement, on a celui de déchiffrement.

On dispose donc de tous les éléments pour déchiffrer `c`, ce qui est réalisé dans le script [`rien-a-signaler-resolve.py`](./rien-a-signaler-resolve.py), puisque :

$$
flag = c^{e} \pmod{n}
$$
