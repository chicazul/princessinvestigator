# You can place the script of your game in this file.

init python:
    stats = ['name','kingdom','image','age','shoesize','birthstone','colours','cupcake','guilty','annoyance']
    p1 = ['Adelaide', 'Mauritania','bookish', '23', '7','Topaz','Teal and Silver','Red Velvet',False,0]
    p2 = ['Terabith', 'Rembel','faun', '17','5','Bone','Grey and Royal Blue','Angel Food',True,0]
    p3 = ['Nachelm', 'Ghreowold','warrior', '28','8.5','Granite','Amber and Red','Honey Almond',False,0]
    p4 = ['Oorit', 'Isiba','mecha', '38','6.5','Celadon','Pink and Gold','Carrot',False,0]
    
    princesses = []
    princess = {}
    princesses.append(dict(zip(stats,p1)))
    princesses.append(dict(zip(stats,p2)))
    princesses.append(dict(zip(stats,p3)))
    princesses.append(dict(zip(stats,p4)))
    
    timer_range = 0
    timer_jump = 'fail'
    
    annoyance = 0
    annoyance_range = 0
    annoyance_jump = 'fail'
    mood = ''
    
    failure = 'assassin'
    gameover = False

# Declare images below this line, using the image statement.
image black = Solid("#000000")
image xray bg = "images/xray-bg.png"
image xray machine = "images/xray-machine.png"
image luggage bookish = "images/luggage-bookish.png"
image luggage bookish xray = "images/luggage-bookish-inner.png"

image faun = "images/princess-faun.png"
image bookish = "images/princess-bookish.png"
image warrior = "images/princess-warrior.png"
image mecha = "images/princess-robo.png"
image faun blink = "images/princess-faun-blink.png"
image bookish blink = "images/princess-bookish-blink.png"
image warrior blink = "images/princess-warrior-blink.png"
image mecha blink = "images/princess-robo-blink.png"
image faun annoyed = "images/princess-faun-annoyed.png"
image bookish annoyed = "images/princess-bookish-annoyed.png"
image warrior annoyed = "images/princess-warrior-annoyed.png"
image mecha annoyed = "images/princess-robo-annoyed.png"
image faun annoyed blink = "images/princess-faun-annoyedblink.png"
image bookish annoyed blink = "images/princess-bookish-annoyedblink.png"
image warrior annoyed blink = "images/princess-warrior-annoyedblink.png"
image mecha annoyed blink = "images/princess-robo-annoyedblink.png"

image bookish cropped = LiveCrop((240,0,300,500),"bookish")
image faun cropped = LiveCrop((250,0,300,500),"faun")
image warrior cropped = LiveCrop((240,0,300,500),"warrior")
image mecha cropped = LiveCrop((250,0,300,500),"mecha")

image bookish animated:
    "bookish"
    pause 4.0
    "bookish blink"
    pause 0.1
    "bookish"
    pause 2.4
    "bookish blink"
    pause 0.1
    repeat
image faun animated:
    "faun"
    pause 4.0
    "faun blink"
    pause 0.1
    "faun"
    pause 2.4
    "faun blink"
    pause 0.1
    repeat
image warrior animated:
    "warrior"
    pause 4.0
    "warrior blink"
    pause 0.1
    "warrior"
    pause 2.4
    "warrior blink"
    pause 0.1
    repeat
image mecha animated:
    "mecha"
    pause 2.5
    "mecha blink"
    pause 0.1
    repeat
image bookish animated annoyed:
    "bookish annoyed"
    pause 2.0
    "bookish annoyed blink"
    pause 0.1
    "bookish annoyed"
    pause 2.4
    "bookish annoyed blink"
    pause 0.1
    repeat
image faun animated annoyed:
    "faun annoyed"
    pause 3.0
    "faun annoyed blink"
    pause 0.1
    "faun annoyed"
    pause 2.4
    "faun annoyed blink"
    pause 0.1
    repeat
image warrior animated annoyed:
    "warrior annoyed"
    pause 2.0
    "warrior annoyed blink"
    pause 0.1
    "warrior annoyed"
    pause 2.4
    "warrior annoyed blink"
    pause 0.1
    repeat
image mecha animated annoyed:
    "mecha annoyed"
    pause 3.0
    "mecha annoyed blink"
    pause 0.1
    repeat

# Declare characters used by this game.
define a = Character('Princess Adelaide')
define processedcount = 0

label start:
    $ time = 120
    $ timer_range = 120
    $ annoyance_range = 60
    $ assassin = renpy.random.randint(10,60)
    $ assassin_range = assassin
    jump intro
    return
    
label dossier:
    scene
    play music "music/Main Princess Theme.mp3"
    show screen annoyance_meter
    while processedcount < len(princesses):
        $ princess = princesses[processedcount]
        call screen dossier(princess)
        if (_return == "interview") | (_return == "xray")|(_return == "accuse"):
            call expression _return
            if gameover:
                jump ending
        elif _return == 1:
            if princess['guilty'] == True:
                show screen assassination_meter
            $ processedcount += 1
    hide screen annoyance_meter
    jump lastchance

label evidence:
    call screen evidence
    jump investigate
    
label intro:
    centered "Coronation Day dawns bright and clear. Everything is in order for the crowning of Princess Kathleen of Romania."
    centered "But wait! A messenger has just arrived, bearing news that one of the visiting princesses is an assassin in disguise! Princess Kathleen's life is in danger!"
    centered "It's up to you, the captain of the guard, to identify the nefarious noble before the ceremony."
    centered "Careful not to offend an innocent princess though--if you set off a diplomatic incident it may be your head on the chopping block."

label investigate:
    
    show screen countdown
    
    menu:
        "Examine evidence":
            jump evidence
        "Investigate princesses":
            jump dossier
    return
    
label interview:
    if princess['annoyance'] > 30:
        $ mood = "annoyed"
    show expression princess['image']+" animated "+mood as princessimage
    a "Why are you asking me this?"
    hide princessimage
    jump dossier
    
label xray:
    play music "music/Princess Beats.mp3"
    scene xray bg
    show layer xray:
        crop(190,100,400,310)
        xpos 190
        ypos 100
    show luggage bookish:
        xpos -0.75
        yalign 0.5
        linear 25.0 xpos 1.5
    show luggage bookish xray onlayer xray:
        xpos -0.75
        yalign 0.5
        linear 25.0 xpos 1.5
    call screen xray
    hide luggage bookish xray onlayer xray
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
    hide screen annoyance_meter
    hide screen countdown
    centered "Congratulations! You have captured the villain and saved Princess Kathleen!"
    $ gameover = True
    return

label fail:
    hide screen annoyance_meter
    hide screen countdown
    play music "music/Princess Fail.mp3" noloop
    if failure == 'assassin':
        centered "Tragedy strikes! The assassin has slipped by you."
        centered "Princess Kathleen is dead!"
    elif failure == 'time':
        centered "The coronation fanfare blares. You can delay the dignitaries no longer."
        centered "You watch the princesses walk away, with a sinking feeling that Princess Kathleen is still in danger..."
    elif failure == 'diplomacy':
        show expression princess['image']+" animated annoyed" as princessimage
        a "I have had quite enough of your impertinence. [princess[kingdom]] is no longer a friend of Romania!"
        hide princessimage
        centered "Uh oh, even if Princess Kathleen survives the coronation, you might have started a war."
    $ gameover = True
    return

label ending:
    centered "Game Over"
    return
    