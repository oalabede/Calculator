import unittest
from Statistics.Statistics import Statistics
from numpy.random import randint
from numpy.random import seed
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 10, 20)
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        test_data = CsvReader('Test/Mean.csv').data
        for row in test_data:
            array = [row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6']]
            array = [float(a) for a in array]
            mean = self.statistics.mean(array)
            self.assertEqual(mean, float(row['Result']))

    def test_median_calculator(self):
        test_data = CsvReader('Test/Median.csv').data
        for row in test_data:
            array = [row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6'], row['Value 7']]
            array = [float(a) for a in array]
            median = self.statistics.median(array)
            self.assertEqual(median, float(row['Result']))

    def test_mode_calculator(self):
        test_data = CsvReader('Test/Mode.csv').data
        for row in test_data:
            array = [row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6']]
            array = [float(a) for a in array]
            mode = self.statistics.mode(array)
            self.assertEqual(mode, float(row['Result']))

    def test_variance_calculator(self):
        test_data = CsvReader('Test/Variance.csv').data
        for row in test_data:
            array = [row['Value 1'], row['Value 2'], row['Value 3'], row['Value 4'], row['Value 5'], row['Value 6']]
            array = [float(a) for a in array]
            variance = self.statistics.variance(array)
            self.assertEqual(variance, float(row['Result']))

    def test_std_calculator(self):
        test_data = CsvReader('Test/Standard_Deviation.csv').data
        for row in test_data:
            array = [row['Value 1']]
            array = [float(a) for a in array]
            std = self.statistics.std(array)
            self.assertEqual(std, float(row['Result']))


if __name__ == '__main__':
    unittest.main()
