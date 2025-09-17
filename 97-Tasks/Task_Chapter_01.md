# Task for Chapter 01

Here you will find all the tasks for chapter _01 An Introduction to Python_. You should do them after going after all sessions of said chapter.

> To see all the features of the file you should download the extension 'Markdown all in One' from the extension Tab in VS code (CTRL + SHIFT + X)
## Requirements and Setup

### Basics
1. Create a Python file on the `Solutions` folder and name it `Test_file`.
2. Use the `print()` function to print a message into the console, then execute the file.

### Variables
1. Which of the following variables are valid? Mark all valid options with an 'X'
   - [ ] `a == "Hello"`
   - [ ] `b - 3`
   - [ ] `cargo = True`
   - [ ] `_e_p_r = 'class'`
   - [ ] `delta=2.13`
   - [ ] `vAr = 1`
   - [ ] `4Var = 1`
   - [ ] `c&n = 1`


### Collections
1. Create a list containing a number and a float. After the creation add a string and a number; then remove the second element of the list.
2. Investigate what functions are available for the collections that were presented during the Tutorium

## Flow, Loops and Arithmetic

### Flow Control
1. Write a program that ask the user for 2 numbers (`a`,`b`) and then compares them to see if `a` is bigger, smaller or equal to `b`.
2. Write a program that ask the user for a `grade` and congratulate them if its a passing grade (under 4.0) or says _"better luck next time"_ if is not.

### Loops
1. Use a `for` loop to print all numbers from 1 to 100
2. Write a program that ask for a number `n`, then use a loop to calculate the **sum** from 1 to `n`
3. Write a program that ask the user for a number `n` and then prints out its multiplication table up to 10
    ```python
    Enter a number: 2

    Output:
    2 x 1 = 2
    2 x 2 = 4
    ...
    2 x 10 = 20
    ```
4. What is the output of the following loop
    ```python
    for i in range(5):
        for x in range(3):
            print(i*x + i)
    ```

5. Why does the following loop fails?
   ```python
    for i in range(5):
    print(i)
    ```

## Combining Varibales, Flow control and loops
1. Write a program that generates a random number then ask the user to guess the number. The program stops only if the guess was correct otherwise it ask again.
> To get a random number write `import random` at the top of the file, then use `a = random.randint(0,100)`

## Functions, Imports and Exceptions
### Functions
1. Create a function called `calculate(a, b, operation)` that:
   1. sums if the operation is `"add"`
   2. subtracts if `"sub"`
   3. multiplies if `"mul"`
   4. divides if `"div"`
   ```python
   calculate(2,3, "add") # output: 5
   ```

2. Create a function `find_max(a,b,c)` that returns the biggest of the 3 numbers.

### Import
1. Use the `datetime` module to print the current date and time in the format
   Expected: `"Today is: DD-MM-YYYY HH:MM:SS"`
2. Ask the user to enter a number using `input()`. Use `try/except` to ensure they entered a valid number (int).

### Exceptions
1. Write a function called `safe_divide(a,b)` that `a` by `b`. If `b` is zero then it should **catch** the exception and print `"Can't devide by zero"`
2. 