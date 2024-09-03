import random
from typing import Set


def generate_n_numbers(n: int) -> frozenset:
    return frozenset(random.randint(1, 39) for _ in range(n))


def number_of_guessed(winning: frozenset, guessed: frozenset) -> int:
    #print(winning.intersection(guessed))
    return len(winning.intersection(guessed))


veljino_prorocanstvo = generate_n_numbers(8)
dobitna_kombinacija = generate_n_numbers(7)
broj_dobitaka = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
}

for _ in range(10_000_000):
    veljino_prorocanstvo = generate_n_numbers(8)
    dobitna_kombinacija = generate_n_numbers(7)
    broj_dobitaka[number_of_guessed(dobitna_kombinacija,veljino_prorocanstvo)] += 1

for key in broj_dobitaka:
    broj_dobitaka[key] /= 100_000

print(broj_dobitaka)

