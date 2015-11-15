'''
Created on Nov 6, 2015

@author: NiharKhetan, Ghanshyam Malu
'''

from World.Grid import Grid
from World.GridWorld import GridWorld
import sys

def getNewStateIndexForAction(action, currIndex):

    ''' Gets indices of the new state reached using the action'''
    row,col = currIndex[0],currIndex[1]
    
    if action == 'up' and currIndex[0]<4:
        row = currIndex[0]+1
    elif action == 'down' and currIndex[0]>0:
        row = currIndex[0]-1
    elif action == 'right' and currIndex[1]<3:
        col = currIndex[1]+1
    elif action == 'left' and currIndex[1]>0:
        col = currIndex[1]-1
    
    if gWorld.getGrids()[row][col].isBlocked():
        return currIndex
    else:
        return row,col


def getGridMatrixValue(gWorld):
    gMatValue = []
    for i in range(0, 5):
        subList = [] 
        for j in range(0, 4):
            subList.append(gWorld.getGrids()[i][j].value)
        gMatValue.append(subList)
    return gMatValue
    
def isConverged(oldGridMatrixValue,newGridMatrixValue):
    for i in range(0, 5): 
        for j in range(0, 4):
            diff = newGridMatrixValue[i][j]-oldGridMatrixValue[i][j]
            if diff != 0:
                return False
    return True
    

def valueIterate():
    gamma = 0.9
    count = 0 
    sys.stdout.write('\n\tIterating.') if printDebugStatementsFlag == False else None
    
    while True:
        count+=1
        oldGridMatrixValue = getGridMatrixValue(gWorld)
        
        if count % 25 == 0:
            sys.stdout.write(".") if printDebugStatementsFlag == False else None             
#         for i in range(4, -1, -1):
        for i in range(0, 5): 
            for j in range(0, 4):
                currState = gWorld.getGrids()[i][j]
                if not currState.isBlocked():

                    allGridsReachableFromCurGrid = gWorld.getAllGridsReachableFromCurGrid(currState)

#                     for dir,grid in allGridsReachableFromCurGrid.iteritems():
#                         print dir, grid.getGridName()

                    sys.stdout.write("\n"+ "-"*50) if printDebugStatementsFlag == True else None
                    sys.stdout.write("\nCurrent Grid: "+ str(currState.getGridName())+ "\tReward : " + str(currState.gridReward)) if printDebugStatementsFlag == True else None
                    sys.stdout.write("\n"+ "-"*50) if printDebugStatementsFlag == True else None
                    #sys.stdout.write("\nPossibleTransitions: "+ ' '.join([key1 + str(val1.getGridName()) for key1,val1 in allGridsReachableFromCurGrid.iteritems()])) if printDebugStatementsFlag == True else None
 
                    values = []
                    for transitionDirection, grid in allGridsReachableFromCurGrid.iteritems():

                        consequentMovesProbabilities =  gWorld.getMovement()[transitionDirection]
                        sys.stdout.write("\n\n\tChecking for "+ str(currState.getGridName())+" "+ str(grid.getIndex())+" "+ str(transitionDirection)) if printDebugStatementsFlag == True else None

                        sumOfProdOfProbOfMoveAndStateValue = 0
                        for direction, probability in consequentMovesProbabilities.iteritems():
                            newStateRow, newStateCol = getNewStateIndexForAction(direction, (i,j))
                            sumOfProdOfProbOfMoveAndStateValue += probability * gWorld.getGrids()[newStateRow][newStateCol].value
                            sys.stdout.write("\n\t\tChecking for '"+direction+"' from ("+ str(i)+","+ str(j)+") \t--> effective state ("+ str(newStateRow)+","+ str(newStateCol)+"); Grid: "+ str(gWorld.getGrids()[newStateRow][newStateCol].getGridName())+" ;Prob: "+ str(probability)+ "; Value: "+ str( gWorld.getGrids()[newStateRow][newStateCol].value)) if printDebugStatementsFlag == True else None 

                        valueMovedToThisGrid = gamma*sumOfProdOfProbOfMoveAndStateValue
                        bellmanValue = currState.gridReward + valueMovedToThisGrid
                        values.append(bellmanValue)
                        sys.stdout.write("\n\t****Calculated value for '"+transitionDirection+"' from current state '"+ str(currState.getGridName())+"' : "+ str(bellmanValue)) if printDebugStatementsFlag == True else None

                    sys.stdout.write("\n\n\tAll values:"+ str( values)+ "\n\t Chosen value:"+ str( max(values))+ "\n") if printDebugStatementsFlag == True else None
                    currState.value = max(values)
                    gWorld.printGridWorldValueMatrix() if printDebugStatementsFlag == True else None
        newGridMatrixValue = getGridMatrixValue(gWorld)
        
        convergedFlag = isConverged(oldGridMatrixValue,newGridMatrixValue)

        gWorld.printGridWorldRewardMatrix() if printDebugStatementsFlag == True else None
        
        if convergedFlag == True:
            print '\n\n{:^{screenWidth}}\n'.format('{:%^{w}}'.format(" Total # of Value Iterations :" + str(count)+" ", w = screenWidth-20), screenWidth=screenWidth)
            break
        
     
  
def valueIterationMain(gWorldArg, gammaArg, printDebugStatementsFlagArg, screenWidthArg):
    global gWorld
    global screenWidth
    global printDebugStatementsFlag
    global gamma
    
    gWorld = gWorldArg
    screenWidth = screenWidthArg
    printDebugStatementsFlag = printDebugStatementsFlagArg
    gamma = gammaArg
    
    print '{:^{screenWidth}}'.format('{:=^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)
    print '{:^{screenWidth}}'.format('{:^{w}}'.format('Welcome to Gold Explorer Using Reinforcement Learning - Value Iteration', w = screenWidth-10), screenWidth=screenWidth)
    print '{:^{screenWidth}}'.format('{:=^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)    
    print 
   
    valueIterate()

    gWorld.printGridWorldRewardMatrix()           
    gWorld.printGridWorldValueMatrix()
 
    print '{:^{screenWidth}}'.format('{:=^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)
    print '{:^{screenWidth}}'.format('{:^{w}}'.format('Thank you for using Gold Explorer Using Reinforcement Learning - Value Iteration', w = screenWidth-10), screenWidth=screenWidth)
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
        
    valueIterationMain(gWorld, 0.9, True, 90)