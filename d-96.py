# async IO
import time
import asyncio
import requests

async def func_1():
    url = 'https://www.facebook.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('facebook.ico', 'wb').write(r.content)
    await func_2()
    await asyncio.sleep(1)
    print("hey")


async def func_2():
    print("hye")
asyncio.run(func_1())