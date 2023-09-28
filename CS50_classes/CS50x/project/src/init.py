import numpy as np
import json
from classes.human import Human
from classes.zombie import Zombie


def initialize():

    with open("../conf/human.json") as f:
        humans_dict = json.load(f)

    with open("../conf/zombie.json") as f:
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
