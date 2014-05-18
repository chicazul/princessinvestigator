# You can place the script of your game in this file.

init python:
    stats = ['name','kingdom','age','shoesize','birthstone','colours','cupcake','guilty','annoyance']
    p1 = ['Adelaide', 'Mauritania', '23', '7','topaz','Green, Coral, and Silver','Red Velvet',0,0]
    p2 = ['Terabith', 'Rembel', '17','5','Bone','Grey and Royal Blue', 'Angel Food',0,0]
    
    princesses = []
    princess = {}
    princesses.append(dict(zip(stats,p1)))
    princesses.append(dict(zip(stats,p2)))
    

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define a = Character('Princess Adelaide')
define processedcount = 0

label start:
    jump dossier
    return
    
label dossier:
    while processedcount < len(princesses):
        $ princess = princesses[processedcount]
        call screen dossier(princess)
        if (_return == "interview") | (_return == "xray")|(_return == "accuse"):
            call expression _return pass (princess=princess)
        elif _return == 1:
            $ processedcount += 1
    

label story:
    centered "Coronation Day dawns bright and clear. Everything is in order for the crowning of Princess Kathleen of Romania."
    
    centered "But wait! A messenger has just arrived, bearing news that one of the visiting princesses is an assassin in disguise! Princess Kathleen's life is in danger!"

    centered "It's up to you, the captain of the guard, to identify the nefarious noble before the ceremony."

    centered "Careful not to offend an innocent princess though--if you set off a diplomatic incident it may be your head on the chopping block."
    return
    
label interview(princess):
    a "Why are you asking me this?"
    jump dossier
    
label xray(princess):
    call screen xray
    if _return == "accuse":
        call expression "accuse" pass (princess=princess,location="xray")
    else:
        jump dossier

label accuse(princess, location="dossier"):
    menu:
        "You are planning to kill Princess Kathleen!":
            if princess['guilty']:
                jump success
            else:
                princess['annoyance'] += 50
    jump expression location
    
label success:

label fail: