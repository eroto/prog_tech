#!/usr/bin/python3

import asyncio
import aiohttp

class AsyncScrapper():
    def __init__(self,urls):
        self.urls = urls
        print(f"self.urls:{self.urls}")
        pass

    async def fetch(self,session,url):
        async with session.get(url) as response:
            return await response.text
    
    async def scrapper_title(self, session, url):
        try:
            async with session.get(url) as resp:
                print(f"resp.status: {resp.status}")
                print(await resp.text())
        except Exception as e:
            print(f"Error, no response reseived {url}:{e}")
    
    async def run(self):
        async with aiohttp.ClientSession() as session:
            print("Running...")
            task =[self.scrapper_title(session, url) for url in self.urls]
            await asyncio.gather(*task)
