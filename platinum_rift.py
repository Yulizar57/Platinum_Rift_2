import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# player_count: the amount of players (always 2)
# my_id: my player ID (0 or 1)
# zone_count: the amount of zones on the map
# link_count: the amount of links between all zones
player_count, my_id, zone_count, link_count = [int(i) for i in input().split()]
for i in range(zone_count):
    # zone_id: this zone's ID (between 0 and zoneCount-1)
    # platinum_source: Because of the fog, will always be 0
    zone_id, platinum_source = [int(j) for j in input().split()]
links = []
for i in range(link_count):
    zone_1, zone_2 = [int(j) for j in input().split()]
    links.append([zone_1,zone_2])

myBase = -1
enemyBase = -1

def availableMoves(x):
    avalMoves = []
    for i in range(len(links)):
        if x == links[i][0]:
            avalMoves.append(links[i][1])
        if x == links[i][1]:
            avalMoves.append(links[i][0])
    return avalMoves
            

# game loop
while True:
    my_platinum = int(input())  # your available Platinum
    vis = []
    pods = []
    owner = []
    for i in range(zone_count):
        # z_id: this zone's ID
        # owner_id: the player who owns this zone (-1 otherwise)
        # pods_p0: player 0's PODs on this zone
        # pods_p1: player 1's PODs on this zone
        # visible: 1 if one of your units can see this tile, else 0
        # platinum: the amount of Platinum this zone can provide (0 if hidden by fog)
        z_id, owner_id, pods_p0, pods_p1, visible, platinum = [int(j) for j in input().split()]
        if visible:
            if owner_id == 0 and myBase == -1:
                myBase = z_id
            elif owner_id == 1 and enemyBase == -1:
                enemyBase = z_id
        if pods_p0 > 0:
            pods.append([z_id,pods_p0])
        vis.append(visible)
        owner.append(owner_id)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print(links, file=sys.stderr)
    print(vis, file=sys.stderr)
    print(owner, file=sys.stderr)
    print(pods, file=sys.stderr)
    print(availableMoves(pods[0][0]), file=sys.stderr)
    for i in range(len(pods)):
        x = pods[i][1]
        y = pods[i][0]
        
        for j in range(len(availableMoves(y))):
            if owner[availableMoves(y)[j]] != 0:
                z=availableMoves(y)[j]
            else:
                z = random.choice(availableMoves(y))
        print(str(x) + " " + str(y) + " " + str(z), end=" ")
    # first line for movement commands, second line no longer used (see the protocol in the statement for details)

    print()
    print("WAIT")
