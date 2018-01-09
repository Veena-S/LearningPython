#####   FRACTION TYPE   

##Fraction implements a rational number object. It keeps both a
##numerator and a denominator explicitly, so as to avoid some of the
##inaccuracies and limitations of floating-point math.

######## Fraction Basics

## Fraction resides in a module, import its constructor and pass in a
## numerator and a denominator to make one.


from fractions import Fraction
# Construct one, by passing numerator and denominator
x = Fraction( 1, 3 )
# Following one will be simplified to 2, 3 by gcd
y = Fraction(4, 6 )

x
# Result: Fraction(1, 3)
y
# Result: Fraction(2, 3)
print( y )
# Result: 2/3

# Once created, fractions can be used in mathematical
# expressions as usual
# Results are exact: numerator, denominator
 
x + y
# Result: Fraction(1, 1)
x - y
# Result: Fraction(-1, 3)
x * y
# Result: Fraction(2, 9)
 
# Fraction objects can also be created from floating-point number strings
Fraction( '0.25' )
# Result: Fraction(1, 4)
Fraction( '1.25' )
# Result: Fraction(5, 4)
Fraction( '.25' ) + Fraction( '1.25' )
# Result: Fraction(3, 2)


#### Numeric accuracy in fractions and decimals
# Only as accurate as floating-point hardware
# Can lose precision over many calculations
a = 1 / 3.0
b = 4 / 6.0
a
# Result:   0.3333333333333333
b
# Result:   0.6666666666666666

a + b
# Result:   1.0
a - b
# Result:   -0.3333333333333333
a * b
# Result:   0.2222222222222222

# This floating point limitation is especially apparent for
# Values that cannot be represented accurately given their
# limited number of bits in memory.
# Both Fraction and Decimal provide ways to get exact results.
 
# The result of following operations should be zero
# ( close, but not exact )
0.1 + 0.1 + 0.1 - 0.3
# Result:   5.551115123125783e-17

from fractions import Fraction
Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)
# Result:   Fraction(0, 1)

from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Result:   Decimal('0.0')

# Fractions and decimals both allow more intuitive and accurate
# results than floating points sometimes can, by different ways -
# by using rational representation and by limiting precision.

1 / 3 	# Use a ".0" in Python 2.X for true "/"
# Result:   0.3333333333333333
# Numeric accuracy, two ways
Fraction(1, 3)
# Result:   Fraction(1, 3)

import decimal
decimal.getcontext().prec = 2
Decimal( 1 ) / Decimal( 3 )
# Result:   Decimal('0.33')

# Fractions both retain accuracy and automatically simplify results.
(1 / 3) + (6 / 12)	# Use a ".0" in Python 2.X for true "/"
# Result:   0.8333333333333333

# Automatically simplified
Fraction( 6, 12)
# Result:   Fraction(1, 2)
Fraction(1, 3) + Fraction(6, 12 )
# Result:   Fraction(5, 6)

decimal.Decimal( str(1 / 3)) + decimal.Decimal( str( 6 / 12))
# Result:   Decimal('0.83')

1000.0 / 1234567890
# Result:   8.100000073710001e-07
Fraction( 1000, 1234567890)
# Result:   Fraction(100, 123456789)

### Fraction conversions and Mixed Types
# To support fraction conversions, floating-point objects have a
# method that yeilds their numeratir and denominator ratio,
# fractions have a "from_float" method, and float accepts
# a Fraction as an argument.

# float object method
(2.5).as_integer_ratio()
# Result:   (5, 2)

f = 2.5
# Convert float -> fraction: two args
z = Fraction( *f.as_integer_ratio())
z
# Result:   Fraction(5, 2)

x
# Result:   Fraction(1, 3)
# 5/2 + 1/3 = 15/6 + 2/6
x + z
# Result:   Fraction(17, 6)
# Convert fraction -> float
float( x )
# Result:   0.3333333333333333
float( z )
# Result:   2.5
float( x + z )
# Result:   2.8333333333333335
17 / 6
# Result:   2.8333333333333335

# Convert float -> fraction: other way
Fraction.from_float( 1.75 )
# Result:   Fraction(7, 4)
Fraction( *(1.75).as_integer_ratio())
# Result:   Fraction(7, 4)

# Samples of type mixing
x
# Result:   Fraction(1, 3)
# Fraction + int => Fraction
x + 2
# Result:   Fraction(7, 3)
# Fraction + float => float
x + 2.0
# Result:   2.3333333333333335
x + (1./3)
# Result:   0.6666666666666666
x + (4./3)
# Result:   1.6666666666666665
# Fraction + Fraction => Fraction
x + Fraction(4, 3)
# Result:   Fraction(5, 3)

# Although conversion is possible from floating-point to fraction,
# in some cases there is an unavoidable precision loss when it is
# done so, because the number is inaccurate in its original floating-
# point form.
# When needed, such results can be simplified by
# limiting maximum denominator value:
4.0 / 3
# Result:   1.3333333333333333
# Precision loss from float
( 4.0 / 3 ).as_integer_ratio()
# Result:   (6004799503160661, 4503599627370496)
x
# Result:   Fraction(1, 3)
a = x + Fraction(*(4.0 / 3 ).as_integer_ratio())
a
# Result:   Fraction(22517998136852479, 13510798882111488)
# 5 / 3 or close to it
22517998136852479 / 13510798882111488.
# Result:   1.6666666666666667
# Simplify to closest fraction
a.limit_denominator( 10 )
# Result:   Fraction(5, 3)
