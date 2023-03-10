from Parser import Parser
from Dataset import Dataset
import pandas as pd
class GDP_Object(Dataset):
    def __init__(self,path):
        self.country, self.value= Parser(path).GDP_parse()
        super().__init__(self.country,self.value)


        """
        Merge the data
        This function returns the GDP and life satisfaction data for countries
        Example:
        The GDP dataset should looks like such
        Data                    Label
        Afghanistan             599.994
        Albania                 3995.383
        Algeria                 4318.135
        .......
        Austria                 43724.031
        Belgium                 40106.632

        The LifeSat dataset should looks like such
        Data                   Label
        Australia              7.3
        Austria                6.9
        Belgium                6.9
        ......


        What you need to do is
        you need to create two separate lists for the GDP dataset label 
        and LifeSat dataset label. 
        However, note that the GDP dataset contains 190 data 
        while the LifeSat dataset only has 37 data. 
        This indicates that some countries do not have life satisfaction data. 
        Therefore, you need to filter out the countries that don't have life satisfaction data and 
        keep only the countries that have both GDP and life satisfaction data.

        Note that the first element of the tuple should be the GDP dataset label list, 
        while the second element should be the life satisfaction dataset label list.


        >> print(GDP_Object.merge(Lifesat_Object))
        >> (
            [40106.632,.....],[6.9,.....]
        )


        """ 
    def merge(self,data:Dataset) -> tuple[list,list]:
        # write your code below