import tkinter as tk
root = tk.Tk()
root.geometry("1080x720")
root.title(string="IBM Challenge")

titleLabel = tk.Label(root,text = "Welcome to IBM Challenge")

titleLabel.grid(padx=25,row=0, column=0)

gridInputLabel = tk.Label( text = "Input grid dimensions")
gridInputLabel.grid(pady=25,row=1, column=0)

gridentry = tk.Entry(root, width=10)
roverEntry = tk.Entry(root, width=10)

gridentry.grid(row=1, column=1)

#Grid dimensions
plateauGrid = [0,0]
def createGrid(plateauGrid):
    columns = plateauGrid[0] + 1 
    rows = plateauGrid[1] + 1
    #Start PlateauGrid in row 3

    for c in range(columns):
        tk.Label(root, text=(c)).grid(padx=25,row= rows + 5, column=c+1)

    for r in range(rows):
        tk.Label(root, text=(rows -1 - r)).grid(pady=25,row=r+5, column=0)
        
    for r in range(0, rows):
        for c in range(0, columns):
            cell = tk.Entry(root, width=10, state='disabled')
            cell.grid(row=r+5, column=c+1)
            cell.insert(0, '({}, {})'.format(r, c))

    initialRow = rows + 6
    createRoverInitialPositionButton(initialRow)

def createRoverInitialPositionButton(initialRow):
    roverPosition = tk.Label( text = "Input Rover initial position")
    roverPosition.grid(pady=25,row=initialRow, column=0)

    roverEntry.grid(padx=5,pady=25, row= initialRow, column=1)
    
    insertRoverPositionButton = tk.Button(root, text = "Insert values", command = lambda: setRoverInitialPosition(initialRow -2)) #-2 to start in coordinates y=0
    insertRoverPositionButton.grid(pady=25,row=initialRow, column=3)

def setRoverInitialPosition(y):    
    roverPosition = roverEntry.get().split(' ')
    xRover = int(roverPosition[0])
    yRover = int(roverPosition[1])

    entry_text = tk.StringVar()
    entry = tk.Entry(root, width=10, state='disabled', textvariable=entry_text)
    new_text = "Rover"
    entry_text.set(new_text)
    entry.grid(row=y - yRover, column=xRover+1)

def setGridDimensions():
    splittedInput = gridentry.get().split(' ')
    plateauGrid = int(splittedInput[0]),int(splittedInput[1])
    createGrid(plateauGrid)

insertGridDimensionsButton = tk.Button(root, text = "Insert values", command = setGridDimensions)
insertGridDimensionsButton.grid(padx=25, row=1, column=3)


root.mainloop()

