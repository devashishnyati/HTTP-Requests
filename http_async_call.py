import asyncio
import requests

async def main():
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None, 
            requests.get, 
            'https://webhook.site/9713cf49-d43c-477f-9a22-ccd1a5458e81'
        )
        for i in range(3)
    ]

    for response in await asyncio.gather(*futures):
        print('Response ID: {} \tResponse Time: {}'.format(response.headers['X-Request-Id'], response.headers['date']))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())