import numpy as np
from classes.common import Character


class Human(Character):

    def __init__(self, x, y, velocity, power, n_killed=0):

        super().__init__(x, y, velocity, power)
        self.n_killed = n_killed

    def choose_new_position(self, zombies):

        vectors_to_zombies = [np.array([z.x - self.x, z.y - self.y]) for z in zombies]
        normalized_vectors = [vec / (np.linalg.norm(vec) + .000001) for vec in vectors_to_zombies]

        weighted_vectors = [vec * (self.power + self.n_killed - z.power - z.n_infected)
                            for vec, z in zip(normalized_vectors, zombies)]

        vectors_sum = sum(weighted_vectors)  # -> np.array([x, y])
        normalized_vectors_sum = vectors_sum / (np.linalg.norm(vectors_sum) + .001)

        delta_x, delta_y = normalized_vectors_sum * self.velocity

        return delta_x, delta_y
