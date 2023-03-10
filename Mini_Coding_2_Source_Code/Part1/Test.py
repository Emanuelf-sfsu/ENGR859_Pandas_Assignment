from Main import Main
import unittest
import os
"""
Sample Test, To get full credit of this assignment, there should be no error occur.
""" 
class Grader(unittest.TestCase):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Initialize Object
        """
        self.Main = Main()

    def test_validation(self):
        self.Main.training()
        linear_regression,poly_regression = self.Main.validation()
        self.assertGreater(linear_regression, poly_regression)
            
if __name__ == '__main__':
    unittest.main()