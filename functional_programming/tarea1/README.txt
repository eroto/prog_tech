This read me file is for "Tarea 1" Building a Monad-Based Stream Processing Framework
Student developer: Eng. Enrique Rodriguez Toscano

Content

README.txt
This File

fp.py
This file contains the implementation of a monad the monad is implemented in a MyMonadClass it implements it how filter and map methods, to differentiate from the built-in map and filter functions the method are called flap_map and flat_filter, flat since they do not need parameter as the monad vale are used
Required packages are
	functools
	itertools
	collections
	requests
	time
	random
	string
This packager are already included in the provided virutal bos and there is no need to install any package.
To tun the program execute "python fp.py"
Is required to have internet connection since the programs fetches data from "https://api.github.com/events" and analyze the "PushEvents" messages

example:
Total PushEvents:18
Total words:82
Most common words:[('update', 7), ('for', 3), ('add', 2)]
PushEvent avg word length:4.555555555555555
next request in: 5.10585604739769
press Ctrl+Z to stop the program

test_fp.py
This is the file that contains the unit test
it contains 5 test cases to test they key functionality of the monad.
it requires unittest package from python, since this is a build in module there is no need to install any additional package-
to run the unit test fp.py and test_fp.py shall be in the same folder, then go to the path where the zip flat extracted and run the command "python3 -m unittest test_fp.py"
