# class for managing catalog of diffrent products
import sys
from product_info import product_info

class product_data_base:

    # instance var for product_id:product_info class
    product_dict = {}

    # updates catalog or adds new item to catalog
    def save_product(self, product_id: str, product_name: str, price: float) -> None:
        if product_id in self.product_dict:
            self.product_dict[product_id].update_info(product_name, price)
        else:
            curr_product = product_info(product_id, product_name, price)
            self.product_dict[product_id] = curr_product

    # add product to the inventory
    def purchase_product(self, product_id: str, quantity: int, price: float) -> None:
        if product_id in self.product_dict:
            self.product_dict[product_id].increase_amount(quantity, price)
        else:
            print("No such product ID")

    # removes product from the inventory
    def order_product(self, product_id: str, quantity: int) -> None:
        if product_id in self.product_dict:
            if self.product_dict[product_id].product_quantity >= quantity:
                self.product_dict[product_id].decrease_amount(quantity)
            else:
                print("Not enough")
        else:
            print("No such product ID")

    # return quantity of a certain product based on id
    def get_quantity_of_product(self, product_id: str) -> int:
        if product_id in self.product_dict:
            return self.product_dict[product_id].get_quantity()
        else:
            print("No such product ID")
            return None;

    # returns purchase average for certain product based on id
    def get_average_price(self, product_id: str) -> float:
        if product_id in self.product_dict:
            return self.product_dict[product_id].purchase_avg()
        else:
            print("No such product ID")
            return None;

     # returns product profit for certain product based on id
    def get_product_profit(self, product_id: str) -> float:
        if product_id in self.product_dict:
            return self.product_dict[product_id].get_profit()
        else:
            print("No such product ID")
            return None;

     # determines fewest product in inventory
    def get_fewest_product(self,) -> str:
        fewest_id = ""
        fewest_quantity = sys.maxsize
        for key in self.product_dict:
            if self.product_dict[key].get_quantity() < fewest_quantity:
                fewest_id = key
                fewest_quantity = self.product_dict[key].get_quantity()
        if fewest_id == '':
            print("No products")
            return None;
        return self.product_dict[fewest_id].get_product_name()

    # determines most product in inventory
    def get_most_popular_product(self,) -> str:
        most_id = ""
        most_quantity = 0
        for key in self.product_dict:
            if self.product_dict[key].get_order_num() > most_quantity:
                most_id = key
                most_quantity = self.product_dict[key].get_quantity()
        if most_id == '':
            print("No products")
            return None;
        return self.product_dict[most_id].get_product_name()
    
    # generates report for the entire catalog
    # reurns list
    def get_report(self, ) -> list:
        res = []
        for key in self.product_dict:
            str = self.product_dict[key].get_order_report()
            if str != '':
                res.append(str)
        return res
