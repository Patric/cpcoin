from typing import List
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from blockChain import Blockchain
from coin import Coin
from transaction import Transaction
from user import User

class ChainManager:
    def __init__(self, users: List[User]):
        self.__private_key = RSA.generate(1024)
        self.public_key = self.__private_key.publickey().export_key()
        coins = [Coin(1, 1), Coin(2, 1), Coin(3, 1), Coin(4, 1), Coin(5, 1)]
        user_idx = 0
        initial_transactions = []
        for coin in coins:
            if (user_idx >= len(users)):
                user_idx = 0
            
            transaction = Transaction(self.public_key, users[user_idx].public_key, coin)
            transaction = self.get_chainmanager_signed_transaction(transaction)
            initial_transactions.append(transaction)
            user_idx += 1
        # Create blockchain
        self.__blockchain = Blockchain(initial_transactions)

    def get_chainmanager_signed_transaction(self, transaction: Transaction):
        transaction_data = transaction.generate_data()
        hash_object = SHA256.new(transaction_data)
        signature = pkcs1_15.new(self.__private_key).sign(hash_object)
        transaction.set_signature(signature)
        return transaction

    def add_transaction(self, sender: User, recipient: User, coin_id: int):
        coin = self.get_coin(sender.get_public_key(), coin_id)
        if coin == None:
            return False
        transaction = Transaction(sender.public_key, recipient.public_key, coin)
        transaction = sender.sign(transaction)
        result_block = self.__blockchain.append_blockchain([transaction])
        return result_block

    def get_coin(self, sender_pk: str, coin_id: int):
        user_coins = self.user_wallet_check(sender_pk)
        transaction_coin = None
        for i in range(0, len(user_coins)):
            if coin_id == user_coins[i].coin_id:
                transaction_coin = user_coins[i]
        return transaction_coin

    def user_wallet_check(self, user_pk: str):
        user_coins = []
        for block in self.__blockchain.get_chain:
            for transaction in block.transactions:
                if transaction.get_recipient_pk() == user_pk:
                    user_coins.append(transaction.coin)
                elif transaction.get_sender_pk() == user_pk:
                    user_coins = [
                        coin for coin in user_coins if coin.coin_id != transaction.coin.coin_id]
        return user_coins

    def pay(self, sender: User, recipient: User, coin_id: int):
        result_block = self.add_transaction(sender, recipient, coin_id)
        if result_block == False:
            print("user " + sender.username + " does not own coin id " + str(coin_id))
            return None
        if result_block != None:
            sender.set_current_hash(result_block.hash)
            recipient.set_current_hash(result_block.hash)
            return self
        return result_block

  
    def get_last_block_hash(self):
        return self.__blockchain.last_block.hash

    def validate_coins(self):
        for transaction in self.__blockchain.first_block.transactions:
            if not self.validate_signature(self.public_key, transaction.signature, transaction.generate_data()):
                return False
        
        return True

    def validate_transactions(self):
        for block in self.__blockchain.get_chain:
            for transaction in block.transactions:
                if not self.validate_signature(transaction.sender_pk, transaction.signature, transaction.generate_data()):
                    return False
        
        return True

    def validate_signature(self, public_key: bytes, signature: bytes, transaction_data: bytes):
        public_key_object = RSA.import_key(public_key)
        transaction_hash = SHA256.new(transaction_data)
        try:
            pkcs1_15.new(public_key_object).verify(transaction_hash, signature)
        except ValueError:
             return False
   
        return True

    def validate_blockchain(self):
        return self.__blockchain.validate_chain(self.__blockchain.get_chain)
