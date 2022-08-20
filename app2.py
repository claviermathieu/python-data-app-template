

class Voiture:

    def __init__(self, marque, prix, couleur):
        self.marque = marque
        self.prix = prix
        self.couleur = couleur


def main():

    maVoiture = Voiture('renault', 10000, 'rouge')
    a = 3

    print(f"etest {a}")



if __name__ == "__main__":
    main()

    print('uniquement ça est executét')

    for i in range(10):
        print('uniquement ça est executét')
        print(i)




# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------
import numpy as np

import timeit


N = 100_000_000

def sum_python():
    return sum(range(100_000_000))


def sum_np():
    return(np.sum(np.arange(100_000_000)))

timeit.timeit(sum_python, number=1)
timeit.timeit(sum_np, number=1)