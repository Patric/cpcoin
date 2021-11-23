from chainmanager import ChainManager


class User:
    def __init__(self, username: str, chain_manager: ChainManager):
        self.username = username
        self.current_hash = ""
        self.chain_manager = chain_manager

    def pay(self, recipient: str, coin_id: int):
        result = self.chain_manager.add_transaction(self.username, recipient, coin_id)
        if result == True:
            return self.chain_manager
        return None


    # check list coins
    def check_wallet(self):
        return self.chain_manager.user_wallet_check(self.username)

    def validate_blockchain():
        return True

    #funkcja hashująca