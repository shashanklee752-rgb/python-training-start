import pandas as pd
employee_ages = pd.Series([25, 30, 22, 35, 28], 
                          index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'])

print(employee_ages)
print(f"Index: {employee_ages.index}")
print(f"Values: {employee_ages.values}")
print(f"Dtype: {employee_ages.dtype}")
data = { 
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], 
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT'], 
    'Salary': [60000, 75000, 62000, 80000, 70000] 
} 

employee_data_df = pd.DataFrame(data)
print(employee_data_df)

