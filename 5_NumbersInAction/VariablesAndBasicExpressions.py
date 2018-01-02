
# Code to show basic numeric operations

# Name created: not declared ahead of time
a = 3 	
b = 4

# Variables are replaced with their values whenever they are used
a + 1, a - 1 	# Addition (3 +1), Subtraction( 3 - 1)
# Result:- (4, 2)

b * 3, b / 2 	# Multiplication and division. 
# Result:- (12, 2.0)

b // 2
# Result:- 2

a % 2, b ** 2 	# Modulus and power
# Result:- (1, 16)

2 + 4.0, 2.0 ** b 	# Mixed-type conversions
# Result:- (6.0, 16.0)

# Using a variable that has not yet assigned.
c ** 2
# Result:-
#Traceback (most recent call last):
#  File "<pyshell#46>", line 1, in <module>
#    c ** 2
#NameError: name 'c' is not defined

