from chainmanager import ChainManager


class User:
    def __init__(self, username: str, chain_manager: ChainManager):
        self.username = username
        self.chain_manager = chain_manager
        self.current_hash = self.chain_manager.get_last_block_hash() 

    def pay(self, recipient: str, coin_id: int):
        result_block = self.chain_manager.add_transaction(self.username, recipient, coin_id)
        if result_block != None:
            self.current_hash = result_block.hash
            return self.chain_manager
        return result_block

    def check_wallet(self):
        return self.chain_manager.user_wallet_check(self.username)

    def validate_blockchain(self):
        return self.chain_manager.get_last_block_hash() == self.current_hash
