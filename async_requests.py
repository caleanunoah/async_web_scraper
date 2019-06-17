import aiohttp
import asyncio
import time


# Task - async function that we are defining below
async def fetch_page(url):
    start = time.time()
    # Note that instead of : __enter__ and __exit__
    # The methods are __aenter__ and __aexit__
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'Page took {time.time() - start}')
            return response.status


# Run the task (event) loop
loop = asyncio.get_event_loop()
tasks = [fetch_page('http://google.com') for i in range(50)]
start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f'All tasks took {time.time()-start}')
