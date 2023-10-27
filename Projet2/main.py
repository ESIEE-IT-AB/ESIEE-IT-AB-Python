from force_mdp import FORCE_MDP
from gen_mdp import GEN_MDP
from gen_passphrase import GEN_PASSPHRASE

# FORCE MDP
force_mdp = FORCE_MDP("Joba1563ADz511qzd")

# NEW MDP
gen_mdp = GEN_MDP()

# NEW PASSPHRASE
gen_passphrase = GEN_PASSPHRASE()

def print_menu():
    print('\n\n1 Tester la force d\'un mot de passe')
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
            force_mdp.set_mdp(mdp)
            force_mdp.test_force_mdp()
        case 2:
            print("Création de votre mot de passe\n")
            gen_mdp.new_mdp()
        case 3:
            print("Création de votre passphrase\n")
            gen_passphrase.new_passphrase()
        case 4:
            exit(0)

