#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(1, 11):
    print(i)


# In[2]:


a = 0
while a < 5:
    print("Good morning!")
    a += 1


# In[6]:


fruits = ["apple", "banana", "orange", "grape", "dragonfruit", "strawberry", "jackfruit"]
for fruit in fruits:
    if fruit == "banana":
        pass
    else:
        print(fruit)


# In[11]:


for letter in "hello diego":
    if letter == "d":
        break
    else:
        print(letter)


# In[1]:


for i in range(1, 21):
    if i % 2 == 0:
        print(i)
print(f"Last value: {i}")


# In[15]:


for i in range(1, 6):
    i **= 2
    print(i)


# In[14]:


banana = [1, 2, 3, 4, 5]
for j in banana:
    print(j ** 2)


# In[ ]:




