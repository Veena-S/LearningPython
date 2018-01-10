# Quiz 1
# Consider the following three statements. Do they change the value printed for A?
A = "spam"
B = A
B = "shrubbery"
A
# Result: 'spam'
B
# Result: 'shrubbery'
# Answer:  No: A still prints as "spam". When B is assigned to the
#string "shrubbery", all that appens is that the variable B is reset to
#point to the new string object. A and B nitially share (i.e.,
#reference/point to) the same single string object "spam", but two ames
#are never linked together in Python. Thus, setting B to a different
#object has o effect on A. The same would be true if the last statement
#here were B = B + shrubbery', by the way—the concatenation would make a
#new object for its result, hich would then be assigned to B only. We
#can never overwrite a string (or number, r tuple) in place, because
#strings are immutable.



# Quiz 2:
# Consider these three statements. Do they change the printed value of A?
A = ["spam"]
A
# Result: ['spam']
B = A
B
# Result: ['spam']
B[0] = "shrubbery"
B
# Result: ['shrubbery']
A
# Result: ['shrubbery']
##Answer: Yes: A now prints as ["shrubbery"]. Technically, we haven’t
##really changed either A or B; instead, we’ve changed part of the object
##they both reference (point to) by overwriting that object in place
##through the variable B. Because A references the same object as B, the
##update is reflected in A as well.


# Quiz 3:
# How about these—is A changed now?
A = ["spam"]
B = A[:]
B[0] = "shrubbery"
A
# Result: ['spam']
B
# Result: ['shrubbery']
# Answer:  A is not changed.
##No: A still prints as ["spam"]. The in-place assignment through B has no
##effect this time because the slice expression made a copy of the list
##object before it was assigned to B. After the second assignment
##statement, there are two different list objects that have the same value
##(in Python, we say they are ==, but not is). The third statement changes
##the value of the list object pointed to by B, but not that pointed to by
##A.

