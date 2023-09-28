import numpy as np
from project import initialize, run_simulation, find_all_pairs_about_to_clash


def test_initialize():
    initialize()


def test_run_simulation():
    map2d = np.zeros([100, 100])
    humans, zombies = initialize()
    run_simulation(humans, zombies, map2d)


def test_find_all_pairs_about_to_clash():
    humans, zombies = initialize()
    find_all_pairs_about_to_clash(humans, zombies)
