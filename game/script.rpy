# You can place the script of your game in this file.

init python:
    stats = ['name','kingdom','image','age','shoesize','birthstone','colours','cupcake','guilty','annoyance','luggage']
    p1 = ['Adelaide', 'Mauritania','bookish', '23', '7','Topaz','Teal and Silver','Red Velvet',False,0,0]
    p2 = ['Terabith', 'Rembel','faun', '17','5','Bone','Grey and Royal Blue','Angel Food',True,0,0]
    p3 = ['Nachelm', 'Ghreowold','warrior', '28','8.5','Granite','Amber and Red','Honey Almond',False,0,0]
    p4 = ['Oorit', 'Isiba','mecha', '38','6.5','Celadon','Pink and Gold','Carrot',False,0,0]
    
    princesses = []
    princess = {}
    princesses.append(dict(zip(stats,p1)))
    princesses.append(dict(zip(stats,p2)))
    princesses.append(dict(zip(stats,p3)))
    princesses.append(dict(zip(stats,p4)))
    
    weapons = ['bear','book','gun','flask']
    items = ['bear','book','bra','comb','flask','gun','necklace','racket','shoe']
    
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
image bars = "images/bars.png"
image bg interview = "images/bg-interview.png"
image bg dungeon = "images/bg-dungeon.png"
image bg xray = "images/xray-bg.png"
image bg shoe = "images/shoe.png"
image fail flask = "images/failure-flask.png"
image fail book = "images/failure-book.png"

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

image bear = "images/item-bear-innocent.png"
image book = "images/item-book-innocent.png"
image bra = "images/item-bra-innocent.png"
image comb = "images/item-comb-innocent.png"
image flask = "images/item-flask-innocent.png"
image gun = "images/item-gun-innocent.png"
image necklace = "images/item-necklace-innocent.png"
image racket = "images/item-racket-innocent.png"
image shoe = "images/item-shoe-innocent.png"
image bear xray = "images/item-bear-sil.png"
image book xray = "images/item-book-sil.png"
image bra xray = "images/item-bra-sil.png"
image comb xray = "images/item-comb-sil.png"
image flask xray = "images/item-flask-sil.png"
image gun xray = "images/item-gun-sil.png"
image necklace xray = "images/item-necklace-sil.png"
image racket xray = "images/item-racket-sil.png"
image shoe xray = "images/item-shoe-sil.png"
image bear guilt = "images/item-bear-guilty.png"
image book guilt = "images/item-book-guilty.png"
image flask guilt = "images/item-flask-guilty.png"
image gun guilt = "images/item-gun-guilty.png"

    
# Declare characters used by this game.
define current = 0
define p = Character("'Princess '+princesses[current]['name']",dynamic=True)

init:
    transform luggage_placement(x,y):
        xoffset x
        yoffset y
    
    transform luggage_scroll:
        xpos -0.75
        yalign 0.5
        linear 25.0 xpos 1.5
        
label start:
    $ time = 120
    $ timer_range = 120
    $ annoyance_range = 60
    $ assassin = renpy.random.randint(10,60)
    $ assassin_range = assassin
    call initialize_princesses
    
    #insert code for testing here
    jump intro
    return

label initialize_princesses:
    python:
        suspicious = []
        for princess in princesses:
            princess['annoyance'] = 0
            princess['shoesize'] = renpy.random.randint(4,11)
            princess['guilty'] = ''
            luggage = set()
            weapon = weapons[renpy.random.randint(0,3)]
            luggage.add(weapon)
            suspicious.append(weapon)
            while len(luggage) < 6:
                luggage.add(items[renpy.random.randint(0,8)])
            princess['luggage'] = luggage
        guilty = renpy.random.randint(0,3)
        princesses[guilty]['guilty'] = suspicious[guilty]
        
    return
    
label dossier:
    scene black
    play music "music/Main Princess Theme.mp3"
    show screen annoyance_meter
    while current < len(princesses):
        $ princess = princesses[current]
        
        call screen dossier(princess)
        if (_return == "interview") | (_return == "xray")|(_return == "accuse"):
            call expression _return
            scene black
            if gameover:
                jump ending
        elif _return == 1:
            if princess['guilty'] == True:
                show screen assassination_meter
            $ current += 1
    hide screen annoyance_meter
    jump lastchance
    
label evidence:
    call screen evidence
    jump investigate
    
label intro:
    centered "Coronation Day dawns bright and clear. Everything is in order for the crowning of Princess Kathleen of Romania."
    scene bg shoe
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
    scene bg interview
    if princess['annoyance'] > 30:
        $ mood = "annoyed"
    else:
        $ mood = ""
    show expression princess['image']+" animated "+mood as princessimage
    p "Why are you asking me this?"
    hide princessimage
    return
    
label xray:
    play music "music/Princess Beats.mp3"
    scene bg xray
    show layer xray:
        crop(190,100,400,310)
        xpos 190
        ypos 100
    show luggage bookish at luggage_scroll
    show luggage bookish xray at luggage_scroll onlayer xray
    python:
        x,y,width,height = 210,-90,360,265 #Initial x,y offset to make up for drawing onto moving luggage
        xcenter = x + (width / 2)
        xright = x + width
        ybottom = y + height
        positions = ['topleft','topcenter','topright','bottomleft','bottomcenter','bottomright']
        i = 0
        for item in princess['luggage']:
            renpy.show(item,[luggage_placement(x,y)],layer='hidden')
            ix,iy,iw,ih = renpy.get_image_bounds(item,layer='hidden')
            nx,ny = x,y
            if 'center' in positions[i]:
                nx = int(xcenter - (iw/2))
            if 'right' in positions[i]:
                nx = int(xright - iw)
            if 'bottom' in positions[i]:
                ny = int(ybottom - ih)
            renpy.hide(item,layer='hidden')
            renpy.show(item+" xray",[luggage_scroll, luggage_placement(nx,ny)],layer='xray')
            i += 1
            if i > 5:
                i = 0
    call screen xray
    scene onlayer xray
    if _return == "accuse":
        call expression "accuse" pass (location="xray")
    return

label accuse(location="blank"):
    if location == "dossier" or location == "interview":
        scene bg interview
        if princess['annoyance'] > 30:
            $ mood = "annoyed"
        else:
            $ mood = ""
        show expression princess['image']+" animated "+mood as princessimage
    elif location == "xray":
        scene onlayer xray
        scene bg xray
        show xray machine
        show luggage bookish xray behind xray
        python:
            x,y,width,height = 225,140,360,265 #Initial x,y offset to make up for drawing onto moving luggage
            xcenter = x + (width / 2)
            xright = x + width
            ybottom = y + height
            positions = ['topleft','topcenter','topright','bottomleft','bottomcenter','bottomright']
            i = 0
            for item in princess['luggage']:
                renpy.show(item,[luggage_placement(x,y)],layer='hidden')
                ix,iy,iw,ih = renpy.get_image_bounds(item,layer='hidden')
                nx,ny = x,y
                if 'center' in positions[i]:
                    nx = int(xcenter - (iw/2))
                if 'right' in positions[i]:
                    nx = int(xright - iw)
                if 'bottom' in positions[i]:
                    ny = int(ybottom - ih)
                renpy.hide(item,layer='hidden')
                renpy.show(item+" xray",[luggage_placement(nx,ny)])
                i += 1
                if i > 5:
                    i = 0
    else:
        $ location = "dossier"
    menu:
        "I see the murder weapon!" if location == "xray":
            python:
                for item in princess['luggage']:
                    type = ''
                    #renpy.say(narrator,"[item] [princess[guilty]]")
                    if item == princess['guilty']:
                        type = " guilt"
                    ix,iy,iw,ih = renpy.get_image_bounds(item,layer='master')
                    renpy.show(item+type,[luggage_placement(ix,iy)])
                if princess['guilty'] == '':
                    princess['annoyance'] += 50
                location = "dossier"
            menu:
                "You are planning to kill Princess Kathleen!":
                    if princess['guilty'] != '':
                        jump success
                    else:
                        $ princess['annoyance'] += 50
                "Never mind.":
                    pass
        "You're lying!" if location == "interview":
            pass
        "You are planning to kill Princess Kathleen!":
            if princess['guilty'] != '':
                jump success
            else:
                $ princess['annoyance'] += 50
        "Never mind.":
            pass
    jump expression location
    return

label lastchance:
    centered "Oh no! You haven't identified the assassin!"
    centered "There's one last chance to save Princess Kathleen. Who is guilty?"
    $ current = 0
    jump dossier

label success:
    play music "music/Princess Fanfare.mp3"
    hide screen annoyance_meter
    hide screen countdown
    scene bg dungeon
    show expression princess['image']+" animated annoyed" as princessimage
    pause 1
    show bars with moveinright
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
        scene bg interview
        show expression princess['image']+" animated annoyed" as princessimage
        p "I have had quite enough of your impertinence. [princess[kingdom]] is no longer a friend of Romania!"
        hide princessimage
        centered "Uh oh, even if Princess Kathleen survives the coronation, you might have started a war."
    $ gameover = True
    return

label ending:
    centered "Game Over"
    return
    