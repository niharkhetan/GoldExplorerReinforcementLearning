'''
Created on Nov 9, 2015

@author: NiharKhetan
'''

if __name__ == '__main__':
    pass

from World.Grid import Grid
from World.GridWorld import GridWorld


def printGridsDeleteMe(gWorld):
    '''
    for i in range(0,3):
        for j in range(0,3):
            print "    "+"%2.2f"+"    "
    '''
    newWorld = []
    for row in gWorld.getGrids():
        newRow = []
        for grid in row:
            newRow.append("     ")
            newRow.append('{:^8}'.format('{: .2f}'.format(grid.getQDown())))            
            newRow.append("     ")
        newWorld.append(newRow)
        newRow = []
        for grid in row:
            newRow.append('{:<3}'.format('{: .2f}'.format(grid.getQLeft())))
            newRow.append('{:^8}'.format('('+grid.getGridName()+')'))
#             newRow.append('{:^8}'.format(''))            
            newRow.append('{:>4}'.format('{: .2f}'.format(grid.getQRight())))
        newWorld.append(newRow)
        newRow = [] 
        for grid in row:
            newRow.append("     ")
            newRow.append('{:^8}'.format('{: .2f}'.format(grid.getQUp())))            
            newRow.append("     ")
        newWorld.append(newRow)
    
    rowCount = 0
    print '-'*93
    for n in range(len(newWorld) - 1, -1, -1):
        row = newWorld[n]
        colCount = 0
        print '|',
        for smallerGrid in row:
            print smallerGrid,
            colCount += 1
            if colCount % 3 == 0:
                print "|",
        rowCount += 1
        if rowCount % 3 == 0:
            print 
            print '-'*93
        else:
            print 


def printGrids(gWorld):
    '''
    for i in range(0,3):
        for j in range(0,3):
            print "    "+"%2.2f"+"    "
    '''
    newWorld = []
    for row in gWorld.getGrids():
        newRow = []
        for grid in row:
            newRow.append("      ")
            newRow.append("{0:.2f}".format(grid.getQDown()).rjust(6))
            newRow.append("      ")
        newWorld.append(newRow)
        newRow = []
        for grid in row:
            newRow.append("{0:.2f}".format(grid.getQLeft()).rjust(6))
            newRow.append("      ")
            newRow.append("{0:.2f}".format(grid.getQRight()).rjust(6))
        newWorld.append(newRow)
        newRow = [] 
        for grid in row:
            newRow.append("      ")
            newRow.append("{0:.2f}".format(grid.getQUp()).rjust(6))
            newRow.append("      ")
        newWorld.append(newRow)
    
    rowCount = 0
    print '-'*93
    for n in range(len(newWorld) - 1, -1, -1):
        row = newWorld[n]
        colCount = 0
        print '|',
        for smallerGrid in row:
            print smallerGrid,
            colCount += 1
            if colCount % 3 == 0:
                print "|",
        rowCount += 1
        if rowCount % 3 == 0:
            print 
            print '-'*93
        else:
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
    
    printGrids(gWorld)