price = [1,2,3,9,8]

price_iter = price.__iter__()

print(price_iter.__next__())
print(price_iter.__next__())
print(price_iter.__next__())

while True:
    try:
        print(price_iter.__next__())
    except StopIteration:
        break;
    
################################################################################

class InfiniteNaturalNumbers:
    
    def __init__(self) -> None:
        self.num = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        num = self.num
        self.num+=1
        return num
    
values = iter(InfiniteNaturalNumbers()) 
print(next(values))
print(next(values))


################################################################################


def even_numbers():
    # generate  the even_numbers < 20
    for i in range(20):
        if i%2 == 0:
            yield i
        else:
            continue
        
even_nos = even_numbers()

print(even_nos.__next__())
print(even_nos.__next__())
print(even_nos.__next__())