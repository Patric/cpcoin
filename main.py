from chainmanager import ChainManager
from user import User

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

# Create identity
ala = User("Ala")
bob = User("Bob")
john = User("John")
users = [ala, bob, john]

# Create blockchain and initial transactions (inside)
chain_manager = ChainManager(users)
for coin in chain_manager.user_wallet_check(ala.public_key):
  print(str(coin))

# Create transactions
chain_manager.pay(ala, bob, 1)
chain_manager.pay(bob, john, 1)
chain_manager.pay(john, ala, 1)
for coin in chain_manager.user_wallet_check(ala.public_key):
  print(str(coin))

#validate coins
print("Coins valid: ", chain_manager.validate_coins())


#validate transactions
print("Transactions valid: ", chain_manager.validate_transactions())


#validate blockchain
print("Blockchain valid: ", chain_manager.validate_blockchain())

# END