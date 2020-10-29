#!/usr/bin/env python

from .Distribution import Distribution
class Gaussian(Distribution):

    def __init__(self, mu, sigma):
        Distribution.__init__(self, mu, sigma)

    def read_data_file(self, file_name):
