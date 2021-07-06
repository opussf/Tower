#!/usr/bin/env python3
#########################################

import random
random.seed()

maxEnemyStrength = 10
maxEnemies = 3


# start the player as value 1
player = 1
isAlive = True

tower = [[1]]

targetValue = player   # starting value is the same as the player
for floor in range( random.randint(5,20) ):
	enemies = []
	for numEnemies in range( random.randint( 1, min( targetValue, maxEnemies ) ) ):
		enemies.append( random.uniform( 1, min( targetValue, maxEnemyStrength ) ) )
	tower.append( enemies )
	targetValue += sum( enemies )

random.shuffle( tower )


while isAlive and len( tower ) > 0:
	# Find the max number of enemies in a floor in the tower
	floorMaxSize = 0
	for floor in tower:
		floorMaxSize = max( floorMaxSize, len( floor ) )
	# Print tower
	for f in range( len( tower ) ):
		enemyList = list( map( lambda x: "%2d" % int(x), tower[ f ] ) )

		print( "%2d\t[%s ]" % ( f, ",".join( enemyList ) ) )

	# choose a floor
	isValidFloor = False
	while not isValidFloor:
		attackFloor = int( input( "You are strength (%2d). Which floor do you want to attack? " % ( int( player, ) ) ) )
		isValidFloor = ( attackFloor >= 0 and attackFloor < len( tower ) )
		if not isValidFloor:
			print( "Your choice of %d is not valid.  Please choose again." )

	floorStrength = sum( tower[ attackFloor ] )
	if player >= floorStrength:
		player += floorStrength
		tower.pop(attackFloor)
	else:
		isAlive = False

# Game is over
if isAlive:
	print( "You have beaten the tower." )
else:
	print( "You have died trying." )
