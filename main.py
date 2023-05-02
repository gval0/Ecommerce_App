from product_data_base import product_data_base
import csv
import os

args: list
data_base: product_data_base
report: list

# methods perform action based on input 

def check_len(lenght: int) -> bool:
    if len(args) < lenght:
        print("Not valid amount of arguments")
        return True
    return False

def check_if_float(word: str) -> bool:
    try:
        float(args[3])
        return False
    except ValueError:
        print("Price is invalid")
        return True
    
def save_product():
    if check_len(4) or check_if_float(args[3]):
        return
    id = args[1]
    name = args[2]
    price = float(args[3])
    data_base.save_product(id, name, price)

def purchase_product() -> None:
    if check_len(4) or check_if_float(args[3]) or not args[2].isdigit():
       return

    id = args[1]
    quantity = int(args[2])
    price = float(args[3])
    data_base.purchase_product(id, quantity, price)

def order_product() -> None:
    if check_len(3) or not args[2].isdigit():
        return
    id = args[1]
    quantity = int(args[2])
    data_base.order_product(id, quantity)

def get_quantity_of_product() -> None:
    if check_len(2):
        return
    res = data_base.get_quantity_of_product(args[1])
    if res != None:
        print(res)

def get_average_price() -> None:
    if check_len(2):
        return
    res = data_base.get_average_price(args[1])
    if res !=  None:
        print(res)

def get_product_profit() -> None:
    if check_len(2):
        return
    res = data_base.get_product_profit(args[1])
    if res !=  None:
        print(res)

def get_fewest_product() -> None:
    res = data_base.get_fewest_product()
    if res !=  None:
        print(res)

def get_most_popular_product() -> None:
    res = data_base.get_most_popular_product()
    if res !=  None:
        print(res)

# console command: method name
switch = {
    'save_product': save_product,
    'purchase_product': purchase_product,
    'order_product': order_product,
    'get_quantity_of_product': get_quantity_of_product,
    'get_average_price': get_average_price,
    'get_product_profit': get_product_profit,
    'get_fewest_product': get_fewest_product,
    'get_most_popular_product': get_most_popular_product

}

VALID = {
    'save_product',
    'purchase_product',
    'order_product',
    'get_quantity_of_product',
    'get_average_price',
    'get_product_profit',
    'get_fewest_product',
    'get_most_popular_product'
}

# runs the console programme
if __name__ == '__main__':
    data_base = product_data_base()
    args = []
    report = []
    while True:
        user_input = input("Enter command: ")
        if user_input[-1:] == '\r':
            user_input =  user_input[:-1]
        command = ''
        args = user_input.split(' ')
        command = args[0]
        if user_input == 'exit':
            break
        if command in VALID:
            switch[command]()
        else:
            print(command + " is incorrect")