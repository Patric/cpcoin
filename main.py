from blockChain import Blockchain
from transaction import Transaction

menu_hint_text = """
                                                                                        
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

0. Quit
1. Change mining diffulty level 
2. Add transaction 
3. Mine transaction 
4. Validate blockchain 
5. Show transactions
6. Show blockchain
7. Restart
"""
option = int(input(menu_hint_text))
blockchain = Blockchain()
while option is not 0:
    if option == 1:
        difficulty_level = int(input('Enter difficulty level: '))
        blockchain.change_difficulty_level(difficulty_level)
        print("Difficulty level set to " + str(difficulty_level))
    elif option == 2:
        sender = str(input("Enter sender name: "))
        recipent = str(input("Enter recipent name: "))
        amount = float(input("Enter amount: "))
        blockchain.add_transaction(sender, recipent, amount)
        print("Transaction added")
    elif option == 3:
        address = str(input("Enter miner's address: "))
        blockchain.mine(address)
        print("Transaction mined")
    elif option == 4:
        print('Is blockchain valid: ' + str(blockchain.validate_chain(blockchain.get_chain)))
    elif option == 5:
        for transaction in blockchain.get_current_transactions:
            print(transaction)
    elif option == 6:
        for block in blockchain.get_chain:
            print(block.serialize())
    elif option == 7:
        blockchain = Blockchain()
    else:
        print("Invalid option number")
    
    option = int(input(menu_hint_text))
