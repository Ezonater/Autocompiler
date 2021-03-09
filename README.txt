- Make sure you are in Python 3.6 (I am using 3.6.5)
- Make a new Virtual Environment
- Go into the terminal and clone the git repository
- Go to Settings, Project:, and Python Interpreter
- Click the plus button and add tensorflow
	- Make sure to check the specify version button and choose "1.14.0"
- Add librosa
	- Choose version "0.7.0"
- Add numpy
	- Choose version "1.19.2"

- Make sure you are in the musicnn folder in the terminal
- run "python setup.py install --user"

- Add musicnn in the same place you added tensorflow
- Uninstall the current numba (version 0.52)
- Install numba
	- Choose version "0.48"