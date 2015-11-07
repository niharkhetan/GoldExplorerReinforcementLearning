'''
Created on Nov 3, 2015

@author: NiharKhetan
'''
from Grid import Grid
class GridWorld(object):

    def __init__(self, listOfGrids):
        '''
        listOfGrids is a list of object type Grid.
        It is stored in order from 1 to 20. 
        '''
        self.movement = None
        self.grids = listOfGrids
        
    def setMovement(self, movement):
        '''
        movement is a dict of the form:
        left : {left : probability of left, down: probability of down}
        ''' 
        self.movement = movement
    
    def getGrids(self):
        return self.grids
    
    def getLeftMovement(self):
        return self.movement['left']
    
    def getRightMovement(self):
        return self.movement['right']
    
    def getUpMovement(self):
        return self.movement['up']
    
    def getDownMovement(self):
        return self.movement['down']
    
    def getMovement(self):
        return self.movement
    
    def getMovesPossible(self, grid):
        movesPossible = []
        # Moves are represented as (From, to)
        i, j = grid.getIndex()
        #Up, Down, Right, Left
        movesPossibleToGrids = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
        for move in movesPossibleToGrids:
            x, y = move            
            if x < 5 and x >= 0 and y >=0 and y < 4 :
                gridToMoveTo = self.grids[x][y]
                if not gridToMoveTo.isBlocked:
                    movesPossible.append(gridToMoveTo)
        return movesPossible
    
    def getMoveDirection(self, currentGrid, movedToGrid):
        diff = currentGrid.getGridName() - movedToGrid.getGridName()
        if diff == 1:
            return 'left'
        elif diff == -1:
            return 'right'
        elif diff == 4:
            return 'down'
        else:
            return 'up'
        
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
    
    for i in range(0, 5): 
        for j in range(0, 4):
            grid = gWorld.getGrids()[i][j]
            if not grid.isBlocked:
                print str(grid.getGridName()) + " :: ",
                for x in gWorld.getMovesPossible(grid):
                    print str(x.getGridName()) + " ,",
                print ""