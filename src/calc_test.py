import unittest
import calc

class CalcTest(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(calc.add(1,1), 2)
        self.assertEqual(calc.add(100,-100), 0)
        self.assertEqual(calc.add(1122334455,5544332211), 6666666666)
        self.assertEqual(calc.add(5,-100), -95)

    def testSub(self):
        self.assertEqual(calc.sub(1,1), 0)
        self.assertEqual(calc.sub(100,-100), 200)
        self.assertEqual(calc.sub(12345,1234), 11111)
        self.assertEqual(calc.sub(-5,-100), 95)
        
    def testMul(self):
        self.assertEqual(calc.mul(1,1), 1)
        self.assertEqual(calc.mul(20,50), 1000)
        self.assertEqual(calc.mul(12345,1234), 15233730)
        self.assertEqual(calc.mul(-5,-100), 500)

    def testDiv(self):
        self.assertEqual(calc.div(1,1), 1)
        self.assertEqual(calc.div(10,5), 2)
        self.assertEqual(calc.div(1200,6), 200)
        self.assertEqual(calc.div(-1000,5), -200)
        with self.assertRaises(ValueError):
            calc.div(12345, 0)

if __name__ == '__main__':
    unittest.main()
