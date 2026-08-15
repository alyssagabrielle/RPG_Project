from interface import userInterfaceController
ui = userInterfaceController()

from character import character
from weapon import weapon

def openingSequence():
    #ui.output("""
    #Sequence One. Smoky Night.\nYou glance over her shoulder for just a moment. Enough to witness a wash
    #of sparkling wet moonlight on a distant beach through a small window, dissipating into darkness as the wave slips 
    #away to some ocean, far away, with better prospects than I. The next glimmer to harness your eye next is 
    #of equal beauty, but unparalleled superiority, in the deep brown eye of the woman sitting across from you. 
    #She shines everywhere. Gold and jewelled adornments drip across her silk; divinity and richness ooze
    #through every gap between. Uncomfortably opaque smoke hangs constantly in the air, so one can never be certain
    #the figure before you truly sits there. You can't muster the conviction to avert your gaze from that glimmer.\n
    #"I'll consider your request," she spoke slowly, "When three distinct conditions are met. Remind me of your name,
    #traveller?"\n
    #""")
    name = str(input("Enter your name:"))

    ui.output(name + " ventures forth. Shadows jump forth before you. ")
    
    enemies = []
    for i in range(2):
        enemies.append(character(50,5))
    
    ui.displayEnemies(enemies)
    sharpKnife = weapon("Sharp Knife",20)
    club = weapon("Club",30)

    response = ui.getAction(("fight","flee"))
    if response == "flee":
        ui.output("You ran away.")
    elif response == "fight":
        ui.output("You chose to fight the enemies. ")
        ui.getWeapon((sharpKnife,club))
