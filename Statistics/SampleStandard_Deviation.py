import numpy
from Get_sample import getSample


def sample_std(data, sample):
    total = 0
    sample = getSample(data, sample)
    res = numpy.std(data)
    return res
