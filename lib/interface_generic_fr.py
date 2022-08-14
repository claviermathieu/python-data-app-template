""" Genereic FR interface

This file implement some useful functions for interactive Python terminal interface.
"""

# Copyright (c) MClavier (mathieu.clavier@outlook.com - https://github.com/claviermathieu).
# Distributed for personnal use

import os
from datetime import datetime
import lib.interface_special_fr as si

# -----------------------------------------------------------------------------
# Inputs
# -----------------------------------------------------------------------------

def input_menu(n_choices):
    """
    Select input number between 1 and n_choices.
    """
    # Possible values
    choices = [str(i) for i in range(1, n_choices+1)] + [str(7), str(8), str(9)]
    # Ask the input
    choice = input("\n# Votre choix ? > ")
    # Control
    if choice not in choices:
        print("> Erreur de saisie : veuillez saisir un nombre entre 1 -", n_choices, "ou 7-9\n")
        choice = input_menu(n_choices = n_choices)
    return int(choice)

def input_int():
    select = input("> ")
    try:
        select = int(select)
    except:
        print("> Erreur de saisie : veuillez saisir un nombre entier.\n")
        choice = input_int()
        
    return select

def input_float(lb, ub):
    """
    Select a float number between lb and ub.
    """
    select = input("> ")
    # Type control
    try:
        select = float(select)
    except:
        print("\n /!\ --- Veuillez saisir un nombre entre",lb, "et",ub, " --- /!\ \n")
        select = input_float(lb, ub)
    # Value control
    if not ((select >= lb) & (select <= ub)):
        print("> Erreur de saisie : veuillez saisir un nombre entre",lb, "et",ub, "\n")
        select = input_float(lb, ub)
    return float(select)

def input_confirm():
    """
    Confirm input
    """
    possibilities = ['o', 'n']
    choice = input("Confirmer (o/n) ? > ")
    # Vérification de la validité de l'input
    if choice not in possibilities:
        print("\n /!\ --- Veuillez saisir un 'o' ou 'n' --- /!\ ")
        choice = input_confirm()
    if choice == 'o':
        choice = 1
    else:
        choice = 0
    return choice

# -----------------------------------------------------------------------------
# Titles
# -----------------------------------------------------------------------------

def title(monTitre):
    """
    Formatage : nettoyage du terminal plus ajout du titre au format standard.
    """
    os.system("cls")
    n = len(monTitre)
    print("-"*(n+12))
    print("##### "+monTitre+" #####")
    print("-"*(n+12)+"\n")

def sub_title(monTitre):
    """
    Formatage : nettoyage du terminal plus ajout du titre au format standard.
    """
    print("\n#"+"-"*50)
    print("# " + monTitre + "\n")

def describe(my_list):
    for i in range(len(my_list)):
        print(my_list[i])

# -----------------------------------------------------------------------------
# Menu
# -----------------------------------------------------------------------------


def menu_principal(input_folder):
        title("Menu principal")
        describe([
            "Que souhaitez-vous faire ?",
            
            "\n\t1. Gestion des inputs",
            "\t2. Exécuter le programme",

            "\n\t7. Menu principal",
            "\t8. A propos",
            "\t9. Quitter\n\n"
        ])
        # Get choice
        choice = input_menu(2)

        if choice == 1:
            input_folder = menu_input(input_folder)
        elif choice == 2:
            pass
        elif choice == 7:
            menu_principal(input_folder)
        elif choice == 8:
            si.presentation(input_folder)
        elif choice == 9:
            quit(input_folder)
        else:
            raise ValueError("Normally it cannot go here. Check code !")
        
        return input_folder


def menu_input(input_folder):
    # os.system('cls')
    title("Gestion des inputs")
    describe([
        "Que souhaitez-vous faire ?", 
        "\n\t1. Visualiser les dossiers diponibles",
        "\t2. Modifier le dossier d'input sélectionné",
        "\t3. Visualiser les fichiers présents",
    
        "\n\t7. Retour au menu principal",
        "\t8. A propos",
        "\t9. Quitter\n"
    ])
    print("#----------------------------------------------------------------------")
    print("# Dossier actuellement sélectionné :", input_folder)
    print("#----------------------------------------------------------------------\n")
    # Get choice
    choice = input_menu(3)

    # View folder available
    if choice == 1:
        print("\nLes dossiers présents :",os.listdir('input'))
        pause()
        menu_input(input_folder)
    # Modify input folder
    elif choice == 2:
        print("\nLes dossiers présents :",os.listdir('input'))
        input_folder = input("\nRenseignez le dossier d'inputs > ")
        while input_folder not in os.listdir('input'):
            input_folder = input("\nRenseignez un dossier existant > ")
        menu_input(input_folder)
    # Visualize all files in input_folder
    elif choice == 3:
        files = os.listdir('input/' + input_folder)
        print("\n--------------------------------------")
        print("Les fichiers présents sont:")
        for file in files:
            print("\t-", file)
        print("--------------------------------------")
        pause()
        menu_input(input_folder)
    # Main menu
    elif choice == 7:
        menu_principal(input_folder)
    # Program description
    elif choice == 8:
        si.presentation(input_folder)
    # Quit
    elif choice == 9:
        if input_confirm():
            exit
        else:
            menu_input(input_folder)
    else:
        raise ValueError("Normally it cannot go here. Check code !")

    return input_folder

# -----------------------------------------------------------------------------
# Others
# -----------------------------------------------------------------------------

def quit(input_folder):
    if input_confirm():
            exit
    else:
        menu_principal(input_folder)

def pause():
    input("\n# Entrer pour continuer > ")
    print('')

def start(my_str):
    n = len(my_str)
    # Count number of '.' to add
    add_points = 50 - n
    print(my_str + '.'*add_points, end = '')
    return(datetime.now())

def end(t):
    print("OK/", (datetime.now() - t).seconds, "secondes")
























































