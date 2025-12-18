#!/usr/bin/env python
# coding: utf-8

# In[5]:


def add(a, b):
    try:
        return a+b
    except ValueError:
        return "Invalid input."
    finally:
        print("Function is done running.")

add(2,2)


# In[6]:


def changing_direction(elements: list[int]) -> int:
    dirs = []
    for i, j in zip(elements, elements[1:]):
        if j > i and (not dirs or dirs[-1] == '-'):
            dirs.append('+')
        elif j < i and (not dirs or dirs[-1] == '+'):
            dirs.append('-')
    return len(dirs) - bool(dirs)

print(changing_direction([1, 2, 1, 2, 2, 1]))


# In[7]:


def math_ops(a, b):
    return a + b, a - b, a * b

s, d, p = math_ops(10, 2)
print(s)
print(d)
print(p)


# In[8]:


def calculate_total(*prices):
    return sum(prices)

total = calculate_total(10, 20, 5)
print(total)


# In[17]:


def student(name, age):
    return name, age

data1, data2 = student("John", 19)
print(data2)


# In[ ]:


# .upper()
# .lower()
# .isdigit()
# .isnumeric()


# In[22]:


def update_dict(d):
    d["status"] = "active"

user={'name':'Ali'}
update_dict(user)
print(user)


# In[3]:


def add_item(cart: list, item: str) -> list:
    cart.append(item)

shopping_cart = []
while True:
    new_item = str(input("Add your item to cart: "))
    add_item(shopping_cart, new_item)

    print("Would you like to add more items?")
    reset = input("Give y or n: ")

    if reset.lower() == 'y':
        continue
    else:
        break
    
print(f"You have bought {shopping_cart}.")


# In[5]:


def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

tri_recursion(5)


# In[18]:


def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial(10))


# In[5]:


def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))


# In[10]:


def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))


# In[ ]:




