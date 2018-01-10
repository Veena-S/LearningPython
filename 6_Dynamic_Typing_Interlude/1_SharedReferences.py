a = 3
b = a
a
# Result:   3
b
# Result:   3
a = 'spam'
a
# Result:   'spam'
b
# Result:   3
a = 3
a = a + 2
a
# Result:   5
b
# Result:   3

#########################
### SHARED REFERENCES AND IN-PLACE CHANGES

L1 = [2, 3, 4]
L2 = L1
L1
# Result:   [2, 3, 4]
L2
# Result:   [2, 3, 4]
L1[0]
# Result:   2
L1 = 24
L1
# Result:   24
L2
# Result:   [2, 3, 4]
L1 = [2, 3, 4]
L2 = L1
# Perform an in-place change
L1[0] = 24
L1
# Result:   [24, 3, 4]
L2
# Result:   [24, 3, 4]
# Here, not the entire L1 is changed, but only a component of the object is changed. This sort of change overwrites part of the list object's value in place.
# This behavior only occurs for mutable objects that support in-place changes.
# To avoid this, copy the objects instead of making references.
L1 = [2, 3, 4]
# Make a copy of L1 by slicing or making a new list list(L1) or copy.copy(L1) etc.
L2 = L1[:]
L1
# Result:   [2, 3, 4]
L2
# Result:   [2, 3, 4]
L1[0] = 24
L1
# Result:   [24, 3, 4]
L2
# Result:   [2, 3, 4]


###############
### SHARED REFERENCES AND EQUALITY
# Two different ways to check for equality in a Python program
L = [1, 2, 3]
M = L
# M and L reference the same object
# Check for same values
L == M
# Result:   True
# Check for same objects
L is M
# Result:   True

# Here the "==" opeator tests whether the two referenced objects have
# the same values. This method is always used for equality checks in
# Python The "is" operator tests for object identity - it returns True
# only if both names points to the exact same object, so it is a much
# stronger form of equality testing and is rarely applied in most
# programs. The "is" returns False, if the names points to equivalent
# but different objects. It simply compares the pointers that implement
# references.

L = [1, 2, 3]
M = [1, 2, 3]
L == M
# Result:   True
L is M
# Result:   False
# Same operation on small numbers
X = 42
Y = 42
X == Y
# Result:   True
X is Y
# Result:   True
# To get the number of references to an object:
import sys
sys.getrefcount( 1 )
# Result:   912


