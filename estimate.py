import math
import unittest
from random import random
        

class TestWallis(unittest.TestCase):
    def wallis(iterationsCount: int):
        answer=2
        for n in range(1,iterationsCount+1):
            answer=(answer*4*n*n)/(4*n*n-1)
        return answer

    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def monte_carlo(iterationsCount: int):
    count=0
    for n in range(1,iterationsCount+1):
        x=random()
        y=random()
        distance=x*x+y*y
        if distance <=1.000000000:
            count=count+1
    answer=4*count/iterationsCount
    return answer

    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
