import pandas as pd
"""
This class is for parse the raw data to [(country1,value1),(country2,value2),(country3,value3)]
"""
class Parser():
    def __init__(self,path):
        self.path = path

        
    def lifesat_parse(self) -> tuple[list,list]:
        """
        Please refer to Pandas Documentation and handson-ml2 to help you
        handson-ml2 github: https://github.com/ageron/handson-ml2/tree/master/datasets/lifesat

        This function for parse lifesat dataset to the following format
        [('Australia', 1.1), ('Austria', 1.0), ('Belgium', 2.0), ('Canada', 0.2), ('Czech Republic', 0.9), ('Denmark', 0.9).......]
        Hint:
        First, use pandas to read the csv file. 
        Second, extract the data from the 'Country' and 'value' columns. 
        Finally, convert the data to a list and return both lists.
        """
        # keep
        life_sat = pd.read_csv(self.path, thousands=',')
        life_sat = life_sat[life_sat["INEQUALITY"]=="TOT"]
        life_sat = life_sat.pivot(index="Country", columns="Indicator", values="Value")
        life_sat_df = pd.DataFrame(data=life_sat)
        country = list(life_sat_df.index)
        value = list(life_sat_df.iloc[:]["Life satisfaction"])
        return country, value
        
    def GDP_parse(self) -> tuple[list,list]:
        """
        Please refer to Pandas Documentation and handson-ml2 github to help you
        handson-ml2 github: https://github.com/ageron/handson-ml2/tree/master/datasets/lifesat

        This function for parse GDP dataset to the following format
        [('Afghanistan', 599.994),('Zimbabwe', 1064.35),('Yemen', 1302.94).......]

        Hint:
        First, use pandas to read the csv file. 
        Second, rename the 2015 column to 'GDP per capita.' 
        Third, extract the data from the 'Country' and 'GDP per capita' columns. 
        Finally, convert the data to a list and return both lists.
        """
        # Remove
        gdp_per_capita = pd.read_csv(self.path, thousands=',', delimiter='\t',encoding='latin1', na_values="n/a")
        gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
        gdp_per_capita_df = pd.DataFrame(data=gdp_per_capita)
        country = list(gdp_per_capita_df.loc[:,"Country"])
        GDP = list(gdp_per_capita_df.loc[:,"GDP per capita"])
        return country, GDP