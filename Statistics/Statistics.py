from statistics import mean, median, mode, variance

import numpy
from numpy import std
from Calculator import Calculator


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def std(self, data):
        self.result = numpy.std(data)
        return self.result
