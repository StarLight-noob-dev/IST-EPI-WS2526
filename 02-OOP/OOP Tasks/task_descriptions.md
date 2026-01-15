# Task 1: Bank Account Class

## Objective

Create a `BankAccount` that accepts deposits and withdrawals

## Requirements

### BankAccount

#### Attributes
-   account_number (private)
-   balance (protected)
-   owner_name

#### Methods

-   deposit(amount)
-   withdraw(amount)
-   get_balance()

### SavingsAccount (inherits BankAccount)

#### Attributes
-   interest_rate

#### Methods  
-   apply_interest()

## Rules

-   Balance must not be directly accessible
-   No negative deposits
-   Withdrawals cannot exceed balance



# Task 2: Library Management System

## Objective
Represent a library using Classes. The library has a limited inventory of books that can be borrowed by members.

## Requirements
- A library keeps track of all its books and members.
- Each book as a title, author, isbn and a flag representing if the book is available or not.
- Each member has a name, member_id and a list of the books it has borrow at the moment.

## Rules
- Each member can borrow at most 3 books
- Each book can be borrowed by one person at a time.