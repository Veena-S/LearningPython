exec(open('script1.py').read())

### Result
#win32
#65536
#Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!

#Change the script1.py to print 2 ** 32

exec(open('script1.py').read())

### Result
#win32
#65536
#4294967296
#Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!


# Checking the capability of changing overwriting the variable values that are currently using
x = 99
exec(open('script1.py').read())

#### Result
#win32
#65536
#4294967296
#Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!

print(x)
#### Result
#'Spam!'
