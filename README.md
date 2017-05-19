## Fermeture du dépot ##


Bonjour à tous,

Comme vous avez pu le remarquer, ce dépot n'est plus maintenu depuis plusieurs mois, faute de temps et de motivation.
Car en effet ce dépot avait été ouvert à une époque où les solutions de recherche sur les trackers francais (pour couchpotato) disparaissaient ou n'étaient plus maintenues.

Aujourd'hui d'autres solutions s'offrent à vous, je vous propose de vous rapprocher de **Cyberden** (qui est actif sur le [forum Mondedie.fr](https://mondedie.fr/d/8960-couchpotato-xthor-t411 "topic MonDedie.fr: CouchPotato - Xthor & T411")) qui fait un boulot formidable en maintenant un dépot de Couchpotato avec les plugins/trackers que vous recherchez:

- Abnormal
- Cpasbien
- T411 (2 plugins, dont un utilisant l'API)
- Torrent9
- Xthor

et bien d'autres encore. (la gestion du [doublage francais](https://github.com/cyberden/CouchPotatoServer/commit/bf15e1aea5838c3ec15239bae0110a5d9b8e0fee "gestion doublage francais") et des [titres en francais](https://github.com/cyberden/CouchPotatoServer/commit/355ca50684398b5d74ab81b5cf284ff403bca331 "gestion titres en francais") fonctionne)

Voici comment basculer votre installation actuelle (de Couchpotato) vers le dépot de **[Cyberden](https://github.com/cyberden/CouchPotatoServer "dépot de Cyberden")**:

1. En SSH, placez-vous dans le dossier de l'application **Couchpotato** (pour le retrouver: `whereis couchpotato`)

2. Entrez la commande: `nano .git/config`

3. Repérez la ligne: 

> [remote "origin"]
>         
>    url = https://github.com/CouchPotato/CouchPotatoServer.git

Et modifiez la en:

> [remote "origin"]
> 
>    url = https://github.com/cyberden/CouchPotatoServer.git

Sauvegardez en utilisant les commandes `Ctrl+O` puis `Ctrl+X`

4. Entrez la commande: `git pull`

5. Accédez à l'interface de Couchpotato et lancez un redémarrage (`Restart`)


**EnJoY**, protifez de vos nouveaux plugins ;)
