########## BITWISE OPERATIONS	##############

# 1 decimal is 0001 in bits
x = 1

# Shift left x by 2 bits: 0001 becomes 0100
x << 2
# Result: 4

# Bitwise OR (either bit = 1): ( 0001 | 0010 = 0011 )
x | 2
# Result: 3


# Bitwise AND (both bits = 1) : ( 0001 & 0001 = 0001 )
x & 1
# Result: 1


# The binary and hexadecimal number support in Python allow us to code
# and inspect numbers by bit-strings

# Binary literals
X = 0b0001

# Shift left
X << 2
# Result:   4

# Binary digits string
bin( X << 2 )
# Result:   '0b100'

# Bitwise OR
bin( X | 0b010 )
# Result: '0b11'

# Bitwise AND
bin( X & 0b1 )
# Result: '0b1'


# HEX Literals
X = 0xFF

bin( X )
# Result:   '0b11111111'

# Bitwise XOR: either, but not both
X ^ 0b10101010
# Result:   85

bin( X ^ 0b10101010 )
# Result:   '0b1010101'

# Digits ==> Number: string to int per base
int( '01010101', 2)
# Result:   85

# Number ==> digits: Hex digit string
hex( 85 )
# Result:   '0x55'


### Python 3.1 and 2.7 introduced a new integer bit_length method, which
### allows you to query the number of bits required to represent a
### number’s value in binary. You can often achieve the same effect by
### subtracting 2 from the length of the bin string using the len
### built-in function

X = 99

bin( X ), X.bit_length(),  len( bin( X )) - 2
# Result:   ('0b1100011', 7, 7)

bin( 256 ), (256).bit_length(), len( bin( 256 )) - 2
# Result:   ('0b100000000', 9, 9)

