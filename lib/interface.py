""" Interface FR 

This file implement some useful functions for interactive Python terminal interface.
"""

# Copyright (c) MClavier (mathieu.clavier@outlook.com - https://github.com/claviermathieu).
# Distributed for personnal use

# -----------------------------------------------------------------------------
# Inputs
# -----------------------------------------------------------------------------

def input_choice(n_choices):
    """
    Select input number between 1 and n_choices.
    """
    choices = [str(i) for i in range(1, n_choices+1)]
    choix = input("\n# Votre choix (1-"+str(n_choices)+ ") ? ")

    if choix not in choices:
        print("\n /!\ --- Veuillez saisir un nombre entre 1 et", n_choices, " --- /!\ \n")
        choix = input_choix(n_choices = n_choices)
        
    return int(choix)

# -----------------------------------------------------------------------------
# Confirmations
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Titles
# -----------------------------------------------------------------------------





def input_int(n):
    a = int(input("Renseigner une valeur"))
    print(a)






def input_confirmer(self):
    """
    Confirmer la saisie
    """
    possibilites = ['o', 'n']
    choix = input("\n# Confirmer (o/n) ? ")
    # Vérification de la validité de l'input
    if choix not in possibilites:
        print("\n /!\ --- Veuillez saisir un 'o' ou 'n' --- /!\ ")
        choix = input_confirmer()
    return choix



def titre(monTitre):
    """
    Formatage : nettoyage du terminal plus ajout du titre au format standard.
    """
    os.system("cls")

    n = len(monTitre)
    print("#"*(n+8))
    print("### "+monTitre+" ###")
    print("#"*(n+8)+"\n")


def sous_titre(monTitre):
    """
    Formatage : nettoyage du terminal plus ajout du titre au format standard.
    """

    print("-"*60)
    print("# " + monTitre)




def pause(self):
    input("\n------ Appuyer sur entrer pour continuer ------\n")



titre("test")

sous_titre("trez")