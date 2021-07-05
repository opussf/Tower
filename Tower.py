#!/usr/bin/env python3
#########################################

import random
random.seed()

maxEnemyStrength = 10


# start the player as value 1
player = 1
isAlive = True

tower = [[1]]

for floor in range( random.randint(5,15) ):
	enemies = []
	for numEnemies in range( random.randint(1,3) ):
		enemies.append( random.uniform( 1, maxEnemyStrength ) )
	tower.append( enemies )

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

	floorStrength = sum( tower[ attackFloor ] )
	if player >= floorStrength:
		player += floorStrength
		tower.pop(attackFloor)
	else:
		isAlive = False

# Game is over
print( "You have beaten the tower.")
