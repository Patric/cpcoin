import hashlib
import json
from time import time
from typing import List
from Transaction import Transaction

class Block:
    def __init__(self, index: int, transactions: List[Transaction], nonce: int, previous_hash: str):
        self.index = index
        self.timestamp = time()
        self.transactions = transactions
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.hash = self.generate_hash()

    def serialize(self):
        block_params = {x: self.__dict__[x] for x in self.__dict__ if x not in ['hash']}
        block_params['transactions'] = []
        for x in range(0, len(self.transactions)):
            block_params['transactions'].append(self.transactions[x].__dict__)
        for x in range(0, len(block_params['transactions'])):
            block_params['transactions'][x]['coin'] = self.transactions[x].coin.__dict__
        return json.dumps(block_params, sort_keys=True, indent=2)

    def generate_hash(self):
        sha = hashlib.sha256()
        serialized_block = self.serialize().encode('utf-8')
        sha.update(serialized_block)
        return sha.hexdigest()
