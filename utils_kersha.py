"""
Module: utils_kersha

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Kersha Broussard

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
has_international_clients: bool = True 
is_employee_active: bool = True
is_vip_client: bool = False

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
years_in_operation: int = 12

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_client_satisfaction: float = 4.4

# Import the statistics module for calculations
import statistics
# declare a list of strings
# TODO: Add or replace this with your own list  
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence","Web Development","Data Science", "Cybersecurity", "Cloud Computing"  ]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7, 4.5, 4.9]


# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Broussard Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Is Employee Active:          {is_employee_active}
Is VIP Client:               {is_vip_client}
Years in Operation:          {years_in_operation}
Average Client Satisfaction: {average_client_satisfaction:.2f}
Skills Offered:              {", ".join(skills_offered)}
Client Satisfaction Scores:  {client_satisfaction_scores}
Minimum Satisfaction Score:  {min_score}
Maximum Satisfaction Score:  {max_score}
Mean Satisfaction Score:     {mean_score:.2f}
Standard Deviation of Scores: {stdev_score:.2f}
"""

# Print the byline
print(byline)

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
