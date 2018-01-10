x = set( 'abcde' )
y = set( 'bdxyz' )
x
# Result:   {'d', 'c', 'b', 'a', 'e'}
# Sets do not have a positional ordering and so are
# not sequences - their order is arbitrary and may
# vary per python release
x
# Result:   {'d', 'c', 'b', 'a', 'e'}
# Mathematical set operations with expression operators
# Difference
x - y
# Result:   {'a', 'c', 'e'}
# Union
x | y
# Result:   {'d', 'x', 'z', 'c', 'b', 'a', 'e', 'y'}
# Intersection
x & y
# Result:   {'b', 'd'}
# Symmetric Differnce (XOR)
x ^ y
# Result:   {'z', 'c', 'x', 'a', 'e', 'y'}
# Superset, subset
x > y, x < y
# Result:   (False, False)
# Membership (sets)
'e' in x
# Result:   True
# in set membership test works on other types too
'e' in 'Camelot', 22 in [11, 22, 33]
# Result:   (True, True)

# Intersection - same as x & y
z = x.intersection( y )
z
# Result:   {'b', 'd'}
# add - Inserts one item
z.add( 'SPAM' )
z
# Result:   {'b', 'd', 'SPAM'}
# update - Merge:in-place union
z.update( set( ['X', 'Y'] ))
z
# Result:   {'SPAM', 'X', 'd', 'Y', 'b'}
# remove - deletes one item
z.remove( 'b' )
z
# Result:   {'SPAM', 'X', 'd', 'Y'}

for item in set( 'abc' ): print( item * 3 )

# Result:   bbb
# Result:   aaa
# Result:   ccc

S = set([1, 2, 3])
# Expressions require both to be sets
S | set([3, 4])
# Result:   {1, 2, 3, 4}
S | [3, 4]
# Result:   TypeError: unsupported operand type(s) for |: 'set' and 'list'
# But their methods allow any iterable
S.union([3, 4])
# Result:   {1, 2, 3, 4}
S.intersection((1, 3, 5))
# Result:   {1, 3}
S.issubset( range( -5, 5 ))
# Result:   True
# In 3.x, a set can be created by the following literal
{7, 8, 9}
# Result:   {8, 9, 7}
# But in all Pythons, the "set" built-in is still required to create empty sets and to build sets from existing iterable objects. New literal is convenient for initializing a set of known structure.
S = { 's', 'p', 'a', 'm' }
S
# Result:   {'p', 's', 'a', 'm'}
S.add( 'alot' )
S
# Result:   {'s', 'p', 'alot', 'm', 'a'}
# Empty sets
S1 = {1, 2, 3, 4 }
S1 - {1, 2, 3, 4}
# Result:   set()
## Empty set got printed differently
# Because {} is an empty dictionary
type( {} )
# Result:   <class 'dict'>
# Initialize an empty set
S = set()
S
# Result:   set()
S.add(1.23)
S
# Result:   {1.23}
# Some methods allow general iterable operands, that expressions do not:
{1, 2, 3} | {3, 4}
# Result:   {1, 2, 3, 4}
{1, 2, 3} | [3, 4]
# Result:   TypeError: unsupported operand type(s) for |: 'set' and 'list'
{1, 2, 3}.union([3, 4]) # method support list as an operand
# Result:   {1, 2, 3, 4}
{1, 2, 3}.union(set([3, 4]))
# Result:   {1, 2, 3, 4}

{1, 2, 3}.intersection((1, 3, 5))
# Result:   {1, 3}
{1, 2, 3}.issubset( range( -5, 5))
# Result:   True


### IMMUTABLE CONSTRAINTS AND FROZEN SETS
## sets can only contain immutable (a.k.a. “hashable”) object types. Hence, lists and dictionaries cannot be embedded in sets, but tuples can if you need to store compound values.
S
# Result:   {1.23}
# Only immutable objects work in a set
S.add([1, 2, 3])
# Result:   TypeError: unhashable type: 'list'
S.add({'a' : 1})
# Result:   TypeError: unhashable type: 'dict'
# No list or dict, but tuple ok
S.add((1, 2, 3))
S
# Result:   {1.23, (1, 2, 3)}
# Union: same as S.union(...)
S | {(4, 5, 6), (1, 2, 3)}
# Result:   {1.23, (4, 5, 6), (1, 2, 3)}
# Membership: by complete values
(1, 2, 3) in S
# Result:   True
(1, 4, 3) in S
# Result:   False
4 in S
# Result:   False
S | {(4, 5, 6), (1, 2, 3)} | {4}
# Result:   {1.23, (4, 5, 6), 4, (1, 2, 3)}
4 in S
# Result:   False
S.add((4, 5, 6))
S
# Result:   {1.23, (4, 5, 6), (1, 2, 3)}
4 in S
# Result:   False
(4, 5, 6) in S
# Result:   True


### SET COMPREHENSION EXPRESSION
## The set comprehension expression is similar in form to the list
## comprehension, but is coded in curly braces instead of square brackets
## and run to make a set instead of a list. Set comprehensions run a loop
## and collect the result of an expression on each iteration; a loop
## variable gives access to the current iteration value for use in the
## collection expression. The result is a new set you create by running
##the code, with all the normal set behavior.

# 3.X / 2.7 set comprehension
{x ** 2 for x in [1, 2, 3, 4]}
# Result:   {16, 1, 4, 9}
A = {x ** 2 for x in [1, 2, 3, 4]}
type( A )
# Result:   <class 'set'>
# Here the collection expression is x ** 2, which is coded on left and the loop is coded on right.

{x for x in 'spam' } # Same as: set( 'spam' )
# Result:   {'p', 's', 'a', 'm'}

# Set of collected expression results
{ c * 4 for c in 'spam' }
# Result:   {'ssss', 'mmmm', 'aaaa', 'pppp'}
{ c * 4 for c in 'spamham' }
# Result:   {'hhhh', 'aaaa', 'mmmm', 'pppp', 'ssss'}
S = { c * 4 for c in 'spam' }
S | { 'mmmm', 'xxxx' }
# Result:   {'aaaa', 'xxxx', 'pppp', 'ssss', 'mmmm'}
S & { 'mmmm', 'xxxx' }
# Result:   {'mmmm'}


L = [x ** 2 for x in [1, 2, 3, 4]]
L
# Result:   [1, 4, 9, 16]
type( L )
# Result:   <class 'list'>
L = x ** 2 for x in [1, 2, 3, 4]
# Result:   SyntaxError: invalid syntax
L = ( x ** 2 ) for x in [1, 2, 3, 4]
# Result:   SyntaxError: invalid syntax
L = ( x ** 2 for x in [1, 2, 3, 4])
L
# Result:   <generator object <genexpr> at 0x05BFA960>
type( L )
# Result:   <class 'generator'>

###############
# USES OF SETS
# Sets can be used to filter out duplicates
# Convert the collection to a set and then back again
L = [1, 2, 1, 3, 2, 4, 5]
L
# Result:   [1, 2, 1, 3, 2, 4, 5]
set( L )
# Result:   {1, 2, 3, 4, 5}
# Duplicates are removed by converting to set
# Convert back to list
L = list( set( L ))
L
# Result:   [1, 2, 3, 4, 5]

# Order may vary
list( set( ['yy', 'cc', 'aa', 'xx', 'dd', 'aa']))
# Result:   ['dd', 'yy', 'cc', 'xx', 'aa']


# Sets can be used to isolate differences in lists, strings and other iterable objects
# Find list differences
set( [1, 3, 5, 7]) - set([1, 2, 4, 5, 6])
# Result:   {3, 7}
# Find string differences
set( 'abcdefg' ) - set( 'abdghij' )
# Result:   {'f', 'c', 'e'}
# Find differences, mixed
set( 'spam' ) - set( ['h', 'a', 'm'])
# Result:   {'p', 's'}
# In bytes, but not bytearray
set( dir(bytes)) - set( dir(bytearray))
# Result:   {'__getnewargs__'}
set( dir(bytearray)) - set( dir(bytes))
# Result:   {'insert', 'copy', 'pop', 'remove', 'reverse', 'extend', '__setitem__', 'append', 'clear', '__delitem__', '__imul__', '__iadd__', '__alloc__'}


# Sets can be used to perform order-neutral equality tests by converting to a set before the test
# Because, order doesn't matter in sets. Both are equal, if each is a subset of the other.
L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
# Order matters in sequences.
L1 == L2
# Result:   False
# Order-neutral equality
set( L1 ) == set( L2 )
# Result:   True
sorted( L1 ) == sorted( L2 ) # Similar, but results ordered
# Result:   True
'spam' == 'asmp', set( 'spam' ) == set( 'asmp' ), sorted( 'spam' ) == sorted( 'asmp' )
# Result:   (False, True, True)


# Sets can be used to keep track of the traversing through a graph or cyclic structure
# Sets are convenient when dealing with large data sets
engineers = { 'bob', 'sue', 'ann', 'vic' }
managers = { 'tom', 'sue' }
# Is bob an engineer
'bob' in engineers
# Result:   True

engineers & managers    # Who is both engineer and manager?
# Result:   {'sue'}

engineers | managers    # All people in either category
# Result:   {'ann', 'vic', 'sue', 'bob', 'tom'}

engineers - managers    # Engineers who are not managers
# Result:   {'ann', 'bob', 'vic'}

managers - engineers    # Managers who are not engineers
# Result:   {'tom'}

engineers > managers	# Are all managers engineers?
# Result:   False

{ 'bob', 'sue' } < engineers    # Are both engineers? (subset)
# Result:   True

( managers | engineers ) > managers # All people is a superset of managers
# Result:   True

managers ^ engineers # who is in one, but not both
# Result:   {'ann', 'vic', 'bob', 'tom'}

# Intersection
(managers | engineers) - (managers ^ engineers)
# Result:   {'sue'}


