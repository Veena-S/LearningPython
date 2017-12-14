## Usage of Interactive Prompt

The interactive prompt can be used for doing experiments on Python expressions / statements.
It can also be used to test the code that are written in files - import the module file interactively and run tests on the tools they define by typing calls at the interactive prompt on the fly.

Sample Code:

``` Python
>>> # The following code tests a function in a precoded module that ships with Python in its standard library
>>> # (it prints the name of the directory you are currently working in, with a doubled-up backslash that stands for just one)
>>> import os
>>> os.getcwd()
'C:\\Program Files (x86)\\Python\\Python36-32'
```

## Notes on Usage:
1. Type only Python command/code at Python's >>> prompt, not system commands.
2. __print__ statements are required only in files, as the interactive interpreter automatically prins the expression results.
3. Don't intend at the interactive prompt (__yet__):- Be sure to start the unnested statements in column 1 itself, otherwise syntax error.
4. Watch out for prompt changes for compound statements from '>>>' to '...'.
5. Terminate compound statemets at the interactive prompt by entering a blank line i.e. press the "Enter" button twice.
6. The interactive prompt runs one statement at a time.
