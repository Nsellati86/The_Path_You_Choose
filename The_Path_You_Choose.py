import sys
import time
import random

# List 1
user_selection_1 = [
    "\nYou have come to a water bank. There is a large log that you can ride to the other side of the river.\n"
    "That was a fun little ride. You even managed to catch a fish-like creature with your bare hands! You reach the \n"
    "the other side, sit, start a fire, prepare that fishy-looking thing, fry it up, and....hey, it wasn't half bad.\n"
    "You get up, turn around to get back onto the path and.....ah shit another fork. \n\t(1) Left or (2) Right?",

    "\nYou have come to a cliff. It is not very high and easy to climb, so you do so. \n\tNow, (1) Left or (2) Right?",

    "\nYou have come to a large, rocky hill. At the top you stop to see what is ahead; you see a short stretch of desert\n"
    "you walk towards the desert. After 20 minutes, you are now at an oasis! NICE. After resting, you head towards an\n"
    "ancient-looking forest and arrive at....you guessed it...another fork... \n\t(1) Left or (2) Right?",

    "\nYou have come to a lake. You see marine life swimming about, you decide to walk around it instead of swim. After a\n"
    "few minutes you reach a new path on the other die of the lake. That path brings you to another damn fork! \n\t(1) Left"
    " or (2) Right?"
]
# List 2
user_selection_2 = [
    "\nA bear looking creature tears out onto the path you are walking and without any notice, attacks you!! You dodge\n"
    "out of the way, but the bear-like creature manages to just barely slash you upper back with it claws. You roll on\n"
    "the ground, twist around as you draw your blaster, and shoot the menacing creature right between the eyes! you\n"
    "continue down the path and you arrive at another fork! Almost as if this planet is just a series of forks.....\n"
    "\tAre you going (1) Left or (2) Right?",

    "\nA cute, little baby deer-like creature comes frolicking out of the brush. It stops in front of you on your path, \n"
    "looks up at you with big, brown adorable eyes; you bend down to pet it on the head, 'Hey there little guy' you\n"
    "say, and then it runs away in the cutest fashion. You continue down the path until you arrive at yet another\n"
    "fork in the path......this planet seems to be all forks in the road!! \n\tYou going (1) Left or (2) Right?",

    "\nA winged-creature comes flying at top speed out of the brush, where it evidently was hiding, and it starts to\n"
    "attack and scratch the top of your head! 'Maybe it doesn't like my hair-do?!' you think yto yourself as you draw\n"
    "your blaster. This thing is quick, so you blindly aim above your head, lick a shot off, and scare the winged-\n"
    "creature away. Whew, that could have been worse! You continue on until you reach another freaking fork! \n\tYou going"
    " (1) Left or (2) Right?",

    "\nYou start walking for a bit. Nothing happens. 'What a relief!' you think to yourself. You keep on walking. \n"
    "Your feet are starting to ache a bit. You sit down to rest. After a few minutes, you get back up and trudge along. \n"
    "After a short while, you pull up to yet another FORK! 'This freaking planet is all freaking forks!' \n\tYou going (1) "
    "Left or (2) Right?"
]
# List 3
user_selection_3 = [
    "\nWhat a journey it has been! You see the perfect spot to make camp atop a plateau that has cover. You feel you would \n"
    "be safe here while you repair your radio equipment. You start to move with caution, expecting some beastly thing to spring \n"
    "out of nowhere and maul you to death. Fortunately nothing of the like happens. You reach the safe spot and \n"
    "begin working on repairing your radio because you've had enough of this forky-ass planet!!",

    "\n'This has been such a freaking hassle and I am ready to bail on this planet.' you look up and see a perfect spot \n"
    "from where you can make camp and finally repair your radio because you will get a good signal and be able to reach \n"
    "out to your people to send a rescue ship. You head up to the spot, make your camp, and get to work on the radio.\n",

    "\n'I cannot wait until I am rescued and this forky-freaking planet is in my rearview mirror!' you say as look up and \n"
    "see the perfect spot atop a plateau that looks safe and secure and you have no doubt you'll be able to get a clear \n"
    "signal to message your people and get rescued! You quickly run up there, make camp, and start to fix your radio.\n",

    "\nYou are so exhausted from this trek that you take a moment to sit and gather your resolve. After a minute, you \n"
    "look up and see the perfect spot, on the highest ground around you, to make camp and have the enough safety and \n"
    "security to repair your radio. From there you will get a clear signal and finally be closer to getting off of \n"
    "this planet! You stand up, but too quickly and black out.............\n"
    "You regain consciousness to find yourself on the ground being nibbled on by small, mouse-like creatures. \n"
    "You scream, 'AAAAAHHHHHHHHHHH!!!!!!!!!' to make them all scatter, then you pick yourself up and head to the high \n"
    "ground so that you can make camp and begin repairing your radio to get the hell off of this planet!"
]
# List 4
user_last_choice = [
    "\nYou get a strong signal that is picked up by your people. They send a message saying that you will\n"
    "be rescued within the hour! YAY!!!\nThanks for playing!\n\nProgrammer: Nick Sellati\nSympol_TBG's Studios",

    "\nYour radio blows up and takes you with it to oblivion where you can now rest easy because now all\n"
    "of your problems are solved and you have nothing to worry about.\nThanks for playing!\n\nProgrammer: Nick Sellati"
    "\nSympol_TBG's Studios"
]
# Empty lists to store user integer selections
l_moves = []
r_moves = []


# Function to give player option to end game or replay
def quit_game():
    print("\nPress 'Q' or 'q' to quit game.")
    print("Press any other key to start a new game.")
    user_choice = input("\n>>> ").lower()
    print()
    # Checking for user input
    while True:
        if user_choice == 'q':
            sys.exit("Thank you for playing!")
        else:
            start_game()
            first_choice()


# Function for game introduction and context
def play_intro():
    print('''
        .................Whoa.................My head.....................................
        ''')
    time.sleep(2)
    print('''
        ..........Where am I?................The last thing that I remember was that my ship had 
        sustained heavy damage and I had to put her down on the nearest habitable spatial body.......
        ''')
    time.sleep(4)

    print("\nYou have crash-landed on an alien world after a malfunction on your spacecraft rendered it unable")
    print("to continue on its course through deep space. Luckily you were not mortally harmed, you realize that")
    print("you crash-landed on a planet that oddly seems to have naturally formed in a series of layers. Even if your")
    print("radio equipment was functional, you wouldn't be able to get a signal out to your people unless you reach")
    print("higher ground! You search around for your survival pack, you find it with everything intact; you put on")
    print("your O2-breather mask, exit your craft, and pull out your handheld nav-pad to ping the location")
    print("of the safest, most isolated high ground for a clear signal to send a distress call to your people.")
    time.sleep(10)
    print('''
        Just my luck..............my radio equipment is damaged. I need to set out to find suitable high ground 
        to make camp so that I can repair my radio and call for a lift off of this rock!  Hopefully I do not run into
        any trouble. Good thing my blaster is not damaged and has a full charge!
        ''')
    time.sleep(6)


# Function to begin the game
def start_game():
    print("\n\t\t\t\t******************** THE PATH YOU CHOOSE!! ********************\n\n")
    print("You must begin your expedition to a safe location to make camp and repair your communication equipment")
    print("in order to send out a distress signal to your people the next galaxy over for them to rescue you. On your")
    print("journey, you will be presented with 2 paths to choose between, and how your journey unfolds depends upon the")
    print("choices you make....choose wisely and best of luck!")
    time.sleep(6)
    l_moves.clear()
    r_moves.clear()


# Function for the first user choice
def first_choice():
    print("\n**********You come to a fork in the path: \nTo the (1) Left is a path through thick brush.")
    print("To the (2) Right is a path where you must wade through a small pond. \n\tChoose one!")
    user_choice_1 = int(input("\n>>> "))
    # Checking user input
    if user_choice_1 == 1:
        print("\nYou make a left and travel through the brush...nothing happens. You come up to another fork...")
        l_moves.append(user_choice_1)   # Adds user choice to proper list
        choice_2()
    elif user_choice_1 == 2:
        print("\nYou make a right, wade through the shallow pond...now you have wet socks...and arrive at another fork.")
        r_moves.append(user_choice_1)   # Adds user choice to proper list
        choice_2()
    else:
        print("\t\t*****Not a valid selection, please enter either '1' or '2'\n")
        time.sleep(3)
        first_choice()


# Function for the second choice presented to player
def choice_2():
    time.sleep(3)
    print("\nOf the path before you, \nTo the (1) Left is a rocky path through a ravine.")
    print("To the (2) Right is a soft, dirt path that leads through a field of tall grass. \n\tWhich way will you choose?")
    user_choice_2 = int(input("\n>>> "))
    # Checking user input
    if user_choice_2 == 1:
        print("\nYou head to the left. After a few minutes of walking, a shrill scream fills the air as a winged alien")
        print("swoops down to take a bite out of your head. You dodge the attack, and run down the path. After a")
        print("short while, you have lost that flying menace and have arrived at a new fork in the path...")
        l_moves.append(user_choice_2)   # Adding user selection to proper list
        choice_3()
    elif user_choice_2 == 2:
        print("\nYou head to the right...After a few minutes of walking through the tall grass, you start to itch")
        print("unbearably to the point that you want to scratch the skin off of your legs to stop the burning!")
        print("Clearly there were some species of bug in that field that decided to feast on your flesh for")
        print("disrupting their habitat! You apply a cream you have in your pack and now are at a new fork....")
        r_moves.append(user_choice_2)   # Adding user selection to proper list
        choice_3()
    else:
        print("\t\t*****Not a valid selection, please enter either '1' or '2'\n")
        time.sleep(3)
        choice_2()


# Function to present player with third choice
def choice_3():
    time.sleep(7)
    print("\n\tDo you want to go (1) Left or (2) Right?")
    random_selection = int(input("\n>>> "))
    # Checking user input
    if random_selection == 1:
        user_choice = random.sample(user_selection_1, 1)[0]     # Random selection from list
        print(user_choice)
        l_moves.append(random_selection)    # Adding user selection to proper list
        choice_4()
    elif random_selection == 2:
        user_choice = random.sample(user_selection_1, 1)[0]     # Random selection from list
        print(user_choice)
        r_moves.append(random_selection)    # Adding user selection to proper list
        choice_4()
    else:
        print("\t\t*****Not a valid selection, please enter either '1' or '2'\n")
        time.sleep(3)
        choice_3()


# Function to present player with a fourth choice
def choice_4():
    time.sleep(7)
    random_selection_1 = int(input("\n>>> "))
    # Checking user input
    if random_selection_1 == 1:
        user_choice_2 = random.sample(user_selection_2, 1)[0]       # Random selection from list
        print(user_choice_2)
        l_moves.append(random_selection_1)      # Adding user selection to proper list
        # Checking list for if player made for of the same integer selections in a row
        if len(l_moves) == 4:
            time.sleep(2)
            print("\nWait a minute...............")
            time.sleep(3)
            print("You just made 4 left turns!")
            time.sleep(2)
            print("Now you are right back where you started!")
            time.sleep(2)
            first_choice()      # Puts player back to the beginning
        else:
            choice_5()

    elif random_selection_1 == 2:
        user_choice_2 = random.sample(user_selection_2, 1)[0]       # Random selection from list
        print(user_choice_2)
        r_moves.append(random_selection_1)      # Adding user selection to proper list
        # Checking list for if player made four of the same integer selections in a row
        if len(r_moves) == 4:
            time.sleep(2)
            print("\nWait a minute.................")
            time.sleep(3)
            print("You just made 4 right turns!")
            time.sleep(2)
            print("Now you are right back where you started!")
            time.sleep(2)
            first_choice()      # Puts player back to the beginning
        else:
            choice_5()

    else:
        print("\t\t*****Not a valid selection, please enter either '1' or '2'\n")
        time.sleep(3)
        choice_4()


# Function that gives player a fifth choice to make
def choice_5():
    time.sleep(7)
    random_selection_2 = int(input("\n>>> "))
    # Checking user input
    if random_selection_2 == 1:
        user_choice_3 = random.sample(user_selection_3, 1)[0]       # Random selection from list
        print(user_choice_3)
        final_choice()
    elif random_selection_2 == 2:
        user_choice_3 = random.sample(user_selection_3, 1)[0]       # Random selection from list
        print(user_choice_3)
        final_choice()
    else:
        print("\t\t*****Not a valid selection, please enter either '1' or '2'\n")
        time.sleep(3)
        choice_5()


# Function for the final choice that decides the outcome of the game (win or lose) at random
def final_choice():
    time.sleep(10)
    print("\n'OK, rewire these here........ re-connect at these points...........'\n")
    time.sleep(3)
    print("'Now I just twist that in and tighten here, here, and there........and..........'\n")
    time.sleep(3)
    print("'Wow, I really want to get off of this planet. So badly in fact that I didn't even realize that I've been")
    print("trying to fix this radio for hours!'")
    time.sleep(2)
    print("\nAfter several hours of diligent, focused, painstaking work, you have done your very best to fix your")
    print("damaged radio and now you are ready to turn it on to send a distress call to your nearby home world so that")
    print("you can finally go home!\n")
    print("Do you want to (1) Turn the radio on....or..... (2) TURN THAT DAMN RADIO ON and get the hell of this planet!!")
    random_selection_3 = int(input("\n>>> "))
    # Checking player input
    if random_selection_3 == 1:
        user_choice_4 = random.sample(user_last_choice, 1)[0]       # Random selection from list
        print(user_choice_4)
        time.sleep(3)
        quit_game()
    elif random_selection_3 == 2:
        user_choice_4 = random.sample(user_last_choice, 1)[0]       # Random selection from list
        print(user_choice_4)
        time.sleep(3)
        quit_game()
    else:
        print("\t\t*****Not a valid selection, please enter either '1' or '2'\n")
        time.sleep(3)
        final_choice()


# Function calls
play_intro()
start_game()
first_choice()
