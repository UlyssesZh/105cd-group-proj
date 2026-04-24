define p = Character("Protagnist", color="#000000")
define s = Character("Nature spirit", color="#0077aa")
define a = Character("Character A", color="#aa8800")
define b = Character("Character B", color="#007788")
define c = Character("Character C", color="#8800aa")
define pp = Character("Protagnist's another self", color="#000000")

default chosen_a = False
default chosen_b = False
default chosen_c = False

label start:
    jump intro

label intro:
    scene bg intro
    "In a world where magic exists, and people each have their own form of it"
    "Each person has their ability, and then a semi adjacent ability that is usually stronger, related, but different"
    "The engineer: builds device/ how device works"
    "The idealist: hope for better world"
    "The researcher: timeline?"
    "However, society is like modern day society"
    p "I go to a university"
    show spirit normal
    p "I have nature related power, can communicate with nature spirits, use nature related powers"
    jump day_one

label day_one:
    scene bg home
    p "I wake up"
    scene bg university
    p "I go to the university"
    show a normal
    p "I encounter Character A"
    a "Hello there"
    a "There is a conspiracy"

    scene bg university
    show b normal
    p "I encounter Character B"
    b "Hello there"
    b "There is a device"

    scene bg university
    show c normal
    p "I encounter Character C"
    c "Hello there"
    c "The device does something"

    scene bg room
    show device normal
    p "Just WTF is this device"
    show device activate
    "The device goes off"
    hide device
    "It rewrites reality into one that only retains technology like medical and other essential things"
    "but the rest is undone, and what remains is replaced with magic equivalents"
    show spirit normal
    s "It's wrong"
    s "This will lead to the end of everything, even if it at first seems better"
    p "Man I need to fix this"
    show butterfly normal at right
    "A glowing butterfly lands on you"

    jump day_two

label day_two:
    scene bg home
    p "I am brought back to the start of the same day"
    if not (chosen_a and chosen_b and chosen_c):
        menu:
            p "Who should I visit?"
            "Character A":
                jump choice_a
            "Character B":
                jump choice_b
            "Character C":
                jump choice_c
    jump after_all

label choice_a:
    $ chosen_a = True
    p "I go to visit Character A"

    scene bg university
    show a normal
    p "Bro listen to me"
    a "It's not me lol"
    p "Damn no way"

    scene bg room
    show b normal
    show device normal at right
    p "Bro stop"
    b "No I am activating it"
    show device activate at right
    "Mission failed"
    show butterfly normal at left
    p "Yo butterfly again"

    jump day_two

label choice_b:
    $ chosen_b = True
    p "I go to visit Character B"

    scene bg university
    show b normal
    p "You see"
    b "What? I did nothing"
    p "Damn no way"

    scene bg room
    show c normal
    show device normal at right
    p "Wait a sec"
    c "No I go burr"
    show device activate at right
    "Mission failed"
    show butterfly normal at left
    p "Yo butterfly again"

    jump day_two

label choice_c:
    $ chosen_c = True
    p "I go to visit Character C"

    scene bg university
    show c normal
    p "Hear me out"
    c "Nah you trippin'"
    p "Damn no way"

    scene bg room
    show a normal
    show device normal at right
    p "Don't"
    a "I do"
    show device activate at right
    "Mission failed"
    show butterfly normal at left
    p "Yo butterfly again"

    jump day_two

label after_all:
    p "Man I am out of ideas"
    show butterfly normal
    p "Yo you here butterfly"

    scene bg room
    show protagnist normal
    p "You look the same as me"
    pp "Yeah I am your other self"
    p "Bro that's amazing af"
    pp "I am the one sending butterflies"
    pp "I come from a timeline that branched off before today"
    pp "I fired the machine once in that timeline"
    pp "However, instead of the function you know of, this machine was instead designed to give powers"
    pp "The method was the same, but targeted humans instead of the earth."
    pp "the additional power the other you awakened was the butterfly effect, being able to mess with time and consequences of actions"
    pp "however this awakening had a side effect of making the powers spread so they had always existed, which led to you being different"
    pp "although due to the control they had, they remained as well."
    pp "They were the one who activated the machine the first time"
    pp "and it was in fact your own power that allowed you to go back in time before the changes to the timeline as a whole became permanent, to their dismay."
    menu:
        pp "Your choice?"
        "Destroy the machine":
            jump destroy_route
        "Fix the machine":
            jump fix_route
        "Reverse the machine":
            jump reverse_route

label destroy_route:
    scene university
    "This is the destroy route"
    "ENDING 1"
    return

label fix_route:
    scene university
    "This is the fix route"
    "ENDING 2"
    return

label reverse_route:
    scene university
    "This is the reverse route"
    "ENDING 3"
    return
