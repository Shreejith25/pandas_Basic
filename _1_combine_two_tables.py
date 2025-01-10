'''175. Combine Two Tables

Write a solution to report the first name, last name, city, and state of each person in the Person table. 
If the address of a personId is not present in the Address table, report null instead.

Return the result table in any order.

'''

import pandas as pd  # Import the pandas library

# Create a dictionary for the Person data
person_data = {
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
}

# Convert the dictionary to a DataFrame
person_df = pd.DataFrame(person_data)

# Create a dictionary for the Address data
address_data = {
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
}

# Convert the dictionary to a DataFrame
address_df = pd.DataFrame(address_data)

# Merge the Person and Address DataFrames on 'personId', keeping all rows from the Person DataFrame
new = pd.merge(person_df, address_df, how='left', left_on='personId', right_on='personId')

# Select and display specific columns from the merged DataFrame
print(new[['firstName','lastName','city','state']])
