from visualization import visualize_simulation
from fight_functions import *


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
