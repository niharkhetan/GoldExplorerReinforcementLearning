'''
Created on Nov 3, 2015

@author: NiharKhetan
'''
from codecs import getincrementaldecoder

class Grid(object):
    '''
    Grid world will look like this:
    
    17 18 19 20
    13 14 15 16
    9  10 11 12
    5  6  7  8
    1  2  3  4
    
    4,0 4,1 4,2 4,3
    3,0 3,1 3,2 3,3
    2,0 2,1 2,2 2,3
    1,0 1,1 1,2 1,3
    0,0 0,1 0,2 0,3
    '''


    def __init__(self, Name, gridReward, isBlocked = False):
        '''
        Constructor
        '''
        self.gridName = Name
        self.gridReward = gridReward
        self.pLeft = None
        self.pRight = None
        self.pUp = None
        self.pDown = None
        self.isBlocked = isBlocked
        self.isGoal = False
    
    def getPLeft(self):
        return self.pLeft
    
    def getPRight(self):
        return self.pLeft
    
    def getPUp(self):
        return self.pUp
    
    def getPDown(self):
        return self.pDown
    
    def setPLeft(self, pLeft):
        self.pLeft = pLeft
        
    def setPRight(self, pRight):
        self.pRight = pRight
        
    def setPUp(self, pUp):
        self.pUp = pUp
    
    def setPDown(self, pDown):
        self.pDown = pDown
    
    def getGridName(self):
        return self.gridName
    
    def getIsGoal(self):
        return self.isGoal
    
    def isBlocked(self):
        return self.isBlocked
    
    def setIsGoal(self):
        self.isGoal = True
    
    def getIndex(self):
        i = (self.gridName -1) // 4
        j = (self.gridName -1) % 4
        return (i, j)
        
if __name__ == '__main__':
    for i in range(1,21):
        grid = Grid(i)
        print grid.getIndex()
    
    