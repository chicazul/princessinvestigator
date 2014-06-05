# You can place the script of your game in this file.

init python:
    # Make all the xray buttons be the same size.
    style.xray_button.size_group = "xray"
    
    stats = ('name','kingdom','image','age','shoesize','birthstone','colours','cupcake','guilty','annoyance','luggage')
    p1 = ['Adelaide', 'Mauritania','bookish', '23', '7','Topaz',('teal','silver'),'Red Velvet',False,0,0]
    p2 = ['Terabith', 'Rembel','faun', '17','5','Bone',('grey','royal blue'),'Angel Food',True,0,0]
    p3 = ['Nachelm', 'Ghreowold','warrior', '28','8.5','Granite',('amber','red'),'Honey Almond',False,0,0]
    p4 = ['Oorit', 'Isiba','mecha', '38','6.5','Celadon',('pink','gold'),'Carrot',False,0,0]
    
    princesses = []
    princess = {}
    princesses.append(dict(zip(stats,p1)))
    princesses.append(dict(zip(stats,p2)))
    princesses.append(dict(zip(stats,p3)))
    princesses.append(dict(zip(stats,p4)))
    
    inquirylines = ('bookish','faun','warrior','mecha')
    a0 = ["What can I help you with today?","Did you wish to speak to me?","What do you want?","I will allow your questions."]
    # 1 Kathleen
    a1 = ["I have the utmost affection for dear Kathleen!","She seems a most pleasant individual","We respect each other's sovereignty.","We have met."]
    # 2 shoe
    a2 = ["Why would you think I had seen it?","No.","Of course not.","It does not look familiar to me."]
    # 3 spooon
    a3 = ["On the right side, to the right of the outside knife, typically.","My people have not put much research into Romanian dinner customs.","You have got to be kidding me.","Right."]
    # 4 coronation
    a4 = ["To further the pleasant relations between our two countries.","It was expected.","I like parties.","Does one need a reason?"]
    # 5 angry
    a5 = ["Is this really necessary?","...","You don't seriously suspect me of anything, do you?","I am displeased with your interrogation."]
    # 6 goodbye
    a6 = ["You're very welcome.","Blessings upon your people.","Good luck catching whoever you're looking for.","Goodbye."]
    
    answers = []
    answers.append(dict(zip(inquirylines,a0)))
    answers.append(dict(zip(inquirylines,a1)))
    answers.append(dict(zip(inquirylines,a2)))
    answers.append(dict(zip(inquirylines,a3)))
    answers.append(dict(zip(inquirylines,a4)))
    answers.append(dict(zip(inquirylines,a5)))
    answers.append(dict(zip(inquirylines,a6)))
    
    weapons = ['bear','book','gun','flask']
    items = ['bear','book','bra','comb','flask','gun','necklace','racket','shoe']
    
    timer_range = 0
    timer_jump = 'fail'
    
    assassin = 0
    guilt = 0
    herring = 0
    annoyance = 0
    annoyance_range = 0
    annoyance_jump = 'fail'
    mood = ''
    shoe = 0
    colour = ''
    colours = ''
    
    failure = 'assassin'
    gameover = False
    ended = False

# Declare images below this line, using the image statement.
image black = Solid("#000000")
image bars = "images/bars.png"
image bg interview = "images/bg-interview.png"
image bg dungeon = "images/bg-dungeon.png"
image bg xray = "images/xray-bg.png"
image bg shoe = "images/shoe.png"
image bg town = "images/bg-town.png"
image fail poison = "images/failure-poison.png"
image fail knife = "images/failure-knife.png"
image bg fail random:
    choice:
        "fail poison"
    choice:
        "fail knife"
image bg success = "images/win.png"

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
define evidence = Character("",window_left_margin=400,window_yminimum=600,window_top_padding=300)

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
    $ assassin = renpy.random.randint(1,15)
    $ assassin_range = assassin
    call initialize_princesses
    
    #insert code for testing here
    jump intro
    return

label initialize_princesses:
    python:
        suspiciousitems = []
        for princess in princesses:
            princess['annoyance'] = 0
            princess['shoesize'] = renpy.random.randint(4,11)
            princess['guilty'] = ''
            luggage = set()
            weapon = weapons[renpy.random.randint(0,3)]
            luggage.add(weapon)
            suspiciousitems.append(weapon)
            while len(luggage) < 6:
                luggage.add(items[renpy.random.randint(0,8)])
            princess['luggage'] = luggage
        guilt = renpy.random.randint(0,3)
        herring = guilt
        while herring == guilt:
            herring = renpy.random.randint(0,3)
        culprit = princesses[guilt]
        suspects = [princesses[herring],culprit]
        culprit['guilty'] = suspiciousitems[guilt]
        princesses[herring]['guilty'] = 'herring'
        shoe = culprit['shoesize']
        colour = suspects[renpy.random.randint(0,1)]['colours'][renpy.random.randint(0,1)]
        
    return
    
label dossier:
    if gameover:
        jump ending
    scene black
    show screen annoyance_meter
    while current < len(princesses):
        $ princess = princesses[current]
        
        call screen dossier(princess)
        if (_return == "interview") | (_return == "xray"):
            call expression _return
            scene black
            play music "music/Main Princess Theme.mp3"
            if gameover:
                jump ending
        elif _return == 1:
            if princess['guilty'] in weapons:
                show screen assassination_meter
            $ current += 1
    hide screen annoyance_meter
    jump lastchance
    
label evidence:
    scene bg shoe with dissolve
    evidence "The Royal Guard intercepted a coded message telling of the plot against Princess Kathleen."
    evidence "Unfortunately the conspirators escaped, but the guards retrieved a few items believed to belong to the guilty princess."
    evidence "A crystal dancing slipper, size [shoe]."
    evidence "A linen handkerchief, embroidered in [colour]"
    jump investigate
    
label intro:
    play music "music/Main Princess Theme.mp3"
    scene bg town with dissolve
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
    scene bg interview
    $ id = princess['image']
    $ song = "music/Princess-"+id+".mp3"
    play music song
    if princess['annoyance'] > 30:
        $ mood = "annoyed"
    else:
        $ mood = ""
    show expression princess['image']+" animated "+mood as princessimage
    if princess['annoyance'] < 10:
        $ answer = answers[0]
        p "[answer[%(id)s]]"
    else:
        $ answer = answers[5]
        p "[answer[%(id)s]]"
    menu:
        "Are you on good terms with Princess Kathleen?":
            $ answer = answers[1]
            p "[answer[%(id)s]]"
        "What is your shoe size?":
            if princess['image'] == 'faun':
                p "..."
            $ choice = renpy.random.randint(0,10)
            if choice < 2 or princess['guilty'] != '':
                $lieshoe = princess['shoesize'] - renpy.random.randint(1,3)
                p "[lieshoe]"
                jump interviewlieshoe
            else:
                p "[princess[shoesize]]"
        "Are you an assassin?":
            call expression "accuse" pass (location="interview")
            if gameover:
                jump ending
    jump interview2
    
label interviewlieshoe:
    menu:
        "Why did you lie about your shoe size?":
            p "I don't know what you mean."
            menu:
                "Accuse of lying":
                    call expression "accuse" pass (location="interview")
                    if gameover:
                        jump ending
                "Never mind.":
                    jump interview2
        "Thank you for your time":
            jump dossier
    jump interview2

label interviewlie:
    if princess['guilty'] != '':
        p "Ok, you caught me."
    else:
        p "I can't believe you would say that!"
        $ princess['annoyance'] += 10
    jump interview2
    
label interview2:
    menu:
        "Have you seen this shoe before?":
            if princess['image'] == 'faun':
                p "..."
            $ choice = renpy.random.randint(0,10)
            if princess['guilty'] == '':
                $ choice -= 2
            if choice < 2 and princess['guilty'] not in weapons:
                p "I believe I have seen Princess [princesses[%(guilt)d]['name']"
            elif choice > 1 and choice < 5:
                p "Yes."
            else:
                $ answer = answers[2]
                p "[answer[%(id)s]]"
        "In a formal table setting, which side of the plate would a soup spoon be?":
            $ answer = answers[3]
            p "[answer[%(id)s]]"
            $ princess['annoyance'] += 5
        "Why are you coming to the coronation?":
            $ answer = answers[4]
            if princess['image'] == 'faun':
                p "..."
            p "[answer[%(id)s]]"
    jump interviewend

label interviewend:
    menu:
        "Thank you for your time":
            $ answer = answers[6]
            p "[answer[%(id)s]]"
        "Don't go too far, I have more questions for you.":
            $ princess['annoyance'] += 10
        "You're the assassin!":
            call expression "accuse" pass (location="interview")
            if gameover:
                jump ending
    jump dossier
    
label xray:
    play music "music/Princess Beats.mp3"
    scene bg xray
    show layer xray:
        crop(190,100,400,310)
        xpos 190
        ypos 100
    show luggage bookish at luggage_scroll
    show luggage bookish xray at luggage_scroll onlayer xray
    # convoluted method for drawing items within suitcase
    python:
        x,y,width,height = 210,-90,360,265 #Initial x,y offset to make up for drawing onto moving luggage
        xcenter = x + (width / 2)
        xright = x + width
        ybottom = y + height
        positions = ['topleft','topcenter','topright','bottomleft','bottomcenter','bottomright']
        i = 0
        for item in princess['luggage']:
            # can't get the size until image is instantiated, so load on hidden layer
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
        if gameover:
            jump ending
    return

label accuse(location="dossier",accusation="You're lying!"):
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
                        jump interview
                "Never mind.":
                    pass
        "[accusation]" if location == "interview":
            jump interviewlie
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
    scene bg town
    with dissolve
    centered "Oh no! You haven't identified the assassin!"
    centered "There's one last chance to save Princess Kathleen. Who is guilty?"
    $ current = 0
    jump investigate

label success:
    if gameover == False:
        play music "music/Princess Fanfare.mp3"
        hide screen annoyance_meter
        hide screen countdown
        scene bg dungeon
        show expression princess['image']+" animated annoyed" as princessimage
        pause 1
        show bars with moveinright
        pause 1
        scene bg success
        pause
        $ gameover = True
    return

label fail:
    if gameover == False:
        hide screen annoyance_meter
        hide screen countdown
        play music "music/Princess Fail.mp3" noloop
        if failure == 'assassin':
            scene bg fail random
            pause
        elif failure == 'time':
            scene bg interview
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
    scene black
    with dissolve
    return
    
