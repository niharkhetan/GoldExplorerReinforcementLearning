'''
Created on Nov 6, 2015

@author: NiharKhetan
'''

from World.Grid import Grid
from World.GridWorld import GridWorld

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
    grid20.setIsGoal()
    
    gWorld = GridWorld([[grid1,grid2,grid3,grid4],[grid5,grid6,grid7,grid8],[grid9,grid10,grid11,grid12],[grid13,grid14,grid15,grid16],[grid17,grid18,grid19,grid20]])
    gWorld.setMovement({"left":{"left":1}, "right":{"right":0.8, "down":0.2}, "up":{"up":0.8, "left":0.2}, "down":{"down":1}})
    
    gamma = 0.9


    for i in range(0, 5): 
        for j in range(0, 4):
            currState = gWorld.getGrids()[i][j]
            possibleTransitions = gWorld.getMovesPossible(currState)
            values = []
            for eachPossibleMove in possibleTransitions:
                transitionDirection = gWorld.getMoveDirection(currState, eachPossibleMove)
                probabilityDirection = gWorld.getMovement()[transitionDirection][transitionDirection]
                valueMovedToThisGrid = gamma*probabilityDirection*eachPossibleMove.value
                bellmanValue = currState.gridReward + valueMovedToThisGrid
                values.append(bellmanValue)
            currState.value = max(values)
    print "\n\n"
    for i in range(0, 5): 
        for j in range(0, 4):
            currState = gWorld.getGrids()[i][j]
            print str(currState.value) + " ",
        print ''    
        
    print "\n\n"    
    
   
            
    