import unittest
from numpy.random import seed
from numpy.random import randint
from Statistics.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 10, 20)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 20)

    def test_median_calculator(self):
        median = self.statistics.median(self.testData)
        self.assertEqual(median, 19)

    def test_mode_calculator(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, 5)

    def test_variance_calculator(self):
        variance = self.statistics.variance(self.testData)
        self.assertEqual(variance, 49.2)

    def test_std_calculator(self):
        std = self.statistics.std(self.testData)
        self.assertEqual(std, 7.014)


if __name__ == '__main__':
    unittest.main()
