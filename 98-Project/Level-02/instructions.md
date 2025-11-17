# Instructions

You already have a working supermarkt program from `Level-01` this time the task is to rewrite it using functions. This helps to make the code more structured and reusable (Nobody likes to reapeat the same code over and over).

## Requirements

1. Change the structure of all products so that each product is **self-contained** that means no 2 list each storing one kind of information. Do **NOT** use classes just simple data types.
   * _If you don't have know how, ask other students during the tutorium :)_
   
2. Create at least the following functions 

    ```python
    def show_products(product, prices):
        # Display the list of products and prices
        pass

    def ask_for_product():
        # Ask the user what product it wants and returns the product and it's price
        pass

    def add_to_cart(product, price, inventory, cart):
        # If the product exists and the store has inventory of it, add it to the cart otherwise says that the product is not available.
        pass
    
    def print_reciept(cart, total):
        # Prints what the user bought and the total to pay
        pass

    def calculate_total(cart) -> float:
        # **Optional**: calculates the total price of all items in the cart.
        pass 
    ```

    You can change the number of arguments that the function takes to accommodate to what your logic and structure is.

    You can also create more functions if you need them.

3. Implement an inventory of products for the supermarket so that the user can not buy items if they are not available at the moment. (from last week extra's)

4. Create a function called `main()` that contains all the logic for the supermarket using the functions you implemented before. The output is the same or very similar as what you did on `Level-01` but organized into functions. Something like:
    ```python
    def main():
        products = ...
        prices = ...
        cart = ...
        inventory = ...

        show_products(products, prices)

        While True:
            item, price = ask_for_item()
            
            if item == "pay":
                break
            
            add_to_cart(item, price, inventory, cart)

        print_reciept(cart)
    ```

## Extra Ideas
1. Instead of having to write the products by hand all the time import them from `products.csv`
2. Make the products display sort by product category
3. **DIFFICULT**: Make a menu where the user can decide what to do (eg. See products, buy (3-5 times), see products, buy (multiple times), pay)