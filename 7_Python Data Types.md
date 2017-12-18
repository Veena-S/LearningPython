## Python Conceptual Hierarchy

Python programs can be decomposed into modules, statements, expressions and objects as follows:
1. Programs are composed of modules
2. Modules contain statements
3. Statements contain expressions
4. Expressions _create_ and _process_ objects.

## Need of Built-in Types
1. Built-in objects make programs easy to write
2. Built-in objects are components of extensions
3. Built-in objects are often more efficient than custom data structures
4. Built-in objects are a standard part of the language

## Python's Core Data Types
*__Built-in object's preview__*

Object Type                   | Example literal/creation
------------------------------|--------------------------------------------------
Numbers                       | 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
Strings                       | 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
Lists                         | [1, [2, 'three'], 4.5], list(range(10))
Dictionaries                  | { 'food' : 'spam', 'taste' : 'yum' }, dict(hours=10)
Tuples                        | (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
Files                         | open('eggs.txt'), open(r'C:\ham.bin', 'wb')
Sets                          | set('abc'), {'a', 'b', 'c'}
Other Core Types              | Booleans, types, None
Program unit types            | Functions, modules, classes
Implementation-related types  | Compiled code, stack tracebacks


Once an object is created, its operation set are bound for all time. 
i.e. Python is _dynamically typed_, a model that keeps track of types automatically instead of requiring declaration code, but it is also a _strongly typed_, a constraint that means you can perform on an object only operations that are valid for it's type.

Pyhton variables never need to be declared ahead of time. A variable is created when a value is assigned to it, may be assigned any type of object, and is replaced with its value value when it shows up in an expression.

### Numbers
Includes:
- _integers_ that have no fractional part
- _floating-point_ numbers that has fractional part
- _complex_ numbers with imaginary parts
- _decimals_ with fixed precision
- _rationals_ with numerator and denominator
- full-featured _sets_

Numbers in Python support the normal mathematical operations like:
- + performs addition
- * performs multiplication
- ** performs exponentiation

Floating point numbers behaves differently in version before Python 2.7 and 3.1 and the after those versions (3.X):- 
In Pyhtons < 2.7 and 3.1
```Python
>>> 3.1415 * 2            # repr: as code. i.e result is shown with full precision.
6.2830000000000004
>>> print(3.1415 * 2)     # str: user friendly. Result is shown in a user friendly way
6.283
```

In Pythons>=2.7 and 3.1
```Python
>>> 3.1415 * 2            # repr: as code
6.283
```


### Strings
Strings are used to record both textual information aa well as arbitrary collections of bytes ( such as image file's contents).
Strings are an example of _sequence_ in Python - a positionally ordered collection of other objects. Sequences maintain a left-to-right order among the items they contain : their items are stored and fetched by their relative positions.
Strings are sequences of one-character strings.
Other sequence types include lists, tuples etc.

#### Sequence Operations:
1. Strings supports operations that assume a positional ordering among items.
2. In Python, _backward indexing_ is also possible - positive indexes count from the left and negative indexes count back from right.
   Formally, negative index is simply added to the length of the string sequence.
   Sample code:
   ```Python
   >>> S = 'Spam'	# Make a 4-character string and assign it to a name
   >>> len(S)
   4
   >>> S[0]	# First item in S, indexed by zero based position
   'S'
   >>> S[1]	# Second item from left
   'p'
   >>> S[-1]  # Last item in S
   'm'
   >>> S[-2]	# Second-to-last item from the end.
   'a'
   >>> # Negative index == Add negative index to the string length.
   >>> S[len(S)-2]	#== S[-2]
   'a'
   >>> 
   ```
3. Sequences support a more general form of indexing known as _slicing_ , which is a way to extract an entire-section (slice) in a single step.
   Sample Code:
   ```Pyhton
   >>> S
   'Spam'
   >>> S[1:3]
   'pa'
   >>> 
   ```
   Slicing can be considered to be a way of extracting an entire column from a string in a single step.
   General form ```X[I:J]```, means give me everything in X from offset I up to, but not includeing, offset J.
   The result is returned in a new object. 
   In a slice, the left bound defaults to zero, and the right bound defaults to the length of the sequence to be sliced.
   Sample Code:
     ```Python
     >>> S[1:]	# Everything past the first i.e. 1:len(S)
    'pam'
    >>> S 		# S itself hasn't changed
    'Spam'
    >>> S[0:3]	# Everything but the last
    'Spa'
    >>> S[:3]	# Same as S[0:3]
    'Spa'
    >>> S[:-1]	# Everything but the last, S[0:-1]
    'Spa'
    >>> S[:]	# All of S as a top-level copy S[0:len(S)]
    'Spam'
    >>> 
    ```
4. As sequences, Strings also support _concatenation_ with plus sign (joining two strings to form a new string ) and _repetition_ (making a new string by repeating another)
    Sample Code:
    ```Python
    >>> S
    'Spam'
    >>> S + 'xyz'     # Concatenation
    'Spamxyz'
    >>> S             # Unchanged
    'Spam'
    >>> S * 8         # Repetition
    'SpamSpamSpamSpamSpamSpamSpamSpam'
    >>> S
    'Spam'
    >>> 
    ```

