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

## Principles
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

## Test implementation
I decided to use the Nose framework to implement my tests. Nose is a really efficient tool to implement tests in python and to automate them. Futhermore, the log of each test is well made with Nose, so that it is easy to debub afterwards. Moreover, I already work with NoseTest, so it was a obvious choice for me.

## Commands
Each test is written in an individual file so that it is possible to play only one test. It is also possible to play all the tests in one proces with the testing command _pytest_

To call a test you can directly use the command:
pytest <file_name>.py_

To call all test in one process you can directly use the command:
_pytest_