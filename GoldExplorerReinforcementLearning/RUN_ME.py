#! /usr/bin/env python

from World.Grid import Grid
from World.GridWorld import GridWorld
from Strategy.QLearning import *
from Strategy.ValueIteration import *

def createGridWorld():
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

    return gWorld

def getUserInput(msg, inputType, options = []):
    ''' Generalized method to get user input '''
    while True:
        try:
            userOption = raw_input(msg).upper()
            if inputType == "int":
                userOption = int(userOption)
            if len(options) > 0 and userOption not in options:
                raise ValueError('Invalid choice !') 
        except: 
            print '\n{:^{screenWidth}}\n'.format('{:<{w}}'.format('Invalid choice !', w = screenWidth-10), screenWidth=screenWidth)
        else:
            break
    
    return userOption


def getUserChoice(optionsDict):
    ''' Display available datasets to user'''

    print '{:^{screenWidth}}'.format('{:=^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)
    print '{:^{screenWidth}}'.format('{:^{w}}'.format('Welcome to Gold Explorer Using Reinforcement Learning', w = screenWidth-10), screenWidth=screenWidth)
    print '{:^{screenWidth}}'.format('{:=^{w}}'.format('', w = screenWidth-10), screenWidth=screenWidth)    
    print 
               
    msg = '{:^{screenWidth}}'.format('{:<{w}}'.format('Choose one of the available options: ', w = screenWidth-10), screenWidth=screenWidth)
    for k, v in optionsDict.iteritems():
        msg += '\n{:^{screenWidth}}'.format('{:<{w}}'.format('\t'+str(k)+" - "+v, w = screenWidth-10), screenWidth=screenWidth)
    
    msg += '\n\n{:^{screenWidth}}'.format('{:<{w}}'.format('Your choice from '+ str(optionsDict.keys())+"...", w = screenWidth-10), screenWidth=screenWidth)
    
    userOption = getUserInput(msg, "int", optionsDict.keys())
    return userOption


if __name__ == '__main__':
    
    printDebugStatementsFlag = False
    screenWidthArg = 90
    # Q Learning Parameters
    gamma = 0.9
    alpha = 0.1
    epsilon = 0.9
    
    optionsDict = {0: "Explore Gold using Reinforcement Learning - Value Iteration",
               1: "Explore Gold using Reinforcement Learning - Q Value"}
    
    userChoiceRL = getUserChoice(optionsDict)

    msg = '\n{:^{screenWidth}}'.format('{:<{w}}'.format('Show detailed log (Y/N)?... : ', w = screenWidth-10), screenWidth=screenWidth)
    printDebugStatementsFlag = True if getUserInput(msg, "char", ['Y','N']).lower() == 'y' else False

    gWorld = createGridWorld()
    if userChoiceRL==0:
        valueIterationMain(gWorld,gamma, printDebugStatementsFlag,screenWidthArg )
    else:
        qLearnMain(gWorld,gamma,alpha, epsilon, printDebugStatementsFlag,screenWidthArg )
    