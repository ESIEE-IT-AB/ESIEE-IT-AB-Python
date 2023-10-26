from mdp import MDP

# FORCE MDP
mdp1 = MDP("Joba1563ADz511qzd")

# NEW MDP
mdp2 = MDP()

# NEW PASSPHRASE
mdp3 = MDP()

def print_menu():
    print('\n\n\n1 Tester la force d\'un mot de passe')
    print('2 Crée un mot de passe et tester sa force')
    print('3 Crée une passphrase')
    print('4 Exit')

while(True):
    print_menu()
    option = int(input('Saisissez votre choix: \n'))
    while option not in [1, 2, 3, 4]:
        if option not in [1, 2, 3, 4]:
            print("Choix inconnu\n")
        option = input("\nSaisissez votre choix: \n")
    match option:
        case 1:
            print("Test de force de votre mot de passe\n")
            mdp = input('Saisissez votre mot de passe :\n')
            mdp1.set_mdp(mdp)
            mdp1.test_force_mdp()
        case 2:
            print("Création de votre mot de passe\n")
            mdp2.new_mdp()
        case 3:
            print("Création de votre passphrase\n")
            mdp3.new_passphrase()
        case 4:
            exit(0)

