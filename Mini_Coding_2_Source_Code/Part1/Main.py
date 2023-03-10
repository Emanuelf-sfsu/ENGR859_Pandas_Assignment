# Code example
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import sklearn.linear_model
from GDP_Object import GDP_Object
from Lifesat_Object import Lifesat_Object
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures


class Main():
    def __init__(self):

        # Hyper parameters setting
        self.test_size = 0.33
        self.random_seed = 42
        self.poly_degree = 2
        self.GDP_path = os.path.join("Data","gdp_per_capita.csv")
        self.life_sat_path = os.path.join("Data","oecd_bli_2015.csv")
        self.training_data,\
        self.test_data,\
        self.training_label,\
        self.test_label = self.data_preparation()

        self.poly_training_data,\
        self.poly_test_data,\
        self.poly_training_label,\
        self.poly_test_label = self.data_preparation(polynomial=True)

        self.raw_training_data,self.raw_training_label = self.data_preparation(raw_data=True)
        self.linear_regression_model = sklearn.linear_model.LinearRegression()
        self.polynomial_model = sklearn.linear_model.LinearRegression()

    # Prepare the data
    def data_preparation(self, polynomial = False,raw_data = False):
        GDP = GDP_Object(self.GDP_path)
        life_sat = Lifesat_Object(self.life_sat_path)

        # merge the GDP and life sat dataset
        training_data,training_label = GDP.merge(life_sat)

        # convert training_data and training_label to numpy array
        # Write your code below
        training_data = np.array([training_data])
        training_label = np.array([training_label])

        # training_data and training_label are 1D numpy array, 
        # you will need to use numpy.expand_dims to expand them to 2D numpy array
        # because linear regression model only accept 2D numpy array as input
        # Write your code below
        training_data = np.expand_dims(training_data, axis=(2,0))
        training_label = np.expand_dims(training_label, axis=(2,0))


        # Generated polynomial features from the training_data
        # Complete the code below
        poly_features = training_data

        if raw_data:
            return training_data,training_label
        # Split training and validating dataset
        if polynomial:
            return train_test_split(poly_features, training_label, test_size=self.test_size, random_state=self.random_seed)
        else:
            return train_test_split(training_data, training_label, test_size=self.test_size, random_state=self.random_seed)

    def visualization(self) -> None:
        # Visualize the data
        plt.scatter(self.raw_training_data,self.raw_training_label)
        plt.show()

    def training(self) -> None:
        # train linear regression model
        #Write your code below

        # train linear regression model with polynomial features
        #Write your code below
        return

    def validation(self) -> tuple[float,float]:
        # Test linear regression model
        #Write your code below

        #Test linear regression model with polynomial features
        #Write your code below

        linear_regression_rmse = np.sqrt(mean_squared_error(self.test_label, linear_regression_predict))
        polynomial_rmse = np.sqrt(mean_squared_error(self.poly_test_label, polynomial_predict))

        return linear_regression_rmse,polynomial_rmse

    def predict(self,data:float,model:str) -> float:
        if model == "linear regression":
            model = self.linear_regression_model
        elif model == "polynomial":
            model = self.polynomial_model
        return model.predict(data)