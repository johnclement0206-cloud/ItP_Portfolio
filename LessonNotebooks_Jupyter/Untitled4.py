#!/usr/bin/env python
# coding: utf-8

# In[9]:


marks = 99
attendance = 100

if marks >= 60 and attendance >= 85:
    print("You passed.")
    if marks >= 90:
        print("You are on the honors list!")
        if marks >= 99:
            print("How?")
    if attendance >= 90:
        print("You were remarkably present.")
        if attendance >= 95:
                print("You were present in almost everything.")
                if attendance >= 100:
                    print("You were present in everything.")
else:
    print("You failed.")


# In[15]:


age = 20 
citizen = True
id_card = False

if age >= 18 and (citizen or id_card):
    print("Allowed to vote.")
else: 
    print("Not allowed.")


# In[17]:


day = "Sunday"
time = 10

if day != "Sunday" and (time >= 9 and time <= 17):
    print("Shop is open")
else:
    print("Shop is closed")


# In[ ]:




