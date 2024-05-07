import time
import asyncio
import requests


async def function1():
    URL = "https://images.pexels.com/photos/842711/pexels-photo-842711.jpeg"
    response = requests.get(URL)
    open("download1.jpeg","wb".write(response.content))
    # time.sleep(3)
    await asyncio.sleep(3)
    print("func1")

async def function2():
    URL = "https://images.pexels.com/photos/842711/pexels-photo-842711.jpeg"
    response = requests.get(URL)
    open("download2.jpeg","wb".write(response.content))
    print("func2")

async def function3():
    URL = "https://images.pexels.com/photos/842711/pexels-photo-842711.jpeg"
    response = requests.get(URL)
    open("download3.jpeg","wb".write(response.content))
    print("func3")

async def main():
    # L = await asyncio.gather(
    #     function1(),
    #     function2(),
    #     function3(),
    #  )
    # print (L)

#  task = asyncio.create_task(function1())
 await function1()
 await function3()
 await function2()

asyncio.run(main())