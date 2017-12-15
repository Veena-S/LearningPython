Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
====== RESTART: D:/LearningPython/CodeSamples/threeNames/threeNames.py ======
dead parrot sketch
>>> 
>>> 
>>> import threeNames
dead parrot sketch
>>> 
>>> threeNames.b, threeNames.c		#Access it's attributes
('parrot', 'sketch')
>>> 
>>> 
>>> 
>>> from threeNames import a, b, c      # Copy multiple names out
>>> b, c
('parrot', 'sketch')
>>> 
>>> 
>>> # The results printed here are in tuples
>>> 
>>> # the built-in dir function can be used to fetch a list of all the names
>>> # available insidea module
>>> # The following returns a Python list of strings in square brackets
>>> 
>>> dir(threeNames)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c']
>>> 
>>> # When dir function is called for a module, it returns all the attributes inside that module. Names with leading and trailing double underscores (__X__) are built-in names that are always predefined by the Python and have special meaning to the interpreter.
