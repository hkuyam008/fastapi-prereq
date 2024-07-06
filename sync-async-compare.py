import asyncio
import time

numbers_range = 10000

async def add_to_list(numbers, i):
    print(f"Added {i} to numbers list")
    numbers.append(i)

async def countdown():
    
    numbers = []
    
    await asyncio.gather(*[add_to_list(numbers, i) for i in range(0,numbers_range)])
    
loop = asyncio.get_event_loop()
start = time.time()
loop.run_until_complete(countdown())
end = time.time()
print("Time elapsed async: ", end - start)


def countdown_sync():
    numbers = []
    for i in range(0,numbers_range):
        print(f"Added {i} to numbers list")
        numbers.append(i)
        
# start = time.time()
# countdown_sync()
# end = time.time()
# print("Time elapsed sync: ", end - start)
