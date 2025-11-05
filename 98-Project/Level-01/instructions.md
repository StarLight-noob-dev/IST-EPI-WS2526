# Instructions

Create a simple Python program that simulates a supermarket checkout.
For now, don’t use functions or classes. Everything should be written in a **single** sequence of code.

The idea here is to practice the basic concepts seen on the first 2-3 classes such as

* Variables
* Basic data structures (List, Dict, Set, etc)
* Loops
* Conditionals
* Basic input/output

### Requirements
1. Choose a data structure to define at least 3 products and their prices per unit. You can use any structure you feel is the most appropiate. e.g
    ```python3
    products = ["shoe", "apple", "shawarma"]
    price = [20, 0.5, 2.5]
    ```

2. Display all available products and their price
3. Ask the user, **repeatedly**, what product they want to buy.
   - If the product exist it should be added to the total
   - If not print a message saying the product is not available or doesnt exist
   - Once the user types "pay" it finishes
4. Once it finishes display the total cost of the products and a list of what the user bought

    ```
    Available products:
    shoe - 20€
    apple - 0.5€
    shawarma - 2.5€

    What do you want to buy? shoe
    What do you want to buy? apple
    What do you want to buy? shawarma
    What do you want to buy? done

    You bought: ['show', 'apple', 'shawarma']
    Total: 23€
    Thank you for shopping!
    ```

## Extra ideas
1. Make the supermarket have an arbitrary number of products and check the stock before the person buy (if there's only 1 apple I can't buy 2...)
2. Allow to enter quantities (buy 2 shoes) 
3. Format the total of the purchase with 2 decimals
4. Handle capitalization; Is buying `Shoe` and `shoe` the same?
5. Make an stylized reciept for your supermarket