import random
import math
import pandas as pd

life_sat = pd.read_csv("./Data/oecd_bli_2015.csv", usecols=['Country','Value'])
# life_sat_country = life_sat.pop('Country')
# pd.read_csv("student_scores2.csv", usecols = ['IQ','Scores'])
# life_sat = pd.read_csv("oecd_bli_2015.csv", usecols=['Value'])

# print(life_sat_country.values)
print(life_sat.values)
