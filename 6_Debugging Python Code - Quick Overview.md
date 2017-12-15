Strategies commonly used to debug Python Code:

1. Do nothing:- Read the error message, ao and fix the tagged line and file.

2. Insert _print_ statements

3. Use IDE GUI debuggers

4. Use the pdb command-line debugger:- Python comes with a source code debugger names _pdb_, available as a module in Python's standard library. In pdb, you type commands to step line by line, display variables, set and clear breakpoints, continue to a breakpoint or error and so on. You can launch pdb interactively by importing it or as a top-level script. 
  pdb also includes a postmortem function (pdb.pm()) that you can run after an exception occurs, to get information from the time of error.
 
5. Use Python's _-i_ command-line argument:- If the script is run from a command lineand pass a -i argument between _python_ and the name of the script (e.g: python -i m.py), Python will enter into its interactive interpreter mode (the >>> prompt) when your script exits, whether it ends successfully or runs into an error. At this point, the final values of the variables can be printed to get more details about what happened in the code because they are in top-level namespace. You can also then import and run the pdb debugger; its postmortem mode will let to inspect the latest error if your script failed.

6. Other options: Check for additional tools in open source domain - e.g: Windpdb system
