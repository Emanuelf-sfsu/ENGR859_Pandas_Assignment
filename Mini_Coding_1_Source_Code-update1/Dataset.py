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

        

    def get_item(self,index:int) -> tuple[str,float]:
        """
        "Return the pair of data and label corresponding to a given index."
        Example:
        Your data should look like ["Australia","Austria","Belgium"]
        Your label should look like [1.1,1.0,2.0]
        >> print(get_item(0))
        >> ("Australia",1.1)
        >> print(get_item(1))
        >> ("Austria",1.0)
        >> print(get_item(2))
        >> ("Belgium",2.0)

        Hint:
        In Python, you can return multiple values by using a comma-separated list of values, 
        such as 
        return var1, var2. 
        Python will automatically wrap these values in a tuple and return the tuple as a single object.
        """
        # Write your code below
        

        

    def get_max(self) -> tuple[str,float]:
        """
        Return the pair of data and the corresponding label with the highest value in the label list.
        Example:
        Your data should look like ["Australia","Austria","Belgium".....]
        Your label should look like [1.1,1.0,2.0.....]
        >> print(get_max)
        >> ("Belgium",2.0)

        Hint:
        To find the maximum value in a list, you can use the max() function. 
        To find the index of a specific element in a list, you can use the list.index() function.
        """
        # Write your code below
        

        
    def get_min(self) -> tuple[str,float]:
        """
        Return the pair of data and the corresponding label with the smallest value in the label list.
        Example:
        Your data should look like ["Australia","Austria","Belgium".....]
        Your label should look like [1.1,1.0,2.0.....]
        >> print(get_min())
        >> ("Austria",1.0)

        Hint:
        To find the maximum value in a list, you can use the min() function. 
        """
        # Write your code below
        

        
    def get_length(self) -> int:
        """
        Return the length of your data and 
        ensure that both the length of the data and the length of the label are equal.
        Example:
        Your data should look like ["Australia","Austria","Belgium"]
        Your label should look like [1.1,1.0,2.0]
        >> print(get_length())
        >> 3
        """
        # Write your code below

        return len(self.label)

        
    def get_all(self) -> list[tuple[str,float]]:
        """
        Return all pairs of your data and label.
        Example:
        Your data should look like ["Australia","Austria","Belgium"]
        Your label should look like [1.1,1.0,2.0]
        >> print(get_all())
        >> [("Australia",1.1),("Austria",1.0),("Belgium",2.0)]

        Hint:
        You can append data to a list in the following manner:
        myList = []
        for i in range(5):
            myList.append(i)
        """
        # Write your code below

        return list(self)
    
        
    def shuffle(self):
        """
        Shuffle the data
        Example:
        Your data should look like ["Australia","Austria","Belgium"]
        Your label should look like [1.1,1.0,2.0]

        >> print(get_all())
        >> [("Australia",1.1),("Austria",1.0),("Belgium",2.0)]
        >> shuffle()
        >> print(get_all())
        >> [("Austria",1.0),("Belgium",2.0),("Australia",1.1)]

        You can use the random.Random.shuffle(list) method to shuffle the data list. 
        You also need shuffle the label list so that the corresponding pair of data and label remains the same.
        """ 
        # Write your code below
        return  random.shuffle(self)

    def reverse(self):
        print("Please Override this function in the GDP Object")

        
    def train_val_split(self,radio:float,data_type:str) -> tuple[list,list]:
        """
        Split dataset to the training data and validation data
        The first argument is the radio value. 
        To determine the split point, you need to multiply the length of your data by the radio. 
        The training dataset consists of the data from index 0 to the split point. 
        The validation dataset consists of the data from the split point to the end of the data.

        If the split point less than 0, you should round it to 1
        If the split point is decimal, you should rounds a number down to the nearest integer.

        The second argument specifies the return data type, 
        either the training dataset or the validation dataset.
        Example:
        Your data should look like ["Australia","Austria","Belgium","Canada"]
        Your label should look like [1.1,1.0,2.0,0.2]
        >> print(train_val_split(0.5,train))
        >> (["Australia","Austria"],[1.1,1.0])
        >> print(train_val_split(0.5,val))
        >> (["Belgium","Canada"],[2.0,0.2])
        >> print(train_val_split(0.9,"val")
        >> (['Canada'], [0.2])
        >> print(train_val_split(0.9,"train")
        >> (['Australia', 'Austria', 'Belgium'], [1.1, 1.0, 2.0])
        """
        split_point = radio*self.get_length()
        data = None
        label = None
        if split_point < 1:
            split_point = math.ceil(split_point)
        else:
            split_point = math.floor(split_point)
        if (data_type == "train"):
            data = self.data[:split_point]
            label = self.label[:split_point]
            
        elif (data_type == "val"):
            data = self.data[split_point:self.get_length()]
            label = self.label[split_point:self.get_length()]
        return data,label
    