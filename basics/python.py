# variable
studentsCount = 1000
rating = 4.5
addmited = True
skillName = "Python Programming"
print(studentsCount)

# strings
skill = ("python programming")
# len--> count characters
print(len(skill)) 
print(skill[0]) # prints first character
print(skill[-1]) #prints last character
print(skill[0:3]) #prints first three characters
print(skill[:]) #prints full

# escape sequences
# we can use \' or \" or \\ or \n
skill = "Python \"Programming \' \\ break \nbreak"
print(skill)

# formatted strings
first = "Mahidul"
last = "Haque"
full = f"{first} {last}\n"
print(full)

# string methods
skill = "Python PRogramming"
# access functions by writing "." dot
capital = skill.upper() 
lower = skill.lower()
print(capital)
print(lower)
print(skill.strip)
print(skill.find("PRo"))
print(skill.replace("P", "J"))
print("PRo" in skill)
print("PRo" not in skill)

# numbers
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x = x + 3 #sum
x += 3 #sum
print(x)

import math
print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))

# type conversation -->

# int()
# float()
# bool()
# str()

y = input("x: ")
z = int(x) + 1
print(f"x: {x}, y: {y}")


