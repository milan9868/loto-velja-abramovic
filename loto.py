import random


def generate_n_numbers(n: int) -> set[int]:
    return {random.randint(1,39) for _ in range(n+1)}

def number_of_guessed(winning: set[int], guessed: set[int]) -> int:
    print(winning.intersection(guessed))
    return len(winning.intersection(guessed))




veljino_prorocanstvo = generate_n_numbers(8)
dobitna_kombinacija = generate_n_numbers(7)
print(veljino_prorocanstvo)
print(dobitna_kombinacija)
print(number_of_guessed(dobitna_kombinacija,veljino_prorocanstvo))

mapa = {}
