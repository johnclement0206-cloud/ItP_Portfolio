#!/usr/bin/env python
# coding: utf-8

# In[1]:


from time import sleep

for i in range(1, 10, 2): # for variable in range(start, stop, step)
    print(f"Iteration {i + 1}")
    sleep(0.5)
print("Done!")


# In[7]:


name = 0

while name < 5 and name >= -1:
    print("My name is Clement.")
    name += 1
    print(f"Iteration {name}")
    sleep(0.5)
print("Loop finalized!") 


# In[8]:


attempts = 0
MAX_ATTEMPTS = 3

while attempts < MAX_ATTEMPTS:
    login = input("Enter login: ")
    password = input("Enter password: ")
    if login == "admin" and password == "12345":
        print("Access granted.")
        break
    attempts += 1
    remaining = MAX_ATTEMPTS - attempts
    if remaining > 0:
        print(f"Incorrect credentials. {remaining} attempt(s) remaining.")
else:
    print("Access denied.")


# In[16]:


i = 0
while i < 6:
    if i == 1:
        pass
    i += 1
    if i == 3:
        continue
    print(i)


# In[21]:


car = "Ford"

print(len(car))


# In[ ]:




