from bs4 import BeautifulSoup

import re
import requests


class Heroes:

    def __init__(self):
        self.base_url = "https://overwatch.guide/"
        self._raw_hero_data = self._hero_data()
        self.heroes = self.available_heroes()

    def _page_data(self):
        try:
            raw_page_data = requests.get(self.base_url).content
            soup = BeautifulSoup(raw_page_data, "html.parser")
        except Exception as e:
            print("Error while obtaining hero information.\nError:\t" + str(e))

        return soup

    def _hero_data(self):

        return self._page_data().find_all(class_="sub-menu")[0]

    def hero_pages(self):
        soup = self._raw_hero_data()
        hero_pages = {}

        for li in soup.find_all("li"):
            li.get("href")
            if li.text != "ALL HEROES":
                hero_pages.update(
                    {li.text: re.search("https://.*(?=\")", str(li)).group()}
                )

        return hero_pages

    def available_heroes(self):

        return list(self.hero_pages().keys())
