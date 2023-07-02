""" Write a function that takes a list of numbers as input and 
returns a new list containing only the even numbers from the input list. 
Use list comprehension to solve this problem.

Example:

Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Output: [2, 4, 6, 8, 10]
"""
Input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

output = [i for i in Input if i % 2 == 0]
    
print(output)

