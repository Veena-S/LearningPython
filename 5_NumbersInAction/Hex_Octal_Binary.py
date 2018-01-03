####### Hex, Octal and Binary: Literals and Conversions

# Octal literals: base 8, digits 0 - 7
0o1,  0o20,  0o377
# Result: (1, 16, 255)

# Hex literals: base 16, digits 0 - 9, A - F
0x01,  0x10,  0xFF
# Result: (1, 16, 255)


# Binary literals: base 2, digits 0 - 1
0b1,   0b10000,   0b11111111
# Result: (1, 16, 255)

# Here, the octal value 0o377, the hex value 0xFF, and the binary value 0b11111111 are all decimal 255.
# The F digits in the hex value, for example, each mean 15 in decimal and a
# 4-bit 1111 in binary, and reflect powers of 16. 
# Thus, the hex value 0xFF and others convert to decimal values as follows:

0xFF, ( 15 * ( 16 ** 1 )) + ( 15 * ( 16 ** 0 ))
# Result: (255, 255)

0x2F, ( 2 * ( 16 ** 1 )) + ( 15 * ( 16 ** 0 ))
# Result: (47, 47)

0xF, 0b1111, (( 1 * ( 2 ** 3 )) + ( 1 * ( 2 ** 2 )) + ( 1 * ( 2 ** 1 )) + ( 1 * ( 2 ** 0 )))
# Result: (15, 15, 15)

0o1,  0o20,  0o377
# Result: (1, 16, 255)

0o1, ( 1 * ( 8 ** 0 ))
# Result: (1, 1)

0o20, (( 2 * ( 8 ** 1 )) + ( 0 * ( 8 ** 0 )))
# Result: (16, 16)

0o377, (( 3 * ( 8 ** 2 )) + ( 7 * ( 8 ** 1 )) + ( 7 * ( 8 ** 0 )))
# Result: (255, 255)

# Python prints integer values in decimal (base 10) by default,
# but provides built-in functions that allow you to convert integers to 
# other bases’ digit strings, in Python-literal form

oct(64), hex(64), bin(64)
# Result:	('0o100', '0x40', '0b1000000')

# To go the other way, the built-in int function converts a string of 
# digits to an integer, and an optional second argument lets you specify 
# the numeric base

64, 0o100, 0x40, 0b1000000 # Digits=>numbers in scripts and strings 
# Reslut:	(64, 64, 64, 64)

int('64'), int('100', 8), int('40', 16), int('1000000', 2)	
# Result:	(64, 64, 64, 64)

int('0x40', 16), int('0b1000000', 2) # Literal forms supported too	
# Result:	(64, 64)
 

# The eval function, treats strings as though they were Python code.
eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000') 
# Result:	(64, 64, 64, 64)

# Finally, integers can be converted to base-specific strings with string formatting
# method calls and expressions, which return just digits, not Python literal strings
# Numbers ==> digits
'{0:o}, {1:x}, {2:b}'.format(64, 64, 64)
# Result:	'100, 40, 1000000'
 
'%o, %x, %x, %X' % (64, 64, 255, 255 )
# Result:	'100, 40, ff, FF'


# These literals can generate arbitrarily long integers
X = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF
X	
# Result:	5192296858534827628530496329220095

oct( X ) 	
# Result:		'0o17777777777777777777777777777777777777'

bin( X )	
# Result:	'0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
