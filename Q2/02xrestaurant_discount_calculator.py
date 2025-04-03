# function to calculate 20% discount 
def twenty_percent(amt):
    discount = amt * 0.2
    price = amt - discount
    print (f'Your discount:\n {discount}')
    print(f'price to pay:\n {price}')

# function if customer is part of the loyalty program
def loyalty_program(amt):
    discount = amt * 0.25
    price = amt - discount
    print (f'Your discount:\n {discount}')
    print(f'price to pay:\n {price}')
# function if not a customer
def not_customer(amt):
    charge = amt * 0.25
    price = amt + charge
    print(f'price to pay:\n {price}')

def main_function(amt):
    amt = input(int("Enter price:\n "))



loyalty_program(10000)