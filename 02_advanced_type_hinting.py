#from typing import List, Tuple, Dict, Union
import pdb


nums: list[int] = [12,23,4,5]
sample_tuple: tuple[int,int,int] = (2,3,4)
prices: dict[str,int] = {'item1': 23, 'item2': 21}

def num_sum(nums: list[int]):
    return sum(nums)
    
print(num_sum([1,2,3]))

################################################################################

x: list[int | float] = [1,2,3,4,5,6.7]

################################################################################

Image = list[list[int]]

def flatten_image(pic: Image) -> list:
    
    flat_list = []
    
    for sublist in pic:
        for item in sublist:
            flat_list.append(item)

    return flat_list

image = [[1,2,3],[4,5,6]]

################################################################################

class Job:
    
    def __init__(self,title: str,description: str|None) -> None:
        self.title = title
        self.description = description
        
    def __repr__(self):
        return self.title
    
job1 = Job(title="Team Lead", description="team lead")
job2 = Job(title="Senior Manager", description="senior manager")

jobs: list[Job]=[job1,job2]

################################################################################
from typing import Callable

def smart_divide(func: Callable[[int,int],float|None]):
    
    def inner(a,b):
        if b == 0:
            print("Whoops! Division by 0")
            return None
        return func(a,b)
    
    return inner

@smart_divide
def divide(a: int,b: int) -> None:
    print(a/b)
    

divide(9,'a')