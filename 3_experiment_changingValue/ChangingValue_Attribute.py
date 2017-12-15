Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: D:\LearningPython\CodeSamples\myFile\myFile.py ==========
>>> title
'The Meaning of Life'
>>> title = "Hii hello"
>>> title
'Hii hello'
>>> 
========== RESTART: D:\LearningPython\CodeSamples\myFile\myFile.py ==========
>>> title
'The Meaning of Life'
>>> import myFile
>>> myFile.title
'The Meaning of Life'
>>> myFile.title = "Try try"
>>> myFile.title
'Try try'
>>> import myFile
>>> myFile.title
'Try try'
>>> reload(myFile)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    reload(myFile)
NameError: name 'reload' is not defined
>>> import imp
>>> imp.reload(myFile)
<module 'myFile' from 'D:\\LearningPython\\CodeSamples\\myFile\\myFile.py'>
>>> myFile.title
'The Meaning of Life'
>>> 
