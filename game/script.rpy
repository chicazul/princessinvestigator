# You can place the script of your game in this file.

init python:
    stats = ['name','kingdom','image','age','shoesize','birthstone','colours','cupcake','guilty','annoyance']
    p1 = ['Adelaide', 'Mauritania','bookish', '23', '7','topaz','Green, Coral, and Silver','Red Velvet',0,0]
    p2 = ['Terabith', 'Rembel','faun', '17','5','Bone','Grey and Royal Blue', 'Angel Food',0,0]
    p2 = ['', '','warrior', '28','8.5','Granite','Amber and Red', '',0,0] #finish filling these out
    p2 = ['', '','mecha', '17','5','Bone','Grey and Royal Blue', 'Angel Food',0,0]
    
    princesses = []
    princess = {}
    princesses.append(dict(zip(stats,p1)))
    princesses.append(dict(zip(stats,p2)))
    #princesses.append(dict(zip(stats,p3)))
    #princesses.append(dict(zip(stats,p4)))
    
    timer_range = 0
    timer_jump = 'fail'
    

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image faun neutral = "princess_faun.png"
image bookish neutral = "princess_bookish.png"
image warrior neutral = "princess_warrior.png"
image mecha neutral = "princess_robo.png"

image bookish cropped = LiveCrop((240,0,300,500),"bookish neutral")
image faun cropped = LiveCrop((240,0,300,500),"faun neutral")

# Declare characters used by this game.
define a = Character('Princess Adelaide')
define processedcount = 0

label start:
    jump intro
    return
    
label dossier:
    play music "music/Main Princess Theme.mp3"
    while processedcount < len(princesses):
        $ princess = princesses[processedcount]
        call screen dossier(princess)
        if (_return == "interview") | (_return == "xray")|(_return == "accuse"):
            call expression _return
        elif _return == 1:
            $ processedcount += 1
    jump lastchance

label evidence:
    call screen evidence
    jump investigate
    
label intro:
    centered "Coronation Day dawns bright and clear. Everything is in order for the crowning of Princess Kathleen of Romania."
    centered "But wait! A messenger has just arrived, bearing news that one of the visiting princesses is an assassin in disguise! Princess Kathleen's life is in danger!"
    centered "It's up to you, the captain of the guard, to identify the nefarious noble before the ceremony."
    centered "Careful not to offend an innocent princess though--if you set off a diplomatic incident it may be your head on the chopping block."
    $ time = 120
    $ timer_range = 120

label investigate:
    
    show screen countdown
    
    menu:
        "Examine evidence":
            jump evidence
        "Investigate princesses":
            jump dossier
    return
    
label interview:
    show expression princess['image']+" neutral" as princessimage
    a "Why are you asking me this?"
    hide princessimage
    jump dossier
    
label xray:
    play music "music/Princess Beats.mp3"
    call screen xray
    if _return == "accuse":
        call expression "accuse" pass (location="xray")
    else:
        jump dossier

label accuse(location="dossier"):
    menu:
        "You're lying!":
            pass
        "You are planning to kill Princess Kathleen!":
            if princess['guilty']:
                jump success
            else:
                $ princess['annoyance'] += 50
    jump expression location

label lastchance:
    centered "Oh no! You haven't identified the assassin!"
    centered "There's one last chance to save Princess Kathleen. Who is guilty?"
    $ processedcount = 0
    jump dossier

label success:

label fail: