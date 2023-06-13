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

En complément de ces tests, on peut imaginer des scénarios plus complet en fonction du système :


## Implémentation
**test_NoFileGenerated.py** :


**test_RightNumberOfKeys.py** :


**test_RightKeyNames.py** :


**test_RightKeyTypes** :


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