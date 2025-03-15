#!/usr/bin/python3

import asyncio
import aiohttp
from bs4 import BeautifulSoup


class AsyncScrapper:
    def __init__(self, urls):
        self.urls = urls
        pass

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text

    async def scrape_tittle(self, session, url):
        try:
            html = await self.fetch(session, url)
            soup = BeautifulSoup(html,'html.parser')
            title = soup.find('h1').get_text()
        except Exception as e:
            print(f"Error, scrapping:{url}: Code --> {e}")

    async def run(self):
        async with aiohttp.ClientSession( ) as session:
            tasks = [self.scrape_tittle(session, url) for url in self.urls]
            asyncio.gather(*tasks)
