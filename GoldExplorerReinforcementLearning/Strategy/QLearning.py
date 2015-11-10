'''
Created on Nov 6, 2015

@author: NiharKhetan
'''

from World.Grid import Grid
from World.GridWorld import GridWorld
from Strategy.PrintGridWorld import printGrids
import sys
from random import randint
import random

def randChoiceList(weighted_choices):
    ''' Random Weighted List '''    
    population = [val for val, cnt in weighted_choices for i in range(int(cnt*100))]
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

def updateGridQValue(currGrid, maxQValueNextStateDirection, maxQValueNextState):
    ''' Update the given Q Value of the grid'''
    sys.stdout.write("\n\t"+"Updating Grid "+ currGrid.getGridName()+" "+ maxQValueNextStateDirection+ " to: "+ str(maxQValueNextState)+"\n") if printDebugStatementsFlag == True else None    
    if maxQValueNextStateDirection == 'up':
        currGrid.setQUp(maxQValueNextState)
        
    elif maxQValueNextStateDirection == 'down':
        currGrid.setQDown(maxQValueNextState)
    
    elif maxQValueNextStateDirection == 'left':
        currGrid.setQLeft(maxQValueNextState)
    
    elif maxQValueNextStateDirection == 'right':
        currGrid.setQRight(maxQValueNextState)
    
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
    
def qLearn():
    gamma = 0.9
    alpha = 0.1
    epsilon = 0.5    
    
    steps = 0
    episodeCount=0
    
#     currGrid = gWorld.getGrids()[randint(0,4)][randint(0,3)]
    currGrid = gWorld.getGrids()[0][0]   
    
    epsilon_choices = randChoiceList([('explore', epsilon), ('exploit', 1-epsilon )])
    print 

    while True:

        oldGridMatrixValue = getGridWorldQValues(gWorld) # To Check for convergence        
        episodeCount +=1
        goalTraversedFlag = False
        
        print "\n\n======================= New Episode :", episodeCount
        if episodeCount % 10 == 0 :
            epsilon = epsilon / (1 + epsilon)
            print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%Updating epsilon to:", epsilon
        
        while True:
                                    
            if currGrid.isGoal():
                print "Goal Reached Once"
                goalTraversedFlag = True
            
            print "\n\n********Curr Grid:", currGrid.getGridName()
    
            sys.stdout.write("\n"+ "-"*50) if printDebugStatementsFlag == True else None
            sys.stdout.write("\nCurrent Grid: "+ str(currGrid.getGridName())+ "\tQ Value : " + str(currGrid.value) + "\tReward : " + str(currGrid.gridReward)) if printDebugStatementsFlag == True else None
            sys.stdout.write("\n"+ "-"*50) if printDebugStatementsFlag == True else None
           #sys.stdout.write("\nPossibleTransitions: "+ ' '.join([key1 + str(val1.getGridName()) for key1,val1 in allGridsReachableFromCurGrid.iteritems()])) if printDebugStatementsFlag == True else None
    
            if currGrid.isBlocked():
                sys.stdout.write("\n\tBlocked Grid... Skipping") if printDebugStatementsFlag == True else None  
            else:
                steps +=1            
                allGridsReachableFromCurGrid = gWorld.getAllGridsReachableFromCurGrid(currGrid)
                
                exploitOrExplore = random.choice(epsilon_choices)
                
                if exploitOrExplore == 'explore':
                    sys.stdout.write("\n\t*****"+ exploitOrExplore) if printDebugStatementsFlag == True else None                
             
                    nextGridDirection,nextGrid = random.choice([(k,v) for k,v in allGridsReachableFromCurGrid.iteritems()])
    
                    allQValuesOfNextGrid = [nextGrid.getQLeft(),nextGrid.getQRight(),nextGrid.getQUp(),nextGrid.getQDown()]
                    maxQValueNextGrid = max(allQValuesOfNextGrid)
    
                    sys.stdout.write("\n\t\t"+"Random allQValuesOfNextGrid-"+ nextGridDirection+ nextGrid.getGridName()+": "+  "".join(','.join(str(v) for v in allQValuesOfNextGrid))) if printDebugStatementsFlag == True else None
                    sys.stdout.write("\t"+"Max from allQValuesOfNextGrid: " + str(max(allQValuesOfNextGrid)) ) if printDebugStatementsFlag == True else None
    
                    sys.stdout.write("\n\t"+"nextGridDirection: "+ nextGridDirection+ "\tmaxQValueNextState: "+ str(maxQValueNextGrid)) if printDebugStatementsFlag == True else None
                    
                    # Compute the Q(s,a) 
                    qValofCurrGrid = getQValueforCurrGrid(currGrid, nextGridDirection) 
                    newQValofCurrGrid = qValofCurrGrid + alpha * (currGrid.getGridReward() + (gamma * maxQValueNextGrid) - qValofCurrGrid)  
                    
                    # Update Q Value of the current grid for the corresponding direction
                    updateGridQValue(currGrid, nextGridDirection, newQValofCurrGrid)
                    
    
                                
                    
                elif exploitOrExplore == 'exploit':
                    sys.stdout.write("\n\t*****"+ exploitOrExplore) if printDebugStatementsFlag == True else None                
                    
                    nextGrid = None
                    maxQValueNextGridDirection = None
                    maxQValueNextGrid = -sys.maxint - 1 # Minimum Number
                    
                    for direction,grid in allGridsReachableFromCurGrid.iteritems():
                        allQValuesOfNextGrid = [grid.getQLeft(),grid.getQRight(),grid.getQUp(),grid.getQDown()]
                        maxOfAllQValuesOfNextGrid = max(allQValuesOfNextGrid)
                        
                        if maxOfAllQValuesOfNextGrid >= maxQValueNextGrid:
                            nextGrid = grid
                            maxQValueNextGrid = maxOfAllQValuesOfNextGrid
                            maxQValueNextGridDirection = direction
    
                        sys.stdout.write("\n\t\t"+"allQValuesOfNextGrid-"+ direction+ grid.getGridName()+": "+  "".join(','.join(str(v) for v in allQValuesOfNextGrid))) if printDebugStatementsFlag == True else None
                        sys.stdout.write("\t"+"Max from allQValuesOfNextGrid: " + str(max(allQValuesOfNextGrid)) ) if printDebugStatementsFlag == True else None
    
                    sys.stdout.write("\n\t"+"maxQValueNextStateDirection: "+ maxQValueNextGridDirection+ "\tmaxQValueNextState: "+ str(maxQValueNextGrid)) if printDebugStatementsFlag == True else None
                    
                    # Compute the Q(s,a) 
                    qValofCurrGrid = getQValueforCurrGrid(currGrid, direction) 
                    newQValofCurrGrid = qValofCurrGrid + alpha * (currGrid.getGridReward() + (gamma * maxOfAllQValuesOfNextGrid) - qValofCurrGrid)  
                    
                    # Update Q Value of the current grid for the corresponding direction
                    updateGridQValue(currGrid, maxQValueNextGridDirection, newQValofCurrGrid)
                    
                # Update current grid
                currGrid = nextGrid
                
                if goalTraversedFlag == True:
                    print "Goal Reached"
                    break

                printGrids(gWorld)
                print "\n\n"

        
        currGrid = gWorld.getGrids()[0][0]

        newGridMatrixValue = getGridWorldQValues(gWorld)
        convergedFlag = isConverged(oldGridMatrixValue,newGridMatrixValue)
                
#         if convergedFlag == True:
#             print "No. of iterations:", steps
#             print "No of episodes:", episodeCount
#             break
                        
        if episodeCount > 5: 
            print "No. of iterations:", steps
            print "No of episodes:", episodeCount
            break
      
if __name__ == '__main__':

    screenWidth = 90
    print '{:^{screenWidth}}'.format('{:=^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)
    print '{:^{screenWidth}}'.format('{:^{w}}'.format('Welcome to Gold Explorer Using Reinforcement Learning  - Q Learning', w = screenWidth-10), screenWidth=screenWidth)
    print '{:^{screenWidth}}'.format('{:=^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)    
    print 
     
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
           
    printDebugStatementsFlag = True
    qLearn()
    printGrids(gWorld)
    print '{:^{screenWidth}}'.format('{:=^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)
    print '{:^{screenWidth}}'.format('{:^{w}}'.format('Thank you for using Gold Explorer Using Reinforcement Learning - Q Learning', w = screenWidth-10), screenWidth=screenWidth)
    print '{:^{screenWidth}}'.format('{:=^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)    
    print 
    