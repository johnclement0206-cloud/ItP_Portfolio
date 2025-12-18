#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from typing import Any, List, Iterable, Dict

def add(a: int, b: int) -> int:
    return a+b

print(add(-43, 12432))


# In[16]:


student = {
    "name": "Ali",
    "age":  20,
    "grade": 88.5,
}

print(student["grade"])
print(len(student))


# In[39]:


student = dict(name = "Ali", age = 20, grade = 88.5)

x = student.keys()

print(x)

student["course"] = "Cybersecurity"

print(x)
print(student.values())
print(student.items())

student.update({"grade": 95})
print(student.items())

student.pop("course")
print(student.keys())

student["course"] = "Creative Computing"
print(student.items())

student.popitem()
print(student.keys())

del student["age"]
print(student.keys())

student.clear()
print(student)


# In[61]:


import sys
import time

students = [
    {"name": "John", "age": 19, "grade": 95},
    {"name": "Aisha", "age": 19, "grade": 80},
    {"name": "Ali", "age": 20, "grade": 88}
]

for student in students:
    if student["name"] == "John":
        print(student.values())


# In[65]:


class Student:
    def __init__(self, name, age, grade, course):
        self.name = name
        self.age = age
        self.grade = grade
        self.course = course


s1 = Student("Ali", 20, 80, "Cybersecurity")

print(s1.name)


# In[68]:


class Person:
    pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25
p1.grade = 99

print(p1.age)


# In[90]:


inventory = [
    {"item": "Pen", "price": 2.0, "stock": 60},
    {"item": "Notebook", "price": 5.0, "stock": 45},
    {"item": "Pencil", "price": 1.5, "stock": 110},
]

def display_stock():
    for product in inventory:
        print(f"{product['item']}: {product['stock']} units")
    
    def calculate_total_stock():
        total = sum(product['stock'] for product in inventory)
        print(f"Total stock: {total} units")
    
    calculate_total_stock()
            
display_stock()


# In[21]:


import numpy

employees = [
    {"id": 101, "name": "John Doe", "role": "Cashier", "salary": 2500},
    {"id": 102, "name": "Aisha Khan", "role": "Manager", "salary": 4500},
    {"id": 103, "name": "Bilal Ahmed", "role": "Storekeeper", "salary": 3000},
]

for employee in employees:
    print(f"{employee['name']}, {employee["role"]}, {employee["salary"]}") 
    
    def calculate_total_salary():
        total = sum(employee['salary'] for employee in employees)
        print(f"Total salary of staff: {total} USD")

calculate_total_salary()

salaries = numpy.array([e['salary'] for e in employees])
avg_numpy = numpy.mean(salaries)

print(f"Average salary: {avg_numpy:.2f} USD")

def find_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            emp["salary"] = 2800
            return {emp["id"]}, {emp["name"]}, {emp["role"]}, {emp["salary"]}
    return None
print(find_employee(101))


# In[20]:


filtered = [e for e in employees if e['salary'] >= 3000]
if filtered:
    for e in filtered:
        print(f"{e['name']}, {e['role']}, {e['salary']}")
else:
    print("No employees with salary >= 3000")


# In[26]:


for i in range(len(employees)):
    if employees[1]["id"] == 109:
        del employees[i]
        break
print(employees)


# In[ ]:




