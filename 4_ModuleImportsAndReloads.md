### Import and Reload basics
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
```
>>> from imp import reload      # Must load from module in 3.X (only)
>>> reload(script1)
win32
65536
Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!
<module 'script1' from 'D:\\LearningPython\\CodeSamples\\script1.py'>
```
The __from__ statement here simply copies a name out of a module. The __reload__ function itself loads and runs the current version of the file's code, picking up changes.
