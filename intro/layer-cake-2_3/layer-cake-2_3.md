# Layer Cake 2/3

<img alt="énoncé du challenge" src="enonce.png" width=300>

----

En regardant l'historique de l'image docker, on s'aperçoit effectivement qu'un fichier `/tmp/secret ` a été supprimé :

```sh
{ ~ }  » docker pull anssi/fcsc2024-forensics-layer-cake-2

{ ~ }  » docker history anssi/fcsc2024-forensics-layer-cake-2 --no-trunc --format '{{.CreatedBy}}'
CMD ["/bin/sh"]
USER guest
RUN /bin/sh -c rm /tmp/secret # buildkit
COPY secret /tmp # buildkit
/bin/sh -c #(nop)  CMD ["/bin/sh"]
/bin/sh -c #(nop) ADD file:37a76ec18f9887751cd8473744917d08b7431fc4085097bb6a09d81b41775473 in /

{ ~ }  » docker save anssi/fcsc2024-forensics-layer-cake-2 -o fcsc2024-forensics-layer-cake-2.tar
```

Or pour construire une image, à l'issue de "chaque" instruction dans le Dockerfile, un layout est généré. Ce layout est une sorte de `diff` entre l'état "avant" et "après" de l'instruction. Ensuite, c'est l'empilement successif des layouts qui permet l'obtention de l'image finale.

A noter que les layouts restent présents dans l'image du container.

Ainsi lors de la construction de l'image de `anssi/fcsc2024-forensics-layer-cake-2` on aura :
- un layout `COPY secret /tmp` dans lequel le fichier `secret` est rajouté
- suivi par le layout `RUN /bin/sh -c rm /tmp/secret` supprimant celui-ci

Pour obtenir le contenu du fichier, il suffit donc d'accéder au layout où le fichier est ajouté.

Une façon d'obtenir les layouts consiste à récupérer l'image sous forme d'archive :

```sh
{ ~ }  » docker save anssi/fcsc2024-forensics-layer-cake-2 -o fcsc2024-forensics-layer-cake-2.tar
```

Dans l'archive on trouve alors le fichier `4971931b4037e1af1affdf7e4371faa2555c0eb9e482d08564400bfc5a81a26a/layer.tar/tmp/secret` contenant le flag recherché.
