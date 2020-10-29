#!/usr/bin/env python

import math


class Distribution:

    stdev: float
    mean: float
    data: list

    def __init__(self, mu, sigma):
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def read_data_file(self, file_name, sample=True):
        data_list = []
        with open(file_name, 'r') as data_file:
            data = data_file.readlines()
            for line in data:
                data_list.append(int(line))
            self.data = data_list

        self.calculate_mean()
        self.calculate_stdev(sample)

    def calculate_mean(self):
        avg = sum(self.data) / len(self.data)
        self.mean = avg
        return self.mean

    def calculate_stdev(self, sample):

        n = 0
        if sample:
            n = len(self.data)
        else:
            n = len(self.data) - 1
        sum = 0
        for x in self.data:
            sum += (x - self.mean) * (x - self.mean)

        self.stdev = math.sqrt(sum / n)
        return self.stdev
