import threading
from typing import List
from user import User
import simulationUtils
import time
from ThreadWithException import ThreadWithException


logo = """
                                                                                        
      _____        _____               _____           _____     ____  _____   ______   
  ___|\    \   ___|\    \          ___|\    \     ____|\    \   |    ||\    \ |\     \  
 /    /\    \ |    |\    \        /    /\    \   /     /\    \  |    | \\    \| \     \ 
|    |  |    ||    | |    |      |    |  |    | /     /  \    \ |    |  \|    \  \     |
|    |  |____||    |/____/|      |    |  |____||     |    |    ||    |   |     \  |    |
|    |   ____ |    ||    ||      |    |   ____ |     |    |    ||    |   |      \ |    |
|    |  |    ||    ||____|/      |    |  |    ||\     \  /    /||    |   |    |\ \|    |
|\ ___\/    /||____|             |\ ___\/    /|| \_____\/____/ ||____|   |____||\_____/|
| |   /____/ ||    |             | |   /____/ | \ |    ||    | /|    |   |    |/ \|   ||
 \|___|    | /|____|              \|___|    | /  \|____||____|/ |____|   |____|   |___|/
   \( |____|/   \(                  \( |____|/      \(    )/      \(       \(       )/  
    '   )/       '                   '   )/          '    '        '        '       '   
        '                                '                                  
"""

print(logo)

def print_users_coins(users: List[User], optional_text=""):
  print(optional_text)
  for user in users:
    print(user.username + "'s coins: ")
    for coin in user.user_wallet_check(user.get_public_key()):
       print(str(coin) + " ")


# Create identity
ala = User("Ala")
bob = User("Bob")
john = User("John")
users = [ala, bob, john]

users = simulationUtils.initiate_users_with_blockchain(users)

print_users_coins(users)

# Create transactions
print("Ala pays 1 to Bob")
ala.broadcast_new_transaction(bob, 1, users)

print("Bob pays 2 to John")
bob.broadcast_new_transaction(john, 2, users)

print("John pays 3 to Ala")
john.broadcast_new_transaction(ala, 3, users)

print_users_coins(users)


# #validate coins
# print("Coins valid: ", chain_manager.validate_coins())

# #validate transactions
# print("Transactions valid: ", chain_manager.validate_transactions())

# #validate blockchain
# print("Blockchain valid: ", chain_manager.validate_blockchain())

# # END
#!/usr/bin/python

def getUserByName(list: List[User], name):
  for elem in list:
    if elem.username == name:
      return elem



def makeTurn(user: User):
  global threads
  try:
    user.mine()
    print(f'{user.username} received an award \n')
    for thread in threads:
      if thread.name != user.username:
        thread.raise_exception()
        # 


        # if broadcasting to the winner failed transactions that failed are not persisted in blockchain of the others (if blockchain is valid)
        externalUser = getUserByName(users, thread.name)
        old_blockchain = externalUser.get_blockchain()
        updated_blockchain = user.get_blockchain()
        externalUser.set_blockchain(updated_blockchain)
        is_new_blockchain_correct = externalUser.validate_all()
        if not is_new_blockchain_correct:
          externalUser.set_blockchain(old_blockchain)
        
    print_users_coins(users)
  except Exception as e:
    pass
 
bobsMining = ThreadWithException(bob.username, makeTurn, [bob])
alasMining = ThreadWithException(ala.username, makeTurn, [ala])
johnsMining = ThreadWithException(john.username, makeTurn, [john])

threads = [bobsMining, alasMining, johnsMining]

bobsMining.start()
alasMining.start()
johnsMining.start()




