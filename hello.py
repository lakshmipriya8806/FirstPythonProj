#This is a comment in Python
"""This is a multi line quote  in python"""

import matplotlib.pyplot as plt

has_license=True
age=18

able_to_drive=(has_license)and(age>=18)
print(able_to_drive)
power= 10**2
cube = 10**3

name="Priya"
name="Hari"

#print("My name is "+ name) 


message="I love Python programming with Python"

print("Python" in message)
print(message.startswith("I"))
print(message.endswith("Python"))

print(message.find("Python"))
print(len(message))
print(message.count("Python"))

print(message.lower())
print(message.upper())
print(message.title())
new_message=message.replace("Python","javascript")
print(new_message)

plt.figure(figsize=(5, 3))
plt.plot([1,2,3],[10,20,30])
plt.show()