from typing import List
from Crypto.PublicKey import RSA
from blockChain import Blockchain
from coin import Coin
from transaction import Transaction
from user import User

class ChainManager:
    def __init__(self, users: List[User]):
        key = RSA.generate(256)
        self.__private_key = key
        self.public_key = key.publickey().export_key()
        coins = [Coin(1, 1), Coin(2, 1), Coin(3, 1), Coin(4, 1), Coin(5, 1)]
        user_idx = 0
        initial_transactions = []
        for coin in coins:
            if (user_idx > len(users)):
                user_idx = 0

            initial_transactions.append(Transaction(self, users[user_idx].public_key, coin))

        self.__blockchain = Blockchain(initial_transactions)

    # TODO: repair below code
    def add_transaction(self, sender: str, recipient: str, coin_id: int):
        coin = self.get_coin(sender, coin_id)
        if coin == None:
            return False
        transaction = Transaction(sender, recipient, coin)
        result_block = self.__blockchain.append_blockchain([transaction])
        return result_block

    def get_coin(self, sender: str, coin_id: int):
        user_coins = self.user_wallet_check(sender)
        transaction_coin = None
        for i in range(0, len(user_coins)):
            if coin_id == user_coins[i].coin_id:
                transaction_coin = user_coins[i]
        return transaction_coin

    def user_wallet_check(self, username: str):
        user_coins = []
        for block in self.__blockchain.get_chain:
            for transaction in block.transactions:
                if transaction.recipient == username:
                    user_coins.append(
                        Coin(transaction.coin['coin_id'], transaction.coin['value']))
                elif transaction.sender == username:
                    user_coins = [
                        coin for coin in user_coins if coin.coin_id != transaction.coin['coin_id']]
        return user_coins

    def get_last_block_hash(self):
        return self.__blockchain.last_block.hash
