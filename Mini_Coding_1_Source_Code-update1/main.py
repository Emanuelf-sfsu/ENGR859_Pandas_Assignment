import random
import math
import pandas as pd

# life_sat = pd.read_csv("./Data/oecd_bli_2015.csv", usecols=['Country','Value'])
# life_sat_country = life_sat.pop('Country')
# pd.read_csv("student_scores2.csv", usecols = ['IQ','Scores'])
# life_sat = pd.read_csv("oecd_bli_2015.csv", usecols=['Value'])

# print(life_sat_country.values)
# print(life_sat.values,life_sat.loc)
# input list
lst = [10, 11, 12, 13, 14, 15]
# the above input can also be given as
# lst=list(map(int,input().split()))
l = []  # empty list
# iterate to reverse the list
for i in lst:
    l.insert(0, i)
# printing result
print(l)