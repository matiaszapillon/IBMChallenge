import re
import numpy

print("Starting program")

splitedInputString = (input("Input the rover's instructions.\n")).split(' ') # Ej: "5 5 1 2 N LMLMLMLMM 3 3 E MMRMMRMRRM 1 1 W RLRRMLLLM"
plateauGrid = int(splitedInputString[0]),int(splitedInputString[1]) 
roversInstructions = splitedInputString[2:] #get the input related to rover's instructions without taking into account the upper-right coordinates of the plateau
size = len(roversInstructions)
numberOfRovers = size / 4 #Each rover is contained in every 4 elements (Position, heading, instructions) Ej: [0,1,M,RLLRM] => 1 Rover
roversInstructions = numpy.array_split(roversInstructions, numberOfRovers)

print(roversInstructions)
print(roversInstructions[0])
print(roversInstructions[1])
print(roversInstructions[2]) 

class Rover:
    def __init__(self, position, heading, instructions):
        self.position = position
        self.heading = heading
        self.instructions = instructions

my_objects = []

for rover in roversInstructions:
    roverPosition = [int(rover[0]),int(rover[1])]
    roverHeading = rover[2]
    roverInstructions = rover[3]
    my_objects.append(Rover(roverPosition, roverHeading, roverInstructions))


#currentCoordinate = input("Input coordinates.\n")
#currentCoordinate = [1,2]
#currentHeading = input("Input heading.\n")
currentHeading = ''
currentCoordinate = []
#instructions = input("Input instructions\n")
#plateauGrid = [5,6]

def split(instructions):
 return [char for char in instructions];

#Heading
def calculateNewHeadingFromWest(position,rover): 
    print("Oeste")
    if position == 'R':
        rover.heading = 'N' #North
    elif position == 'L':
        rover.heading = 'S' #South
    
def calculateNewHeadingFromNorth(position,rover): 
    print("Norte")
    if position == 'R':
        rover.heading = 'E' #East
    elif position == 'L':
        rover.heading = 'W' #West

def calculateNewHeadingFromSouth(position,rover): 
    print("Sur")
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
        print("Calculo posicion Oeste")
        rover.position[0] -= 1
        print(rover.position)
        #return rover.position;
    #else: return rover.position
    
def calculateNewCoordinateFromNorth(instruction,rover): 
    if instruction == 'M':
        print("Calculo posicion Norte")
        if(rover.position[1] < plateauGrid[1]): 
            rover.position[1] += 1
        #return rover.position;
    #else: return rover.position

def calculateNewCoordinateFromSouth(instruction,rover): 
    if instruction == 'M':
        print("Calculo posicion Sur")
        rover.position[1] -= 1
        #return rover.position;
    #else: return rover.position

def calculateNewCoordinateFromEast(instruction,rover): 
    if instruction == 'M':
        print("Calculo posicion Este")
        if(rover.position[0] < plateauGrid[0]): 
            rover.position[0] += 1
        #return rover.position;
    #else: return rover.position

for rover in my_objects:

    instructionsInArray = split(rover.instructions);
    print(rover.position)
    print(rover.heading)
    print(rover.instructions)

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
    for rover in my_objects:
        print(rover.position)
        print(rover.heading)
        #output = output + rover.position
        #output = output + rover.heading + ' '
    #print(output)     

showResults(my_objects)

