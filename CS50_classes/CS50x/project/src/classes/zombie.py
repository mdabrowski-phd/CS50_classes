import numpy as np
from classes.common import Character


class Zombie(Character):

    def __init__(self, x, y, velocity, power, n_infected=0):

        super().__init__(x, y, velocity, power)
        self.n_infected = n_infected

    def choose_new_position(self, humans):

        vectors_to_humans = [np.array([h.x - self.x, h.y - self.y]) for h in humans]
        normalized_vectors = [vec / (np.linalg.norm(vec) + .000001) for vec in vectors_to_humans]

        weighted_vectors = [vec * (self.power + self.n_infected - h.power - h.n_killed)
                            for vec, h in zip(normalized_vectors, humans)]

        vectors_sum = sum(weighted_vectors)  # -> np.array([x, y])
        normalized_vectors_sum = vectors_sum / (np.linalg.norm(vectors_sum) + .001)

        delta_x, delta_y = normalized_vectors_sum * self.velocity

        return delta_x, delta_y
