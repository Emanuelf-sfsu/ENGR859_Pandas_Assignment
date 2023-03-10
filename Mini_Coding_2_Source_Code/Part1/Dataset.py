import random
import math
import pandas as pd
class Dataset():
    def __init__(self,data,label):
        """
        data and label are list
        >> print(self.data)
        >> ["Australia","Austria","Belgium".....]
        >> print(self.label)
        >> [1.1,1.0,2.0.....]
        """
        self.data = data
        self.label = label
    
    
        
    