IDLE provides a graphical user interface for Python development.

Technically, IDLE is a Python program that uses the standard library's tkinter GUI toolkit to build its windows. This makes IDLE portable.

Because IDLE is just a Python script on the module search path in the standard library, it can be run on any platform and from any directory by typing the following in a system command shell window:

```
% python -m idlelib.idle  # Run idle.py in a package on module path
```

### Basic Usage:

1. To make a new script file
2. IDLE uses syntax-directed colorization
3. To run a file of code:- Choose the _Run Module_ option for that. When run this way, the output of the script and any error messages it may generate show up back in the main interactive window. The "RESTART" message appears on the main window tells us that the user-code process was restarted to run the edited script and serves to separate script output.

### Usability Features:
1. Access to command history
   _Alt+P_ for backward scrolling and _Alt+N_ for forward scrolling
2. Syntax colrization
3. Word auto-completion, by a Tab press
4. Balloon help pop-ups for function calls when "(" is typed
5. Pop-up selection lists of object attributes when a "." is typed or tab is pressed.

### Usage Notes:
1. You must add ".py" explicitly when saving files
2. Run scripts by selectin Run->Run Module in text edit windows, not by interactive imports and reloads.
3. Need to reload only modules being tested interactively
4. Can customize IDLE
5. Currently, no clear screen option available.
6. tkinter GUI and threaded programs may not work well with IDLE
7. If connection errors arise, try starting IDLE in single-process mode - it's "-n" command line flag forces this mode.
   On Windows, start a Command Prompt window and run the system command line __idle.py -n__ from within the directory _C:\Python33\Lib\idellib_. A _python -m idlelib.idle -n_ command works from anywhere.
8. When you run a file of code. IDLE also automatically changes to file's directory and adds it to the module import search path. (It's IDLE behavior not Python.)


### Other IDEs:
1. Eclipse & PyDev
2. Komodo
3. NetBeans IDE for Python
4. PythonWin
5. Wing, Visual Studio, pyCharm, PyScripter, Pyshield and Spyder
