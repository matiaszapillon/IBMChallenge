import re
import numpy

print("Starting program")

splittedInputString = (input("Input the rover's instructions.\n")).split(' ') # Ej: "5 5 1 2 N LMLMLMLMM 3 3 E MMRMMRMRRM 1 1 W RLRRMLLLM 1 2 N RLRRMLLLM"
plateauGrid = int(splittedInputString[0]),int(splittedInputString[1]) 
roversInstructions = splittedInputString[2:] #get the input related to rover's instructions without taking into account the upper-right coordinates of the plateau
size = len(roversInstructions)
numberOfRovers = size / 4 #Each rover is contained in every 4 elements (Position, heading, instructions) Ej: [0,1,M,RLLRM] => 1 Rover
roversInstructions = numpy.array_split(roversInstructions, numberOfRovers)

class Rover:
    def __init__(self, position, heading, instructions):
        self.position = position
        self.heading = heading
        self.instructions = instructions

roverList = []

for rover in roversInstructions:
    roverPosition = [int(rover[0]),int(rover[1])]
    roverHeading = rover[2]
    roverInstructions = rover[3]
    roverList.append(Rover(roverPosition, roverHeading, roverInstructions))


def split(instructions):
 return [char for char in instructions];

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
    if instruction == 'M':
        rover.position[0] -= 1
    
def calculateNewCoordinateFromNorth(instruction,rover): 
    if instruction == 'M' and rover.position[1] < plateauGrid[1]:
        rover.position[1] += 1

def calculateNewCoordinateFromSouth(instruction,rover): 
    if instruction == 'M':
        rover.position[1] -= 1

def calculateNewCoordinateFromEast(instruction,rover): 
    if instruction == 'M' and rover.position[0] < plateauGrid[0]:
        rover.position[0] += 1

for rover in roverList:

    instructionsInArray = split(rover.instructions);
    for instruction in instructionsInArray:
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


def showResults(roverObjectList):
    output = ''
    for rover in roverList:
        print(rover.position)
        print(rover.heading)
        #output = output + rover.position
        #output = output + rover.heading + ' '
    #print(output)     

showResults(roverList)

