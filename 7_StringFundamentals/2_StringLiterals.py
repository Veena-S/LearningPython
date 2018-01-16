######  STRING LITERALS
#

# Single quotes
'spa"m'
# Result:   'spa"m'

# Double quotes
"spa'm"
# Result:   "spa'm"

# Triple quotes
'''aaa
aaaa
fff
'''
# Result:   'aaa\naaaa\nfff\n'

"""
eee
q
e
r '''
"""
# Result:   "\neee\nq\ne\nr '''\n"

# Escape Sequences
"s\tp\na\0m"
# Result:   's\tp\na\x00m'

# Raw strings
r"C:\new\test.spm"
# Result:   'C:\\new\\test.spm'

# Byte literals
b'sp\x01am'
# Result:   b'sp\x01am'

# Unicode literals
u'eggs\u0020spam'
# Result:   'eggs spam'



# SINGLE AND DOUBLE QUOTES
# Single and double quoted strings are the same
# Python displays strings in single quotes unless they embed one
# Adding commas between strings would result in a tuple
# Without comma, Python automatically concatenates adjacent string literals

'shrubbery', "shrubbery"
# Result:   ('shrubbery', 'shrubbery')

'knight"s', "knight's"
# Result:   ('knight"s', "knight's")

title = "Meaning" ' of ' "Life"
title
# Result:   'Meaning of Life'

'knight\'s', "knight\"s"
# Result:   ("knight's", 'knight"s')

# ESCAPE SEQUENCES REPRESENT SPECIAL CHARACTERS
#
#
# The interactive echo shows the special characters as
# escapes, but print interprets them instead:
s = 'a\nn\tc'
s
#Result:    'a\nn\tc'
print(s)
#Result:    a
#Result:    n	c

# This string is five characters long: it contains an ASCII a,
# newlinecharacter, an ASCII , and so on.
len(s)
#Result:    5


# Some escape sequences allow to embed absolute binary values
# into the characters of a string
# E.g.: A five character string that embeds two characters
# with binary zero values (coded as octal escapes of one
# digit):

s = 'a\0b\0c'
s
#Result:    'a\x00b\x00c'
len(s)
#Result:    5

# In Python, a zero (null) character like this does not
# terminate a string the way a “null byte” typically does
# in C. Instead, Python keeps both the string’s length and
# text in memory. In fact, no character terminates a string
# in Python. Here’s a string that is all absolute binary
# escape codes - a binary 1 and 2 (coded in octal), followed
# by a binay 3 ( coded in hexadecimal)

s = '\001\002\x03'
s
#Result:    '\x01\x02\x03'
len(s)
#Result:    3


# Python displays non printable characters in hex, regardeless of how
# they were specified. The following string contains the characters
# "spam", a tab and a newline and an absolute zero value character coded
# in hex:
S = "s\tp\na\x00m"
S
#Result:    's\tp\na\x00m'
len(S)
#Result:    7
print(S)
#Result:    s	p
#Result:    a m
print(s)
#Result:    


# if Python does not recognize the character after a \ as being a valid
# escape code, it simply keeps the backslash in the resulting string
x = "C:\py\code"  # keeps \ as such and displays as \\
x
#Result:    'C:\\py\\code'
len(x)
#Result:    10


# \a -> Bell
a = "\a"
a
#Result:    '\x07'
print( a)
#Result:    
a = "A\aB C"
print( a)
#Result:    AB C



##################
# RAW STRINGS SUPPRESS ESCAPES
##################
##If the letter r or R appears just before the opening quote of a string,
##it turns off the escaping mechanism in strings.
myfile = open(r'C:\new\text.dat', 'w')
## Or can use two backslashes
myfile = open('C:\\new\\text.dat', 'w')



######################
### TRIPLE QUOTES CODE MULTILINE BLOCK STRINGS
######################

# Use 1: For coding multi-line text data

mantra = """ Always look
on the bright
side of life"""
mantra
# Result:    ' Always look\non the bright\nside of life'
print( mantra )
# Result:     Always look
# Result:    on the bright
# Result:    side of life

menu = """ spam  # comments here are added to string!
eggs \t		# ditto
"""
menu
# Result:    ' spam  # comments here are added to string!\neggs \t\t\t# ditto\n'
print( menu )
# Result:     spam  # comments here are added to string!
# Result:    eggs 			# ditto

menu = (
	"spam\n" # Comments here ignored
	"eggs\n" # but newlines are not automatic
	)
menu
# Result:    'spam\neggs\n'
print( menu )
# Result:    spam
# Result:    eggs

# Use 2: For documentation strings

# Use 3: To temporarily disable lines of code during development
# Python really might make a string out of the lines of ode disabled
# this way, but this is probably not significant in terms of performance
X = 1
# Below lines will be considered just as a string
"""
import os
print ( os.getcwd())
"""
# Result:   '\nimport os\nprint ( os.getcwd())\n'
Y = 2
