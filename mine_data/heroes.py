import json
import requests


class Heroes:

    def __init__(self):
        self.heroes_brute_data = None

    def __heroes_brute_data(self):
        endpoint = "https://best-overwatch-api.herokuapp.com/heroes"
        try:
            heroes_data = json.loads(requests.get(endpoint).content.decode("utf-8"))
            self.heroes_brute_data = heroes_data
        except Exception as e:
            print("Could not get hero data from \"" + endpoint + "\"\nError: " + str(e))

    def heroes(self):
        self.__heroes_brute_data()

        return self.heroes_brute_data
