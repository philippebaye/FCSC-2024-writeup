# Illuminated

<img alt="énoncé du challenge" src="enonce.png" width=300>

Les fichiers fournis :
- [capture.pcap](capture.pcap)
- [cheatsheet.pdf](cheatsheet.pdf)

----

En ouvrant le fichier `capture.pcap` fourni, on se rend compte que celui-ci contient exclusivement des trames "DMX Channels", ce qui est cohérent par rapport à l'énoncé. On a donc une capture qui contient exclusivement les différents états de la table d'éclairage composée de 2 parties.

Le fichier PDF permet de comprendre comment interpréter ces trames.

Art-Net > ArtDMX packet > Universe :
- 0 : correspond au haut de la table (annoté Universe 1 dans le PDF),
- 1 : correspond au bas de la table (annoté Universe 2 dans le PDF)

DMX Channel :
- Chaque octet représente le niveau de couleur, qui en fonction de sa position est Rouge, Vert ou Bleu.
- En regroupant 3 par 3 ces octets, on récupère les 3 composantes RVB de chacune des LED.
    - Pour la LED 1, il s'agit des 3 premiers octets de l'Universe 0 : 0, 1, 2
    - Pour la LED 2, les 3 suivants : 3, 4, 5
    - ...
- Le cablage des LED est réalisé en "serpent". Ainsi comme indiqué sur le schéma, la LED 17 est située juste en dessous de la LED 16.
    - Les octets 45, 46, 47 correspondent aux couleurs de la LED 16
    - Les octets 48, 49, 50 correspondent aux couleurs de la LED 17
- La partie haute de la table est composée de 10x16 LED, soit 3x10x16 octets
- La partie basse de la table est composée de 6x16 LED, soit 3x6x16 octets

Par conséquent pour chaque couple de données (Universe 0, Universe 1), on peut reconstituer l'image globale de la table.

En mettant bout à bout les différentes images on reconstitue un film, dont le visionnage permet de récupérer le flag.

Le script [`illuminated.py`](./illuminated.py) permet de reconsituer le film [`illuminated.avi`](./illuminated.avi)

Pour construire les images, la 1ère approche a été d'utiliser des cercles pour simuler les différentes LED de la table. Mais l'utilisation de rectangles donne au final un rendu plus lisible.
