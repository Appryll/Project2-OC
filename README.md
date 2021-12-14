# Project2-OC

Comment créer et activer l'environnement virtuel, puis exécuter le code d'application

--- Pour créer un environnement virtuel, dans la racine du projet, en votre terminal exécutez la commande python -m venv <environment name>  .

--- Pour activer l'environnement, exécutez source env/bin/activate  (si vous êtes sous Windows, la commande sera env/Scripts/activate.bat  ). 
    À ce stade, votre terminal ajoutera probablement le nom de votre environnement au début de chaque ligne de votre terminal.
    Si vous exécutez pip freeze, vous ne devriez maintenant pas voir de paquet répertorié. Cela montre qu'aucun paquet n'est installé dans votre environnement virtuel. 
    C'est le comportement par défaut lorsque vous créez un environnement virtuel.

--- cd dans le répertoire où se trouve requirements.txt et dans votre terminal utilisez pip install -r requirements.txt

--- Dans la racine du projet, en votre terminal tapez 'python main.py' pour que la magie commence

--- Si vous devrez « quitter » ou « désactiver » votre environnement virtuel, exécutez la commande deactivate  pendant que votre environnement virtuel est activé. 
Selon le terminal que vous utilisez, le suffixe (env)  n’apparaîtra plus.
