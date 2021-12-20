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

def print_users_coins(chain_manager, ala, bob, john):
  coins_summary = "Ala's coins: "
  for coin in chain_manager.user_wallet_check(ala.get_public_key()):
    coins_summary += str(coin) + " "
  coins_summary += "\nBob's coins: "
  for coin in chain_manager.user_wallet_check(bob.get_public_key()):
    coins_summary += str(coin) + " "
  coins_summary += "\nJohn's coins: "
  for coin in chain_manager.user_wallet_check(john.get_public_key()):
    coins_summary += str(coin) + " "
  coins_summary += "\n------------------- \n"
  print(coins_summary)

# Create identity
ala = User("Ala")
bob = User("Bob")
john = User("John")
users = [ala, bob, john]

# Create blockchain and initial transactions (inside)
chain_manager = ChainManager(users)
print_users_coins(chain_manager, ala, bob, john)

# Create transactions
print("Ala pays 1 to Bob")
chain_manager.pay(ala, bob, 1)
print_users_coins(chain_manager, ala, bob, john)

print("Bob pays 2 to John")
chain_manager.pay(bob, john, 2)
print_users_coins(chain_manager, ala, bob, john)

print("John pays 2 to Ala")
chain_manager.pay(john, ala, 2)
print_users_coins(chain_manager, ala, bob, john)

#validate coins
print("Coins valid: ", chain_manager.validate_coins())

#validate transactions
print("Transactions valid: ", chain_manager.validate_transactions())

#validate blockchain
print("Blockchain valid: ", chain_manager.validate_blockchain())

# END