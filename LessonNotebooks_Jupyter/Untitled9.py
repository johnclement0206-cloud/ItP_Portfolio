#!/usr/bin/env python
# coding: utf-8

# In[1]:


cars = ["Ford", "Toyota", "Mitsubishi"]

for x in cars:
    print(x)


# In[12]:


users = [{'name': 'Bob', 'age': 30}, {'name': 'Alice', 'age': 25}]
users.sort(key=lambda user: user['age'])
print(users)


# In[23]:


num = [10, 20, 30, 40, 50]
print(num)
print(num[2])


# In[24]:


numbers = [5, 10, 15]
numbers.append(20)
print(numbers)


# In[31]:


initial_list = ["cherry", "apple", "durian", "banana"]
sorted_list = sorted(initial_list)
print(initial_list)
print(sorted_list)


# In[29]:


my_list = [3, 1, 4, 1, 5, 9, 2, 6]
my_list.sort(reverse=True)
print(my_list)


# In[1]:


marks = [80, 75, 90, 85]

total = 0
for m in marks:
    total += m
avg = total / len(marks)
print(f"Average Marks: {avg}")


# In[3]:


matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])


# In[4]:


mat = [[1, 2, 3], [4, 5, 6]]
for row in mat:
    for col in row:
        print(col, end="")
    print()


# In[6]:


nums = [12, 5, 18, 7, 80]
max_val = nums[0]
for n in nums:
    if n > max_val:
        max_val = n
print(f"Maximum: {max_val}")


# In[7]:


grades = [85, 70, 90, 65]
passed = 0
for g in grades:
    if g >= 70:
        passed += 1
print(f"Passed students: {passed}")


# In[11]:


names = ["Ali", "Sara", "John"]
search = str(input("Search for a name: "))
found = False
for n in names:
    if n == search:
        found = True
        break
print(len(names[2]))
if found:
    print(f"Name {n} found in the the list!")
else:
    print(f"Name {search} not found in the list.")


# In[13]:


numbah = [2, 4, 6, 8]
for i in range(len(numbah)):
    nums[1] += 2
print(f"Updated list: {numbah}")


# In[17]:


grades = [90, 90, 85, 75, 70]
total = 0
passed = 0
for g in grades:
    total += g
    if g >= 80:
        passed += 1
avg = total / len(grades)
print(f"The average is {avg}.")
print(f"There are a total of {passed} passed students.")


# In[ ]:




