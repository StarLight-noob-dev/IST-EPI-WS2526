inp = input("Enter the numbers as comma separated values: ")
numbers = inp.split(",")

number_dict = {
    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}


for number in numbers:
    if number in number_dict:
        print(number_dict[number], end="")
    else:
        print(f"[ERROR: {number}]", end="")
