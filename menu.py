from character import Character
from race import Race

#this class will handle all menu selections
class Menu():
    def __init__(self):
        self.quick = None
        self.detailed = None

    #this method will define whether they want a detailed menu or a quick fill menu going forward
    def menuOption(self):
        exitLoop = False
        #will run as long as they don't input a correct menu option
        while exitLoop == False:
            print("Welcome to the DnD Character Sheet Builder!\n"
                  "Please select either Beginner or Experienced to get started:\n"
                  "1.Experienced\n"
                  "2.Beginner")
            option = input()
            #option 1 is associated with quick menu going forward
            if option == '1':
                self.quick = True
                exitLoop = True
            #option 2 is associated with detailed menu going forward
            elif option == '2':
                self.detailed = True
                exitLoop = True
            #error: not a correct input
            else:
                print(option + ' is not a valid menu option. Please select a valid menu option.\n')

    #master character sheet function
    def buildCharacterSheet(self, character):
        #get player name
        print("Please enter the name of the player")
        playerName = input()

        #get character name
        print("Please enter the name of the character")
        characterName = input()

        #setting variables like this for now in case we want to put it in a try/except for
        #error handling later
        character.player_name = playerName
        character.char_name = characterName

        #race class will handle all race attributes
        race = Race()

        #race will be filled in depending on menu selection
        if self.quick == True:
            race.chooseRace(character, menuOption='quick')
        else:
            race.chooseRace(character, menuOption='detailed')