""" Generic utils

Some useful functions to commun tasks.
"""

# Copyright (c) MClavier (mathieu.clavier@outlook.com - https://github.com/claviermathieu).
# Distributed for personnal use

import os

# -----------------------------------------------------------------------------
# OS functions
# -----------------------------------------------------------------------------

def create_folder(path, folder_name):
    try:
        mode = 0o666
        os.mkdir(path + "/" + folder_name + "/", mode)
    except:
        pass



