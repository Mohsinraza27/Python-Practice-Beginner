## Bike Rental System 
# 1__Display available bikes
# 2__Request a bike for rent(Rs.2500 --> 1 qt.)
# 3__Exit
class bike_Shop:
    def __init__(self, stock):
        self.stock = stock
    def display_Bike(self):
        print("Total Bikes", self.stock)
    def rent_For_Bike(self, q):
        if q <= 0:
            print("Enter the positive value or greater the zero!")
        elif q > self.stock:
            print("Enter the (less then stock)")
        else:
            self.stock = self.stock - q
            print("Total Prices ", q*2500)
            print("Total Bikes ", self.stock)
while True:
    obj = bike_Shop(100)
    user_input = int(input('''
                   1__Display available bikes
                   2__Request a bike for rent(Rs.2500 --> 1 qty.)
                   3__Exit
                   '''))
    if user_input == 1:
        obj.display_Bike()
    elif user_input == 2:
        n = int(input("Enter the Qty:-- "))
        obj.rent_For_Bike(n)
    else:
        break              
                                 
                                       
                       