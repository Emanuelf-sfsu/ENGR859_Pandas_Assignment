from Parser import Parser
from Dataset import Dataset

class GDP_Object(Dataset):
    def __init__(self,path):
        self.country, self.value= Parser(path).GDP_parse()
        super().__init__(self.country,self.value)

    def reverse(self):
        """
        Override function
        Reverse the order of the data pairs
        Example:
        >> print(get_all())
        >> [("Australia",1.1),("Austria",1.0),("Belgium",2.0)]
        >> reverse()
        >> print(get_all())
        >> [("Belgium",2.0),("Austria",1.0),("Australia",1.1)]

        Hint: You can use the list.reverse method to reverse the order of a list.
        """
        # Write your code below
        