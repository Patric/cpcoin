import time
import json

from coin import Coin

# TODO: add sign to Transaction
class Transaction:
    def __init__(self, sender: str, recipient: str, coin: Coin):
        self.sender = sender
        self.recipient = recipient
        self.coin = coin
        self.timestamp = self.generate_timestamp()
    
    def generate_timestamp(self):
        return time.time()

    # TODO: add checking sender wallet for resources
    # TODO: check sign of transaction
    def is_valid(self):
        return True

    def __str__(self):
        return "Sender: " + self.sender + "\nRecipient: " + self.recipient + "\nAmount: " + str(self.amount)