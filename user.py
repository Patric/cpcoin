from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from transaction import Transaction

class User:
    def __init__(self, username: str):
        self.username = username
        self.__private_key = RSA.generate(1024)
        self.public_key = self.__private_key.publickey().export_key()
    
    def sign(self, transaction: Transaction):
        transaction_data = transaction.generate_data()
        hash_object = SHA256.new(transaction_data)
        signature = pkcs1_15.new(self.__private_key).sign(hash_object)
        # self.signature = binascii.hexlify(signature).decode("utf-8")
        transaction.set_signature(signature)
        return transaction

    def get_public_key(self):
        return str(self.public_key)

    def set_current_hash(self, hash: str):
        self.current_hash = hash

    def validate_blockchain_last_hash(self, last_hash):
        return self.current_hash == last_hash