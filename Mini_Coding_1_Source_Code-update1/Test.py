import pandas as pd
from GDP_Object import GDP_Object
from Lifesat_Object import Lifesat_Object
import unittest
import os
"""
Sample Test, To get full credit of this assignment, there should be no error occur.
""" 
class Grader(unittest.TestCase):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        path for the dataset
        """
        self.GDP_path = os.path.join("Data","gdp_per_capita.csv")
        self.life_sat_path = os.path.join("Data","oecd_bli_2015.csv")

        """
        Initialize Object
        """
        self.GDP = GDP_Object(self.GDP_path)
        self.life_sat = Lifesat_Object(self.life_sat_path)

    def test_parser(self):
        self.assertNotEqual(self.GDP.data, None)
        self.assertNotEqual(self.life_sat.data, None)

    def test_getMax(self):
        self.assertEqual(self.GDP.get_max(),('Luxembourg', 101994.093))
        self.assertEqual(self.life_sat.get_max(),('United States', 145769.0))
    def test_getMin(self):
        self.assertEqual(self.GDP.get_min(),('South Sudan', 220.86))
        self.assertEqual(self.life_sat.get_min(),('Netherlands', 0.0))
    def test_get_length(self):
        self.assertEqual(self.GDP.get_length(),190)
        self.assertEqual(self.life_sat.get_length(),3292)
    def test_get_item(self):
        self.assertEqual(self.GDP.get_item(20),('Bosnia and Herzegovina', 4088.212))
        self.assertEqual(self.life_sat.get_item(20),('Norway', 0.3))
    
        
    def test_reverse(self):
        """
        Test reverse function
        Compare the first item and the last item before reverse and after reverse
        """
        temp_GDP = GDP_Object(self.GDP_path)
        first_item = temp_GDP.get_item(0)
        last_item = temp_GDP.get_item(-1)
        temp_GDP.reverse()
        self.assertEqual(temp_GDP.get_item(-1), first_item)
        self.assertEqual(temp_GDP.get_item(0), last_item)
        
    def test_get_all(self):
        """
        Test get_all function
        Compare the length of the output from the get_all function with the parsed data and check if they match. 
        
        Compare the 20th item in the output of the get_all function with the output of get_item(20) 
        and check if they match.
        """
        self.assertEqual(len(self.GDP.get_all()), len(self.GDP.data)) 
        self.assertEqual(len(self.GDP.get_all()), len(self.GDP.label)) 

        self.assertEqual(len(self.life_sat.get_all()), len(self.life_sat.data)) 
        self.assertEqual(len(self.life_sat.get_all()), len(self.life_sat.label)) 

        self.assertEqual(self.GDP.get_all()[20], self.GDP.get_item(20)) 
        self.assertEqual(self.life_sat.get_all()[20], self.life_sat.get_item(20))

    def test_shuffle(self):
        """
        Test shuffle function
        Compare the first item and the last item before reverse and after reverse.

        Check if shuffle both data and label

        """
        temp_GDP = GDP_Object(self.GDP_path)
        temp_lifesat = Lifesat_Object(self.life_sat_path)
        first_item = temp_GDP.get_item(0)
        last_item = temp_GDP.get_item(-1)
        test_item_data_pair = temp_lifesat.get_item(20)
        temp_GDP.shuffle()
        self.assertNotEqual(temp_GDP.get_item(-1), first_item)
        self.assertNotEqual(temp_GDP.get_item(0), last_item)
        self.assertTrue(test_item_data_pair in temp_lifesat.get_all())



        first_item = temp_lifesat.get_item(0)
        last_item = temp_lifesat.get_item(-1)
        test_item_data_pair = temp_lifesat.get_item(20)
        temp_lifesat.shuffle()
        self.assertNotEqual(temp_lifesat.get_item(-1), first_item)
        self.assertNotEqual(temp_lifesat.get_item(0), last_item)
        self.assertTrue(test_item_data_pair in temp_lifesat.get_all())
            
if __name__ == '__main__':
    unittest.main()