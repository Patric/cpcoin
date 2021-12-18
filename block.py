import json
from time import time
from typing import List
from transaction import Transaction
from utils import calculate_hash

class Block:
    def __init__(self, index: int, transactions: List[Transaction], nonce: int, previous_block = None,):
        self.index = index
        self.timestamp = time()
        self.transactions = transactions
        self.nonce = nonce
        self.previous_block = previous_block

    @property
    def previous_block_hash(self):
        previous_block_hash = ""
        if self.previous_block:
            previous_block_hash = self.previous_block.hash

        return previous_block_hash

    @property
    def hash(self) -> str:
        transaction_dicts = []
        for transaction in self.transactions:
            transaction_dicts.append(transaction.generate_data())

        block_content = {
            "transaction_data": transaction_dicts,
            "timestamp": self.timestamp,
            "index": self.index,
            "nonce": self.nonce,
            "previous_block_hash": self.previous_block_hash
        }
        block_content_bytes = json.dumps(block_content, indent=2).encode('utf-8')
        return calculate_hash(block_content_bytes)
