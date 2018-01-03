##In addition to its core object types, Python also provides both
##built-in functions and standard library modules for numeric
##processing.

import math

# Common constants
math.pi, math.e
# Result:   (3.141592653589793, 2.718281828459045)

# Sine, tangent and cosine
math.sin( 2 * math.pi / 180 )
# Result:   0.03489949670250097

# Square root
math.sqrt( 144 ), math.sqrt( 2 )
# Result:   (12.0, 1.4142135623730951)

# Exponentiation (power)
pow( 2, 4), 2 ** 4, 2.0 ** 4.0
# Result:   (16, 16, 16.0)

# Absolute value, summation
abs( -42.0 ), sum((1, 2, 3, 4 ))
# Result:   (42.0, 10)

# Minimum, maximum
min( 3, 1, 2, 4), max(3, 1, 4, 2)
# Result:   (1, 4)


# Floor(next-lower integer)
math.floor( 2.567 ), math.floor( -2.567 )
# Result: (2, -3)

# Truncate ( drop decimal digits )
math.trunc( 2.567 ), math.trunc( -2.567 )
# Result: (2, -2)

# Truncate (using integer conversion)
int( 2.567 ), int( -2.567 )
# Result: (2, -2)

# Round
round(2.567), round(2.467), round(2.567, 2)
# Result:   (3, 2, 2.57)

## round rounds and drops decimal digits but still produces a
## floating-point number in memory, whereas string formatting produces a
## string, not a number:
# Round for display
'%.1f' % 2.567, '{0:.2f}'.format( 2.567 )
# Result:   ('2.6', '2.57')

( 1 / 3.0 ), round( 1 / 3.0, 2 ), ('%.2f' % (1 / 3.0 ))
# Result:   (0.3333333333333333, 0.33, '0.33')

## there are three ways to compute square roots in Python: using a module
## function, an expression, or a built-in function

import math
# Module
math.sqrt( 144 )
# Result:   12.0

# Expression
144 ** .5
# Result:   12.0

# Built-in
pow(144, .5 )
# Result:   12.0

# For larger numbers
math.sqrt( 1234567890 )
# Result:   35136.41828644462

1234567890 ** .5
# Result:   35136.41828644462

pow( 1234567890, .5 )
# Result:   35136.41828644462



## The standard library modules such as math must be imported, but
## built-in functions such as abs and round are always available without
## imports. In other words, modules are external components, but built-in
## functions live in an implied namespace that Python automatically
## searches to find names used in your program. This namespace simply
## corresponds to the standard library module called builtins in Python
## 3.X


## The standard library random module must be imported as well. This
## module provides an array of tools, for tasks such as picking a random
## floating-point number between 0 and 1, and selecting a random integer
## between two numbers:
import random
random.random()
# Result:   0.8021456360516563

# Random floats, integers, choices, shuffles
random.random()
# Result:   0.46836729420790235

random.randint( 1, 10)
# Result:   6

random.randint( 1, 10)
# Result:   10


##This module can also choose an item at random from a sequence, and
##shuffle a list of items randomly:

random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life'])
# Resule:   'Holy Grail'

random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life'])
# Resule:   'Meaning of Life'

suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)
suits
# Resule:   ['clubs', 'diamonds', 'spades', 'hearts']

random.shuffle(suits)
suits
# Resule:   ['hearts', 'diamonds', 'spades', 'clubs']


