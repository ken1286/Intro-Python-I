"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for x in sys.argv:
    print(x)

# Print out the OS platform you're using:
# YOUR CODE HERE
print(sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(os.getpid())
# YOUR CODE HERE

# Print the current working directory (cwd):
print(os.getcwd())
# YOUR CODE HERE

# Print out your machine's login name
print(os.getlogin())
# YOUR CODE HERE
