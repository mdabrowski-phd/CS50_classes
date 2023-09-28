import matplotlib.pyplot as plt


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
