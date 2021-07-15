import numpy
from Get_sample import getSample


def sample_median(data, sample_size):
    total = 0
    sample = getSample(data, sample_size)
    res = numpy.median(data)
    return res
