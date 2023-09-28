import numpy as np
from classes.zombie import Zombie


def find_all_pairs_about_to_clash(humans, zombies):

    clash_pairs = list()

    for i, h in enumerate(humans):
        for j, z in enumerate(zombies):

            if np.sqrt((h.x - z.x)**2 + (h.y - z.y)**2) < 3:
                clash_pairs.append((i, j))

    return clash_pairs


def calculate_n_of_rivals(humans, zombies, clash_pairs):

    rivals_number = {"humans": np.zeros(len(humans), dtype=int), "zombies": np.zeros(len(zombies), dtype=int)}

    for pair in clash_pairs:

        rivals_number["humans"][pair[0]] += 1
        rivals_number["zombies"][pair[1]] += 1

    return rivals_number


def carry_out_clashes(humans, zombies, clash_pairs, rivals_number):

    victories = {"humans": np.zeros(len(humans), dtype=int), "zombies": np.zeros(len(zombies), dtype=int)}
    loosers = {'humans': list(), 'zombies': list()}

    for pair in clash_pairs:

        h, z = humans[pair[0]], zombies[pair[1]]

        if (h.power + h.n_killed) / rivals_number["humans"][pair[0]] > \
           (z.power + z.n_infected) / rivals_number["zombies"][pair[1]]:

            victories["humans"][pair[0]] += 1
            loosers["zombies"].append(pair[1])

        elif (h.power + h.n_killed) / rivals_number["humans"][pair[0]] < \
             (z.power + z.n_infected) / rivals_number["zombies"][pair[1]]:

            victories["zombies"][pair[1]] += 1
            loosers["humans"].append(pair[0])

        else:  # przypadek remisu, obie postaci umierają

            loosers["humans"].append(pair[0])
            loosers["zombies"].append(pair[1])

    return victories, loosers


def implement_results(humans, zombies, victories, loosers):

    for i, human in enumerate(humans):
        human.n_killed += victories["humans"][i]

    for i, zombie in enumerate(zombies):
        zombie.n_infected += victories["zombies"][i]

    for looser in sorted(np.unique(loosers["humans"]))[::-1]:

        zombies.append(Zombie(humans[looser].x, humans[looser].y, humans[looser].velocity, humans[looser].power))
        del humans[looser]

    for looser in sorted(np.unique(loosers["zombies"]))[::-1]:
        del zombies[looser]
