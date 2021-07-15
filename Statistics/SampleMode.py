import numpy
from Get_sample import getSample


def sample_mode(data, sample_size):
    total = 0
    sample = getSample(data, sample_size)
    res = numpy.mode(data)
    return res
