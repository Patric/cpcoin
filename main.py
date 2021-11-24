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

main_menu = """
0. Quit
1. Login
"""

user_menu = """
1. Logout
2. Make Payment
3. Check Wallet
4. Validate blockchain  
"""

print(logo)
option = int(input(main_menu))
chain_manager = ChainManager()
user = User("", chain_manager)
while option is not 0:
    if user.username == "":
        if option == 1:
            print("Available users are: Ala, Bob, John")
            username = input('Enter username: ')
            print("User " + username + " logged in")
            user = User(username, chain_manager)
        
    else:
        if option == 1:
            user = User("", chain_manager)
        elif option == 2:
            recipent = str(input("Enter recipent name: "))
            coin_id = int(input("Enter coin id: "))
            payment_result = user.pay(recipent, coin_id)
            if payment_result == None:
                print("Transaction error")
            else:
                chain_manager = payment_result
        elif option == 3:
            coins = user.check_wallet()
            coins_serialized = []
            print("Your coins: ")
            for coin in coins:
                coins_serialized.append(coin.serialize())
            print(coins_serialized)

        elif option == 4:
            is_valid = user.validate_blockchain()
            print("Validation result is: " + str(is_valid))
        else:
            print("Invalid option number")
    
    if (user.username == ""):
        option = int(input(main_menu))
    else:
        option = int(input(user_menu))
