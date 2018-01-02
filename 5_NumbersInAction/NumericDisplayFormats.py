#### NUMERIC DISPLAY FORMATS - Showing ways to display the numeric values ###

# Auto-echoes
num
# Result: 0.3333333333333333

# Print explicitly
print(num)
# Result: 0.3333333333333333

# String formatting expression
'%e' % num
# Result: '3.333333e-01'
# Alternative floating-point format
'%4.2f' % num
# Result: '0.33'
