# VRP - v2
Script pour avoir la console en petite fenêtre par dessus tout

## Configuration
Pour l'utiliser, il faudra mettre votre session ID qui permet de vous connecter au site
Pour le trouver:
1. Sur votre navigateur, allez sur le site
2. Ouvrez l'inspecteur web / DevTool (CTRL + MAJ + I)
3. Allez dans l'onglet application puis dans cookies
4. Trouvez le cookie correspondant au site
5. Vous devriez avoir une ligne avec une chaine de caractère aléatoire, copiez là
6. Ouvrez `app.py` dans le bloc note et dans les dernières lignes, dans `cookie_value`, collez la chaine de caractère à la place de `SESSION_ID`
7. Enregistrez

**Attention, ne partagez pas votre session ID, cela donnerais l'accès à votre compte**

## Utilisation
Une fois configuré, lancé juste `run.bat`

*Ne fermer pas la fenêtre de console, ça arrêterait le programme*

## Customization
Taille de la fenêtre dans `self.setFixedSize(400, 300)`
Titre et icon dans `self.setWindowTitle("VRP - v2")` et `self.setWindowIcon(QtGui.QIcon("logo.png"))`
