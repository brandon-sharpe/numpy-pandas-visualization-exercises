import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
print()
print(f"The array is {a}")
# How many negative numbers are there?
a_negative = a[a<0]
print(f" There are {len(a[a<0])} negative numbers")
print()

# How many positive numbers are there?
a_positve = a[a>0]
print(f" There are {len(a[a>0])} postive numbers")
print()

# How many even positive numbers are there?
print(f" There are {len(a_positve[a_positve % 2 == 0 ])} positive even numbers. ")
print()

# If you were to add 3 to each data point, how many positive numbers would there be?
a_plus_three = a + 3
print(f" There would be {len(a_plus_three[a_plus_three > 0])} positive numbers if we added 3 to the array ")
print()

# If you squared each number, what would the new mean and standard deviation be?
a_squared = a**2
print(f" The mean of the array if we squared each number would be {a_squared.mean()} and the standard deviation would be {a_squared.std()} ")
print()

# A common statistical operation on a dataset is centering.
#  This means to adjust the data such that the mean of the data is 0.
#  This is done by subtracting the mean from each data point. Center the data set. 
a_center = a - a.mean()
print(f" The center is {a_center}")
print()

# Calculate the z-score for each data point. Recall that the z-score is given by:
from scipy import stats as stats
print(f" The z- score is {stats.zscore(a)}")
print()

# More numpy excercises
print("SETUP #1")
print()
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f" The new array is {a}")
print()
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(f" The sum of a is {sum_of_a}")
print()

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = a.min()
print(f" The minimum of all the numbers in this array is {min_of_a}")
print()

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = a.max()
print(f" The maximum of all the numbers in this array is {max_of_a}")
print()

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = a.mean()
print(f" The mean of all the numbers in this array is {mean_of_a}")
print()

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = a.prod()
print(f" The product of all the numbers in this array is {product_of_a}")
print()

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = a**2
print(f" The square of every number in this array is {squares_of_a}")
print()

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = a[a % 2 != 0]
print(f" This array with only odd numbers looks like {odds_in_a}")
print()

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = a[a % 2 == 0]
print(f" This array with only even numbers looks like {evens_in_a}")
print()
print("SETUP #2")
print()
b = np.array([[ 3, 4, 5],[6, 7, 8]])
print(f" The new array is\n {b}")
print()
#  Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable.
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)
sum_of_b = b.sum()
print(f" The sum of array b is {sum_of_b}")
print()

# Exercise 2 - refactor the following to use numpy. 
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
min_of_b = b.min()
print(f" The minimum number of array b is {min_of_b}")
print()

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b = b.max()
print(f" The maximum number of array b is {max_of_b}")
print()

# Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b = b.mean()
print(f" The mean number of array b is {mean_of_b}")
print()

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number
product_of_b = b.prod()
print(f" The product of all the numbers of array b is {product_of_b}")
print()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)
squares_of_b = b**2
print(f" The squares of all the numbers of array b are \n{squares_of_b}")
print()

# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)
odds_in_b = b[b % 2 != 0]
print(f" All of the odd numbers in array b are \n{odds_in_b}")
print()

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)
evens_in_b = b[b % 2 == 0]
print(f" All of the even numbers in array b are \n{evens_in_b}")
print()

# Exercise 9 - print out the shape of the array b.
print(f" The shape of array b is {b.shape}")
print()

# Exercise 10 - transpose the array b.
print(f" Array b transposed is \n{b.transpose()}")
print()

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print(f" Array b reshaped into one list is \n{b.reshape(1,6)}")
print()

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
print(f" Array b reshaped into six lists is \n{b.reshape(6,1)}")
print()

print("SETUP #3")
print()

c = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(f" The new array is array c \n{c}")
print()

# Exercise 1 - Find the min, max, sum, and product of c.
print(f" The minimum number of array c is {c.min()} the maximum number is {c.max()}\n the sum of array c is {c.sum()}\n the product of all the numbers in array c is {c.prod()} ")
print()

# Exercise 2 - Determine the standard deviation of c.
print(f" The standard deviation of c is {c.std()}")
print()
# Exercise 3 - Determine the variance of c.
print(f" The variance of c is {c.var()}")
print()
# Exercise 4 - Print out the shape of the array c
print(f" The shape of array c is {c.shape}")
print()

# Exercise 5 - Transpose c and print out transposed result.
print(f" Array c transposed is \n{c.transpose()}")
print()

# Exercise 6 - Get the dot product of the array c with c. 
print(f" The dot product of c with c is \n{np.dot(c,c)}")
print()
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
print(f" The sum of the result of c times c transposed is {sum(sum(c*c.transpose()))}")
print()

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
print(f" The product of the result of c times c transposed is {(c*c.transpose()).prod()}")
print()

print("SETUP #4")
print()
d = np.array([[90, 30, 45, 0, 120, 180],[45, -90, -30, 270, 90, 0],[60, 45, -45, 90, -45, 180]])
print(f" The new array is array d \n{d}")
print()

# Exercise 1 - Find the sine of all the numbers in d
print(f" The sine of array d are \n{np.sin(d)}")
print()

# Exercise 2 - Find the cosine of all the numbers in d
print(f" The cosine of array d are \n{np.cos(d)}")
print()

# Exercise 3 - Find the tangent of all the numbers in d
print(f" The tangents of array d are \n{np.tan(d)}")
print()

# Exercise 4 - Find all the negative numbers in d
print(f" The negative numbers of array d are \n{d[d<0]}")
print()

# Exercise 5 - Find all the positive numbers in d
print(f" The positive numbers of array d are \n{d[d>0]}")
print()

# Exercise 6 - Return an array of only the unique numbers in d.
print(f" The unique number of array d are \n{np.unique(d)}")
print()

# Exercise 7 - Determine how many unique numbers there are in d.
print(f" There are {len(np.unique(d))} unique number in array d")
print()

# Exercise 8 - Print out the shape of d.
print(f" The shape of array d is {d.shape}")
print()

# Exercise 9 - Transpose and then print out the shape of d.
print(f" Array d transposed is \n{d.transpose()}")
print()

# Exercise 10 - Reshape d into an array of 9 x 2
print(f" Array d reshaped as 9x2 is \n{d.reshape(9,2)}")
print()