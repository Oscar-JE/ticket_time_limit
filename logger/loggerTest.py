import unittest
import logger

class TestLogger(unittest.TestCase):

    def test_singelLogger(self):
        values = [2,2,2,2]
        myLogger = logger.SingleLogger()
        for value in values:
            myLogger.update(value)
        self.assertEqual(myLogger.getMean(),2)

    def test_distLogger(self):
        values1 = [1,1]
        values2 = [1,2]
        myLogger = logger.DistLogger(2)
        myLogger.update(values1)
        myLogger.update(values2)
        self.assertEqual(myLogger.getDistribution(), [1,1.5])

if __name__ == "__main__":
    unittest.main()
