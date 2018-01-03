########## DIVISION ##################
# X / Y ==> true division in 3.X and classic division in 2.X
# X // Y ==> performs floor division in both 2.X and 3.X

5/2
# Result: 2.5
a = 5
b = 3
a / b
# Result: 1.6666666666666667
a // b
# Result: 1

10 / 4 		# In 3.X: keeps remainder i.e. returns float, In 2.X, result is 2
# Result: 2.5

10 / 4.0 	# In 3.X: keeps remainder. In 2.X also.
# Result: 2.5

10 // 4 	# Same in 3.X & 2.X: truncates remainder
# Result: 2

10 // 4.0 	# Same in 3.X & 2.X: truncates to floor
# Result: 2.0

# Floor versus truncation
# the // operator is informally called truncating division, but it’s more
# accurate to refer to it as floor division—it truncates the result down to
# its floor, which means the closest whole number below the true result.

5 / 2, 5 / -2
# Result:	(2.5, -2.5)

5 // 2, 5 // -2
# Result:	(2, -3)

5 / 2.0, 5 / -2.0
# Result:	(2.5, -2.5)

5 // 2.0, 5 // -2.0
# Result:	(2.0, -3.0)


# If you really want truncation toward zero regardless of sign, you can always 
# run a float division result through math.trunc, regardless of Python version

import math
5 / -2
# Result:	-2.5

5 // -2
# Result:	-3

math.trunc( 5 / -2 )
# Result:	-2


### SUMMARY

# ************ In 3.X
# True division
(5 / 2), (5 / 2.0), (5 / -2.0), (5 / -2)
# Result:	(2.5, 2.5, -2.5, -2.5)

# Floor division
(5 // 2), (5 // 2.0), (5 // -2.0), (5 // -2)
#Result:	(2, 2.0, -3.0, -3)

# Both
( 9 / 3), (9.0 / 3), (9 // 3 ), ( 9 // 3.0 )
# Result:	(3.0, 3.0, 3, 3.0)

# ********* In 2.X
# 2.X classic division (differs)
(5 / 2), (5 / 2.0), (5 / −2.0), (5 / −2) 
# Result:	(2, 2.5, −2.5, −3)

# 2.X floor division (same)
(5 // 2), (5 // 2.0), (5 // −2.0), (5 // −2)
# Result:	(2, 2.0, −3.0, −3)

# Both
(9 / 3), (9.0 / 3), (9 // 3), (9 // 3.0) 
# Result:	(3, 3.0, 3, 3.0)
 
