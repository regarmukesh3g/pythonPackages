#!/usr/bin/env python
"""
General distribution Module.
"""
import math


class Distribution:

    def __init__(self, mu, sigma):
        """
        Base distribution class for data.
        Args:
            mu: mean of the data.
            sigma: standard deviation of data.
        """
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def read_data_file(self, file_name):
        """
        Read data from a data file.
        Args:
            file_name: Filename.

        Returns:
            None
        """
        data_list = []
        with open(file_name, 'r') as data_file:
            data = data_file.readlines()
            for line in data:
                data_list.append(int(line))
        data_file.close()
        self.data = data_list

    def calculate_mean(self):
        """
        Calculates mean of the distribution.
        Returns:
            Mean of the data.
        """
        avg = sum(self.data) / len(self.data)
        self.mean = avg
        return self.mean

    def calculate_stdev(self, sample):
        """
        Calculates standard deviation of the distribution.
        Args:
            sample: Whether data is sample or population.

        Returns:
            Standard deviation of the data.
        """
        data_len = 0
        if sample:
            data_len = len(self.data) - 2
        else:
            data_len = len(self.data)
        total = 0
        for x_val in self.data:
            total += (x_val - self.mean) * (x_val - self.mean)
        self.stdev = math.sqrt(total / data_len)
        return self.stdev
