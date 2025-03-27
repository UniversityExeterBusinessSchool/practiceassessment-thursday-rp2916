#######################################################################################################################################################
# 
# Name:
# SID:
# Exam Date:
# Module:
# Github link for this assignment:  
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 
# Write your search code here and provide comments. 
"""
# List of words to search for
comments_type = {
    0: 'satisfactory',
    1: 'impressed',
    2: 'intuitive',
    3: 'usability',
    4: 'constructive',
    5: 'reliable',
    6: 'defect',
    7: 'durability',
    8: 'value',
    9: 'improve'
}
# declaring a variable called customer_feedback which contains a string 
customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""
# creting a empty list called my_list in which the keywords will get stored as the loop in the fuction follows 
my_list = []
# creating a for loop to display the starting and ending position
for key,word in comments_type.items():
    start_pos = customer_feedback.find(word)
    end_pos = start_pos + len(word)
    my_list.append((start_pos, end_pos))

print("Positions where the keywords are stored is :", my_list)
"""
# output
""" Positions where the keywords are stored is : [(38, 50), (-1, 8), (-1, 8), (-1, 8), (-1, 11), (-1, 7), (-1, 5), (-1, 9), (-1, 4), (-1, 6)]"""
##########################################################################################################################################################
"""
# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:74
# Insert last two digits of ID number here:70

# Write your code for Operating Profit Margin
# defining the function for calulating Operating Profit Margin
def opt_profit_marg(net_profit,revenue):
    return (net_profit / revenue) * 100
# Write your code for Revenue per Customer
# defining the function for calulating Revenue per Customer  
def rev_per_cust(total_rev,num_cust):
    return (total_rev/num_cust)
# Write your code for Customer Churn Rate
# defining the function for calulating Customer Churn Rate    
def cust_curn_rate(cust_lost,Total_cust_start):
    return (cust_lost / Total_cust_start) * 100
# Write your code for Average Order Value
# defining the function for calulating Average Order Value    
def Avg_order_value(total_rev,num_order_placed):
    return (total_rev / num_order_placed) 
# Call your designed functions here
# calling the functions to display the required Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value

print(f"Operating profit for net profit of 74 and revenue of 70 is:{opt_profit_marg(74,70)}")
print(f"revenue per customer for total revenue of 74 and number of cust 70 is:{rev_per_cust(74,70)}")
print(f"Customer churn rate with lost cutomer 74 and total customer 70 is:{cust_curn_rate(74,70)}")
print(f"Average order value for total revenue of 74 and number of orders placed 70 is:{Avg_order_value(74,70)}")
# Output 
Operating profit for net profit of 74 and revenue of 70 is:105.71428571428572
revenue per customer for total revenue of 74 and number of cust 70 is:1.0571428571428572
Customer churn rate with lost cutomer 74 and total customer 70 is:105.71428571428572
Average order value for total revenue of 74 and number of orders placed 70 is:1.0571428571428572
"""
##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""
"""
# Write your code here
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# creating array called price and demand 
price = np.array([20,25,30,35,40,45,50,55,60,65,70]).reshape(-1,1)
demand = np.array([300,280,260,240,210,190,160,140,120,100,85])

# Creating a regression model

model = LinearRegression()
model.fit(price,demand)
# predicting the optimal price of the product 
optimal_price = -model.predict([[0]]) / model.coef_[0]  # Predict demand for price 0 and then calculate optimal price. #([[0]]) to reshape into 2D array.
print("Optimal price: £",optimal_price[0])

# creating a predition model for forcasting the demand based on the price

predict_demand = model.predict([[52]])
print(f"The Predicted demand based on the price of the product is: {predict_demand[0]:.2f} ")# calling the function 
# plotting graphs 
plt.plot(price,model.predict(price),color = "Red")
plt.scatter(price,demand,color = "Black")
plt.xlabel("Price £")
plt.ylabel("Demand")
plt.title("Price vs Demand")
plt.show()

Output :
Optimal price: £ 87.2920892494929
The Predicted demand based on the price of the product is: 158.17 
"""
##########################################################################################################################################################
"""
# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max-value = integer(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
plt.title(Line Chart of 100 Random Numbers)
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()

output :
correct code:

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
max_value = int(input("Enter your Student ID: "))
random_numbers = [random.randint(1, max_value) for i in range(0,100)]
# Error: `max_value` is not defined (due to incorrect variable name above)
# Plotting the numbers in a line chart
plt.plot(random_numbers, marker='*', markerfacecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')# Errors: 
# - `marker='O'` should be `marker='*'` (uppercase 'O' is not a standard marker, lowercase 'o' is valid)  
# - `markercolor` is invalid, should be `markerfacecolor`  
# - `markeredgcolor` has a typo, should be `markeredgecolor`  
# - `lable` is a typo, should be `label`  
# - Semicolon (`;`) at the end is unnecessary (not an error but unconventional in Python plotting)

plt.title("Line Chart of 100 Random Numbers")# Error: Missing quotes around the string (should be `plt.title("Line Chart of 100 Random Numbers")`)
plt.xlabel=("Index")# Error: Should be plt.xlabel("Index") (function call missing parentheses)
plt.ylabel=("Random Number") Error: Should be plt.ylabel("Random Number") (function call missing parentheses)
plt.legend()# Error: Invalid argument for legend, should be plt.legend() or with proper labels
plt.grid(True)
plt.show()


    
"""


