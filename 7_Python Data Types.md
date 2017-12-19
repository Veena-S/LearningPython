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
Strings are _immutable_.

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
#### Immutability:-
Strings are _immutable_ in Python - every string operation is defined to produce a new string as its result, that cannot be changed in place after they are created.
i.e Valued of immutable objects can never be overwritten. But you can always build a new one and assign it to the same name. This is because, Python cleans up old objects on the go.

``` Python
>>> S = 'Spam'
>>> S
'Spam'
>>> S[0]
'S'
>>> S[0] = 'z'		# Immutable objects cannot be changed.
    ....error text...
    S[0] = 'z'		# Immutable objects cannot be changed.
TypeError: 'str' object does not support item assignment
>>> S = 'z' + S[1:]	# Can make new objects
>>> S
'zpam'
>>> 
```

Every object in Python is classified as Immutable (unchangeable) or not.
The core types _numbers_, _strings_ and _tuples_ are immutable, while _lists_, _dictionaries_ and _sets_ are not.
Immutability can be used to guarantee that an object remains constant throughout the program; mutable objects' values can be changed at any time and place.

The text based data can be changed _in-place_, in either of two ways:
1. Expand it into a _list_ of individual characters and join it back together with nothing in between
```Python
>>> S = 'shrubberry'	# Expand to a list: [...]
>>> L = list(S)
>>> L
['s', 'h', 'r', 'u', 'b', 'b', 'e', 'r', 'r', 'y']
>>> L[1] = 'c'		# Change it in place
>>> ''.join(L)		# Join with empty delimiter - joining all the items in the list.
'scrubberry'
>>> L
['s', 'c', 'r', 'u', 'b', 'b', 'e', 'r', 'r', 'y']
>>> '@'.join(L)   # Try joining with another delimiter e.g: @
's@c@r@u@b@b@e@r@r@y'
```
2. Use _bytearray_ type available in Pythons 2.6, 3.0 and later
```Python
>>> B = bytearray(b'spam')	# A bytes/list hybrid (ahead)
>>> B.extend(b'eggs')		# b needed in 3.X, not in 2.X
>>> B
bytearray(b'spameggs')
>>> B.decode()			# Translate to normal string
'spameggs'
```
The _bytearray_ supports in-place changes for text, but only for text whose characters are all at most 8-bits wide (e.g: ASCII).
All other strings are still immutable - _bytearray_ is a distinct hybrid of immutable _bytes_ strings (whose b'...' syntax is required depending on Python version) and mutable _lists_ ( coded and displayed in [] ).

#### Type-Specific Methods:
In addition to generic sequence operations, strings also have operations all their own, available as methods.
Sample code to show some string methods and its usage:
```Python
>>> S = 'Spam'
>>> # To find the offset of a substring is S
>>> S.find('pa')
1
>>> S.find('pq')     # If the substring is not present it will return -1
-1
>>> S
'Spam'
>>> # To replace occurrences of a substring with another
>>> S.replace( 'pa', 'XYZ')
'SXYZm'
>>> S
'Spam'
>>> 
```
Other methods split a string to substrings on a delimiter, perform case conversions, test the content of the string and strip whitespcae characters off the ends of the string:
```Python
>>> line = 'aaa, bbbb, ccccc, dd'
>>> line.split(',')	# Split on a delimiter into a list of substrings
['aaa', ' bbbb', ' ccccc', ' dd']
>>> line
'aaa, bbbb, ccccc, dd'
>>> line.split(', ')
['aaa', 'bbbb', 'ccccc', 'dd']
>>> 
>>> S = 'Spam'
>>> S.upper()        # Upper-case conversion
'SPAM'
>>> S.lower()        # Lower-case conversion
'spam'
>>> S                # No change in the original string
'Spam'
>>> S.isalpha()      # Content test: isalpha, isdigit etc.
True
>>> S.isdigit()
False
>>> X = 'a2'
>>> X.isdigit()
False
>>> X = '2'
>>> X.isdigit()
True
>>> 
>>> line = 'aaa,bbb,ccc,dd\n'
>>> line
'aaa,bbb,ccc,dd\n'
>>> line.rstrip()	         # Remove whitespace
'aaa,bbb,ccc,dd'
>>> line
'aaa,bbb,ccc,dd\n'
>>> line.rstrip().split(',')     # Combining both the operations
['aaa', 'bbb', 'ccc', 'dd']
>>> 
```

Strings also support an advanced substitution operation known as _formatting_, available as both an expression and a string method call.
```Python
>>> # Formatting Expression
>>> '%s, eggs, and %s' % ('spam', 'SPAM!')
'spam, eggs, and SPAM!'
>>> 
>>> # Formatting Method ( 2.6+, 3.0+)
>>> '{0}, eggs, and {1}'.format('spam', 'SPAM!')
'spam, eggs, and SPAM!'
>>> 
>>> # Numbers optional (2.7+, 3.1+)
>>> '{}, eggs, and {}'.format('spam', 'SPAM!')
'spam, eggs, and SPAM!'
>>> 
>>> ### Formatting to generate numeric reports
>>> '{:,.2f}'.format(296888.2567)	# Separators, decimal digits
'296,888.26'
>>> '%.2f | %+05d' % ( 3.14159, -42) 	# Digits, padding and signs
'3.14 | -0042'
```

#### Getting Help
The built-in ```dir``` function returns a list of all the attributes available to for any object passed to it.
```Python
>>> S
'Spam'
>>> dir(S)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
The names with _double underscores_ represent the implementation of the string object and are available to support customization.
For e.g.: the ```__add__``` method is what really performs concatenation. Python maps plus operation to this internally, though one should not use this form.
```Python
>>> S + 'NI!'
'SpamNI!'
>>> S.__add__('NI!')
'SpamNI!'
>>> 
```

Generally, leading and trailing double underscores is the naming pattern Python uses for implementation details. The names without the underscores in this list are the callable methods on the String objects.

The ```dir``` function simply gives the name of methods. To ask what they do, use  the help function.
```Python
>>> help(S.replace)
Help on built-in function replace:

replace(...) method of builtins.str instance
    S.replace(old, new[, count]) -> str
    
    Return a copy of S with all occurrences of substring
    old replaced by new.  If the optional argument count is
    given, only the first count occurrences are replaced.

>>> help(S)
No Python documentation found for 'Spam'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>>
```
_PyDoc_ - a tool for extracting documentation from objects.

Both dir and help accepts either a real object (like S) or the name of a data type (like str, list and dict) as arguments. The latter form returns the same list for dir, but shows full type details for help and allows to ask about a specific method via type name.
```Python
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |      ####
 |      # Other Functions removed
 |      ####
 |  
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(...)
 |      S.capitalize() -> str
 |      
 |      Return a capitalized version of S, i.e. make the first character
 |      have upper case and the rest lower case.
 |  
 |  casefold(...)
 |      S.casefold() -> str
 |      
 |      Return a version of S suitable for caseless comparisons.
 |
 |				####
 |				# Other Functions removed
 |				####
 |  
 |  zfill(...)
 |      S.zfill(width) -> str
 |      
 |      Pad a numeric string S with zeros on the left, to fill a field
 |      of the specified width. The string S is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> 
```
#### Other Ways to Code Strings
Special characters can be represented as backslash escape sequences, which Python displays in ```\xNN``` hexadecimal escape notation, unless they represent printable characters.
```Python
>>> S = 'A\nB\tC'	      # \n is end-of-line, \t is tab
>>> S
'A\nB\tC'
>>> len(S)              # Each stands for just one character
5
>>> P = 'k\o'
>>> P
'k\\o'
>>> P = 'k\\o'
>>> P
'k\\o'
>>> ord('\n')           # \n is a byte with binary value 10 in ASCII
10
>>> 
>>> S = 'A\0B\0C'	      # \0, a binary zero byte, does not terminate string
>>> len(S)
5
>>> S                   # Non-printables are displayed as \xNN hex escapes
'A\x00B\x00C'
```


Python allows strings to be enclosed in single or double quote characters - they mean the same thing, but allow the other type of quote to be embedded with an escape.
It also allows multiline string literals enclosed in triple quotes (single or double ) - when this form is used, all the lines are concatenated together, and end-of-lone characters are added where line breaks appear. 
```Python
>>> msg = """
aaaaaaaaaaaa
bb'''bbbbb""yy'yyyy
cccccccccc
"""
>>> msg
'\naaaaaaaaaaaa\nbb\'\'\'bbbbb""yy\'yyyy\ncccccccccc\n'
>>> nextMsg = """aaa
bb'bbbbbb"yy'uuuuuu"""
>>> nextMsg
'aaa\nbb\'bbbbbb"yy\'uuuuuu'
>>> changeQuote = '''aaa
bb"bbbbbb'yy"uuuuuu'''
>>> changeQuote
'aaa\nbb"bbbbbb\'yy"uuuuuu'
>>> 
```

Python also supports a _raw_ string literal that turns off the backslash mechanism. Such literals start with the letter ```r``` and are useful for strings like directory paths on Windows.
```Python
>>> pt = r'C:\text\new'
>>> pt
'C:\\text\\new'
>>> pt = r'C:/text/new'
>>> pt
'C:/text/new'
>>> pt = 'C:/text/new'
>>> pt
'C:/text/new'
>>> pt = 'C:\text\new'
>>> pt
'C:\text\new'
>>> 
```

#### Unicode Strings
Python's Strings supports full Unicode required for processing text in internationalized character sets.
In Python 3.X:-
   - normal ```str``` string handles Unicode text (including ASCII)
   - a distinct ```bytes``` string type represents raw byte values ( including media and encoded text )
   - for 2.X compatibility, 2.X Unicode literals are supported in 3.3 and later ( they are treated the same as normal 3.X str strings)
   
   ```Python
   >>> 'sp\xc4m'		# 3.X: normal str strings are Unicode texts
   'spÄm'
   >>> b'a\x01c'		# bytes strings are byte-based data
   b'a\x01c'
   >>> u'sp\u00c4m'	# The 2.X Unicode literal works in 3.3+: just str
   'spÄm'
   >>> 
   ```
   
  In Python 2.X:-
   - the normal ```str``` string handles both 8-bit character strings (including ASCII text) and raw byte values
   - a distinct ```unicode``` string type represents Unicode text
   - For 3.X compatibility, 3.X bytes literals are supported in 2.6 and later ( they are treated the same as normal 2.X ```str``` strings)
   ```Python
   >>> print ( u'sp\xc4m' )	#2.X: Unicode strings as distinct types
   spÄm
   >>> 'a\x01c'			      # Normal str strings contain byte-based text/data
   'a\x01c'
   >>> b'a\x01c'			      # The 3.X bytes literal works in 2.6+: just str
   b'a\x01c'
   ```
   In both 2.X and 3.x, non-unicode strings are sequences of 8-bit bytes that print with ASCII characters when possible, and Unicode strings are sequences of Unicode code points - identifying numbers for characters, which do not necessarily map to single bytes when encoded to files or stored in memory. In fact, the notion of bytes doesn't apply to Unicode: some encodings include character code points too large for a byte, and even simple 7-bit ASCII text is not stored one byte per character under some encodings and memory storage schemes.
   
  ```Python
  >>> 'spam'		# Characters may be 1, 2 or 4 bytes in memory
   'spam'
   >>> 'spam'.encode( 'utf8' )	#Encoded to 4 bytes in UTF-8 files
   b'spam'
   >>> 'spam'.encode( 'utf16' )	# But encoded to 10 bytes in UTF-16
   b'\xff\xfes\x00p\x00a\x00m\x00'
   >>> 
  ```
  
  Both 3.X and 2.X also supports the following:
   - the ```bytearray``` string type,which is essentially a ```bytes``` string ( a ```str``` in 2.X) that supports most of the list object's in-place mutable change operations.
   - Support coding the n-n-ASCII characters with _\x_ hexadecimal and shot _\u_ and long _\U_ Unicode escapes, as well as file-wide encodings declared in program source files.
   ```Python
   >>> # Sample code showing non-ASCII character coded in 3 ways in 3.X
   >>> 'sp\xc4\u00c4\U000000c4m'
   'spÄÄÄm'
   >>> # In 2.X
   >>> print(u'sp\xc4\u00c4\U000000c4m')
   spÄÄÄm
   ```
   
What these values mean and how they are used differs between _text_ strings and _byte_ strings.
   - text strings: which are the normal string in 3.X and Unicode in 2.X
   - byte strings: which are bytes in 3.X and the normal string in 2.X
All these escapes can be used to embed actual Unicode code-point ordinal value integers in text strings. 
By contrast, byte strings use only \x hexadecimal escapes to embed the encoded form of text, not its decoded code point values - encoded bytes are same as code points, only for some encodings and charachters.

```Python
>>> '\u00A3', '\u00A3'.encode('latin1'), b'\xA3'.decode('latin1')
('£', b'\xa3', '£')
```

Differenece: Python 2.X allows its normal and Unicode strings to be mixed in expressions as long as the normal string is all ASCII
             Python 3.X never allows its normal and byte strings to mix without explicit conversion.
             
             ```
             u'x' + b'y'            # Works in 2.X, where b is optional and ignored
                                    # Fails in 3.3, where u is optional and ignored
             u'x' + 'y'             # Works in 2.X: u'xy' and Works in 3.3: 'xy'
             'x' + b'y'.decode()    # Works in 3.X if decode bytes to str: 'xy'
             'x'.encode() + b'y'    # Works in 3.X if encode str to bytes: b'xy'
             ```
             
Apart from these string types, Unicode processing mostly reduces to transferring text data to and from files - text is encoded to bytes when stored in a file, and decoded into characters (a.k.a. code points) when read back into memory. Once it is loaded, we usually process text as strings in decoded form only.

Because of this model, though, _files are also content specific in 3.X_: 
   - text files implement named encodings and accept & return ```str``` strings
   - binary files deal in ```bytes``` strings for raw binary data
   In 2.X, normal files' content is ```str``` bytes, and a special ```codecs``` module handles Unicode and represents content with the ```unicode``` type.
   
 
#### Pattern Matching
None of the string objects in Python own methods to support pattern-based text processing.

To do pattern matching in Python, import a module ```re```. This module has analogous calls for searching, splitting and replacement.

An example to search for a substring that begins with the world "Hello", followed by zero or more tabs or spaces, followed by srbitrary characters to be saved as a matched group, terminated by the word "world".
```Python
>>> import re
>>> match = re.match( 'Hello[ \t]*(.*)world', 'Hello    Python world' )
>>> match.group( 1 )
'Python '
>>> match.groups()
('Python ',)
>>> match = re.match( 'Hello[\t]*(.*)world', 'Hello    Python world' )
>>> match.group( 1 )
'    Python '
>>> match = re.match( 'Hello[\t]*(.*)world', 'Hello~~~~~Python world' )
>>> match.group( 1 )
'~~~~~Python '
>>> match = re.match( 'Hello[\t]*(.*)world', 'Hello~~~~~Python~~~world' )
>>> match.group( 1 )
'~~~~~Python~~~'
>>> match = re.match( 'Hello[\t]*world', 'Hello~~~~~Python~~~world' )
>>> match.group( 1 )
###.....................Error Message...........
AttributeError: 'NoneType' object has no attribute 'group'
```

If such a substring is found, portions of the substring matched by parts of the pattern enclosed in parentheses are available as groups.

Following code picks out three groups separated by slashes, and is similar to splitting by an alternative program
```Python
>>> match = re.match( '[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack' )
>>> match.groups()
('usr', 'home', 'lumberjack')

>>> re.split( '[/:]', '/usr/home/lumberjack' )
['', 'usr', 'home', 'lumberjack']
>>> 

>>> # Following code returns error.
>>> match = re.match( '[/](.*)[/](.*)[/](.*)', '/usr/home:lumberjack' )
>>> match.groups()
AttributeError: 'NoneType' object has no attribute 'groups'

>>> match = re.match( '[/](.*)[:](.*)[/](.*)', '/usr/home:lumberjack' )
>>> match.groups()
AttributeError: 'NoneType' object has no attribute 'groups'

>>> match = re.match( '[/](.*)[/](.*)[:](.*)', '/usr/home:lumberjack' )
>>> match.groups()
('usr', 'home', 'lumberjack')
```


### LISTS
Most general sequence provided by the language.
__Lists are positionally ordered collections of arbitrary typed objects, and they have no fixed size.__
They are __mutable__: Lists can be modified in place by assignment to offsets as well as a variety of list method calls.
A very flexible tool for representing arbitrary collections:- lists of files in a folder, employees in a company etc.

#### Sequence operations:
List supports all sequence operations (discussed for strings)
Result of those operation will be a list itself.
```Python
>>> 
>>> L = [123, 'spam', 1.23]	# A list of three different type objects
>>> len(L)
3
>>> L[0]                      # Indexing
123
>>> L[-1]
1.23
>>> L[:-1]                    # Slicing
[123, 'spam']
>>> L + [4, 5, 6]		# Concat/repeat makes new lists too
[123, 'spam', 1.23, 4, 5, 6]
>>> L * 2
[123, 'spam', 1.23, 123, 'spam', 1.23]
>>> L
[123, 'spam', 1.23]
>>> 
```

#### Type-Specific Operations:
- Have no fixed type constraint
- Have no fixed size: can grow and shrink on demand
```Python
>>> L.append('NI')	   # Growing: add an object at the end of the list
>>> L
[123, 'spam', 1.23, 'NI']
>>> L.pop(2)		      # Shrinking: deleting an item in the middle
1.23
>>> L
[123, 'spam', 'NI']

>>> L.append(1.23)
>>> L
[123, 'spam', 'NI', 1.23]
>>> del L[3]            # To remove an item from an index
>>> L
[123, 'spam', 'NI']
>>> 

>>> # To insert an item at an arbitrary position
>>> L.insert(3, '4u')      # Item is inserted before the specified index.
>>> L
[123, 'spam', 'NI', '4u']
>>> L.insert(6, '4u')      # Item is inserted as the last item, even though specified index is not valid.
>>> L
[123, 'spam', 'NI', '4u', '4u']

>>> # Removes a given item by value
>>> L.remove('4u')         # removes the first occurance of the value
>>> L
[123, 'spam', 'NI', '4u']

>>> # Add multiple items at the end
>>> L.extend( 'A1')     # Iterates through the given value and adds each .
>>> L
[123, 'spam', 'NI', '4u', 'A', '1']
>>> L.extend( 567 )
TypeError: 'int' object is not iterable
>>> L.extend( '5''67' )
>>> L
[123, 'spam', 'NI', '4u', 'A', '1', '5', '6', '7']

>>> M = ['bb', 'xx', 'aa' ]
>>> M
['bb', 'xx', 'aa']
>>> M.sort()
>>> M
['aa', 'bb', 'xx']
>>> M.reverse()
>>> M
['xx', 'bb', 'aa']
>>> 

```

#### Bounds Checking:
Pythons doesn't allow to refer items that are not present in the List
Indexing off the end of a list and Assigning off the end are mistakes. Python throws error.
```Python
>>> L
[123, 'spam', 1.23]
>>> L[99]
Traceback (most recent call last):
  File "<pyshell#336>", line 1, in <module>
    L[99]
IndexError: list index out of range
>>> L[99] = 21
Traceback (most recent call last):
  File "<pyshell#337>", line 1, in <module>
    L[99] = 21
IndexError: list assignment index out of range
>>> L.insert(99, 21)
>>> L
[123, 'spam', 1.23, 21]
>>> 
```

#### Nesting:
Supports arbitrary nesting.
```Python
>>> # A list containing 3 other lists - matrix
>>> Matrix = [[1, 2, 3],
	           [4, 5, 6],
	           [7, 8, 9]]
>>> Matrix
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> # To get second row 
>>> Matrix[1]
[4, 5, 6]
>>> # Get the item at second row , thrid column
>>> Matrix[1][2]
6
>>> 
```

#### Comprehensions: 
List comprehensions derive from set notation; they are a way to build a new list by running an expression on each item in a sequence, one at a time, from left to right.

List comprehensions are coded in square brackets and are composed of an expression and a looping construct that share a variable name.
(_row_ in the following example)
```Python
>>> 
>>> # To get the column of a matrix by list comprehension
>>> Matrix
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> col2 = [row[1] for row in Matrix]
>>> col2
[2, 5, 8]
>>> Matrix
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> 
```
This comprehension means "Give me row[1] for each row in the matrix Matrix, in a new list." The result is a new list containing column 2 of the matrix.

```Python
>>> 
>>> # To add 1 to each item in column 2
>>> [row[1] + 1 for row in Matrix]
[3, 6, 9]
>>> # To filter out odd items
>>> [row[1] for row in Matrix if row[1] % 2 == 0 ]
[2, 8]
>>> 
```
