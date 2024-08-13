import numpy as np

def generate_random_2d_points(n,number_of_particle, x_range=(0, 50), y_range=(0, 100)):
    id_range = (1,number_of_particle+1)
    ids = np.random.randint(id_range[0], id_range[1], n)
    x = np.random.randint(x_range[0], x_range[1], n)
    y = np.random.randint(y_range[0], y_range[1], n)
    return np.vstack((ids, x, y)).T