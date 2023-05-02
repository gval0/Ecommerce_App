# class for managing information for the certain product
# product id is unique

class product_info:
    product_id: str
    product_name: str
    product_price: float
    product_quantity: int
    purchase_history = []
    order_num : int
    orders_N: int

    # init function
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = price
        self.product_quantity = 0
        self.order_num = 0

    #updates product infrom regarding name and current price
    def update_info(self, product_name: str, price: float):
        self.product_name = product_name
        self.product_price = price

    # increaseas amount of inventory
    def increase_amount(self, quantity: int, price: float) -> None:
        self.product_quantity += quantity
        self.purchase_history.append(str("purchase " + str(quantity) + " " + str(price)))
        
     # decreases amount of inventory
    def decrease_amount(self, quantity: int) -> None:
        self.product_quantity -= quantity
        self.purchase_history.append(str("order " + str(quantity) + " " + str(self.product_price) + " " + str(self.purchase_avg())))
        self.order_num += quantity

    # returns product quantity
    def get_quantity(self) -> int:
        return self.product_quantity

    # returns ordered amount
    def get_order_num(self) -> int:
        return self.order_num

    # returns product name
    def get_product_name(self) -> str:
        return self.product_name

    # calculates and returns purchase average for this product
    def purchase_avg(self) -> float:
        product_N = 0
        product_totoal_price = 0
        for action in self.purchase_history:
            str_arr = action.split(" ")
            if str_arr[0] == 'purchase':
                product_N += int(str_arr[1])
                product_totoal_price += float(str_arr[2]) * int(str_arr[1])
        return float(product_totoal_price)/product_N

    #calculates and returns profit for this product
    def get_profit(self) -> float:
        purchased_N = 0
        purchased_price = 0
        order_N = 0
        order_price = 0
        for action in self.purchase_history:
            str_arr = action.split(" ")
            if str_arr[0] == 'purchase':
                purchased_N += int(str_arr[1])
                purchased_price += float(str_arr[2]) * int(str_arr[1])
            else:
                order_N += int(str_arr[1])
                order_price += float(str_arr[2]) * int(str_arr[1])
        avg_purchase = float(purchased_price)/purchased_N
        avg_order = float(order_price)/order_N
        profit_per_unit = avg_order - avg_purchase
        return  profit_per_unit * order_N

    #give order report for this product
    # format product_id priduct_name quantity price purchase average
    def get_order_report(self,) -> str:
        res = ''
        for action in self.purchase_history:
            str_arr = action.split(" ")
            if str_arr[0] == 'order':
                res += (self.product_id + " " + self.product_name + " " + str(str_arr[1]) + " " + str(str_arr[2]) + " " + str(str_arr[3]))
        return res
    

