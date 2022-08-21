# Faultline
Malware Python subtilisant les données.

Le but étant de programmer un spyware entièrement en python.
Le logiciel a été testé sur une machine Windows et sera probablement inefficace sur un autre OS.

# Mise en place : 

Si vous rencontrez des difficultés lors de l'installation des modules Python avec la commande 'pip install -r requirements.txt', essayez 'pip install --upgrade pip' avant de relancer la commande.

Une version de Microsoft Visual C++ supérieure ou égale à 14.0 est également nécessaire.

Il est possible de convertir un logiciel Python en .exe, qui sera testé plus tard avec un logiciel comme nuitka (par exemple).

Lancez le code dans le dossier 'Hacker_Side' sur la machine de l'attaquant,
puis le code dans le dossier 'Target_Side' sur la machine cible.
Vous aurez très probablement besoin de modifier l'adresse IP présente dans le fichier 'Target_Side/src/networking.py' afin de mettre la votre.

Comme je n'ai personnellement pas d'intention malveillante avec ce programme, je n'ai pris absolument aucune mesure pour me cacher ou pour ne pas faire en sorte qu'on ne puisse pas remonter jusqu'à moi car la seule personne que je vais pirater n'est autre que moi-même. Si vous utilisez ce programme à des fins malveillantes, c'est donc à vos risques et périls à moins que vous ne preniez des mesures afin d'espérer être plus anonymes.

# Crédits :
Pour écrire le code, je me suis beaucoup aidé du livre 'Black Hat Python' achetable sur Internet.

Je m'aiderai aussi probablement d'autres logiciels du net ou de vidéos Youtube comme par exemple sur la chaîne de David Bombal, pour récupérer des mots de passe stockés sur l'ordinateur (Wi-Fi, navigateur web, hash NTLM, etc...).
