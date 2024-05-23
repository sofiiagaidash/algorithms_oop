class Shop():
    def __init__(self,shop_name,store_type,number_of_units = 0):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = number_of_units
    def describe_shop(self):
        print(f"Shop name:{self.shop_name}")
        print(f"Store_type:{self.store_type}")
        print(f"number_of_units:{self.number_of_units}")
    def set_number_of_units(self,count):
        self.number_of_units = count
    def increment_number_of_units(self,surplus):
        self.number_of_units += surplus
class Discount(Shop):
    def __init__(self,shop_name,store_type,number_of_units = 0,store_disount = []):
        super().__init__(shop_name,store_type,number_of_units)
        self.discount = store_disount
    def get_discounts_ptoducts(self):
        print(self.discount)

shop1 = Shop("Silpo","supermarket",15)
shop1.describe_shop()
shop1.increment_number_of_units(900)
store_discount = Discount("@","Supermrker",140,["Fruits","Meat"])
store_discount.get_discounts_ptoducts()