'''
Created on Nov 3, 2015

@author: NiharKhetan, Ghanshyam Malu
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
    
    def getUpGrid(self,grid):
        ''' Get the Up grid from a given grid'''
        i, j = grid.getIndex()
        iNew, jNew = i+1, j
        if not grid.isGoal() and  iNew < 5 and iNew >= 0 and not self.grids[iNew][jNew].isBlocked() :
            return self.grids[iNew][jNew]
        else:
            return grid
            
    def getDownGrid(self,grid):
        ''' Get the Down grid from a given grid'''
        i, j = grid.getIndex()
        iNew, jNew = i-1, j
        if not grid.isGoal() and  iNew < 5 and iNew >= 0 and not self.grids[iNew][jNew].isBlocked() :
            return self.grids[iNew][jNew]
        else:
            return grid
          
    def getLeftGrid(self,grid):
        ''' Get the Left grid from a given grid'''
        i, j = grid.getIndex()
        iNew, jNew = i, j-1
        if not grid.isGoal() and  jNew >=0 and jNew < 4 and not self.grids[iNew][jNew].isBlocked() :
            return self.grids[iNew][jNew]
        else:
            return grid
          
    def getRightGrid(self,grid):
        ''' Get the Right grid from a given grid'''
        i, j = grid.getIndex()
        iNew, jNew = i, j+1
        if not grid.isGoal() and jNew >=0 and jNew < 4 and not self.grids[iNew][jNew].isBlocked() :
            return self.grids[iNew][jNew]
        else:
            return grid
                                          
    def getNextGrid(self,grid,direction):
        ''' Given a grid , return the next grid for the given direction'''
        return {
        'up': self.getUpGrid(grid),
        'down': self.getDownGrid(grid),
        'left': self.getLeftGrid(grid),
        'right': self.getRightGrid(grid),
        }[direction]
   
   
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
      
    def getAllGridsReachableFromCurGrid(self,grid):
        ''' getAllGridsReachableFromCurGrid '''

        directions = {'up':{'x':1,'y':0},'down':{'x':-1,'y':0},'right':{'x':0,'y':1},'left':{'x':0,'y':-1}}
        allReachableGrids = {}
        i, j = grid.getIndex()
        for direction,val in directions.iteritems():
            newX =  i + val['x']
            newY =  j + val['y']
            if 0 <= newX < 5  and 0 <= newY < 4 and not grid.isGoal() :
                gridToMoveTo = self.grids[newX][newY]
                if not gridToMoveTo.isBlocked():
                    allReachableGrids[direction] = gridToMoveTo
                else:
                    allReachableGrids[direction] = grid
            else:
                allReachableGrids[direction] = grid
                    
        return allReachableGrids
    
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

    def getDirectionString(self, dirList):
        ''' Creates a string of direction of symbols from the given direction list '''

        dirStr = ''        
        dirDict = {
        'up': '^',
        'down': 'v',
        'left': '<',
        'right': '>'
        }
        
        for dir in dirList:
            if len(dirStr)>0:
                dirStr += ' / '
            dirStr += dirDict[dir]
            
        return dirStr
       
    def printGridWorldOptimumPolicyValueIteration(self):
        ''' Print the optimum policy '''
        print        
        print '{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = 69), screenWidth=screenWidth)
        print '{:^{screenWidth}}'.format('{:^{w}}'.format('Grid World Optimum Policy', w = 49), screenWidth=screenWidth)
        print '{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = 69), screenWidth=screenWidth)    
                 
        for i in range(4, -1, -1):                              
            rowText = '' 
            for j in range(4):
                currGrid = self.grids[i][j]
                if currGrid.isBlocked():
                    rowText += '|{:^15}'.format('######')
                else:
                    allGridsFromCurrGrid = self.getAllGridsReachableFromCurGrid(currGrid)
                    allGridsFromCurrGrid = [[grid.value, direction] for direction,grid in allGridsFromCurrGrid.iteritems()]
                    m = max(allGridsFromCurrGrid)
                    optimumDirections = [elem[1] for idx, elem in enumerate(allGridsFromCurrGrid) if elem[0] == m[0]]
                    optimumDirStr = self.getDirectionString(optimumDirections)
                    rowText += '|{:^15}'.format(optimumDirStr)
                    
                if j==3:
                    rowText +=  "|"
            print '{:^{screenWidth}}'.format('{:^{w}}'.format(rowText, w = 69), screenWidth=screenWidth)
            print '{:^{screenWidth}}'.format('{:-^{w}}'.format('', w = 65), screenWidth=screenWidth)

        print '{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = 69), screenWidth=screenWidth)
        print '{:^{screenWidth}}'.format('{:^{w}}'.format('^ : Up    v : Down    < : Left    > : Right     / : Or', w = 49), screenWidth=screenWidth)
        print '{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = 69), screenWidth=screenWidth)    
        print "\n"

       
    def printGridWorldOptimumPolicyQValue(self):
        ''' Print the optimum policy '''
        print        
        print '{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = 69), screenWidth=screenWidth)
        print '{:^{screenWidth}}'.format('{:^{w}}'.format('Grid World Optimum Policy', w = 49), screenWidth=screenWidth)
        print '{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = 69), screenWidth=screenWidth)    
        for i in range(4, -1, -1):                      
            rowText = '' 
            for j in range(4):
                currGrid = self.grids[i][j]
                if currGrid.isBlocked():
                    rowText += '|{:^15}'.format('######')
                else:                    
                    allQValuesCurrGrid = currGrid.getAllQValues()
                    allQValuesCurrGrid = [[v,k] for k,v in allQValuesCurrGrid.iteritems()]
                    m = max(allQValuesCurrGrid)
                    optimumDirections = [elem[1] for _, elem in enumerate(allQValuesCurrGrid) if abs(elem[0] - m[0]) <= 0.05]
                    optimumDirStr = self.getDirectionString(optimumDirections)
                    
                    rowText += '|{:^15}'.format(optimumDirStr)
                
                if j==3:
                    rowText +=  "|"
            
            print '{:^{screenWidth}}'.format('{:^{w}}'.format(rowText, w = 69), screenWidth=screenWidth)
            print '{:^{screenWidth}}'.format('{:-^{w}}'.format('', w = 65), screenWidth=screenWidth)
            
        print '{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = 69), screenWidth=screenWidth)
        print '{:^{screenWidth}}'.format('{:^{w}}'.format('^ : Up  v : Down  < : Left   > : Right   Diff. Threshold : (0.05)', w = 49), screenWidth=screenWidth)
        print '{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = 69), screenWidth=screenWidth)    
        print "\n"

                        
    def printGridWorldValueMatrix(self):
        ''' Print Grid World Value Matrix'''
        
        print        
        print '{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = 69), screenWidth=screenWidth)
        print '{:^{screenWidth}}'.format('{:^{w}}'.format('Grid World Value Matrix', w = 49), screenWidth=screenWidth)
        print '{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = 69), screenWidth=screenWidth)    
                 
        for i in range(4, -1, -1):             
            rowText = '' 
            for j in range(0, 4):
                currState = self.grids[i][j]
                rowText += '|{:^15}'.format('{: f}'.format(currState.value))
                if j==3:
                    rowText +=  "|"
            print '{:^{screenWidth}}'.format('{:^{w}}'.format(rowText, w = 69), screenWidth=screenWidth)
            print '{:^{screenWidth}}'.format('{:-^{w}}'.format('', w = 65), screenWidth=screenWidth)
        print "\n"
        
    def printGridWorldRewardMatrix(self):
        ''' Print Grid World Reward Matrix'''

        print        
        print '{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = 49), screenWidth=screenWidth)
        print '{:^{screenWidth}}'.format('{:^{w}}'.format('Grid World Reward Matrix', w = 49), screenWidth=screenWidth)
        print '{:^{screenWidth}}'.format('{:*^{w}}'.format('', w = 49), screenWidth=screenWidth)    
 
        for i in range(4, -1, -1):
            rowText = '' 
            for j in range(0, 4):
                currState = self.grids[i][j]
                rowText+= '|{:^10}'.format('{: d}'.format(currState.gridReward))
                if j==3:
                    rowText+= "|"
            print '{:^{screenWidth}}'.format('{:^{w}}'.format(rowText, w = 49), screenWidth=screenWidth)
            print '{:^{screenWidth}}'.format('{:-^{w}}'.format('', w = 45), screenWidth=screenWidth)
        print "\n"


screenWidth = 90
            
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
    
#     for i in range(0, 5): 
#         for j in range(0, 4):
#             grid = gWorld.getGrids()[i][j]
#             if not grid.isBlocked():
#                 print str(grid.getGridName()) + " :: ",
#                 for x in gWorld.getMovesPossible(grid):
#                     print str(x.getGridName()) + " ,",
#                 print ""
#                 
    gWorld.getAllGridsReachableFromCurGrid(grid17)
    gWorld.printGridWorldValueMatrix()
#     gWorld.printGridWorldOptimumPolicyValueIteration()
    gWorld.printGridWorldOptimumPolicyQValue()
#     gWorld.printGridWorldRewardMatrix()
# 
#     print "getUpGrid", gWorld.getUpGrid(grid17).getGridName()
#     print "getDownGrid", gWorld.getDownGrid(grid17).getGridName()
#     print "getLeftGrid",gWorld.getLeftGrid(grid17).getGridName()
#     print "getRightGrid",gWorld.getRightGrid(grid17).getGridName()

#     print gWorld.getNextGrid(grid1,'down').getGridName()