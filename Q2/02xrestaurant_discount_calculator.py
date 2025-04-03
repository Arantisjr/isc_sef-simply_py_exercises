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
    charge = amt * 0.05
    price = amt + charge
    print(f'price to pay:\n {price}')

def main_function():
    choice =   input("""enter the following
        1: if a customer and buying at 10000frs and above\n
        2: if a customer, buying at 10000frs and above and part of the loyalty program\n
        3: if not a customer  
          """)
    amt = int(input('Enter price:\n'))
    if choice == '1' and amt >= 10000:
        twenty_percent(amt)
    elif choice == '2 'and amt >= 10000:
        loyalty_program(amt)
    elif choice == '3' and amt < 10000:
        not_customer(amt)
    else:
        print("Enter the correct format")
  


main_function()
