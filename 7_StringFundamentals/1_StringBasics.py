#### Python strings are categorized as immutable sequences, meaning that
#### the characters they contain have a left-to-right positional order
#### and that they cannot be changed in place.

## Common literals and operations
# Empty String
S = ""
S
# Resule:   ''
S = ''
S
# Resule:   ''
# Double quotes, same as single
S = "spam's"
S
# Resule:   "spam's"
S = 'spam''s'
S
# Resule:   'spams'
S = 'spam'"'"'s'
S
# Resule:   "spam's"

# Esacpe sequences
S = 's\np\ta\x00m'
S
# Resule:   's\np\ta\x00m'

# Triple quoted block strings
S = """aaaaaaaaaabbbbbbbbbbbbbbbbbbbccccccccdsssdsdsjhjhjshdaj"""
S
# Resule:   'aaaaaaaaaabbbbbbbbbbbbbbbbbbbccccccccdsssdsdsjhjhjshdaj'
S = """aaaaaaaaaa
bbbbbbbbbbbb
cccccccccccc
ddddddddddd
"""
S
# Resule:   'aaaaaaaaaa\nbbbbbbbbbbbb\ncccccccccccc\nddddddddddd\n'

# Raw strings - no escapes
S = r'\temp\spam'
S
# Resule:   '\\temp\\spam'

S = 'spam'
S * 3
# Result:   'spamspamspam'
# Index, slice, length
S[2]
# Result:   'a'
S[1:3]
# Result:   'pa'
len(S)
# Result:   4


S
# Result:   'spam'
# Some string methods:
# Search
S.find( 'pa' )
# Result:   1
# Remove whitespace
S.rstrip()
# Result:   'spam'
# Replace
S.replace( 'pa', 'xx' )
# Result:   'sxxm'
S.replace(  'xx', 'x,x' )
# Result:   'spam'
S
# Result:   'spam'
S.replace( 'pa', 'xx' )
# Result:   'sxxm'
S
# Result:   'spam'
X = S.replace( 'pa', 'x,x' )
X
# Result:   'sx,xm'
# Split on delimiter
X.split(','
	)
# Result:   ['sx', 'xm']
# Content test
S.isdigit()
# Result:   False
# Case conversion
S.lower()
# Result:   'spam'
S.upper()
# Result:   'SPAM'
# End test
S.endswith('spam')
# Result:   True
S.endswith('am')
# Result:   True
# Unicode encoding
S.encode( 'latin-1')
# Result:   b'spam'
# Iteration, membership
for x in S: print( x )

# Result:   s
# Result:   p
# Result:   a
# Result:   m
'spam' in S
# Result:   True
[c * 2 for c in S]
# Result:   ['ss', 'pp', 'aa', 'mm']
map( ord, S)
# Result:   <map object at 0x060DFC70>
