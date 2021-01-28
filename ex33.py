i = 0
x = 6
numbers = []

while i < x:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
    print("\n")

print("The numbers: ")

for num in numbers:
    print(num)

print("So now let's do a quick test.")
for elo in numbers:
    print(numbers[elo])
    if elo == 3:
        print("\tOh shit that's my lucky number.")
    