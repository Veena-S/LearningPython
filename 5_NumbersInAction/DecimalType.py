###### 	DECIMAL TYPE 	###########

##Functionally, decimals are like floating- point numbers, but they have a
##fixed number of decimal points. Hence, decimals are fixed-precision
##floating-point values.

#	~~~~ Decimal Basics ~~~~~~

##floating-point math is less than exact because of the limited space used
##to store values. For example, the following should yield zero, but it
##does not. The result is close to zero, but there are not enough bits to
##be precise here:
    
0.1 + 0.1 + 0.1 - 0.3
# Result:   5.551115123125783e-17

int( 0.1 + 0.1 + 0.1 - 0.3)
# Result:   0


print(0.1 + 0.1 + 0.1 - 0.3)
# Result:   5.551115123125783e-17

##we can make decimal objects by calling the Decimal constructor function
##in the decimal module and passing in strings that have the desired
##number of decimal digits for the resulting object

from decimal import Decimal
Decimal( '0.1' ) + Decimal( '0.1' ) + Decimal( '0.1' ) - Decimal( '0.3' )
# Result:   Decimal('0.0')

Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30')
#Result:    Decimal('0.00')
# Precision of the larget number of decimal digits is adopted in the result.

Decimal( 0.1 ) + Decimal( 0.1 ) + Decimal( 0.1 ) - Decimal( 0.3 )
# Result:   Decimal('2.775557561565156540423631668E-17')


#### Setting decimal precision globally
### A context object in the decimal module allows for specifying
### precision (number of decimal digits ) and rounding modes (down, ceiling etc)
### The precision is applied globally for all decimals created
### in the calling thread:

import decimal
# Default precision
decimal.Decimal( 1 ) / decimal.Decimal( 7 )
# Result:   Decimal('0.1428571428571428571428571429')

# Fixed Precision
decimal.getcontext().prec = 4
decimal.Decimal( 1 ) / decimal.Decimal( 7 )
# Result:   Decimal('0.1429')
Decimal( 0.1 ) + Decimal( 0.1 ) + Decimal( 0.1 ) - Decimal( 0.3 )
# Result:   Decimal('1.110E-17')


1999 + 1.33
# Result:    2000.33
decimal.getcontext().prec  = 2
pay = decimal.Decimal( str( 1999 + 1.33 ))
pay
# Result:   Decimal('2000.33')


########### Decimal Context Manager
### In Python 2.6 and 3.0 and later, it's also possible to reset precision
### temporarily by using the with context manager statement.
### The precision is reset to its original value on statement exit

### After taking a new IDLE

import decimal
decimal.Decimal( '1.00' ) / decimal.Decimal( '3.00' )
# Result:   Decimal('0.3333333333333333333333333333')
with decimal.localcontext() as ctx:
    ctx.prec = 2
    decimal.Decimal( '1.00' ) / decimal.Decimal( '3.00' )

	
#Result: Decimal('0.33')

decimal.Decimal( '1.00' ) / decimal.Decimal( '3.00' )
# Result:   Decimal('0.3333333333333333333333333333')


