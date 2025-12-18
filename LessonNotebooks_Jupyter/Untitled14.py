#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

employees = [
    {"id": 101, "name": "John Doe", "role": "Cashier", "salary": 2500},
    {"id": 102, "name": "Aisha Khan", "role": "Manager", "salary": 4500},
    {"id": 103, "name": "Bilal Ahmed", "role": "Storekeeper", "salary": 3000},
]

def add_employee():
    if employees:
        next_id = max(employee['id'] for employee in employees) + 1
    else:
        next_id = 101  # starting ID if no employees exist
    
    name = input("Enter employee name: ")
    role = input("Enter employee role: ")
    salary = float(input("Enter employee salary: "))
    
    new_employee = {
        "id": next_id,
        "name": name,
        "role": role,
        "salary": salary
    }
    
    employees.append(new_employee)
    print(f"Employee added successfully! ID: {next_id}")
    return new_employee

print("Existing Employees:")
for employee in employees:
    print(f"{employee['name']}, {employee['role']}, {employee['salary']}") 
    
def calculate_total_salary():
    total = sum(employee['salary'] for employee in employees)
    print(f"Total salary of staff: {total} USD")

calculate_total_salary()

salaries = np.array([e['salary'] for e in employees])
avg_numpy = np.mean(salaries)
print(f"Average salary: {avg_numpy:.2f} USD")

print("\n--- Add New Employees ---")
while True:
    add_more = input("\nWould you like to add a new employee? (yes/no): ").lower()
    if add_more in ['yes', 'y']:
        add_employee()
    else:
        break

print("\n--- Updated Employee List ---")
for employee in employees:
    print(f"ID: {employee['id']}, {employee['name']}, {employee['role']}, {employee['salary']}")

calculate_total_salary()
salaries = np.array([e['salary'] for e in employees])
avg_numpy = np.mean(salaries)
print(f"Updated average salary: {avg_numpy:.2f} USD")


# In[ ]:




