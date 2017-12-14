# System Command Lines and Files

The disadvantage of interactive interpreter is that, the programs are never stored and it goes away as soon as it is executed. 

### Modules
Modules - Text files that contain the Python statements. These files can be executed any number of times, in a variety of ways like by system command lines, by file icon clicks, by options in the IDLE user interface etc.

#### Types of Terminology used:
1. Module files are often referred to as __programs__. i.e. A program is considered to be a series of precoded statements stored in a file for repeated execution.
2. Module files that are run directly are also sometimes known as __scripts__ - meaning top level program file.
3. Some reserver the term __module__ for an imported file and __script__ for the main file of a program.


### First Script

```Python
# First Python Script - Fetches the name of the platform.
import sys              # Load a library module
print( sys.platform )
print( 2 ** 100 )       # Raise 2 to a power
x = 'Spam!'
print( x * 8 )          # String repetition.
```

This module file is saved as script1.py. As for all top-level files, it could also be called simply __script__, but files of code that needs to be imported into a client have to end with a __.py__ suffix.

### Running Files with CommandLine
Change the command line directory to the one where script file is save execute it.
```
python script1.py
```
. __Stream Redirection__:- The printed output of a Python script can be routed to a file: 
  ```
  python script1.py > saveit.txt
  ```
. If you are using a Windows Launcher as in Python 3.3, change the command line directory the script directory and execute the following:
  ```
  py -3 script1.py
  ```
 . On all recent version of Windows, we can omit the name of Python itsel, just the name of the script is enough. Because, newe Windows systems uses Registry to find a program with which to run a file. So, the command can be as simple as
 ```
 script1.py
 ```
### Clicking Icon on Windows:
Python generated a pop-up black DOS console window (CommandPrompt) to serve as clicked files input and output. If a script just prints and exits,the output console window closes and disappears on program exit.
Workaround is to put a call to the built-in _input_ function at the very bottom of the script in 3.X
```Python
# First Python Script - Fetches the name of the platform.
import sys              # Load a library module
print( sys.platform )
print( 2 ** 100 )       # Raise 2 to a power
x = 'Spam!'
print( x * 8 )          # String repetition.
input()                 # ADDED
```

This trick is usually needed only if 
  - it is Windows
  - only if the script prints texts and exits
  - only if you will launch the script by clicking it's icon
  
It is also possible to completely suppress the pop-up console window that appears on on file clicking. Files whose names end in __.pyw__ extension will display only windows constructed by your script, not the default console window. __.pyw__ files are simply __.py__ files that have this special operational behavior on Windows. 
  
  
