my_name = "Jan Pozywilko"
my_age = 19
my_height = 187 # in centimeters
my_weight = 80 # kilograms
my_eyes = "blue"
my_teeth = "white"
my_hair = "blue"

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} centimeters tall.")
print(f"He's {my_weight} kilograms heavy.")
print("But I can quickly convert it to pound if I want by simply multiplying it by 3")
print(f"My weight in pounds is:", my_weight * 3, "pounds")
print("Actually that's not to heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the cofee.")

#this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_weight}, and {my_weight}, I get {total}.")