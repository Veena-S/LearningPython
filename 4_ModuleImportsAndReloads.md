## Import and Reload basics
Every file of Python source code whose name ends in a __.py__ extension is a module. No special code or syntax is required to make a file a module - any such file will do.
Other files can access the item defined in a module by __importing__ that module - import operations load another file and grant access to that file's contents.
The contents of a module are made available to the outside world through its attributes.

Core idea behind __program architecture__ in Python - module based services model.

The __import__ operation works only once per session (i.e. per process ) by default. After the first import, later imports do nothing, even if you change and save the module's source file again in another window. This is by design; imports are too expensive an operation to repeat more than once per file, per program run. [Import must find files, compile them to byte code and run the code].
```
D:\LearningPython\CodeSamples> python
>>> import script1
win32
1267650600228229401496703205376
Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!

>>> import script1
>>> import script1
>>>
```

To force the Python to run the file again in the same session without stopping and restarting the session, the function *__reload__* available in the __imp__ standard library module can be called.
``` Python
>>> from imp import reload      # Must load from module in 3.X (only)
>>> reload(script1)
win32
65536
Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!
<module 'script1' from 'D:\\LearningPython\\CodeSamples\\script1.py'>
```
In 3.X, the reload built-in is moved to imp standard library module. So, it can be used in following way also:
```Python
import imp
imp.reload(M)
```

The __from__ statement opies a name out of a module. The __reload__ function itself loads and runs the current version of the file's code, picking up the changes done.

The _reload_ function expects the name of an already, successffully, loaded module object. So, the module should be successfully imported before reloading it.
Also, _reload_ also expects a parenthesis around the module object name as it is a function, while _import_ is a statement. That's why reload returns an output - a Python module object.

Reloads aren't transitive - reloading a module reloads that module only, not any modules it may import - so sometimes, we may have to reload multiple files.

## Attributes
A module is a package of variable names, known as _namespace_, and the names within that package are called _attributes_.
An attribute is a variable name that is attached to a specific object (like a module).

Importers gain accesss to all the names assigned at the top level of a module's file. These names are usually assigned to tools exported by the module - functions, classes, variables etc - that are intended to be used in other files and other programs.

Externally, a module file's names can be fetched in the following ways:
1. Using the _import_ statement
2. Using the _from_ statement
3. Using the _reload_ call

Example:-

```
myFile.py

title = "The Meaning of Life"
```
When this file, myFile.py is imported, it's code is run to generate the module's attribute. i.e. the assignment statement creates a variable and module attribute named 'title'.

The attribute can be accessed in two ways:

```Python
>>> import myFile       # Run file; load module as a whole
>>> myFile.title        # Use it's attributes names: '.' to qualify
'The Meaning of Life'
>>>
```
Or
```Python
>>> from myFile import title    # Run file, copy it's names
>>> title                       # Use name directly, no need to qualify
'The Meaning of Life'
>>>
```
Technically, the _from_ statement copies a module's attributes, such that they become simple variables in the recipient. 

In practice, module files usually define more than one name to be used in and out. (Refer the sample code "threeNames" for the usage). That file assigns three variables and so generates three attributes for the outside world.

### Modules and Namespaces
Each module itself is a self-contained namespace.
One module file cannot see the names defined in another file, unless it is imported explicitly. Therefore, modules serve to minimize name collisions.

## Using _exec_ to Run Module Files
The _exec(open('module.py').resd())_ built-in function call is another way to launch files from the interactive prompt without having to import and later reload. 
Each such _exec_ runs the current version of the code read from the file, without requiring later reloads.
The exec call has an effect similar to import, but it doesn't actually import the module.
Each time, a call to exec runs the file's code anew, as though the code is pasted at the place of exec. That's why exec does not require module reloads after the file changes - it skips the normal import logic.

Disadvantage:
Like the _from_ statement, _exec_ has the potential to silently overwrite the variable that are being used currently. 

Sample Code: UsingExec

