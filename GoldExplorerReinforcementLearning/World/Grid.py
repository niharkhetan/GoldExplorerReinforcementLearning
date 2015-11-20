'''
Created on Nov 3, 2015

@author: NiharKhetan, Ghanshyam Malu
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


    def __init__(self, Name, gridReward, isBlockedFlag = False):
        '''
        Constructor
        '''
        self.gridName = Name
        self.gridReward = gridReward
        self.qLeft =  0
        self.qRight = 0
        self.qUp = 0
        self.qDown = 0
        self.isBlockedFlag = isBlockedFlag
        self.isGoalFlag = False
        self.value = 0
    
    def getQLeft(self):
        return self.qLeft
    
    def getQRight(self):
        return self.qRight
    
    def getQUp(self):
        return self.qUp
    
    def getQDown(self):
        return self.qDown
    
    def getAllQValues(self):
        return {'up': self.getQUp(),
                'down': self.getQDown(),
                'left': self.getQLeft(),
                'right': self.getQRight()
                }
        
    def setQLeft(self, qLeft):
        self.qLeft = qLeft
        
    def setQRight(self, qRight):
        self.qRight = qRight
        
    def setQUp(self, qUp):
        self.qUp = qUp
    
    def setQDown(self, qDown):
        self.qDown = qDown
    
    def getGridName(self):
        return str(self.gridName)
    
    def isGoal(self):
        return self.isGoalFlag
    
    def isBlocked(self):
        return self.isBlockedFlag
    
    def setGoal(self):
        self.isGoalFlag = True
    
    def getIndex(self):
        i = (self.gridName -1) // 4
        j = (self.gridName -1) % 4
        return (i, j)
    
    def getGridReward(self):
        return self.gridReward
        
if __name__ == '__main__':
    pass
    
    