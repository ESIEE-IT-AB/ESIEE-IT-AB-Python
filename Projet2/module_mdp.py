"""
Permet de caculer N selon le type de char utiliser dans le mot de passe
"""
import math
import string
def calcul_N(mdp):
    # binaire
    binaire = True
    for char in mdp:
        if char not in '01':
            binaire = False
            break
    if binaire:
        return 2

    # décimal
    decimal = True
    for char in mdp:
        if char not in '0123456789':
            decimal = False
            break
    if decimal:
        return 10

    # hexadécimal
    hexadecimal = True
    for char in mdp:
        if char not in '0123456789ABCDEF':
            hexadecimal = False
            break
    if hexadecimal:
        return 16

    # alphabétique majuscule
    alphabetique_majuscule = True
    for char in mdp:
        if char not in string.ascii_uppercase:
            alphabetique_majuscule = False
            break
    if alphabetique_majuscule:
        return 26

    # alphanumérique majuscule
    alphanumerique_majuscule = True
    for char in mdp:
        if char not in (string.digits + string.ascii_uppercase):
            alphanumerique_majuscule = False
            break
    if alphanumerique_majuscule:
        return 36

    # alphabétique (majuscules et minuscules)
    alphabetique_majuscules_minuscules = True
    for char in mdp:
        if char not in string.ascii_letters:
            alphabetique_majuscules_minuscules = False
            break
    if alphabetique_majuscules_minuscules:
        return 52

    # alphanumérique (majuscules, minuscules et chiffres)
    alphanumerique_majuscules_minuscules_chiffres = True
    for char in mdp:
        if char not in (string.digits + string.ascii_letters):
            alphanumerique_majuscules_minuscules_chiffres = False
            break
    if alphanumerique_majuscules_minuscules_chiffres:
        return 62

    # alphanumérique étendu avec symboles
    alphanumerique_etendu_avec_symboles = True
    for char in mdp:
        if char not in (string.digits + string.ascii_letters + '!#$%?'):
            alphanumerique_etendu_avec_symboles = False
            break
    if alphanumerique_etendu_avec_symboles:
        return 70

    # Sinon plus puissant
    return 90


"""
Permet de caculer L la longueur de charactere du mot de passe
"""
def calcul_L(mdp):
    return len(mdp)


"""
Permet de calculer l'entropie d'un mot de passe afin de connaitre sa force
"""
def calcul_entropie(mdp):
    result = []
    L = calcul_L(mdp)
    N = calcul_N(mdp)

    entropie = L * math.log2(N)

    if entropie <= 64:
        return (round(entropie, 2), "très faible")
    elif 64 < entropie <= 80:
        return (round(entropie, 2), "faible")
    elif 80 < entropie <= 100:
        return (round(entropie, 2), "moyen")
    else:
        return (round(entropie, 2), "fort")

