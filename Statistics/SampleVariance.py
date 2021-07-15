import numpy
from Get_sample import getSample


def sample_variance(data, sample_size):
    total = 0
    sample = getSample(data, sample_size)
    res = numpy.variance(data)
    return res
