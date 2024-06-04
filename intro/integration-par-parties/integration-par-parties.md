# Intégration par parties

<img alt="énoncé du challenge" src="enonce.png" width=300>

Les fichiers fournis :
- [integration-par-parties.py](integration-par-parties.py)
- [output.txt](output.txt)
- [shared_value.py](shared_value.py)

----

L'analyse du script `integration-par-parties.py` permet de comprendre l'état de `key.value[]` suite au `refresh()` qui est alors :

$$
\begin{array}{ll}
value[0] = t_{0,1} \oplus t_{0,2} \oplus t_{0,3} \oplus t_{0,4} \oplus \ldots \oplus t_{0,32} \oplus flag
\\
value[1] = t_{0,1} \oplus t_{1,2} \oplus t_{1,3} \oplus t_{1,4} \oplus \ldots \oplus t_{1,32}
\\
value[2] = t_{0,2} \oplus t_{1,2} \oplus t_{2,3} \oplus t_{2,4} \oplus \ldots \oplus t_{2,32}
\\
value[3] = t_{0,3} \oplus t_{1,3} \oplus t_{2,3} \oplus t_{3,4} \oplus \ldots \oplus t_{3,32}
\\
\ldots
\\
value[32] = t_{0,32} \oplus t_{1,32} \oplus t_{2,32} \oplus t_{3,32} \oplus \ldots \oplus t_{31,32}
\end{array}
$$

Par conséquent :

$$
value[0] \oplus value[1] \oplus value[2] \oplus value[3] \oplus \ldots \oplus value[32] = flag
$$

C'est ce que réalise le script [`integration-par-parties-solve.py`](./integration-par-parties-solve.py) :

```sh
$ python3 integration-par-parties-solve.py
flag = 'FCSC{9d32625a5f1365498854445f129406bbff2835f41db66361263396fef2de7681}'
```
