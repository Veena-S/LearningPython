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
