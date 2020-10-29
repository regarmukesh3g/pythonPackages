#!/usr/bin/env python
"""
A Gaussian class for Gaussian distribution data.
"""
import math
import matplotlib.pyplot as plt
from .general_distribution import Distribution


class Gaussian(Distribution):
    """
    A Class for Guassian data.
    """

    def __init__(self, mu, sigma):
        Distribution.__init__(self, mu, sigma)

    def read_data_file(self, file_name, sample=True):
        """
        Read data from a file
        Args:
            file_name: filename from which data will be parsed.
            sample: Whether it is a sample data?
        Returns:
            None
        """
        Distribution.read_data_file(file_name, sample)
        self.calculate_mean()
        self.calculate_stdev(sample)

    def pdf(self, x_val):
        """
        Calculates distribution function for a given point.
        Args:
            x_val: The point where distribution function is to be calculated.

        Returns:
            Probability distribution at x.
        """
        coeff = 1 / math.sqrt(2 * math.pi * self.stdev * self.stdev)
        power = -(((x_val - self.mean) / self.stdev) ** 2)
        return coeff * math.exp(power)

    def plot_hist(self):
        """
        Plot histogram of the data.
        """
        plt.hist(self.data,density=True)
        plt.title('Histogram of data')
        plt.ylabel('Density')
        plt.show()

    def plot_histogram_pdf(self, n_spaces=20):
        """
        Plots probability distribution function histogram of the given data.
        Args:
            n_spaces: no of spaces for plot.
        Returns
            None
        """
        min_data = min(self.data)
        max_data = max(self.data)
        x_data = range(min_data, max_data, step=(max_data - min_data) / n_spaces)
        y_data = [self.pdf(x) for x in x_data]
        plt.figure()
        plt.subplot(1, 2, 1)
        plt.title('Histogram of data')
        plt.ylabel('Density')
        plt.hist(self.data, density=True)
        plt.subplot(1, 2, 2)
        plt.plot(x_data, y_data)
        plt.title('Normal distribution for sample mean and standard deviation')
        plt.ylabel('Density')
        plt.show()


    def __add__(self, other):
        result = Gaussian(0, 0)
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
        return result
