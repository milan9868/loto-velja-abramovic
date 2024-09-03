import random
from collections import Counter
from typing import Set
import numpy as np


def generate_n_numbers(n: int) -> frozenset:
    return frozenset(random.sample(range(1,40), n))


def number_of_guessed(winning: frozenset, guessed: frozenset) -> int:
    return len(winning & guessed)


veljino_prorocanstvo = generate_n_numbers(8)
dobitna_kombinacija = generate_n_numbers(7)

results = Counter()

NUM_SIMULATIONS = 10_000_000

for _ in range(NUM_SIMULATIONS):
    veljino_prorocanstvo = generate_n_numbers(8)
    dobitna_kombinacija = generate_n_numbers(7)
    results[number_of_guessed(dobitna_kombinacija,veljino_prorocanstvo)] += 1

broj_dobitaka = {x: results[x] / NUM_SIMULATIONS * 100 for x in range(8)}

print(broj_dobitaka)

