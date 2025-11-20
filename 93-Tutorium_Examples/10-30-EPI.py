# Simple for-loop using range()
for i in range(0, 5, 2):
    print(i)

# Example using a iterable collection such as list or sets
t = ["banana", "apple", "dog"]
for x in t:
    print(x) 

# While-loop example with a condition
cond = True
count = 0
while cond:
    #do something
    count += 1
    if count > 1999:
        cond = False

# While-loop example using break keyword to stop the infinite loop
while True:
    #do soemthing
    if 0 < 1:
        break