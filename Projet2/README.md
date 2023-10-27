# Générateur et testeur de mot de passe

## Description

Ce projet vous permet de générer des mots de passe sécurisés ainsi que de tester la robustesse d'un mot de passe existant en fonction de critères précis. Il comprend également un générateur de passphrase basé sur la méthode de dés de l’EFF.

## Fonctionnalités

1. **Testeur de mot de passe** : Calcule la force d'un mot de passe basé sur l'entropie respectant les critères de l’ANSSI. 
2. **Générateur de mot de passe aléatoire** : Permet à l'utilisateur de définir des critères tels que le nombre de minuscules, majuscules, chiffres et caractères spéciaux. Le mot de passe généré est ensuite affiché avec son entropie et sa force.
3. **Générateur de passphrase** : Basé sur la méthode de dés de l’EFF.
4. **Menu** : Un menu permet de selectionner l'outil que vous voulez utiliser.
   
## Comment démarrer ?

1. Exécutez `main.py` pour démarrer le programme.
2. Suivez les instructions à l'écran pour tester un mot de passe, générer un nouveau mot de passe et une nouvelle passphrase.

```
python main.py
```

## Structure du projet

- **main.py** : Point d'entrée du programme.
- **force_mdp.py** : Contient la classe principale `FORCE_MDP` qui permet de calculer la force d'un mot de passe.
- **gen_mdp.py** : Contient la classe principale `GEN_MDP` qui permet de crée un mot de passe et d'afficher sa force.
- **gen_passphrase.py** : Contient la classe principale `GEN_PASSPHRASE` qui permet de crée une passphrase via un dictionnaire de mot.
- **module_mdp.py** : Contient les fonction qui calcule la force d'un mot de passe.
- **file.py** : Contient la classe `FILE` qui gère la lecture du fichier contenant la liste de mots pour la passphrase.
- **test.py** : Contient les tests unitaires pour le projet.

## Tests

Pour exécuter les tests unitaires, exécutez `test.py`.

```
python -m unittest test.py
```

## Liens utiles

- Critères de l’ANSSI pour le calcul de la force d'un mot de passe : [ANSSI](https://www.ssi.gouv.fr/administration/precautionselementaires/calculer-la-force-dun-mot-de-passe/)
- Méthode de dés de l’EFF pour la passphrase : [EFF Dice](https://www.eff.org/fr/dice)

## Auteur

BESSON Antoine
