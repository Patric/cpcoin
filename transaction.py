import time
import json
from coin import Coin

class Transaction:
    def __init__(self, sender: str, recipient: str, coin: Coin):
        self.sender = sender
        self.recipient = recipient
        self.coin = coin
        self.timestamp = self.generate_timestamp()
    
    def generate_timestamp(self):
        return time.time()

    def __str__(self):
        return "Sender: " + self.sender + "\nRecipient: " + self.recipient + "\nAmount: " + str(self.amount)