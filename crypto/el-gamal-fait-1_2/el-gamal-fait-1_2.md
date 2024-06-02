# El Gamal Fait 1/2

<img alt="énoncé du challenge" src="enonce.png" width=300>

Les fichiers fournis :
- [el-gamal-fait-1.py](el-gamal-fait-1.py)

----

Le script `el-gamal-fait-1.py` commence par fournir la clé publique composée de :
- `p` : un nombre premier de 2048 bits
- `g` : un nombre appartenant à $\mathbb{Z}/p\mathbb{Z}$
- `y` : une puissance de `g` dans $\mathbb{Z}/p\mathbb{Z}$, dont l'exposant `x` reste secret : $y \equiv g^{x} \pmod{p}$

Puis il nous invite à fournir `m`, `r` et `s` qui doivent vérifier la relation suivante pour obtenir le flag :

$$
g^{m} \equiv y^{r} \cdot r^{s} \pmod{p}
$$

Si on prend $s = r = y^{-1} \pmod{p}$ alors :

$$
y^{r} \cdot r^{s} \equiv  y^{r} \cdot (y^{-1})^{r} \equiv (y \cdot y^{-1})^{r} \equiv 1 \pmod{p}
$$

La relation à verifier devient alors :

$$
g^{m} \equiv 1 \pmod{p}
$$

Comme `p` est premier, grâce au [petit théorême de Fermat](https://fr.wikipedia.org/wiki/Petit_th%C3%A9or%C3%A8me_de_Fermat), on sait que :

$$
g^{p-1} \equiv 1 \pmod{p}
$$

Par conséquent pour obtenir le flag il suffit de prendre :

$$
\left\lbrace
\begin{array}{ll}
m = p - 1
\\
r = y^{-1} \pmod{p}
\\
s = y^{-1} \pmod{p}
\end{array}
\right.
$$

Le script [`el-gamal-fait-1-solve.py`](./el-gamal-fait-1-solve.py) implémente cette logique et permet de récupérer le flag en se connectant au serveur.
