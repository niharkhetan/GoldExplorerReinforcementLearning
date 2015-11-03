'''
Created on Nov 3, 2015

@author: NiharKhetan
'''

class GridWorld(object):
    '''
    classdocs
    '''


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
    
    def getLeftMovement(self):
        return self.movement['left']
    
    def getRightMovement(self):
        return self.movement['right']
    
    def getUpMovement(self):
        return self.movement['up']
    
    def getDownMovement(self):
        return self.movement['down']
    
    