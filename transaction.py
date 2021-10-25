import time
import json

# TODO: add sign to Transaction
class Transaction:
    def __init__(self, sender: str, recipient: str, amount: float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = self.__generate_timestamp()
    
    def generate_timestamp():
        return time.time()

    # TODO: add checking sender wallet for resources
    # TODO: check sign of transaction
    def is_valid(self):
        if self.amount < 0:
            return False
        return True

    def __str__(self):
        return "Sender: " + self.sender + "\nRecipient: " + self.recipient + "\nAmount: " + str(self.amount)