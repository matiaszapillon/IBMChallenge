# IBMChallenge
Exercise for IBM in python


Required:
- numpy
- python v >= 3.0


Guide instalation Linux (Debian based) environment:

- sudo apt install python3-pip
- pip3 install numpy
- sudo apt-get install python3-tk #Exercise with GUI Interface
- python3 startChallenge.py
- python3 startChallengeGUI.py



How to test 'startChallenge.py':
- Run the file:
    python3 startChallenge.py
- Input the upper-right coordinates of the plateau and the position,heading and instructions for each rover.
    ej: 5 5 1 2 N LMLMLMLMM 3 3 E MMRMMRMRRM 1 1 W RLRRMLLLM 1 2 N RLRRMLLLM
- See the result in console.
    Ej expected output: 1 3 N 5 1 E 2 0 S 0 1 W 


How to test 'startChallengeGUI.py'
- Run the file:
    python3 startChallengeGUI.py
- Input the dimensions of the plateau grid and press 'Create GRID' button.
    Ej: 5 5
- Input the initial position of the Rover with the current heading and press 'Insert initial position'.
    Ej: 1 3 N
- Input the instructions of the Rover and press 'Run instructions'.
    Ej: RLRRMLLLM
- The rover will appear in the grid with the current Heading.
