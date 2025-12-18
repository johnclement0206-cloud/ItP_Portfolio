#!/usr/bin/env python
# coding: utf-8

# In[16]:


def first_word(text: str) -> str:
    text = text.replace('.', '').replace(',','')
    text.split()
    return text[0]

print(first_word("Hello world"))


# In[25]:


def greet():
    print("Welcome!")

greet()


# In[28]:


def add_numbers(a: int, b: int) -> int:
    print("Sum =", a + b)

add_numbers(10, 20)


# In[31]:


def cal_discount(price: int, discount: int) -> int:
    final_price = price - (price * discount / 100)
    return final_price

print(cal_discount(250, 10))
print(cal_discount(40, 30))


# In[35]:


from datetime import date

def days_diff(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return abs((date(*a)-date(*b)).days)

print(days_diff((1945, 9, 2), (2003, 7, 7)))


# In[37]:


def c_to_f(c):
    return (c * 9/5) + 32

print(c_to_f(20))


# In[41]:


def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(1, 2, 3))


# In[43]:


def check_password(password: str) -> str:
    if len(password) < 8:
        return "Weak"
    if not any(char.isdigit() for char in password):
        return "Weak"
    return "Strong"

print(check_password("banana43455"))


# In[45]:


def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Ali")


# In[46]:


def student_info():
    name = "Ahmed"
    age = 20
    return name, age

n, a = student_info()
print(n, a)


# In[47]:


def calculate_bill(qty, price):
    total = qty * price
    tax = total * 0.15
    return total + tax
print(calculate_bill(5, 12))


# In[49]:


import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = math.isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(67))


# In[54]:


import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = math.isqrt(n)
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(67))


# In[48]:


def bonus_salary(salary: int) -> int:
    bonus = (salary * 0.30)
    return salary + bonus

print(bonus_salary(5000))


# In[50]:


def vowel_count(text: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(vowel_count("banana"))


# In[55]:


def delivery_charge(distance_km):
    base_fee = 5
    per_km_rate = 1.2
    return base_fee + (distance_km * per_km_rate)

print(delivery_charge(7.5))


# In[58]:


def valid_mobile(num:str) -> bool:
    return len(num) == 10 and num.isdigit()

print(valid_mobile("4456664664"))


# In[59]:


def taxi_fare(km: int) -> int:
    base_fare = 3
    per_km = 2.5
    return base_fare + (km * per_km)

taxi_fare(12)


# In[60]:


def loan_payment(amount: int, months: int) -> int:
    return amount / months

loan_payment(600000, 12)


# In[62]:


def is_low_stock(stock: int) -> bool:
    return stock < 10

is_low_stock(6)


# In[68]:


def internet_bill(gb: int) -> int:
    return gb * 2

internet_bill(30)


# In[67]:


def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email

is_valid_email("johnclement0206@gmail.com")


# In[77]:


import random

def order_id(name: str) -> str:
    return name[:3].upper() + str(random.randint(1, 999))

order_id("John")


# In[81]:


def parking_fee(hours: int) -> int:
    return hours * 3
    
parking_fee(5)


# In[ ]:




