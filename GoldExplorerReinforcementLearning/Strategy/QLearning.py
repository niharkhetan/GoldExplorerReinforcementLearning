'''
Created on Nov 6, 2015

@author: NiharKhetan, Ghanshyam Malu
'''

from World.Grid import Grid
from World.GridWorld import GridWorld, screenWidth
from Strategy.PrintGridWorld import printGrids
import sys
import random

def randChoiceList(weighted_choices):
    ''' Random Weighted List '''    
    population = [val for val, cnt in weighted_choices for i in range(int(cnt*10))]
    return population

def isConverged(oldGridMatrixValue,newGridMatrixValue):
    ''' Check for convergence'''
    for i in range(5): 
        for j in range(4):
            for k in range(4):
                diff = newGridMatrixValue[i][j][k]-oldGridMatrixValue[i][j][k]
            if diff != 0:
                return False
    return True

def getGridWorldQValues(gWorld):
    ''' Get Matrix Value'''
    gMatValue = []
    for i in range(0, 5):
        subList = [] 
        for j in range(0, 4):
            currGrid = gWorld.getGrids()[i][j]
            subList.append([currGrid.getQLeft(),currGrid.getQRight(),currGrid.getQUp(),currGrid.getQDown()])           
        gMatValue.append(subList)
    return gMatValue

def updateGridQValue(currGrid, nextGridDirection, newQValofCurrGrid):
    ''' Update the given Q Value of the grid'''    
    if nextGridDirection == 'up':
        currGrid.setQUp(newQValofCurrGrid)
        
    elif nextGridDirection == 'down':
        currGrid.setQDown(newQValofCurrGrid)
    
    elif nextGridDirection == 'left':
        currGrid.setQLeft(newQValofCurrGrid)
    
    elif nextGridDirection == 'right':
        currGrid.setQRight(newQValofCurrGrid)
    
def getQValueforCurrGrid(currGrid, direction):
    ''' Get the Q Value of the current grid for the given direction '''
    
    if direction == 'up':
        qValue = currGrid.getQUp()
        
    elif direction == 'down':
        qValue = currGrid.getQDown()
        
    elif direction == 'left':
        qValue = currGrid.getQLeft()
        
    elif direction == 'right':
        qValue = currGrid.getQRight()
    
    return qValue
    
def getNextGridBasedOnDirectionalProbability(currGrid, direction):
    # For a given direction, getting a probable direction. Ex : For Up, 0.8 chance of Up and 0.2 chance of Left
    probableDirectionsForASpecificDirection = randChoiceList([(direction,prob) for direction,prob in gWorld.getMovement()[direction].iteritems()])
    finalProbableActionChoice = random.choice(probableDirectionsForASpecificDirection)
    
    # Get the next grid based on the given direction
    nextGrid = gWorld.getNextGrid(currGrid,finalProbableActionChoice)
    return finalProbableActionChoice, nextGrid
    
def explore(currGrid, gWorld):
    ''' Explore a random direction from a given currGrid in the gWorld ''' 
    # A random direction from the list of all directions
    randomDirection = random.choice(gWorld.getMovement().keys())

    finalProbableActionChoice, nextGrid = getNextGridBasedOnDirectionalProbability(currGrid, randomDirection)
    return finalProbableActionChoice, nextGrid
    
def exploit(currGrid, gWorld):
    ''' Exploit the Q Values of the current grid to choose the maximum Qvalue direction and the corresponding the next grid'''    
    currGridAllQValuesList = sorted([(qValue,direction) for direction,qValue in currGrid.getAllQValues().iteritems()],reverse=True) 
    maxQValueDirection = currGridAllQValuesList[0][1] # First element would be maximum for a reverse sorted list
    
    finalProbableActionChoice, nextGrid = getNextGridBasedOnDirectionalProbability(currGrid, maxQValueDirection)
    return finalProbableActionChoice, nextGrid
       
def qLearn():
        
    global epsilon
    # Counters
    iterationCount = 0
    episodeCount=0
    
    currGrid = gWorld.getGrids()[0][0]   
    epsilon_choices = randChoiceList([('explore', epsilon), ('exploit', 1-epsilon )])
    
    sys.stdout.write('\n\tIterating.') if printDebugStatementsFlag == False else None

    while True:

        oldGridMatrixValue = getGridWorldQValues(gWorld) # To Check for convergence        
        episodeCount +=1
        goalTraversedFlag = False
        
        sys.stdout.write('\n{:^{screenWidth}}\n'.format('{:#^{w}}'.format(' Episode #'+str(episodeCount)+" ", w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None
        
        if episodeCount % 100 == 0 :
            epsilon = epsilon / (1 + epsilon)
            sys.stdout.write('\n\n{:^{screenWidth}}\n'.format('{:<{w}}'.format('***Updating epsilon to:'+ str(epsilon)+" ", w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None
        
        while True:
                                    
            if currGrid.isGoal():
                sys.stdout.write('\n{:^{screenWidth}}\n'.format('{:<{w}}'.format('***Goal Reached Once, setting the flag', w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None
                goalTraversedFlag = True
            
    
            sys.stdout.write('\n{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None
            sys.stdout.write('\n{:^{screenWidth}}'.format('{:<{w}}'.format(" Current Grid: "+ str(currGrid.getGridName())+ "\tQ Value : " + str(currGrid.value) + "\tReward : " + str(currGrid.gridReward), w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None
            sys.stdout.write('\n{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None
    
            if currGrid.isBlocked():
                sys.stdout.write('\n{:^{screenWidth}}'.format('{:<{w}}'.format('Blocked Grid... Skipping', w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None
                 
            else:                
                iterationCount +=1 
                
                if iterationCount % 200 == 0:
                    sys.stdout.write(".") if printDebugStatementsFlag == False else None  
                if iterationCount % 10500 == 0:
                    sys.stdout.write("\n\t") if printDebugStatementsFlag == False else None
            
                sys.stdout.write('\n{:^{screenWidth}}\n'.format('{:#^{w}}'.format(' Iteration #'+str(iterationCount)+" ", w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None
                
                exploitOrExplore = random.choice(epsilon_choices)
                
                if exploitOrExplore == 'explore':
                    sys.stdout.write('\n{:^{screenWidth}}\n'.format('{:<{w}}'.format('*****Exploring', w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None
                    nextGridDirection,nextGrid = explore(currGrid, gWorld)
                elif exploitOrExplore == 'exploit':
                    sys.stdout.write('\n{:^{screenWidth}}\n'.format('{:<{w}}'.format('*****Exploiting', w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None
                    nextGridDirection,nextGrid = exploit(currGrid, gWorld)
                    
                allQValuesOfNextGrid = [nextGrid.getQLeft(),nextGrid.getQRight(),nextGrid.getQUp(),nextGrid.getQDown()]
                maxQValueNextGrid = max(allQValuesOfNextGrid)

                sys.stdout.write('\n{:^{screenWidth}}'.format('{:<{w}}'.format("Action Chosen \t: "+ nextGridDirection+ "\tNextGrid : ("+ nextGrid.getGridName()+")" , w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None
                sys.stdout.write('\n{:^{screenWidth}}'.format('{:<{w}}'.format("All QValues Of NextGrid : "+ ','.join([str(round(v,3)) for v in allQValuesOfNextGrid])+ "\tMax : " + str(maxQValueNextGrid), w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None

                # Compute the Q(s,a) 
                qValofCurrGrid = getQValueforCurrGrid(currGrid, nextGridDirection) 
                newQValofCurrGrid = qValofCurrGrid + alpha * (currGrid.getGridReward() + (gamma * maxQValueNextGrid) - qValofCurrGrid)  
                
                # Update Q Value of the current grid for the corresponding direction
                updateGridQValue(currGrid, nextGridDirection, newQValofCurrGrid)
                sys.stdout.write('\n{:^{screenWidth}}'.format('{:<{w}}'.format("Using the Q(s,a) equation, updated Grid "+ currGrid.getGridName()+"'s "+ nextGridDirection+" QValue to : "+ str(newQValofCurrGrid), w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None
                    
                # Update current grid
                currGrid = nextGrid
                
                if goalTraversedFlag == True:
                    sys.stdout.write('\n{:^{screenWidth}}\n'.format('{:<{w}}'.format("Goal Reached", w = screenWidth-10), screenWidth=screenWidth)) if printDebugStatementsFlag == True else None
                    break

                if printDebugStatementsFlag:
                    printGrids(gWorld)
                    print "\n\n"

        
        currGrid = gWorld.getGrids()[0][0]

        newGridMatrixValue = getGridWorldQValues(gWorld)
        convergedFlag = isConverged(oldGridMatrixValue,newGridMatrixValue)
                  
        if convergedFlag == True:
            print '\n\n{:^{screenWidth}}'.format('{:%^{w}}'.format(" Total # of Iterations\t:" + str(iterationCount)+" ", w = screenWidth-20), screenWidth=screenWidth)
            print '\n{:^{screenWidth}}\n'.format('{:%^{w}}'.format(" Total # of Episodes\t:" + str(episodeCount)+" ", w = screenWidth-20), screenWidth=screenWidth)            
            break
                        
def qLearnMain(gWorldArg, gammaArg, alphaArg, epsilonArg, printDebugStatementsFlagArg, screenWidthArg):
    global gWorld, screenWidth, printDebugStatementsFlag
    global gamma, alpha, epsilon
    
    gWorld = gWorldArg
    screenWidth = screenWidthArg
    printDebugStatementsFlag = printDebugStatementsFlagArg

    # Q Learning Parameters
    gamma = gammaArg
    alpha = alphaArg
    epsilon = epsilonArg    

    print '{:^{screenWidth}}'.format('{:=^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)
    print '{:^{screenWidth}}'.format('{:^{w}}'.format('Welcome to Gold Explorer Using Reinforcement Learning  - Q Learning', w = screenWidth-10), screenWidth=screenWidth)
    print '{:^{screenWidth}}'.format('{:=^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)    
    print 
   
    qLearn()
    gWorld.printGridWorldRewardMatrix() 
    printGrids(gWorld)
    gWorld.printGridWorldOptimumPolicyQValue()

    print '{:^{screenWidth}}'.format('{:=^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)
    print '{:^{screenWidth}}'.format('{:^{w}}'.format('Thank you for using Gold Explorer Using Reinforcement Learning - Q Learning', w = screenWidth-10), screenWidth=screenWidth)
    print '{:^{screenWidth}}'.format('{:=^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)    
    print 

if __name__ == '__main__':
    # Creating a sample world
    grid1 = Grid(1, -1)
    grid2 = Grid(2, -1)
    grid3 = Grid(3, -1)
    grid4 = Grid(4, -1)
    grid5 = Grid(5, -1)
    grid6 = Grid(6, 0, True)
    grid7 = Grid(7, -1)
    grid8 = Grid(8, 0, True)
    grid9 = Grid(9, -1)
    grid10 = Grid(10, -1)
    grid11 = Grid(11, -1)
    grid12 = Grid(12, -1)
    grid13 = Grid(13, -1)
    grid14 = Grid(14, -50)
    grid15 = Grid(15, -1)
    grid16 = Grid(16, -1)
    grid17 = Grid(17, -1)
    grid18 = Grid(18, -1)
    grid19 = Grid(19, -1)
    grid20 = Grid(20, 10)
    grid20.setGoal()
    
    
    gWorld = GridWorld([[grid1,grid2,grid3,grid4],[grid5,grid6,grid7,grid8],[grid9,grid10,grid11,grid12],[grid13,grid14,grid15,grid16],[grid17,grid18,grid19,grid20]])
    gWorld.setMovement({"left":{"left":1}, "right":{"right":0.8, "down":0.2}, "up":{"up":0.8, "left":0.2}, "down":{"down":1}})

    printDebugStatementsFlag = True
    screenWidthArg = 90
    
    # Q Learning Parameters
    gamma = 0.9
    alpha = 0.1
    epsilon = 0.9
    qLearnMain(gWorld,gamma,alpha, epsilon, printDebugStatementsFlag,screenWidthArg )