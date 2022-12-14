"""A template for datascience app. Code format from ipykernel team"""

# Copyright (c) MClavier (mathieu.clavier@outlook.com - https://github.com/claviermathieu).
# Distributed for personnal use

# -----------------------------------------------------------------------------
# Environment
# -----------------------------------------------------------------------------

# Local packages
import lib.interface_generic_fr as gi
import lib.interface_special_fr as si
import lib.utils_generic as gu
import lib.utils_special as su

# Public packages
t = gi.start("Importation des packages")
import os
import numpy as np
import pandas as pd
# import pandas_profiling as pp
from tqdm import tqdm   # Barre de progès
from rich import print
gi.end(t)

# -----------------------------------------------------------------------------
# Inputs and outputs configuration
# -----------------------------------------------------------------------------

DEV_MODE = 1
INPUT_FOLDER = "delits 2022-06-22"
if not DEV_MODE:
    # Get input folder
    input_folder = os.listdir('input')[-1]
    # gs.presentation give the possibility to change the input and output folder
    input_folder = si.presentation(input_folder)
else:
    input_folder = INPUT_FOLDER

# Create output folder if not existing
gu.create_folder('output', input_folder)
gu.create_folder('output/' + input_folder, 'intermediate')
gu.create_folder('output/' + input_folder, 'figures')
gu.create_folder('output/' + input_folder, 'controls')

# # Complete path
output_folder = 'output/' + input_folder + '/'
input_folder = 'input/' + input_folder + '/'

# -----------------------------------------------------------------------------
# Read data
# -----------------------------------------------------------------------------

gi.title("Programme principal")

# Read data
t = gi.start("Lecture des données")
df = pd.read_csv(input_folder + 'donnee-dep-corr.csv', sep = ";")
gi.end(t)

# First visualisation : use pandas profiling -> specify the file
DATA_EXPLORATION = 0
if DATA_EXPLORATION:
    profile = pp.ProfileReport(df, title = input_folder + 'donnee-dep-corr.csv')
    profile.to_file(output_folder + '/intermediate/donnee-dep-corr.html')

# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------

gi.sub_title("Etape 1 : choisir les paramètre")


from rich.theme import Theme
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})


print("[warning]test[/warning]")





gi.describe([
    "[bold u dim cyan]OUTILS[/bold /u dim cyan]!"
])









print("Hello, [bold u dim cyan]World[/bold /u di]!", ":vampire:")









# -----------------------------------------------------------------------------
# Program end
# -----------------------------------------------------------------------------
if not DEV_MODE:
    os.startfile('output')
    input("\n\n# Fermeture du programme. Entrer pour continuer > ")
