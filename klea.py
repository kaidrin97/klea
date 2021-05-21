#opening credits
import time,sys
player_name = ""

#puzzle vars
var_corkscrew = 0
var_matches = 0
rope = 0

#key vars
cellar_key = 0
kitchen_key = 0
bedroom_key = 0

def typewriter(string):
   for l in string + '\n':
     sys.stdout.write(l)
     sys.stdout.flush()
     time.sleep(0.03)

def start_game():
    global player_name
    global var_corkscrew
    global var_matches
    global rope
    global cellar_key
    global kitchen_key
    global bedroom_key

    player_name = ""
    var_corkscrew = 0
    var_matches = 0
    rope = 0
    cellar_key = 0
    kitchen_key = 0
    bedroom_key = 0


####ALEXS CODE BELOW####


    typewriter("Welcome to...")
    print("""
                                      _        _        _______  _______ 
                                     | \    /\( \      (  ____ \(  ___  )
                                     |  \  / /| (      | (    \/| (   ) |
                                     |  (_/ / | |      | (__    | (___) |
                                     |   _ (  | |      |  __)   |  ___  |
                                     |  ( \ \ | |      | (      | (   ) |
                                     |  /  \ \| (____/\| (____/\| )   ( |
                                     |_/    \/(_______/(_______/|/     \|
            """)
    typewriter("What is your name?\n")
    player_name = input("\nName: ")
    player_name = player_name.lower()
    player_name = player_name.capitalize()
    typewriter(f"Hello, {player_name}.\n")
    time.sleep(1)
    cellar()
def cellar():
    typewriter("You awake on a damp cold cellar floor, it is dimly lit and cold down here, you see some stairs to your right leading up to a door, a corkscrew on the floor,\na huge wine rack spanning to the top of the celing and in the corner what looks like a story book.\n")
    time.sleep(1)
    cellar_choices()
def cellar_choices():
    global var_corkscrew
    global cellar_key
    cellar_list = ["1: Stairs", "2: Corkscrew", "3: Wine rack", "4: Book"]
    time.sleep(1)
    typewriter("What would you like to do?\n")
    time.sleep(1)
    for i in cellar_list:
        print(i)
        time.sleep(0.3)
    action = input("\nWhat would you like to do:  ")
    if action.lower() == "1" or action.lower() == "stairs":
        if cellar_key == 0:
            typewriter("you go up the stairs, at the top is a door, you try the handle but it is locked.")
            time.sleep(1)
            cellar_choices()
        elif cellar_key == 1:
          typewriter("you try the key in the door CLUNK! It spins round with ease and the door swings open...")
          time.sleep(1)
          kitchen()
        else:
            cellar_choices()
    elif action.lower() == "2" or action.lower() == "corkscrew":
        if var_corkscrew == 0:
            typewriter("You pick up the corkscrew, congrats!\n")
            var_corkscrew += 1
            cellar_choices()
        else:
            typewriter("You've already picked up the corkscrew.\n")
            cellar_choices()
    elif action.lower() == "3" or action.lower() == "wine rack":
        typewriter("You approach the wine rack, on it are some broken bottles, a line with 6 bottles on it appear to be pristine and corked.")
        time.sleep(1)
        typewriter("Would you like to look at the bottles? [Y/N]")
        action = input()
        if action.lower() == "y":
            wine_bottles()    
        else:
            cellar_choices()
    elif action.lower() == "4" or action.lower() == "book":
        typewriter("You scramble to the book, the corners are dog eared and the back is damp from the floor.\nWould you like to read it? [Y/N]\n")
        time.sleep(1)
        action = input()
        if action.lower() == "y":
            book()
        else:
            cellar_choices()
    else:
        typewriter("Please enter a valid option!\n")
        cellar_choices()
def wine_bottles():
    global cellar_key
    global var_corkscrew
    typewriter("You inspect the bottles, there are 3 opened but empty bottles and 3 corked bottles, the glass is black and you cant see what is inside of them.\n")
    wine_list = ["1: 1964 Pinot Noir\n", "2: 1914 Shiraz\n", "3: 1980 Sauvignon Blanc\n"]
    for i in wine_list:
        typewriter(i)
    typewriter("Which bottle would you like to inspect?")
    bottle_selected = input()
    if bottle_selected.lower() == "2" or bottle_selected.lower() == "1914 Shiraz":
        if var_corkscrew == 1:
            if cellar_key == 0:
              typewriter("You open the bottle using the Corkscrew, inside is a key!")
              cellar_key += 1
              cellar_choices()
            elif cellar_key == 1:
              typewriter("This bottle's is empty, lets put it back\n")
              time.sleep(1)
              cellar_choices()
        if var_corkscrew == 0:
            typewriter("You need something to open this with!")
            cellar_choices()
    elif bottle_selected.lower() in ("1", "3", "1964 Pinot Noir", "1980 Sauvignon Blanc"):
            typewriter("This bottle's is empty, lets put it back\n")
            time.sleep(1)
            wine_bottles()
    else:
        typewriter("Please enter a valid option!\n")
        time.sleep(1)
        wine_bottles()
def book():
    typewriter("You open the book, the first passage reads:\" The last bullet was shot on the morning of 22 November 1914... The poppies grow in the fields of Flanders, where brave men laid their lives down for King and Country.\nThe rest of the pages are damp and unreadable, you put the book down.\"")
    time.sleep(3)
    cellar_choices()

####KYLES STUFF BELOW####

def kitchen():
    typewriter("You walk through the door into a well kept kitchen. . .\n")
    time.sleep(1)
    typewriter("Examining your surroundings you see a stove, next to it a countertop, in the middle of the room a table with chairs surrounding it and on the far side of the room, you see a lone door.\n")
    time.sleep(1)
    kitchen_choices()

def kitchen_choices():
    global var_matches
    global kitchen_key
    kitchen_list = ["1: Door", "2: Stove", "3: Countertop", "4: Table"]
    typewriter("What would you like to do?\n")
    time.sleep(1)

    for i in kitchen_list:
      print(i)
      time.sleep(0.3)
    
    action = input("\nWhat would you like to do:  ")
    if action.lower() == "1" or action.lower() == "door":
        if kitchen_key == 0:
            typewriter("You try to wrestle the door open, you swear you could remove the door from it's hinges... ... ... ... But you fail, you dejectedly return to the kitchen.")
            time.sleep(1)
        elif kitchen_key == 1:
            typewriter("With your newfound key you swiftly jam the key into the hole and twist. CLUNK! The sound of being one step closer to freedom! You pull the door open and continue on your way!")
            time.sleep(1)
            typewriter("proceeding to next room")
            bedroom()
    elif action.lower() == "2" or action.lower() == "stove":
        stove()
    elif action.lower() == "3" or action.lower() == "countertop":
        if var_matches == 0:
            typewriter("Browsing the items on top of the countertop you see a block of knives, a chopping board, but as you start to look away you glance upon a box of matches almost hidden besides the knife block, they might be useful later!")
            var_matches += 1
            time.sleep(1)
            kitchen_choices()
        else:
            typewriter("You've already seen everything this counter has to offer, no point wasting time here.")
            time.sleep(1)
            kitchen_choices()
    elif action.lower() == "4" or action.lower() == "table":
        typewriter("You look at the table, there is yesterdays newspaper folded on it and a pack of cards.")
        time.sleep(1)
        kitchen_choices()
    else:
        typewriter("Please enter a valid option!\n")
        kitchen_choices()

def stove():
    typewriter("You walk over to the stove, on top you see a pot made of cast iron. It looks like you could turn on the stove by the switch.")
    time.sleep(1)
    typewriter("What would you like to do?\n")
    time.sleep(1)
    stove_choices()

def stove_choices():
    global var_matches
    global kitchen_key
    stove_list = ["1: Switch", "2: Pot", "3: Leave"]

    for i in stove_list:
        print(i)
        time.sleep(0.3)
    
    action = input("\nWhat would you like to do:  ")

    if action.lower() == "1" or action.lower() == "switch":
      if var_matches == 0 and kitchen_key == 0:
          typewriter("You flick the switch, and gas starts flowing, but without a source of ignition your efforts are wasted. You flick the switch again and wonder how you can light the old thing.")
          time.sleep(1)
          stove_choices()
      elif var_matches == 1 and kitchen_key == 0:
        typewriter("You flick the switch, and gas starts flowing, you strike a match and hold it to the spewing gas and you start a flame! Like a caveman discovering fire for the first time you revel at the sight as the pot heats up...")
        time.sleep(1.5)
        typewriter("After a while you see the acid within the pot start the evaporate leaving only a key behind, taking it now would be a rather stupid idea, so you turn off the gas and wait for it to cool before taking your prize.")
        time.sleep(1)
        kitchen_key += 1
        kitchen_choices()
      elif kitchen_key == 1:
        typewriter("You already have the key, you wouldn't want to cause a fire hazard doing this...")
        time.sleep(1)
        kitchen_choices()

    if action.lower() == "2" or action.lower() == "pot":
        if kitchen_key == 0:
          typewriter("As you look into the pot you see that it's filled almost to the brim with liquid, and as you stare deeper you see an anomaly... It almost looks like a key! You put your hand in but burn yourself on the acid solution the key is submerged in. There must be another way to get to it!")
          time.sleep(1)
          stove_choices()
        else:
          typewriter("There is nothing in the pot anymore.")
          time.sleep(1)
          stove_choices()
    if action.lower() == "3" or action.lower() == "leave":
        typewriter("You leave the stove and return to the kitchen!")
        time.sleep(1)
        kitchen_choices()

def bedroom():
    typewriter("You enter the bedroom, it is musty and old in here, you see a large 4 poster bed\nin the centre of the room with a bedside table next to it, on the far wall is a\nhuge oak wardrobe opposite to that are some doors that seem to lead to a balcony.\n")
    time.sleep(1)
    bedroom_choices()

def bedroom_choices():
    bedroom_list = ["1: Bed", "2: Wardrobe", "3: Bedside table", "4: Balcony doors"]
    time.sleep(1)
    typewriter("What would you like to do?\n")
    for i in bedroom_list:
        print(i)
        time.sleep(0.3)
    action = input()
    if action.lower() == "1" or action.lower() == "bed":
        bed()
    
    if action.lower() == "2" or action.lower() == "wardrobe":
        wardrobe()

    if action.lower() == "3" or action.lower() == "bedside_table":
        bedside_table()

    if action.lower() == "4" or action.lower() == "balcony doors":
        balcony_doors()
    
    else:
        typewriter("Please enter valid option!\n")
        bedroom_choices()

def bed():
    typewriter("You look under the bed to find dusty old empty boxes, there seems to be nothing important under here.\n")
    bedroom_choices()

def wardrobe():
    typewriter("You look in the wardrobe and find empty hangers and an old man's smoking jacket, it looks like the only thing that has wore this jacket in years is dust and critters.\n")
    bedroom_choices()

def bedside_table():
    typewriter("You walk up to the bedside table, would you like to open it? [Y/N]\n")
    time.sleep(1)
    action = input()
    if action.lower() == "y":    
        open_bedside_table()
    else:
        bedroom_choices()

def open_bedside_table():
    global bedroom_key
    if bedroom_key == 0:
      typewriter("You open the bedside table and have searched around, you come accross a bunch of keys and notice one of them has WALE on it and you pick the keys up.\n")
      bedroom_key += 1
      bedroom_choices()
    else:
      typewriter("You open the bedside table and have a search around again, you find nothing of use.\n")
      bedroom_choices()

def balcony_doors():
    if bedroom_key == 1:
        typewriter("You approach the door and notice the lock also says WALE, you use the key with WALE on it and the balcony door unlocks and slides open with a push!\n")
        balcony()
    else:
        bedroom_key == 0
        typewriter("You walk up to the door, it is locked, you notice the lock says WALE above the keyhole.\n")
        bedroom_choices()

def balcony():
    typewriter("You step out on to the leaf-strewn balcony. The deep grey sky is framed by two columns supporting a crumbling plaster canopy. A dilapidated formal garden stretches out beneath you to meet the perimeter hedgerow.\n")
    time.sleep(0.5)
    balcony_choices()

def balcony_choices():
    typewriter("What will you do?\n")
    time.sleep(0.5)
    balcony_list = ["1. Lean over the parapet (Go left)", "2. Investigate the rusty bistro table (Go right)"]
    for i in balcony_list:
        typewriter(i)
    left_or_right = input()
    if left_or_right == "1" or left_or_right.lower() == "parapet" or left_or_right.lower() == "left":
        typewriter("It's an extremely steep drop. There is a wide lead drainpipe fixed to the wall. Could it support your weight?")
        time.sleep(0.5)
        drainpipe()
    elif left_or_right == "2" or left_or_right.lower() == "table" or left_or_right.lower() == "right":
        typewriter("On the tabletop there are several broken flowerpots, a coil of thick grimy rope and a damp scrap of paper covered in illegible scrawlings.")
        time.sleep(0.5)
        bistro_table()
    else:
        typewriter("Please enter a valid option.")
        balcony_choices()

def bistro_table():
    global rope
    typewriter("What would you like to do?")
    time.sleep(0.5)
    table_list = ["1. Look closer at the flowerpots", "2. Pick up the rope", "3. Pick up the note", "4. Go back"]
    for i in table_list:
        typewriter(i)
    action = input()
    if action.lower() == "1" or action.lower() == "flowerpots":
        typewriter("These are definitely broken.")
        bistro_table()
    elif action.lower() == "2" or action.lower() == "rope":
      if rope == 0:
        typewriter("This must have some use.")
        rope += 1
        bistro_table()
      else:
        typewriter("You already picked up the rope.")
        bistro_table()
      
    elif action.lower() == "3" or action.lower() == "note":
        typewriter("Whoever wrote this must have been very agitated.")
        bistro_table()
    elif action.lower() == "4" or action.lower() == "go back" or action.lower() == "back":
        balcony_choices()
    else:
        typewriter("Please enter a valid option.")
        bistro_table()
    
def drainpipe():
    global rope
    pipe_list = ["1. Attempt to use the drainpipe to escape", "2. Go back"]
    for i in pipe_list:
        typewriter(i)
    action = input()
    if action.lower() == "1" or action.lower() == "drainpipe" or action.lower() == "escape":
        if rope == 1:
            typewriter("You tie a sturdy knot around one of the balusters with the rope and gingerly manuoevre yourself on to the drainpipe ... \nyou start to shimmy down keeping a firm grip of the rope ... \nthe pipe wrenches out of the wall sending rubble and debris plummeting to the ground ... \nyour grip holds and you jump down the remaining five feet ... \nyou're clear!")
            you_win()
        else:
            typewriter("You haul yourself over the parapet and grip on to the drainpipe ... \nyou begin to lower yourself down ... \nyour foot slips on a creeping vine ... \nyou hurtle towards the ground ...")
            game_over()
    elif action.lower() == "2" or action.lower() == "go back" or action.lower() == "back":
        balcony_choices()
    else:
        typewriter("Please enter a valid option.")

def you_win():
    global player_name
    typewriter(f"Congratulations {player_name} you escaped! Would you like to play again? [Y/N]")
    action = input()
    if action.lower() == "y":
      start_game()
    else:
        quit()

def game_over():
  global player_name
  typewriter(f"You broke your legs. Would you like to play again {player_name}? [Y/N]")
  action = input()
  if action.lower() == "y":
    start_game()
  else:
    quit()

start_game()