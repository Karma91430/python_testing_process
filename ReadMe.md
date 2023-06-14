# Test implémentation :

## Librairies 
- pytest : une librairie simple à prendre en main, qui permet de mettre en place différents protocoles de tests.

## Contexte 
L’objectif est de tester un composant logiciel qui à partir d’une base de données de type sqlite, représentant une base de discussion d’une application de messagerie, génère en sortie des fichiers JSON dans un répertoire où chacun d’entre eux représente un message de cette base.

Le format du fichier JSON attendu en sortie est :
- "id": Integer,
- "timestamp": Integer,
- "direction": String [originated or destinating],
- "content": String [base 64],
- "contact": String

J'ai également récupérer le fichier sql sur VScode/SQLpreview. Cela permet de visualiser directement la base de données et les différentes données à disposition.
Je constate la présence de deux tables importantes :
- contact : contient la liste de tous les contacts sauvegardés
- messages : contient la liste de tous les messages reçus et envoyés

## Principles
L'objectif de cet exercice est de concevoir un protocole de test pour valider le bon fonctionnement de la brique logicielle. Pour ce faire, on va analyser la sortie du système, soit un ou plusieurs fichiers JSON.

Dans un premier temps, je souhaite définir chacune des sorties possibles du système :
- Aucun fichier json n'est généré &rarr; **failure**
- Un ou plusieurs fichiers sont générés :
    - les fichiers ne possèdent pas le bon nombre de clés &rarr; **failure**
    - les fichiers ne possèdent pas le/les bon(s) nom(s) de clés &rarr; **failure**
    - les fichiers ne possèdent pas le/les bon(s) type(s) de valeur(s) associé(s) à chaque clé &rarr; **failure**
    - les fichiers en sortie sont conformes à ce qui est attendu &rarr; **success**

## Tests envisagés
On peut alors imaginer plusieurs tests pour identifier toutes les sorties ci-dessus :
- Vérifier que des fichiers ont bien été généré dans le répertoire de sortie prévu _Outputs_ &rarr; **test_NoFileGenerated.py**
- Vérifier que les fichiers JSON générés possèdent bien 5 clés &rarr; **test_RightNumberOfKeys.py**
- Vérifier que les fichiers JSON générés possèdent les bons noms de clés &rarr; **test_RightKeyNames.py**
- Vérifier que les données dans les fichiers JSON générés correspondent bien aux différents types attendus &rarr; **test_RightKeyTypes**
- Vérifier à partir d'un timestamp donné que le fichier JSON généré correspond bien à ce qui se trouve dans la BDD. &rarr; **test_RightMessageWithRightId**
- Vérifier que l'ID du contact existe bien dans la BDD d'origine. 
- Vérifier la cohérence des messages en fonction de l'état direction

On part du principe que les tests de validation de données précises peuvent s'appuyer sur un modèle textuel de la BDD (comme dans les tests .py) ou alors directement via des _query_ vers la BDD. Cette deuxième solution est plus pertinente dans la mesure où cela permet de développer un test générique. Ce test pourra alors s'adapter automatiquement en fonction, du nombre de paramètre, de la leur nom, de leur type, etc.

## Implémentation

### _test_NoFileGenerated.py_
La méthode est très simple, on utilise la commande _os.listdir_ pour scanner la répertoire choisi et ensuite récuper les noms des fichiers présent dans celui-ci. La commande __assert_ nous permet ensuite de vérifier que la liste générée n'est pas nulle. Cela valide notre vérification de fichiers json.

### _test_RightNumberOfKeys.py_
Pour ce test, on va récupérer la liste des fichiers json générés par la brique logicielle dans une liste. On pourra ensuite parcourir cette liste tout en ouvrant le fichier JSON. Le test va ensuite déterminer combien de clés sont présent dans ledit fichier. Si la valeur est différente de 5 le test est faux. 

Ce test est le parfait exemple d'une version statique. En effet, la valeur 5 est écrit directement dans le test, là où une implémentation via une requête BDD pour déterminer le nombre de paramètre requis, serait beaucoup plus pertinente pour un protocole de test auto-suffiant. 

### _test_RightKeyNames.py_
Pour ce test, on va récupérer la liste des fichiers json générés par la brique logicielle dans une liste. On pourra ensuite parcourir cette liste tout en ouvrant le fichier JSON. Le test va ensuite vérifier que chaque clé présente dans ledit fichier JSON appartient bien à la liste des clées définies au préalable.

### _test_RightKeyTypes_
Pour ce test, on va récupérer la liste des fichiers json générés par la brique logicielle dans une liste. On pourra ensuite parcourir cette liste tout en ouvrant le fichier JSON. Le test va ensuite vérifier que pour chaque clé présente dans le fichier JSON est associé le bon type de variable. Cette vérification se fait au travers d'un model de message JSON sous la forme d'un dictionnaire Python.

### _test_ContactExist_
Pour ce test, on va récupérer la liste des contacts définis dans la table _contact_ de la BDD. Grâce à cette liste (fetchall()), on va vérifier que le nom du contact présent dans le fichier json existe bien dans la BDD. Ce test permet de valider rapidement s'il y a eu une erreur avec la brique logicielle.

### _test_RightMessageWithRightId_
Pour ce test, on récupère grâce à la BDD et au timestamp unique le message source présent dans la BDD. On compare ensuite chaque valeur du fichier JSON avec les valeurs associées dans la base de donnée. Cela permet de réaliser un test complet de tous les fichiers générés par la brique logiciel. Ce test est dynamique, cela signifie qu'il sera mis à jour en fonction de l'évolution de la BDD. 

## Utilisation
Chaque test est écrit dans un fichier unique. Cela permet de rejouer chaque test de manière unitaire sans lancer le protocole de test complet. 
Pour lancer chaque test individuellement, on va utiliser la commande suivante :
- _pytest </fileName/>_ 

Dans le cas où l'on souhaite lancer l'intégralité du protocole de test, on pourra simplement lancer la commande suivante, sans paramètre:
- _pytest_

## Analyse 
La librairie **pytest** offre un détail complet des erreurs lors des tests. Cela permet d'identifier rapidement ce qui a posé problème lors de série de tests complet. On peut également définir plusieurs critères autres que simplement succès ou échec, dans le cas de tests plus complexes par exemple. 

Il est possible d'exporter les logs de **pytest** dans un fichier externe, via la commande :
- _pytest --resultlog=</path/>_