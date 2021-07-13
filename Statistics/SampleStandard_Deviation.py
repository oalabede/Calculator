import numpy
from Get_sample import getSample


def sample_mean(data, sample_size):
    total = 0
    sample = getSample(data, sample_size)
    res = numpy.std(data)
    return res
