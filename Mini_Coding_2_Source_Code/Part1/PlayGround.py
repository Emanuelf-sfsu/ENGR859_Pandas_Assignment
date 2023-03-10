from Main import Main
from GDP_Object import GDP_Object
from Lifesat_Object import Lifesat_Object
import os

# Init Object
main = Main()
GDP_path = os.path.join("Data","gdp_per_capita.csv")
life_sat_path = os.path.join("Data","oecd_bli_2015.csv")
GDP = GDP_Object(GDP_path)
life_sat = Lifesat_Object(life_sat_path)
# print GDP merge result
print(GDP.merge(life_sat))
# visualize the dataset
main.visualization()
# training data
main.training()
# visualize 
print(main.data_preparation())

print(main.validation())

print(main.predict([[123456]], "linear regression"))
