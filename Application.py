#!/usr/bin/env python
from distributions.gaussian_distribution import Gaussian

gaussian = Gaussian(0, 0)
gaussian.read_data_file('numbers.txt')
#gaussian.plot_hist()

g1 = Gaussian(20, 5)
g2 = Gaussian(24, 4)
g3 = g1 + g2
g3
from distributions import Binomial

b1 = Binomial()
b1.read_data_file('numbers_binomial.txt')
b2 = Binomial()
b2.read_data_file('numbers_binomial.txt')
b2.plot_bar()
b2.plot_bar_pdf()
b3 = b1 + b2
b3
