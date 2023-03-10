from Parser import Parser
from Dataset import Dataset

class Lifesat_Object(Dataset):
    def __init__(self,path):
        self.country,self.value = Parser(path).lifesat_parse()
        super().__init__(self.country,self.value)

