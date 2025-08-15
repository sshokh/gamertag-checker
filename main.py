from requests.exceptions import RequestException
import requests
import random
import string
import time
import os

from logger import logger

class GamertagChecker:
    def generate_gamertag(self, length):
        letters = string.ascii_lowercase
        allowed = string.ascii_lowercase + string.digits
        return random.choice(letters) + ''.join(random.choice(allowed) for _ in range(length - 1))


    def is_available(self, gamertag):
        response = requests.get(f"https://xboxgamertag.com/search/{gamertag}")
        if response.status_code == 404:
            logger.success(f"Found an available gamertag: {gamertag}")
            return True

        logger.debug(f"Gamertag {gamertag} is not available.")
        return False

    def save(self, gamertag):
        with open("availables.txt", "a") as file:
            file.write(f"{gamertag}\n")


if __name__ == "__main__":
    os.system("cls" or "clear")
    client = GamertagChecker()

    length = int(logger.input("Enter the length of gamertags: "))
    if length < 3 or length > 15:
        raise ValueError(
            "Gamertag length must be at least 3 characters and must not exceed 15 characters."
        )


    while True:
        try:
            gamertag = client.generate_gamertag(length)
            
            if client.is_available(gamertag):
                client.save(gamertag)
            time.sleep(1)  # Sleep to avoid hitting the server too hard
        except RequestException as e:
            logger.error(f"An error occurred: {e}")
            time.sleep(5)
