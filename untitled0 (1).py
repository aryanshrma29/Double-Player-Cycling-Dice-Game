# -*- coding: utf-8 -*-


'''Game rules:
Two cyclists race against each other, where one cyclist starts from position 0 on the track, and
the other cyclist starts from position 15 on the track. Each cyclist rolls their own 6-sided dice
(simultaneously) and moves forward the number of positions indicated by their dice roll. If one cyclist
“catches” (overtakes) their opponent, then they are the winner. If neither cyclist catches the other,
then the first cyclist to complete six laps of the track is the winner. It is also possible that both cyclists
complete six laps of the track on the same dice roll, in which case the race is a draw. Therefore, there
are five possible outcomes of the Individual Pursuit race.'''

import random
def cycling_dice_game():
    '''Cycling dice game # players: 30 points circular board
    P1 starts at 0, P2 starts at 15, both rolls dice simultaneously
    5 Possible outcomes of the game:
        1. P1 completes 6 laps first and wins
        2. P2 completes 6 laps first and wins
        3. Both completes 6 laps on the same roll (DRAW)
        4. P1 overtakes P2 to win
        5. P2 overtakes P1 to win'''

    position1 = 0    # initial position for player 1
    position2 = 0    # initial position for player 2
    print('## WELCOME TO CYCLING DICE GAME ## \n'.center(80,' '))
    print('Player1 -> Lap=',position1,' Point=',position1,end='   ')
    print('Player2 -> Lap=',position1,' Point=',position2+15,'\n')

    continue_rolling = True
    dice_count = 0

    while (continue_rolling):
        dice1 = random.randint(1,6)    # rolling dice
        dice2 = random.randint(1,6)
        dice_count += 1
        print('Rolling dice',dice_count,': Player 1 got',dice1,'&',end=' ')
        print('Player 2 got',dice2)

        position1 += dice1
        position2 += dice2
        lap1 = position1//30    #storing lap value of P1
        point1 = position1%30   #storing point in lap for P1
        lap2 = position2//30    #storing lap value of P2
        point2 = ((position2%30)+15)%30   #storing point in lap for P2

        print('Player1 -> Lap=',lap1,' Point=',point1,end='   ')
        print('Player2 -> Lap=',lap2,' Point=',point2)

        #Following if statements are checking for the overtake taking in
        #        considering the different starting values
        if(position1-15>position2):
            print("\nPlayer 1 overtook 2 in",dice_count,'rolls and wins :)')
            continue_rolling = False   #to break out of the loop
        elif(position2-15>position1):
            print("\nPlayer 2 overtook 1 in",dice_count,'rolls and wins :)')
            continue_rolling = False

        #Below statements check whether any player has completed 6 laps or
        #    both completed at the same time
        if(lap1>=6):
            if(lap2>=6):    #further checks if P2 has also reached lap 6
                print('\nIts a draw in',dice_count,'rolls')
            else:
                print('\nPlayer 1 won in',dice_count,'rolls. :)')
            continue_rolling = False
        elif(lap2>=6):
            if(lap1>=6):    #further checks if P1 has also reached lap 6
                print('its a draw in',dice_count,'rolls. :)')
            else:
                print('\nPlayer 2 won in',dice_count,'rolls. :)')
            continue_rolling = False

    #Below statements are run everytime after the loop to calculate the lead
    # and the split between players
        if(continue_rolling==True):
            if (position2 > position1):
                 print('Player 2 is leading by',position2 - position1,end=' ')
                 print('points...Split=',abs(point2-point1),'\n')
            elif(position2 == position1):
                 print('Going head to head...Split= nill\n')
            else:
                 print('Player 1 is leading by',position1 - position2,end=' ')
                 print('points...Split=',abs(point2-point1),'\n')
    return(dice_count)

cycling_dice_game()