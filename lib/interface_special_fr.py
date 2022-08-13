""" Special FR interface

This file implement some useful functions for interactive Python terminal interface.
"""

# Copyright (c) MClavier (mathieu.clavier@outlook.com - https://github.com/claviermathieu).
# Distributed for personnal use

import os
import lib.interface_generic_fr as gi

# -----------------------------------------------------------------------------
# Menu
# -----------------------------------------------------------------------------

def presentation(input_folder):
        gi.title("A propos")
        gi.describe([
            "# Titre :\t Template de programme de transformation de données",
            "# Crédentials :\t MClavier (mathieu.clavier@outlook.com)",
            
            "\n\n# Objectifs : Définir l'objectif\n\n",
            "-------------------------------------------------------------------------------------",
            "* Input :",
            "\tBase de données issues de CGI",
            "\t- file1.csv",
            "\t- file2.csv",
            "\t- file3.csv",

            "* Output :",
            "\t- output.csv \t fichier contenant tous les contrats du scope",
            "-------------------------------------------------------------------------------------",
            ""
        ])
        gi.pause()
        input_folder = gi.menu_principal(input_folder)
        return input_folder






















