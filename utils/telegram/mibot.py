import os

from telegram import Bot
import yaml


class MiBot:
    path = os.path.join('input', 'telegram_key.yml')
    with open(path) as file:
        keys = yaml.load(file, Loader=yaml.FullLoader)

    def __init__(self):
        self.bot = Bot(token=self.keys['API_KEY'])
        self.chat_id = self.keys['CHAT_ID']

    def send_message(self, message):
        self.bot.send_message(text=message, chat_id=self.chat_id)