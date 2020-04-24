from bs4 import BeautifulSoup

import requests

HERO_TABLE_INDEXES = [2, 3, 5, 6, 7, 10, 11]


class Heroes:

    def __init__(self):
        self.base_url = "https://overwatch.fandom.com/wiki/Heroes"
        self.filtered_raw_data = None
        self.extract_data()

    def _page_data(self):
        try:
            raw_page_data = requests.get(self.base_url).content
            soup = BeautifulSoup(raw_page_data, "html.parser")
        except Exception as e:
            print("Error while obtaining hero information.\nError:\t" + str(e))

        return soup

    def _hero_data(self):
        hero_names = list()
        for t in self.filtered_raw_data:
            for h in t.text.split("\n"):
                if h != "":
                    hero_names.append(h)
        hero_names.sort()
        self.hero_names = hero_names

    def _hero_pages(self):
        hero_pages = {}
        for h in self.hero_names:
            hero_url = self.base_url.replace("Heroes", h).replace(" ", "_")
            hero_pages.update({h: hero_url})
        self.hero_pages = hero_pages

    def extract_data(self):
        raw_data = self._page_data().find_all("table")

        filtered_data = list()
        for i in range(len(raw_data)):
            if i in HERO_TABLE_INDEXES:
                filtered_data.append(raw_data[i])
        self.filtered_raw_data = filtered_data

        self._hero_data()
        self._hero_pages()

