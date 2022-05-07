import asyncio,time
async def func1():
    for _ in range(10):
        print('Function 1')
        await asyncio.sleep(0.1)
async def func2():
    for _ in range(10):
        print('Function 2')
        await asyncio.sleep(0.1)
async def main():
    task1=asyncio.create_task(func1())
    task2=asyncio.create_task(func2())
    await task1
    await task2

start=time.time()
asyncio.run(main())
end=time.time()
print(f'Took {end-start} seconds')