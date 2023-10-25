# Projet QCM Python

Ce projet est un système de questionnaire à choix multiple (QCM) développé en Python. Il permet de poser une série de questions, de mélanger les questions et leurs choix de réponses, et d'évaluer les réponses de l'utilisateur.

## Fonctionnalités

- Pose de questions à choix multiple.
- Mélange aléatoire des questions et des choix.
- Evaluation des réponses de l'utilisateur.
- Affichage du score final de l'utilisateur.

## Structure du projet

Le projet est composé de trois fichiers principaux :

1. `main.py` : Le script principal qui initialise les questions et lance le QCM.
2. `qcm.py` : Contient la classe `QCM` qui gère la logique du questionnaire.
3. `question.py` : Contient la classe `Question` qui définit la structure d'une question et ses méthodes associées.

## Utilisation

Pour démarrer le QCM, exécutez le fichier `main.py` :

```
python main.py
```

Suivez les instructions à l'écran pour répondre aux questions. À la fin du QCM, votre score sera affiché.

## Tests

Des tests unitaires ont été écrits pour assurer le bon fonctionnement des principales fonctionnalités. Vous pouvez les exécuter en utilisant le module `unittest` :

```
python -m unittest test.py
```

## Auteur

BESSON Antoine