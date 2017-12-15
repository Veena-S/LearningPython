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

### Numbers
Includes:
- _integers_ that have no fractional part
- _floating-point_ numbers that has fractional part
- _complex_ numbers with imaginary parts
- _decimals_ with fixed precision
- _rationals_ with numerator and denominator
- full-featured _sets_

