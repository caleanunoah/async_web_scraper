import aiohttp
import asyncio
import async_timeout
import time


# Task - async function that we are defining below
async def fetch_page(session, url):
    start = time.time()
    async with async_timeout.timeout(10):
    # Note that instead of : __enter__ and __exit__
    # The methods are __aenter__ and __aexit__
        async with session.get(url) as response:
            print(f"Page took {time.time() - start}")
            return await response.status


# Passing in event loop as an arg for safeguarding.
# Ensures that new loop isn't created every time
async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        # Each task in grouped_tasks runs synchronously
        grouped_tasks = asyncio.gather(*tasks)  # runs until tasks are DONE.  All pages gathered
        return await grouped_tasks  # suspects after collecting all pages


if __name__ == "__main__":
    # Run the task (event) loop
    loop = asyncio.get_event_loop()

    urls = ['http://google.com' for i in range(50)]
    start = time.time()
    loop.run_until_complete(get_multiple_pages(loop, *urls))
    print(f'All tasks took {time.time()-start}')

