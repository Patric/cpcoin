import binascii
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from coin import Coin
from utils import generate_transaction_data, transaction_to_bytes

class Transaction:
    def __init__(self, sender, recipient: str, coin: Coin, signature: str = ""):
        # Transaction is signed, but still need sender?
        self.sender = sender
        self.recipient = recipient
        self.coin = coin
        self.signature = signature

    def generate_data(self) -> bytes:
        transaction_data = generate_transaction_data(self.sender.public_key, self.recipient, self.coin.coin_id)
        return transaction_to_bytes(transaction_data)

    # TODO: sign in User -> there should be only access to private key
    def sign(self):
        transaction_data = self.generate_data()
        hash_object = SHA256.new(transaction_data)
        signature = pkcs1_15.new(self.sender.__private_key).sign(hash_object)
        self.signature = binascii.hexlify(signature).decode("utf-8")

    def __str__(self):
        return "Sender: " + self.sender.username + "\nRecipient: " + self.recipient + "\Coin: " + str(self.coin.coin_id)