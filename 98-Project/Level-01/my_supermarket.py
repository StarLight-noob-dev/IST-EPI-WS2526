__author__ = "My Supermarket Team, 123456789" # Obviously me this is just a joke

products = ["apple", "banana", "orange", "grape", "watermelon"]
prices = [0.5, 0.45, 0.7, 1.0, 3.0]

print(r"""
  __  __                                                        _        _   
 |  \/  |                                                      | |      | |  
 | \  / |_   _   ___ _   _ _ __   ___ _ __ _ __ ___   __ _ _ __| | _____| |_ 
 | |\/| | | | | / __| | | | '_ \ / _ \ '__| '_ ` _ \ / _` | '__| |/ / _ \ __|
 | |  | | |_| | \__ \ |_| | |_) |  __/ |  | | | | | | (_| | |  |   <  __/ |_ 
 |_|  |_|\__, | |___/\__,_| .__/ \___|_|  |_| |_| |_|\__,_|_|  |_|\_\___|\__|
          __/ |           | |                                                
         |___/            |_|                                                
""")

print("Here are the available products:\n")

print("-"*30)
for product, price in zip(products, prices):
    print(f"{product}: €{price:.2f}")
print("-"*30, "\n")

basket = []

while True:
    choice = input("Enter the product name to buy it (or type 'exit' to quit): ").strip().lower()
    
    if choice == 'exit':
        print("Thank you for visiting My Supermarket!")
        break
    
    if choice in products:
        index = products.index(choice)
        basket.append((choice, prices[index]))
        print(f"Added {choice} to your basket at ${prices[index]:.2f}.")
    else:
        print("Sorry, we don't have that product. Please try again.")

if basket:
    print("\nYour basket contains:")
    total = 0
    for item, price in basket:
        print(f"{item}: ${price:.2f}")
        total += price
    print(f"Total amount: ${total:.2f}")
else:
    print("Your basket is empty.")

print("Thank you for visiting My Supermarket, have a great day!")