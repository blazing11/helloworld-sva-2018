playerkey = []

# main! most programs start with this.
from threading import Timer, Thread
from threadedtimer import ThreadedTimer
import pygame,sys


# timer variables
global totalTime

totalTime = 0


def gameOver():
    print("Game Over!")

def countTime():
    global totalTime # our global variable
  
    # we write our code to happen every frame here!
    if (totalTime > 200):
        print("gameOver")
        myTimer.cancel()
        gameOver()


    # this happens once every second
    totalTime += 1
    #print(totalTime)
    #print("Total time: " + str(totalTime))

# this is our timer!
global myTimer
myTimer = ThreadedTimer(1, countTime, "countTime") # every second
myTimer.daemon = True  # handles part of the error from ctrl+c exiting


def mainGame():
    myTimer.start() # start the timer once only!

    pygame.init()
    pygame.mixer.init()


    source_path='/Users/xianhao3/Music/xiami/Trobar De Morte-Excalibur.wav'
    pygame.mixer.music.load(source_path)
    pygame.mixer.music.play()

    
    printGraphic("title") # call the function to print an image
    introStory() # start the intro
    # imports

    



def printGraphic( name ):
    if (name == "title"):
        print '      _                   _             _   _        _        _        '
        print '    /\ \                 /\_\          /\ \/\ \     /\_\     / /\      '
        print '   /  \ \               / / /  _      /  \ \ \ \   / / /    / /  \     '
        print '  / /\ \ \             / / /  /\_\   / /\ \ \ \ \_/ / /    / / /\ \__  '
        print '/ / /\ \ \           / / /__/ / /  / / /\ \_\ \___/ /    / / /\ \___\  '
        print '\/_//_\ \ \         / /\_____/ /  / /_/_ \/_/\ \ \_/     \ \ \ \/___/  '
        print '   __\___ \ \       / /\_______/  / /____/\    \ \ \       \ \ \       '
        print '/ /\   \ \ \     / / /\ \ \    / /\____\/     \ \ \  _    \ \ \        '
        print '/ /_/____\ \ \   / / /  \ \ \  / / /______      \ \ \/_/\__/ / /       '
        print '/__________\ \ \ / / /    \ \ \/ / /_______\      \ \_\ \/___/ /       '
        print '\_____________\/ \/_/      \_\_\/__________/       \/_/\_____\/        '
        print '                                                        .  ...         '
        print '                                               ...  .8$DI==~DN8,.      '
        print ' .$ZOO$O?, ...                    .,:,:,=.D=:,.   ..,:D,.              '
        print ' +N8D8OO7I=?=:D8Z7I+.....        :,,D===8D~.          .NI.             '
        print ' .,~I??7I+DD8DODDDDD8$~:::,:I87IN+:Z:.Z=$:,~.          .N?.            '
        print ' .?7:77?=,,,:,,,:~~~=IOZONDNNNOO,$,O88.:~=.           .D:.             '
        print '=778ZN+=.            ....,,,:O,,,DDD,,::=.            N~.              '
        print ' :~,.,O$:                     ..,,~8=:.:,=.            Z~.             '
        print '   .,.                  ...Z$.:,,,:,:Z:            .D=.                '
        print '    .. +ZOOOI,,$:O$?DI,:?D~$:,.          $O~.                          '
        print '    . ..+ZO8OZI+~=~II8DNDN8DN8~D:+8~Z$:,,,          $~,                '
        print '  .:Z$OZ~~:,~+7$Z88NNNNNNOZ7==~~:,:$~:NODZI+,~+.       .D~:.           '
        print ' .7$DODODNNDNNNOZI==~~:,,....      =NO$~7D$,,:=:    ...==:.            '
        print '  7O8N7~+$++=,...                .8,7~:I,.$88,:~.. IZ8+~.              '
        print '...Z=~=~?N,               ..O:?DNI.:,:7.,::ONNMN==:.                   '
        print ' IN8$N=I:.           .?7,+DM==,..,,,,,,.+:.....                        '
        print '.M~...::.         7?,IND=~,.     .,:::,.                               '
        print ' ..          . 7$+DNN+~,.                                              '
        print '  ..78:.DND=~,.                                                        '
        print '  O8~78NN+~..                                                          '
        print ' O?+ZNNNZ=:.                                                           '
        print ' Z$+ONNNZ$?:.                                                          '
        print ' .MNDOZZZ$7?.                                                          '
        print ' .,:,.ZO7Z+7~.                                                         '
        print '  Z~=:,.:.                                                             '
        print '  .~,                                                                  '
      
    if (name == "key1"):
        print ' ,o.          8 8'
        print 'd   bzzzzzzzza8o8b'
        print ' `o'

    if (name == "castle"):
        print '                                        o                              '
        print '                                    _---|         _ _ _ _              '
        print '                                 o   ---|     o   ]-I-I-I-[            '
        print '                             _---|      | _---|    \ `  /              '
        print '                ]-I-I-I-I-[   ---|      |  ---|    |.   |              '
        print '                 \ `    _/       |     / \    |    | /^\|              '
        print '                  [*]  __|       ^    / ^ \   ^    | |*||              '
        print '                  |__   ,|      / \  /    `\ / \   | ===|              '
        print '                  | ___ ,|__   /    /=_=_=_=\   \  |,  _|              '
        print '               I_I__I_I__I_I  (====(_________)___|_|____|____          '
        print '               \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_|'
        print '                 |[]      |   | []  |`__  . [  \-\--|-|--/-/'
        print '                 |.   | | |___|_____I___|___I___|---------|' 
        print '                / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] |'
        print '               <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \''
        print '               ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===>'
        print '               ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] ['
        print '              <===>     ' '||||| |   |   | ||||.||  []   <===>'''
        print '               \T/  | |-- ||||| | O | O | ||||.|| .  |    \T/'
        print '                |      . _||||| |   |   | ||||.|| |     | |'
        print '             ../|  v . | .|||||/____|____\|||| /|. . | . ./'
        print '              |//\............/...........\........../../\\\''
    
    if (name == "key2"):
        print '8 8 8 8                     ,ooo.'
        print '8a8 8a8                    oP   ?b'
        print 'd888a888zzzzzzzzzzzzzzzzzzzz8     8b'
        print "`""^""'                   '?o___oP'"

    if (name == "key3"):
        print '          xxxxxxx'
        print '         xxx   xxx'
        print '    xxxxxxx     xxxxxxx'
        print '    xx   xxx   xxx   xx '
        print '   xx     xxxxxxx     xx '
        print '    xx   xxxxxxxxx   xx'
        print '     xxxxx xxxxx xxxxx'
        print '           xxxxx'
        print '           xxxxx'
        print '           xxxxx'
        print '           xxxxx '
        print '           xxxxx'
        print '           xxxxx'
        print '           xxxxx'
        print '           xxxxx '
        print '        xxxxxxxx'
        print '        xxxxxxxx'
        print '           xxxxx'
        print '        xxxxxxxx'
        print '        xxxxxxxx '
        print '           xxxxx'

    if (name == "closedTreasure"):
        print '                  ____...------------...____'
        print '              _.-"` /o/__ ____ __ __  __ \o\_`"-._'
        print '            .      / /                    \  \    . '
        print '            |=====/o/======================\o\=====|'
        print '            |____/_/________..____..________\_\____|'
        print '            /   _/ \_     <_o#\__/#o_>     _/ \_   |'
        print '            \_________\####/_________/'
        print '             |===\!/========================\!/===|'
        print '             |   |=|          .---.         |=|   |'
        print '             |===|o|=========/     \========|o|===|'
        print '             |   | |         \() ()/        | |   |'
        print '             |===|o|======{-.)' 'A (.-''}===|o|===|'
        print '             | __/ \__     -.\uuu/.-      __/ \__ |'
        print '             |==== . . ^ . .====|'
        print '             |  _\o/   __  {.  __   .} _   _\o/  _|'
        print '             `""""-""""""""""""""""""""""""""-""""`'

    if (name == "openedTreasure"):
        print '                           _.--.'
        print '                         -_: - ||'
        print '                   _.- _.-:::: ||'
        print '              _.-: _.-::::::   ||'
        print '            . `-.-:::::::      ||'
        print '           /. `;|:::::::       ||_'
        print '          ||   ||::::::       _.;._-._'
        print "          ||   ||:::::'  _.-!oo @.!-._'-."
        print "          \'.  ||:::::.-!()oo @!()@.-'_.|"
        print "           '.'-;|:.-'.&$@.& ()$%-'o.'\U||"
        print "             `>'-.!@%()@'@_%-'_.-o _.|'||"
        print "              ||-._'-.@.-'_.-' _.-o  |'||"
        print "              ||=[ '-._.-\U/.-'    o |'||"
        print "              || '-.]=|| |'|      o  |'||"
        print "              ||      || |'|        _| ';"
        print "              ||      || |'|    _.-'_.-'"
        print "              |'-._   || |'|_.-'_.-'"
        print "               '-._'-.|| |' `_.-'"
        print "                   '-.||_/.-'" 
    
    if (name == "door"):
        print "          ,-' ;  ! `-."
        print "         / :  !  :  . \ "
        print "        )| .  :)(.  !  |"
        print "        |     (##)  _  |"
        print "        |  :  ;`'  (_) ("
        print "        |  :  :  .     |"
        print "        )_ !  ,  ;  ;  |"
        print "        || .  .  :  :  |"
        print "        |  .  |  :  .  |"
        print "        |mt-2_;----.___|"
       
    if (name == "window"):
        print "            XXXXXXXXXXXXXX"
        print "           XX            XX"
        print "          XX XXXX      XX XX"
        print "         X  X    X    X  X  X"
        print "         | X      X   X   X |"
        print "         | |       |  |   | |"
        print "         | |       |  |   | |"
        print "         | |       |  |   | |"
        print "         | |       |  |   | |"
        print "         | +-------+  +---+ |"
        print "         | +-------+  +---+ |"
        print "         | |       |  |   | |"
        print "         | |       |  |   | |"
        print "         | |       |  |   | |"
        print "         | |       |  |   | |"
        print "         | |       |  |   | |"
        print "         | |       |  |   | |"
        print "         | +-------+  +---+ |"
        print "         +------------------+"
    if (name == "wizard"):
        print"              //"
        print"              //"
        print"            _ //"
        print"         .' . // '."
        print"         '_ '_\/_'  `_"
        print"         .  . \\  .  ."
        print"        .==. ` \\' .'"
        print" .\|   //bd\\   \,"
        print" \_'`._\\__//_.'`.;"
        print"   `.__      __,' \\"
        print"       |    |      \\"
        print"       |    |       `"
        print"       |    |"
        print"       |    |"
        print"       |____|"
        print"      =='  '=="
    if (name == "wizardmaster"):
        print"                   ____"
        print"                 .'* *.' "
        print"               __/_*_*(_ "
        print"              / _______ \ "
        print"             _\_)/___\(_/_  "
        print"            / _((\- -/))_ \  "
        print"            \ \())(-)(()/ /  "
        print"             ' \(((()))/ '    "
        print"            / ' \)).))/ ' \    "
        print"           / _ \ - | - /_  \   "
        print"          (   ( .;''';. .'  )   "
        print"          _\ __ /    )\ __ /_   "
        print"            \/  \   ' /  \/      "
        print"             .'  '...' ' )    "
        print"              / /  |  \ \ "
        print"             / .   .   . \   " 
        print"            /   .     .   \    "
        print"           /   /   |   \   \    "
        print"         .'   /    b    '.  '.   "
        print"     _.-'    /     Bb     '-. '-._  "
        print" _.-'       |      BBb       '-.  '-. "
        print"(________mrf\____.dBBBb.________)____) "
 




























    if (name == "youwin"):
        print "                    ___           ___                    ___                        ___     "
        print "      __           /  /\         /  /\                  /  /\           ___        /  /\    "
        print "  |  |\        /  /::\       /  /:/                    /  /:/_         /__/\      /  /::|      "
        print "  |  |:|      /  /:/\:\     /  /:/                    /  /:/ /\        \__\:\    /  /:|:|   "
        print "  |  |:|     /  /:/  \:\   /  /:/                 /  /:/ /:/_       /  /::\  /  /:/|:|__     "
        print "  |__|:|__  /__/:/ \__\:\ /__/:/     /\          /__/:/ /:/ /\   __/  /:/\/ /__/:/ |:| /\    "
        print "  /  /::::\ \  \:\ /  /:/ \  \:\    /:/          \  \:\/:/ /:/  /__/\/:/~~  \__\/  |:|/:/"
        print " /  /:/~~~~  \  \:\  /:/   \  \:\  /:/            \  \::/ /:/   \  \::/         |  |:/:/ "
        print "/__/:/        \  \:\/:/     \  \:\/:/              \  \:\/:/     \  \:\         |__|::/  "
        print "\__\/          \  \::/       \  \::/                \  \::/       \__\/         /__/:/   "
        print " \__\/          \__\/                                \__\/                      \__\/    "





def testKey():
    if len(playerkey)==3:
        print "Congratulations! You get all 3 keys! Now you need to find the trasure!"
    if len(playerkey)==2:
        print "You have to find the last key!"
    if  len(playerkey)==1:
        print "Now you have 2 keys to find."

def testKeytreasure():
    if len(playerkey)<3:
        print " It seems that you don't have enough keys."
    if len(playerkey)==3:
        printGraphic("openedTreasure")
        playerkey.append("treasure")
        print"You get your treasure! Now you need to escape from this castle! It is collasping!"



def outsideCastle():
    printGraphic("castle")
    print "Now you are the gate of the castle"
    raw_input("press enter to enter it>")
    layoutOfCastle()



def layoutOfCastle():
    print "there are 3 floors and a dungeon in this castle"
    print "You should consider where to go now"

    pcmd = raw_input("Please make your choice [floor1, floor2, floor3, dungeon]")

    if (pcmd == "floor1"):
        floor1()

    if(pcmd == "floor2"):
        floor2()

    if(pcmd == "floor3"):
        floor3()

    if(pcmd == "dungeon"):
        dungeon()


def floor1():
    print "There is roomA roomB and roomC in floor1"
    print "You should consider where to go now"

    pcmd = raw_input("Please make your choice [roomA, roomB, roomC, leavefloor1]")
    if(pcmd == "leavefloor1"):
        layoutOfCastle()
    
    if(pcmd == "roomA"):
        print "there seems to be nothing in roomA, you may choose a different room"
        raw_input("press anything to continue")
        floor1()

    if(pcmd =="roomB"):
        roomB()
        
        if(pcmd == "leave it"):
            floor1()
        if(pcmd == "solve it"):
            mathquestion()

    if(pcmd == "roomC"):
        roomC()

def floor2things():
    print " you find bed and a cabinet and a wardrobe in that room. Guess where is the key."
    pcmd = raw_input("input [bed] or [cabinet] or [wardrobe]")
    if(pcmd == "bed"):
        print"nothing is there, try again."
        raw_input("press anything to re-try")
        floor2things()
    elif(pcmd == "cabinet"):
        print"nothing is there, try again."
        raw_input("press anything to re-try")
        floor2things()
    elif(pcmd == "wardrobe"):
        printGraphic("key2")
        print "Congratulations! You find a key!"
        playerkey.append("key2")
        testKey()
        raw_input("press anything to continue")
        layoutOfCastle()

def testtreasure():
    if "treasure" in playerkey:
        printGraphic("youwin")
        print "Congratulations! You escape successfully!"

    else:
        print "It seems that you should not choose window at this time...."
        raw_input("press anything to continue")
        




def floor2():
    print"There is a big room in floor2"
    pcmd = raw_input("input enter the big room or input leave to leave floor2")
    
    if(pcmd == "enter"):
        floor2things()

    if(pcmd == "leave"):
        layoutOfCastle()

def floor3():
    printGraphic("window")
    print "There is a big window and a secret room"
    pcmd = raw_input("input [big window] or [secret room] or [leave]")
    if(pcmd == "big window"):
        testtreasure()
    elif(pcmd == "leave"):
        layoutOfCastle()
    elif(pcmd == "secret room"):
        printGraphic("wizardmaster")
        print "there is a wizard master in this floor!"
        print "you should answer some question from him in order to get the key."
        print"If you input wrong answers you will be out."
        raw_input("press anything to star")

        pcmd = raw_input("who is the author of The Call of Cthulhu? (just last name all lowercase)")
        if (pcmd =="lovecraft"):
            print"Another question : 439.65*8/2 +4.75-3.339/3+3038-5554*2*9=?"
            pcmd = raw_input("input your answer")
            if(pcmd == "-95171.763"):
                print"Last question: What's the color of the sky?"
                pcmd = raw_input("input your answer")
                if(pcmd == "blue"):
                    
                    printGraphic("key3")
                    print"Congratulations! You are right! You get the key!"
                    
                    playerkey.append("key3")
                    testKey()
                    raw_input("press E to leave floor3")
                    layoutOfCastle()
                    
                else:
                    print "Sorry, you are moved out of the castle."
                    outsideCastle()

            else:
                print "Sorry, you are moved out of the castle."
                outsideCastle()

        else: 
            print "Sorry, you are moved out of the castle."
            outsideCastle()
            






    

def dungeon():
    printGraphic("door")
    print"Are you sure you want to go into it?"
    pcmd = raw_input("input yes or no ")
    if (pcmd == "yes"):
        printGraphic("closedTreasure")
        print"Wow! The treasure box is here!"
        treasure()
    if(pcmd == "no"):
        layoutOfCastle()

    


def treasure():
    raw_input("Do you get 3 keys? If so press Enter to open the treasure box")
    testKeytreasure()
            
def roomC():
    print "there is a wizard in the room, he has one key but you should guess an integer between 0-5"
    print "if you guess rightly, you will get one key"
    import random
    wizardnumber = random.randint(0,5)
    printGraphic("wizard")
    pcmd = raw_input("input your number")

    if (pcmd == str(wizardnumber)):
        print " Congratulations! You get one key!"
        printGraphic("key1")
        playerkey.append("key1")
        testKey()
        raw_input("press anything to continue" )
        floor1()
    else:
        print "Wrong answer! The wizard use magic to get you out of the castle"
        outsideCastle()

def roomB():
    print "there is a security box with a math question on it, do you want to solve it or just leave it?"
    pcmd = raw_input("please input [solve it] or [leave it]") 
    if(pcmd == "solve it"):
      mathquestion()
    if(pcmd == "leave it"):
      raw_input("press E to leave this room")
      floor1()

def mathquestion():
    pcmd= raw_input("4*9/6+335-201=? input your answer")
    if(pcmd == "140"):
  
      print"you are right the security box is open but there is nothing, just badluck you should choose another room"
      raw_input("press anything to continue")
      floor1()
    else:
        print"do that again or leave roomB"
        pcmd = raw_input ("input [redo or leave roomB]")
        if(pcmd == "leave roomB"):

          floor1()
        if(pcmd == "redo"):
          mathquestion()

def introStory():
    # let's introduce them to our world
    print "Good to see you gain! What should I call you?"
    player = raw_input("Please enter your name >")

    # intro story, quick and dirty (think star wars style)
    print "Welcome to the dark castle " + player + "!"
    print "Your mission is to find the 3 keys and open the treasure in 200 seconds (counting at backstage)."
    print "And then you will need to escape from this castle."
    print "Because when time is up it wil collapse."
    print "Now, let's start our advanture!"
    

    pcmd = raw_input("please choose yes or no >")

    # the player can choose yes or no
    if (pcmd == "yes"):
        
        outsideCastle()

        
        
      
              
      


    else:
        print "No? ... That doesn't work here."
        pcmd = raw_input("please choose yes or no>")
        introStory() # repeat over and over until the player chooses yes!







mainGame() # this is the first thin
