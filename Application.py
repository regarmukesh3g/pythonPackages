#!/usr/bin/env python
from distributions.gaussian_distribution import Gaussian

gaussian = Gaussian(0, 0)
gaussian.read_data_file('numbers.txt')
gaussian.plot_hist()

g1 = Gaussian(20, 5)
g2 = Gaussian(24, 4)
g3 = g1 + g2
g3
