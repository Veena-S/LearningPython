###########
##### STRING METHODS
##########

S = 'spam'
# find method
result = S.find( 'pa' )
result
# Result:   1
S.capitalize()
# Result:   'Spam'
S.casefold()
# Result:   'spam'


## Changing Strings with Methods
S = 'spammy'
S = S.replace( 'mm', 'xx' )
S
# Result:   'spaxxy'
'aa$$bb$cc$dd'.replace('$', 'SPAM' )
# Result:   'aaSPAMSPAMbbSPAMccSPAMdd'
# Replacing by finding out the position
S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find( 'SPAM' )
where
# Result:   4
S = S[:where] + 'EGGS' + S[(where + 4 ):]
S
# Result:   'xxxxEGGSxxxxSPAMxxxx'
S = S[:where] + 'EGGS' + S[(where + 5 ):]
S
# Result:   'xxxxEGGSxxxSPAMxxxx'
S = 'xxxxSPAMxxxxSPAMxxxx'
S = S[:where] + 'EGGS' + S[(where + 5 ):]
S
# Result:   'xxxxEGGSxxxSPAMxxxx'

S = 'xxxxSPAMxxxxSPAMxxxx'
S.replace( 'SPAM', 'EGGS') # replace all
# Result:   'xxxxEGGSxxxxEGGSxxxx'
S.replace( 'SPAM', 'EGGS', 1) # replace one
# Result:   'xxxxEGGSxxxxSPAMxxxx'

# Convert string to an object that supports in-place changes, to improve the preformance, as strings are immutable
S = 'spammy'
L = list(S)
L
# Result:   ['s', 'p', 'a', 'm', 'm', 'y']
L[3] = 'x'
L[4] = 'x'
L
# Result:   ['s', 'p', 'a', 'x', 'x', 'y']
# After the changes, convert it back to string
S = ''.join(L)
S
# Result:   'spaxxy'
# join() is a method of strings, not lists.


##### SAMPLE:-    PARSING TEXT
line = 'aaa bbb ccc'
cols = line.split() # Default delimiter is whitespace
cols
# Result:   ['aaa', 'bbb', 'ccc']

line = 'bob,hacker, 40'
# Split the string at comma
line.split(',')
# Result:   ['bob', 'hacker', ' 40']
type(cols)
# Result:   <class 'list'>
# Delimiters can be more than a single character
line = "i'mSPAMaSPAMlumberjack"
line.split("SPAM")
# Result:   ["i'm", 'a', 'lumberjack']


# Common string methods
line = "The knights who say Ni!\n"
line.rstrip()
# Result:   'The knights who say Ni!'

line
# Result:   'The knights who say Ni!\n'

line.upper()
# Result:   'THE KNIGHTS WHO SAY NI!\n'

line.isalpha()
# Result:   False

line.endswith('Ni!\n')
# Result:   True

line.startswith( 'The')
# Result:   True

line.find('Ni') != -1
# Result:   True

'Ni' in line
# Result:   True

sub = 'Ni\n'
line.endswith( sub )
# Result:   False
sub = 'Ni!\n'
line.endswith( sub )
# Result:   True
line[-len(sub):] == sub
# Result:   True

