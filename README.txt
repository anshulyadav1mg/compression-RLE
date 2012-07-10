In this folder, you'll find two Python source files.

You won't need to install any additional Python libraries in order to run either
of these modules. They're both built using the Python standard library.

1. compression.py
	A Python module that implements the described compression scheme in two functions:
		- compress(plainText)
		- decompress(compressed)
	Each of these functions have docstrings that properly explain their usage and
	error cases.

	This file cannot be run on its own. However, it is available as a Python
	module that can be imported and run from other Python scripts.

2. tests.py
	A series of unit tests, all written using the built-in Python unittest module. 

	The test cases should sufficiently cover all types of input strings.

	To run this file, simply type into your command line
	$ python tests.py
