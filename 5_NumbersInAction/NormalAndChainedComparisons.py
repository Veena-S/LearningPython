##### COMPARISONS: Normal and Chained

# Normal Comparisons - compare the relative magnitudes of their operands and return a Boolean result.
# Less than operation
1 < 2
#Result: True
# Greater than or equal: mixed-type 1 converted to 1.0
2.0 >= 1
#Result: True
# Equal Value
2.0 == 2.0
#Result: True
2.0 == 2
#Result: True
# Not equal value
2.0 != 2.0
#Result: False


# Multiple comparisons can be chained together to perform range tests
# Chained comparisons are a sort of shorthand for larger Boolean expressions
X = 2
Y = 4
Z = 6
#Chained Comparisons: range test
# Check whether Y is in between X and Z ( which is equivalent to the Boolean test: X < Y and Y < Z )
X < Y < Z
#Result: True
X < Y and Y < Z
#Result: True
# Arbitrary chain lengths are allowed.
X < Y > Z
#Result: False
X < Y and Y > Z
#Result: False
X < 6 <= Z
#Result: True
X <= 6 <= Z
#Result: True
1 < 2 < 3.0 < 4
#Result: True
1 > 2 > 3.0 > 4
#Result: False


# In chained tests, the resulting expressions can become nonintuitive
# unless you evaluate them the way the Python does.
# For e.g:, the following is false, just because 1 != 2 (order of precedence)
1 == 2 < 3	# Same as 1 == 2 and 2 < 3
#Result:- False		# Not same as: False < 3 (which means 0 < 3, which is true!!)

# Similarly floating point numbers may not work as we usually expect
1.1 + 2.2 == 3.3
#Result: False
1.1 + 2.2
#Result: 3.3000000000000003	# Close to 3.3, not exactly; limited precision
int( 1.1 + 2.2 ) == int( 3.3 )
#Result: True			# OK if convert. Also can use round, floor, trunc

## This stems from the fact that floating-point numbers cannot represent some values exactly due to their limited number of bits.
