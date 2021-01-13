from random import randint
import time

playerName = str(input('What is your name: '))
computerName = str(input('What should your opponent name be: '))
totalRounds = int(input('How many rounds do you want to play? '))

rps = ['Rock', 'Paper', 'Scissors']
computerChoice = rps[randint(0,2)]

def gameStart():

    global totalRounds
    playerScore = int(0)
    computerScore = int(0)

    for i in range(totalRounds):
        i += 1
        print("\n"'Round ' + str(i) + '! ' + str(computerName) +' vs ' + str(playerName))
        time.sleep(2)
        playerChoice = str(input('Rock, Paper, Scissors? '))
        if playerChoice == computerChoice:
            print('Tie')
        elif playerChoice == 'Rock':
            if computerChoice == 'Paper':
                print('Paper destroys rock, YOU IDIOT YOU LOSE!!!')
                computerScore += 1
            else:
                print('ding ding ding, +1 for you')
                playerScore += 1
        elif playerChoice == 'Paper':
            if computerChoice == 'Scissors':
                print('COMPUTER CUT YOU, YOU LOSE!')
                computerScore += 1
            else:
                print('ding ding ding, +1 for you')
                playerScore += 1
        elif playerChoice == 'Scissors':
            if computerChoice == 'Rock':
                print('your scissors got SMASHED, computer +1.. loser')
                computerScore += 1
            else:
                print('ding ding ding, +1 for you')
                playerScore += 1
        else:
            print('Learn to spell idiot, for that -1 point')
            playerScore -= 1

    if i == totalRounds :
        if playerScore == computerScore:
            print('How did you manage to tie? Guess we are heading to the tie breaker.')
            totalRounds = int(1)
            gameStart()
        elif playerScore > computerScore:
            print('Congrats, ' + playerName + ' you have beaten this bot')
            print('Your score: ' + str(playerScore))
            print( computerName +' score: ' + str(computerScore))
        else:
            print('You lost... idiot....')
            print('Your score: ' + str(playerScore))
            print( computerName + ' score: ' + str(computerScore))

if playerName and totalRounds :
    gameStart()