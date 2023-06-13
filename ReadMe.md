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

On peut alors imaginer plusieurs tests pour identifier toutes les sorties ci-dessus :
- Vérifier que des fichiers ont bien été généré dans le répertoire de sortie prévu _Outputs_ &rarr; **test_NoFileGenerated.py**
- Vérifier que les fichiers JSON générés possèdent bien 5 clés &rarr; **test_RightNumberOfKeys.py**
- Vérifier que les fichiers JSON générés possèdent bien 

Based on the given context, we need to verify the structure of the output of the middleware. To do that, we need to define what are all the possible outputs of the programs. This should include the right outputs and the corrupt one.

Here is the list of all the possible outputs :
- Correct Json 
    - Right number of keys
    - Right names
    - Right type of values
    - Correct file
- Corrupt output --> no-json file
- Corrupt output:
    - Wrong numbher of keys
    - Wrong type(s) of parameters
    - Wrong value associated with a parameter

## Implémentation
I decided to use the Nose framework to implement my tests. Nose is a really efficient tool to implement tests in python and to automate them. Futhermore, the log of each test is well made with Nose, so that it is easy to debub afterwards. Moreover, I already work with NoseTest, so it was a obvious choice for me.

## Commands
Each test is written in an individual file so that it is possible to play only one test. It is also possible to play all the tests in one proces with the testing command _pytest_

To call a test you can directly use the command:
pytest <file_name>.py_

To call all test in one process you can directly use the command:
_pytest_