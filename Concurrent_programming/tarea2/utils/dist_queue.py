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
    
    async def scrape_tittle(self, session, url):
        try:
            html = await self.fetch(session,url)
            print(html)
        except Exception as e:
            print(f"Error, no response reseived {ur}:{e}")
    
    async def run(self):
        async with aiohtpp.ClientSession() as session:
            task =[self.scrapper.title(session, url) for url in self.urls]
            await asyncio.gather(*task)
