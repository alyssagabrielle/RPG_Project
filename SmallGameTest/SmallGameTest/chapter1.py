from interface import userInterfaceController
ui = userInterfaceController()

from character import character
from combat import weaponObj
from combat import fight

player = character(150,None)

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
    ui.output("Enter your name: ")
    tempName = input().capitalize()
    player.name = tempName

    ui.output(player.name + " ventures forth. Shadows jump before you. ")
 
    enemies = []
    for i in range(2):
        enemies.append(character(50,("Thug " + str(i+1))))
    ui.displayEnemies(enemies)

    response = ui.getAction(("fight","flee"))
    if response == "flee":
        ui.output("You ran away.")
    elif response == "fight":
        ui.output("You chose to fight the enemies. ")
        sharpKnife = weaponObj("Sharp Knife",20,0.4)
        club = weaponObj("Club",30,0.25)

        enemies[0].equip(club)
        enemies[1].equip(club)

        player.equippedWeapon = ui.getWeapon((sharpKnife,club))
        fight(player,enemies)

