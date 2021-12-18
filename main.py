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

ala = User("Ala")
bob = User("Bob")
john = User("John")
users = [ala, bob, john]
chain_manager = ChainManager(users)

# TODO: prepare examples
# payment_result = user.pay(recipent, coin_id)
# if payment_result == None:
#     print("Transaction error")
# else:
#     chain_manager = payment_result

# coins = user.check_wallet()
# coins_serialized = []
# print("Your coins: ")
# for coin in coins:
#     coins_serialized.append(coin.serialize())
# print(coins_serialized)

# is_valid = user.validate_blockchain()
# print("Validation result is: " + str(is_valid))
