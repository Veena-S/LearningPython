##      STRINGS IN ACTION   ####

########
# BASIC OPERATIONS
########

# Concatenate string using + operator
len( 'abc' )
# Result:   3
'abc' + 'def'
# Result:   'abcdef'


# Repeat string using *
'Nil!' * 4
# Result:   'Nil!Nil!Nil!Nil!'
print('-' * 80 )
# Result:   --------------------------------------------------------------------------------

# "in" operator
# Can use for loops also to iterate over strings
# which repeat actions and test membership for both characters and substrings with the 'in' expression operator, which is essentially a search
myJob = "hacker"
# Step through items, print each
for c in myJob: print( c, end=' ')

# Result:   h a c k e r 
# Search
"k" in myJob
# Result:   True
"z" in myJob
# Result:   False
# Substring search, no position returned. Boolean is returned.
'spam' in 'abcspamdef'
# Result:   True



########
# INDEXING & SLICING / EXTENDED SLICING
########

S = 'spam'
# Indexing from front
S[0]
# Result:   's'
# Indexing from end
S[-2]
# Result:   'a'
# Slicing: extract a section
S[1:3]
# Result:   'pa'
S[:-1] # length + (-1)
# Result:   'spa'
S[1:]
# Result:   'pam'
S[:]
# Result:   'spam'

### Extended slicing S[i : j : k],
### where k is a step / stride which defaults to +1
S = "abcdefghijklmop"
len(S)
15
S[:15]
# Result:   'abcdefghijklmop'
S[0:]
# Result:   'abcdefghijklmop'
S[::2]
# Result:   'acegikmp'
S[::5]
# Result:   'afk'
S[1:10:2]
# Result:   'bdfhj'
S[0:10:2]
# Result:   'acegi'

# Can use negative stride to collect items in the
# opposite order
S[::-1]
# Result:   'pomlkjihgfedcba'
S[::1]
# Result:   'abcdefghijklmop'
S[::-5]
# Result:   'pje'
S[0:10:-2]
# Result:  ''

# With a negative stride, the meaning of first two
# bounds are also reversed.
# i.e. S[i:j:k] means, fetch items from (j+1) to i,
# in reverse order ( i inclusive, j exclusive) i > j
S[10:0:-2]
# Result:   'kigec'
S[9:0:-2]
# Result:   'jhfdb'
S[10:1:-2]
# Result:   'kigec'
S[10:3:-2]
# Result:   'kige'
S[10:2:-2]
# Result:   'kige'
S[5:1:-1]
# Result:   'fedc'


# Slicing is equivalent to indexing with a slice object
#Slicing syntax
'spam'[1:3]
# Result:   'pa'
# Slice objects with index syntax + object
'spam'[slice(1, 3)]
# Result:   'pa'
'spam'[::-1]
# Result:   'maps'
'spam'[slice(None, None, -1)]
# Result:   'maps'


S = "0123456789"
S
# Result:   '0123456789'
len(S)
# Result:   10
S[0:10]
# Result:   '0123456789'
S[0:9]
# Result:   '012345678'
S[0:10:2]
# Result:   '02468'
S[0:10:1]
# Result:   '0123456789'
S[0:10:-1]
# Result:   ''
S[10:0:-1]
# Result:   '987654321'
S[9:0:-1]
# Result:   '987654321'
S[8:0:-1]
# Result:   '87654321'
S[10:-1:-1]
# Result:   ''
S[10::-1]
# Result:   '9876543210'


########
# STRING CONVERSION TOOLS
########

# Convert from a string
int("42")
# Result:   42
# Convert to string
str(42)
# Result:   '42'
a = '42'
int(a)
# Result:   42
# Convert to as-code string
repr(42)
# Result:   '42'

# the repr converts an object to its string
# representation, but returns the object as a string
# of code that can be rerun to recreate the object
str('spam'), repr('spam')
# Result:   ('spam', "'spam'")
print( str('spam'), repr('spam'))
# Result:   spam 'spam'
repr( "spam" )
# Result:   "'spam'"

S = "42"
I = 1
S + I
# Result:   TypeError: must be str, not int
int(S) + I
# Result:   43
S + str(I)
# Result:   '421'

str( 3.1415), float("1.5")
# Result:   ('3.1415', 1.5)
text = "1.234E-10"
float(text)
# Result:   1.234e-10


### Character Code Conversions
### --------------------------
# To get the actual binary value of a single character.
ord( 's' )
# Result:   115
# To convert an integer code to its corresponding character
chr( 115 )
# Result:   's'
# Both of these functions convert characters to and from their Unicode ordinals or "code points".
S = "5"
S = chr( ord( S ) + 1 )
S
# Result:   '6'
S = chr( ord( S ) + 1 )
S
# Result:   '7'
ord(S)
# Result:   55
chr(55)
# Result:   '7'


ord( '5' )
# Result:   53
int( '5' )
# Result:   5
ord( '5' ) - ord( '0' )
# Result:   5
ord( '0' )
# Result:   48
chr( 224 )
# Result:   'à'
chr( 223 )
# Result:   'ß'
chr( 229 )
# Result:   'å'

# Convert binary digits to integer with ord
B = '1101'
B
# Result:   '1101'
I = 0
while B != '':
	I = I * 2 + ( ord(B[0]) - ord( '0'))
	B = B[1:]

	
I
# Result:   13

B
# Result:   ''
B = '1101'
B[0]
# Result:   '1'
ord(B[0])
# Result:   49
ord('0')
# Result:   48
I = 0
B = '1101'
while B != '':
	print( 'B: ', B)
	print( 'I: ', I )
	print( 'B[0]: ', B[0])
	I = I * 2 + ( ord( B[0]) - ord( '0'))
	print('I: ', I)
	B = B[1:]

	
# Result:   B:  1101
# Result:   I:  0
# Result:   B[0]:  1
# Result:   I:  1
# Result:   B:  101
# Result:   I:  1
# Result:   B[0]:  1
# Result:   I:  3
# Result:   B:  01
# Result:   I:  3
# Result:   B[0]:  0
# Result:   I:  6
# Result:   B:  1
# Result:   I:  6
# Result:   B[0]:  1
# Result:   I:  13

# Convert binary to integer: built-in
int( '1101', 2)
# Result:   13
# Convert integer to binary: built-in
bin( 13 )
# Result:   '0b1101'

# Convert binary digits to integer using left shift operation
B = '1101'
I = 0
while B != '':
	I = ( I << 1 ) + ( ord( B[0]) - ord( '0'))
	B = B[1:]

	
I
# Result:   13


## Changing Strings
S = 'spam'
S[0] = 'x'
# Result:   TypeError: 'str' object does not support item assignment
S = S  + 'SPAM!' # Makes a new string
S
# Result:   'spamSPAM!'
S = S[:4] + 'Burger' + S[-1]
S
# Result:   'spamBurger!'
S[-1]
# Result:   '!'
S = 'splot'
S = S.replace( 'pl', 'pamal')
S
# Result:   'spamalot'

# Formatting
'That is %d %s bird!' % (1, 'dead' )
# Result:   'That is 1 dead bird!'
'That is {0} {1} bird!'.format(1, 'dead' )
# Result:   'That is 1 dead bird!'

