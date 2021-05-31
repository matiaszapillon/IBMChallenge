import tkinter as tk
root = tk.Tk()
root.geometry("1080x720")
root.title(string="IBM Challenge")

titleLabel = tk.Label(root,text = "Welcome to IBM Challenge")

titleLabel.grid(padx=25,row=0, column=0)

gridInputLabel = tk.Label( text = "Input grid dimensions")
gridInputLabel.grid(pady=25,row=1, column=0)

gridentry = tk.Entry(root, width=10)
roverInputEntry = tk.Entry(root, width=10) 
roverInputInstructionEntry = tk.Entry(root, width=15)
roverInitialPositionEntry = tk.Entry(root,width = 10)
roverFinalPositionEntry = tk.Entry(root,width = 10)

gridentry.grid(row=1, column=1)

class Rover:
    def __init__(self, position, heading, instructions):
        self.position = position
        self.heading = heading
        self.instructions = instructions

rover = Rover([0,0], '', '')

#Grid dimensions
plateauGrid = [0,0]
def createGrid(plateauGrid):
    columns = plateauGrid[0] + 1 
    rows = plateauGrid[1] + 1
    #Start PlateauGrid in row 3

    #Define numbers in rows/columns
    for c in range(columns):
        tk.Label(root, text=(c)).grid(padx=25,row= rows + 5, column=c+1)

    for r in range(rows):
        tk.Label(root, text=(rows -1 - r)).grid(pady=25,row=r+5, column=0)

    #Define cells inside the grid    
    for r in range(0, rows):
        for c in range(0, columns):
            cell = tk.Entry(root, width=10, state='disabled')
            cell.grid(row=r+5, column=c+1)
            cell.insert(0, '({}, {})'.format(r, c))

    initialRow = rows + 6
    createRoverInitialPositionButton(initialRow)
    createRoverInstructionsButton(initialRow + 1)

def createRoverInitialPositionButton(initialRow):
    roverPosition = tk.Label( text = "Input Rover initial position")
    roverPosition.grid(pady=25,row=initialRow, column=0)

    roverInputEntry.grid(padx=5,pady=25, row= initialRow, column=1)
    
    insertRoverPositionButton = tk.Button(root, text = "Insert values", command = lambda: setRoverInitialPosition(initialRow -2)) #-2 to start in coordinates y=0
    insertRoverPositionButton.grid(row=initialRow, column=3)

def createRoverInstructionsButton(initialRow):
    roverInstructions = tk.Label( text = "Input Rover instructions")
    roverInstructions.grid(pady=25,row=initialRow, column=0)

    roverInputInstructionEntry.grid(padx=5,pady=25, row= initialRow, column=1)
    
    insertRoverInstructionsButton = tk.Button(root, text = "Insert values", command = lambda: setRoverFinalPosition(initialRow - 3)) #-3 to start in coordinates y=0
    insertRoverInstructionsButton.grid(row=initialRow, column=3)

def setRoverInitialPosition(y):    
    roverPosition = roverInputEntry.get().split(' ')
    xRover = int(roverPosition[0])
    yRover = int(roverPosition[1])
    rover.position = [int(roverPosition[0]),int(roverPosition[1])]
    rover.heading = roverPosition[2]
    heading = roverPosition[2]
    entry_text = tk.StringVar()
    roverInitialPositionEntry = tk.Entry(root, width=10, state='disabled', textvariable=entry_text)
    new_text = "Rover("+heading +")"
    entry_text.set(new_text)
    roverInitialPositionEntry.grid(row=y - yRover, column=xRover+1)

def split(instructions):
 return [char for char in instructions];

def setRoverFinalPosition(y):
    print("setRoverFinalPosition()\n")
    rover.instructions = split(roverInputInstructionEntry.get())
    calculateFinalPosition()
    showRoverInFinalPosition(y)

def showRoverInFinalPosition(y):
    entry_text = tk.StringVar()
    roverFinalPositionEntry = tk.Entry(root, width=10, state='disabled', textvariable=entry_text)
    new_text = "Rover("+rover.heading +")"
    entry_text.set(new_text)
    roverFinalPositionEntry.grid(row=y - rover.position[1], column=rover.position[0]+1)
    


    print("rover input")
    print(roverInputEntry.get())
    print((roverInputEntry.get()).split(' '))
    splittedRoverInput = roverInputEntry.get().split(' ')
    xRoverInitial = int(splittedRoverInput[0])
    yRoverInitial = int(splittedRoverInput[1])
    entryRoverInitialPositionText = tk.StringVar()
    roverInitialPositionEntry = tk.Entry(root, width=10, state='disabled', textvariable=entryRoverInitialPositionText)
    cleanText = ""
    entryRoverInitialPositionText.set(cleanText)
    roverInitialPositionEntry.grid(row=y - yRoverInitial, column=xRoverInitial+1)
    print(xRoverInitial)
    print(yRoverInitial)
    print(roverInputEntry.get())


def setGridDimensions():
    splittedInput = gridentry.get().split(' ')
    global plateauGrid 
    plateauGrid = int(splittedInput[0]),int(splittedInput[1])
    createGrid(plateauGrid)

insertGridDimensionsButton = tk.Button(root, text = "Insert values", command = setGridDimensions)
insertGridDimensionsButton.grid(padx=25, row=1, column=3)

#Heading
def calculateNewHeadingFromWest(position,rover): 
    if position == 'R':
        rover.heading = 'N' #North
    elif position == 'L':
        rover.heading = 'S' #South
    
def calculateNewHeadingFromNorth(position,rover): 
    if position == 'R':
        rover.heading = 'E' #East
    elif position == 'L':
        rover.heading = 'W' #West

def calculateNewHeadingFromSouth(position,rover): 
    if position == 'R':
        rover.heading = 'W' #West
    elif position == 'L':
        rover.heading = 'E' #East

def calculateNewHeadingFromEast(position,rover): 
    if position == 'R':
        rover.heading = 'S' #South
    elif position == 'L':
        rover.heading = 'N' #North

#Position
def calculateNewCoordinateFromWest(instruction,rover): 
    if instruction == 'M' and rover.position[0] > 0:
        rover.position[0] -= 1
    
def calculateNewCoordinateFromNorth(instruction,rover): 
    if instruction == 'M' and rover.position[1] < plateauGrid[1]:
        rover.position[1] += 1

def calculateNewCoordinateFromSouth(instruction,rover): 
    if instruction == 'M' and rover.position[1] > 0:
        rover.position[1] -= 1

def calculateNewCoordinateFromEast(instruction,rover): 
    if instruction == 'M' and rover.position[0] < plateauGrid[0] :
        rover.position[0] += 1


def calculateFinalPosition():
    for instruction in rover.instructions:
        print(rover.position)
        print(rover.heading)
        if rover.heading == 'W':
            calculateNewCoordinateFromWest(instruction,rover)
            calculateNewHeadingFromWest(instruction,rover)

        elif rover.heading == 'N':
            calculateNewCoordinateFromNorth(instruction,rover)
            calculateNewHeadingFromNorth(instruction,rover)

        elif rover.heading == 'S':
            calculateNewCoordinateFromSouth(instruction,rover)
            calculateNewHeadingFromSouth(instruction,rover)

        else: #Must be 'E' 
            calculateNewCoordinateFromEast(instruction,rover)
            calculateNewHeadingFromEast(instruction,rover)

    
    

    print(roverInputEntry)
    print(roverInputEntry.get())
    print(rover.position)
    print(rover.heading)
    print(rover.instructions)


root.mainloop()

