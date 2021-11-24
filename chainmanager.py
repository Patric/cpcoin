from blockChain import Blockchain
from coin import Coin
from transaction import Transaction


class ChainManager:
    def __init__(self):
        user1 = "Ala"
        user2 = "Bob"
        user3 = "John"
        self.users = [user1, user2, user3]
        coin1 = Coin(1, 1)
        coin2 = Coin(2, 1)
        coin3 = Coin(3, 1)
        coin4 = Coin(4, 1)
        coin5 = Coin(5, 1)
        initial_transactions = [
            self.create_initial_transaction(user1, coin1),
            self.create_initial_transaction(user2, coin2),
            self.create_initial_transaction(user3, coin3),
            self.create_initial_transaction(user1, coin4),
            self.create_initial_transaction(user2, coin5)]
        self.__blockchain = Blockchain(initial_transactions)

    def create_initial_transaction(self, recipient: str, coin: Coin):
        return Transaction("", recipient, coin)

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
