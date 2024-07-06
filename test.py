import asyncio
import time
import random


async def add_to_list(deffered_num, numbers, i):
    print(f"Added {i} to numbers list")
    if i in deffered_num:
        await asyncio.sleep(0)
    numbers.append(i)
    

async def countdown():
    
    numbers = []
    deffered_num = [random.randint(0,100) for i in range(10)]
    print(deffered_num)
    
    await asyncio.gather(*[add_to_list(deffered_num, numbers, i) for i in range(0,101)])
    
    print(numbers)
    
    return numbers

start = time.time()
asyncio.run(countdown())
end = time.time()
print("Time elapsed: ", end - start)