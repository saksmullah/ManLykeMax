# blockcahin = [[1]]
#
# def get_last_blockchain_value():
#     return blockcahin[-1]
#
# def add_value(transaction_amount):
#     blockcahin.append([get_last_blockchain_value(), transaction_amount])
#     print(blockcahin)
#
#
# add_value(2)
# add_value(0.9)
# add_value(10.89)
#
# print("-" * 100)
# #
# pfc = [[1.50]]
#
#
# def kids_meal(differnt_price):
#     pfc.append([pfc[-1], differnt_price])
#     print(pfc)
#
# kids_meal(1.00)
# kids_meal(1.70)
# kids_meal(2.00)
#
# print("-" * 100)

blockcahin = []

def get_last_blockchain_value():
    return blockcahin[-1]

def add_value(transaction_amount,last_transaction=[1] ):
    blockcahin.append([last_transaction, transaction_amount])
    print(blockcahin)

tx_amount = input('Your transaction amount please: ')
add_value(tx_amount)
add_value( last_transaction=get_last_blockchain_value(), transaction_amount=0.9)
add_value(10.89, get_last_blockchain_value())


# blockcahin = []
#
# def get_last_blockchain_value():
#     return blockcahin[-1]
#
# def add_value(transaction_amount,last_transaction=[1] ):
#     blockcahin.append([last_transaction, transaction_amount])
#     print(blockcahin)
#
# add_value(3)
# add_value(6, get_last_blockchain_value())
# add_value(2, get_last_blockchain_value())


