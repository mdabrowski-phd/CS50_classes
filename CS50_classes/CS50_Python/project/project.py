import json
import numpy as np
import matplotlib.pyplot as plt

from classes.human import Human
from classes.zombie import Zombie


def main():

    map2d = np.zeros([100, 100])
    humans, zombies = initialize()
    run_simulation(humans, zombies, map2d)


def initialize():

    with open("./conf/human.json") as f:
        humans_dict = json.load(f)

    with open("./conf/zombie.json") as f:
        zombies_dict = json.load(f)

    humans = []
    for _ in range(humans_dict["initial_number"]):

        x = np.random.normal(humans_dict["x"][0], humans_dict["x"][1])
        y = np.random.normal(humans_dict["y"][0], humans_dict["y"][1])
        velocity = np.random.normal(humans_dict["velocity"][0], humans_dict["velocity"][1])
        power = np.random.normal(humans_dict["power"][0], humans_dict["power"][1])

        humans.append(Human(x, y, velocity, power))

    zombies = []
    for _ in range(zombies_dict["initial_number"]):

        x = np.random.normal(zombies_dict["x"][0], zombies_dict["x"][1])
        y = np.random.normal(zombies_dict["y"][0], zombies_dict["y"][1])
        velocity = np.random.normal(zombies_dict["velocity"][0], zombies_dict["velocity"][1])
        power = np.random.normal(zombies_dict["power"][0], zombies_dict["power"][1])

        zombies.append(Zombie(x, y, velocity, power))

    return humans, zombies


def run_simulation(humans, zombies, map2d):

    t = 0
    while t <= 1000 and len(humans) and len(zombies):

        t += 1
        visualize_simulation(humans, zombies, map2d, t)

        humans_pos = [np.array(human.choose_new_position(zombies)) for human in humans]
        zombies_pos = [np.array(zombie.choose_new_position(humans)) for zombie in zombies]

        for i, human in enumerate(humans):
            human.move(humans_pos[i][0], humans_pos[i][1])

        for j, zombie in enumerate(zombies):
            zombie.move(zombies_pos[j][0], zombies_pos[j][1])

        clash_pairs = find_all_pairs_about_to_clash(humans, zombies)
        rivals_number = calculate_n_of_rivals(humans, zombies, clash_pairs)
        victories, loosers = carry_out_clashes(humans, zombies, clash_pairs, rivals_number)

        implement_results(humans, zombies, victories, loosers)


def visualize_simulation(humans, zombies, map2d, t):

    map2d_copy = map2d.copy()

    for h in humans:
        map2d_copy[int(h.x)][int(h.y)] = 0.8

    for z in zombies:
        map2d_copy[int(z.x)][int(z.y)] = 0.5

    plt.imshow(map2d_copy)
    plt.title(f'Iteration: {t}, #humans: {len(humans)}, #zombies: {len(zombies)}')

    plt.show(block=False)
    plt.pause(0.2)


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

        else:

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


if __name__ == "__main__":
    main()
    