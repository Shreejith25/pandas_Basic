import pandas as pd

# Creating the DataFrame with employee data
data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 80000, 60000, 90000],
    'managerId': [3, 4, None, None]
}

employee_df = pd.DataFrame(data)


# Define a function to find employees with salaries greater than their managers
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    result = []
    # Iterate over each row in the DataFrame
    for index, row in employee.iterrows():
        manager_id = row['managerId']
        # Check if managerId is not NaN
        if pd.notna(manager_id):
            # Get the manager's salary
            manager_salary = employee[employee['id'] == manager_id]['salary'].values[0]
            # Compare employee's salary with manager's salary
            if row['salary'] > manager_salary:
                # Append the employee's name to the result list
                result.append(row['name'])
    
    # Convert the result list to a DataFrame with a column named 'Employee'
    result_df = pd.DataFrame(result, columns=['Employee'])
    return result_df

# Call the function and print the resulting DataFrame
print(find_employees(employee_df))






