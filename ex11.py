#print("How old are you?", end='')
age = int(input("How old are you?"))
print("How tall are you?", end=' ')
height = int(input())
print("How much do you weight?", end='')
weight = int(input())

print(f"So, you're {age} years old, {height} tall and {weight} heavy.")
print(age + height + weight)
