import random
import pyodbc 
import datetime

"""
Short description with steps to the implementation of the Dice Game
1. Before the start of any game, I have calculated the start time and inserted into the Dice_Game table 
which contains Game_Id, start and end time
2. I have generated Dice values using random generator for both human and computer player
3. Switching turns has been achieved using the odd and even number logic on round number
4. Once die values are generated, implemented a logic to acheive 70% wins for computer which is 
explained as comments in the code based on permututations and combinations
5. These changed values are displayed to human player so that human can beleive that those 70% computer wins 
are randomly happening and there is no logic change in the backend
6. Human_die1, human_die2, computer_die1,computer_die2, winner of each round and Game_Id(primary key from Dice_Game table)
are inserted into Dice_GameRound table making those tables relational.
7. Once the game is quit by the human player, end time is inserted into  Dice_Game table for the corresponding start time 
8. All the queries created to the 4 questions are in one file which is also part of the zip file
"""

#Human points are the total points gained by Human after each round
#Computer points are the total points gained by Computer after each round
human_points = 0
computer_points = 0
round_number = 0
# Start time refers to the start time of each game,
# its inserted into Dice_Game table to determine average game time
start_time = datetime.datetime.now() 

#Connection to database
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                       'SERVER=(localdb)\MSSQLLocalDB;'
                       'DATABASE=DiceGame;'
                        'Trusted_Connection=yes;')
cursor = cnxn.cursor()
z = ("Insert into Dice_Game (Start_Time) Values (?)")
values = [start_time]
cursor.execute(z,values)
game_id = cursor.execute("select Game_Id from [dbo].[Dice_Game] Where [End_Time] is null")
for r in game_id:
    y = r[0]
cursor.commit()


class Game:

    def points(self):
        global human_points
        global computer_points
        global round_number
        global y

        # For the players to switch turns for each round, when the round number is even, human goes first and
        # when the round number is odd, computer goes first
        if(round_number%2)==0:
            human_die1 = random.randint(1,6)
            human_die2 = random.randint(1,6)
            computer_die1 = random.randint(1,6)
            computer_die2 = random.randint(1,6)
        else:
            computer_die1 = random.randint(1,6)
            computer_die2 = random.randint(1,6)
            human_die1 = random.randint(1,6)
            human_die2 = random.randint(1,6)
        round_number+=1
        """
        Logic to make computer win atleast 70%
        If computer die1 is 4 or 6 and computer die1> die2, we make computer_die2 = Computer_die1
        If computer die2 is 2 or 3 and computer die1< die2, we make computer_die2 = Computer_die1
        We display the changed values to the human resulting in computer win 70% rounds
        """
        if((computer_die1 ==4) or (computer_die1 ==6) and (computer_die1 > computer_die2)):
            computer_die2 = computer_die1
        elif((computer_die2 == 2) or (computer_die2 == 3) and (computer_die1 < computer_die2)):
            computer_die2 = computer_die1
        #When both human and computer has a double, chose the winner based on highest number on the dice
        if((human_die1 == human_die2) and (computer_die1 == computer_die2)):
            if(human_die1>computer_die1):
                human_points+=1
            elif(human_die1<computer_die1):
                computer_points+=1
        # When only human has a double, humnan wins
        elif(human_die1 == human_die2):
            human_points+=1
        # When only computer has a double, computer wins
        elif(computer_die1 == computer_die2):
            computer_points+=1
        # Choose the winner based on the total dice value for each player
        elif((human_die1+human_die2)<(computer_die1+computer_die2)):
            computer_points+=1
        elif((human_die1+human_die2)>(computer_die1+computer_die2)):
            human_points+=1
        else:
            # Choose the winner with highest number
            if(max(human_die1,human_die2) > max(computer_die1,computer_die2)):
                human_points+=1
            else:
                computer_points+=1
        #Determining the winner based on total points gained
        if(human_points>computer_points):
            winner = "human"
        elif(computer_points>human_points):
            winner = "computer"
        else:
            winner = "draw"
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                       'SERVER=(localdb)\MSSQLLocalDB;'
                       'DATABASE=DiceGame;'
                        'Trusted_Connection=yes;')
        cursor = cnxn.cursor()
        # Inserting game_id (from Dice_Game table), human_die1, human_die2, compputer_die1, computer_die2 into Dice_GameRound table
        z = ("Insert into Dice_GameRound (Game_Id,Human_Die1,Human_Die2,Computer_Die1,Computer_Die2,winner) Values (?,?,?,?,?,?)")
        values = [y,human_die1,human_die2,computer_die1,computer_die2,winner]
        cursor.execute(z,values)
        cursor.commit()

p1 = Game()

#Game continues as along as human player continues to play
while(input("Do You Want to Continue")=='y'):
    p1.points()
else:
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=(localdb)\MSSQLLocalDB;'
                    'DATABASE=DiceGame;'
                    'Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    # Updating Dice_Game with end_time to determine average game time when each game ends
    z = " Update Dice_Game Set End_Time = Getdate() where Start_Time is not null and [End_Time] is null"

    cursor.execute(z)
    cursor.commit()

    cursor.close()