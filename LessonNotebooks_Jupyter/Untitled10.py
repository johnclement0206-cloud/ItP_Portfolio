#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import getpass

password = str(getpass.getpass("Enter the password: "))
start = time.time()
CHARS = "abcdefghijklmnopqrstuvwxyz"
guess = []
for val in range(5):
    a = [i for i in CHARS]
    for y in range(val):
        a = [x + i for i in CHARS for x in a]
    guess = guess + a
    if password in guess:
        break
end = time.time()
clock = (end - start)

print("Initializing brute force...")
print(f"Password cracked! It took {clock} seconds to crack the password.") 
print(f"The password is: {password}")


# In[1]:


largest = None
smallest = None

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        number = int(user_input)
        if largest is None or number > largest:
            largest = number
        if smallest is None or number < smallest:
            smallest = number
    except ValueError:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)


# In[ ]:




