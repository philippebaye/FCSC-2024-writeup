# El Gamal Fait 2/2

<img alt="énoncé du challenge" src="enonce.png" width=300>

Les fichiers fournis :
- [el-gamal-fait-2.py](el-gamal-fait-2.py)

----

Le script `el-gamal-fait-2.py` est similaire à celui fourni dans [El Gamal Fait 1/2](../el-gamal-fait-1_2/el-gamal-fait-1_2.md) avec quelques différences :
- `p` : un nombre premier de 2048 bits, de la forme : $4 \cdot n + 1$
- `g` : égal à `2`
- `y` : une puissance de `g` dans $\mathbb{Z}/p\mathbb{Z}$, dont l'exposant `x` reste secret : $y \equiv g^{x} \equiv 2^{x} \pmod{p}$

En plus de fournir la clé publique, le script impose le `m` qui est choisi aléatoirement dans $\mathbb{Z}/p\mathbb{Z}$.

On est donc invité à fournir `r` et `s` qui doivent ici aussi vérifier la relation suivante pour obtenir le flag :

$$
g^{m} = 2^{m} \equiv y^{r} \cdot r^{s} \pmod{p}
$$

Le critère supplémentaire sur la forme de `p` (i.e. $p \equiv 1 \pmod{4}$) fait écho à l'algorihme à utiliser pour calculer les racines d'un [résidu quadratique](https://fr.wikipedia.org/wiki/R%C3%A9sidu_quadratique). Par conséquent, en application du [critère d'Euler](https://fr.wikipedia.org/wiki/Crit%C3%A8re_d%27Euler), en prenant $r = \frac{p-1}{2}$ on a 2 possibilités :
- $y^{r} \equiv 1 \pmod{p}$, si `y` est un résidu quadratique modulo `p`
- $y^{r} \equiv -1 \pmod{p}$, sinon

A noter que $(p-1) \equiv -1 \pmod{p}$

Si `y` est un résidu quadratique, la relation à vérifier devient :

$$
\begin{array}{}
2^{m} \equiv 1 \cdot (\frac{p-1}{2})^{s} \pmod{p}
\\
\Rightarrow
2^{m} \equiv (p-1)^{s} \cdot 2^{-s} \equiv (-1)^{s} \cdot 2^{-s} \pmod{p}
\end{array}
$$

Avec `s` pair, la relation devient : $2^m \equiv 2^{-s} \pmod{p}$.

D'après le petit théorême de Fermat $2^{p-1} \equiv 1 \pmod{p}$, donc il en va de même pour son inverse :

$$
(2^{p-1}) \cdot (2^{p-1})^{-1} \equiv 1 \pmod{p}
\Rightarrow
(2^{p-1})^{-1} \equiv 2^{-(p-1)} \equiv 1 \pmod{p}
$$

En prenant $s= (p-1) - m$ la relation est alors vérifiée, mais suppose que `m` soit pair (`s` pair $\iff$ `m` pair)

Par contre, avec `s` impair, la relation devient : $2^m \equiv (-1) \cdot 2^{-s} \pmod{p}$.

Si `2` n'est pas un résidu quadratique modulo `p`, alors $2^{\frac{p-1}{2}} \equiv -1 \pmod{p}$, et la relation peut alors être écrite comme suit : $2^m \equiv 2^{\frac{p-1}{2}} \cdot 2^{-s} \pmod{p}$.

Dans ce cas, on peut prendre $s = \frac{p-1}{2} - m$, à partir du moment où $\frac{p-1}{2}$ est pair, afin que `m` soit aussi impair sinon on se retrouve dans le cas précédent où `m` est pair.

Il reste à traiter le cas où `2` est un résidu quadratique de `p`. Dans ce cas on regarde si $2^{\frac{p-1}{2}}$ est lui même un résidu. Si ce n'est pas le cas on effectue le même type de raisonnement que précédemment, sinon on poursuit la recherche du premier non résidu quadratique parmi les $2^{\frac{p-1}{2^{i}}}$.

On prendra alors $s = \frac{p-1}{2^i} -m$ avec $i \ge 1 $ correspondant au premier $2^{\frac{p-1}{2^{i}}}$ non résidu quadratique.

Un raisonnement identique permet de traiter le cas où `y` n'est pas un résidu quadratique.

Le script [`el-gamal-fait-2-solve.py`](./el-gamal-fait-2-solve.py) implémente cette logique et permet d'obtenir le flag.
