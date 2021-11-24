import hashlib
from typing import List
from block import Block
from transaction import Transaction

class Blockchain:

    @property
    def last_block(self):
        return self.__chain[-1]

    @property
    def first_block(self):
        return self.__chain[0]

    @property
    def get_chain(self):
        return self.__chain

    @property
    def get_current_transactions(self):
        return self.__current_transactions

    def __init__(self, initial_transactions: List[Transaction]):
        self.__current_transactions = initial_transactions
        self.__chain = []
        self.__difficulty = 4
        self.create_genesis()

    def create_genesis(self):
        genesis_block = Block(0, self.__current_transactions, 0, '00')
        self.__chain.append(genesis_block)
    
    def change_difficulty_level(self, level):
        self.__difficulty = level

    def add_block(self, block):
        if self.validate_block(block, self.last_block):
            self.__chain.append(block)
            self.__current_transactions = []
            return True
        
        return False

    def validate_block(self, current_block, previous_block):
        if current_block.index != previous_block.index + 1:
            return False

        if current_block.previous_hash != previous_block.hash:
            return False

        if not self.validate_proof_of_work(previous_block.nonce, previous_block.hash, current_block.nonce):
            return False

        return True

    def append_blockchain(self, transactions: List[Transaction]):
        last_block = self.last_block
        index = last_block.index + 1
        previous_hash = last_block.hash
        nonce = self.generate_proof_of_work(last_block)
        self.__current_transactions = transactions
        block = Block(index, self.__current_transactions, nonce, previous_hash)
        if self.add_block(block):
            return block
        
        return None

    def validate_proof_of_work(self, last_nonce: int, last_hash: str, nonce: int):
        sha = hashlib.sha256(f'{last_nonce}{last_hash}{nonce}'.encode())
        return sha.hexdigest()[:self.__difficulty] == '0' * self.__difficulty

    def generate_proof_of_work(self, block):
        last_nonce = block.nonce
        last_hash = block.hash
        nonce = 0
        while not self.validate_proof_of_work(last_nonce, last_hash, nonce):
            nonce += 1

        return nonce

    def validate_chain(self, chain_to_validate):
        if chain_to_validate[0].generate_hash() != self.__chain[0].generate_hash():
            return False

        for x in range(1, len(chain_to_validate)):
            if not self.validate_block(chain_to_validate[x], chain_to_validate[x - 1]):
                return False

        return True

