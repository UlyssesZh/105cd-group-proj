define p = Character("Pier Papillion", color="#000000")

define s = Character("Nature spirit", color="#0077aa")

define b = Character("[beatrice_name]", color="#aa8800", image="beatrice")
define beatrice_name = "????"

define m = Character("[millie_name]", color="#007788", image="millie")
define millie_name = "????"

define f = Character("[fry_name]", color="#8800aa", image="fry")
define fry_name = "????"

define pp = Character("[p.name]'s another self", color="#000000", image="pier")

default chosen_beatrice = False
default chosen_millie = False
default chosen_fry = False

label start:
    jump intro

label intro:
    scene bg opening
    p "AHHHHHHHHHH! (Trip on top stair falling to the ground)"
    p "Really? In front of everyone? I'll be the laughing stock of the school! Everyone is going to laugh at me!"
    "Everyone" "..."
    p "Oh, I see, guess college really is irreverent. Maybe I would almost prefer to be laughed at...
        Not like my ability is invisibility or anything..."
    p "Although that might be preferable to the one I do have."
    p "After all, being able to communicate with nature spirits and all that is kind of boring
        when the nature spirits in question can't really do much compared to humans in the first place,
        at least without cost."
    p "It seems to be a rule of this world that the magical creatures that do exist don't really outshine humans."
    p "Although, i guess versatility is a plus, but who cares if they heal your scrape from tripping on the stairs
        {b}if they were the ones who grew the roots that tripped you{/b}."
    show beatrice normal
    b "Um, who are you talking to?"
    p "I have no idea what your talking about. (Walk away)"
    b "(Run after [p.name]) Wait! Can you talk to the spirits!!!! That's sooooo cool!!!
        What are they like, what do they say!"
    b "I mean we see them in drawings, but to see them is so interesting! And it's really rare too! Wait up!!"
    p "Oh, um, didn't realize anyone cared that much about them.
        I mean, they can definitely be useful sometimes, but usually with anything other than little things,
        I need to work out deals with them..."
    p "I mean, they are pretty kind, so they are cool to talk to, but it's inconvenient to have
        to give them a handmade water bottle holder to have them grow a plant instantly...
        {i}Especially if there are people who have that power anyway...{/i}"
    p "And then there's the pranks... sigh... Anyway, my name is [p.name].
        I haven't met very many people at this school yet, so it's nice to meet you!"
    $ beatrice_name = "Beatrice Morley"
    b "Wow! That's incredibly fascinating, like you have a magic system all to yourself!
        I'm [beatrice_name], I'm fairly new too!
        Believe it or not you're the first person I've really talked to as well!"
    b "I guess it's only fair that I tell you about my power as well!! Seeing as I basically overheard yours!"
    b "Mine is Memory Viewing.
        With someone's okay, and my agreement as well, I can look at any memory someone has, just like a movie!
        It's not super helpful, but it's really cool!"
    b "Anyway! Got to go to class!!! See you around, new friend!!!"
    p "{i}Friend? Guess that works...{/i} See ya!!!"
    p "Wait, I'm late too! Oh no! (Runs way)"

    scene bg lecture outside
    "[p.name] runs through campus, ignoring anyone they see on the way."
    p "Whew, made it one time!!! Just barely though... Huh?"
    p "Why is everyone still outside? Shouldn't everyone be inside already... are we all late?!"
    show fry normal
    f "Well, well, well... I can see from your face you seem confused.
        I shall illuminate your confusion, bystanding stranger!"
    $ fry_name = "Fry Anthony"
    f "You see, I am [fry_name], and I am in both this upcoming class, and the next one.
        They both have the same professor you see! And that professor is none other than Mattias Sibyll,
        the only person from this school who's even a little famous!"
    f "It's only natural that people would be slow to leave the lecture hall, and wish to speak with him after...
        In fact, I would be too, if I were not taking this class as well!"
    p "Oh, um, hello? I'm [p.name], not a random bystander...
        So there's someone that is cool in this class. Interesting, you seem like you must know a lot!"
    p "Maybe you can help me out sometime, the science of magic has always been so confusing to me,
        but it's pretty much required for my major of healing, so it would be great if you could help me!"
    f "Well, um, sure, I guess I can do that, as long as you actively try outside of that as well.
        ({i}I wasn't expecting for my first potential friend to be today, but I'll take it!{/i})"
    p "Huh? You sound different... I was honestly expecting you to always talk like you are a mad scientist...
        But yeah! Excited to study with you!"
    f "Oh, that, um, I put that on to prevent myself from being around anyone who might be hostile to my interests.
        You see, my power is relatively lame... I can sense what's wrong with technology when it's broken..."
    f "Part of the reason why I like Professor Sibyll so much is, similar to me, his power doesn't have much use...
        Only being able to summon a magic sword when times are this quiet must be incredibly difficult!"
    f "But he didn't let that slow him down! And now he's known for being an incredible genius!!!!"
    p "Oh wow, that is inspiring! Now I'm excited for this lecture.
        I was actually kind of scared it would be boring... like it was in high school... but now it's super exciting!!!"
    f "I'm glad! Wait, someone just got closer.
        I mean, yes, of course you should be overwhelmed by the splendor of our fine professor!"
    f "Now, let us enter, new friend character,
        and see if we can glean a fragment of the boundless wisdom of the professor!!!"
    p "{i}But my name is [p.name]...{/i}"

    scene bg lecture
    p "TODO"
    show millie normal
    m "TODO"
    $ millie_name = "Millie Hayden"
    m "My name is [millie_name]."

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
    if not (chosen_beatrice and chosen_millie and chosen_fry):
        menu:
            p "Who should I visit?"
            "[beatrice_name]":
                jump choice_beatrice
            "[millie_name]":
                jump choice_millie
            "[fry_name]":
                jump choice_fry
    jump after_all

label choice_beatrice:
    $ chosen_beatrice = True
    p "I go to visit [beatrice_name]"

    scene bg university
    show beatrice normal
    p "Bro listen to me"
    b "It's not me lol"
    p "Damn no way"

    scene bg room
    show millie normal
    show device normal at right
    p "Bro stop"
    m "No I am activating it"
    show device activate at right
    "Mission failed"
    show butterfly normal at left
    p "Yo butterfly again"

    jump day_two

label choice_millie:
    $ chosen_millie = True
    p "I go to visit [millie_name]"

    scene bg university
    show millie normal
    p "You see"
    m "What? I did nothing"
    p "Damn no way"

    scene bg room
    show fry normal
    show device normal at right
    p "Wait a sec"
    f "No I go burr"
    show device activate at right
    "Mission failed"
    show butterfly normal at left
    p "Yo butterfly again"

    jump day_two

label choice_fry:
    $ chosen_fry = True
    p "I go to visit [fry_name]"

    scene bg university
    show fry normal
    p "Hear me out"
    f "Nah you trippin'"
    p "Damn no way"

    scene bg room
    show beatrice normal
    show device normal at right
    p "Don't"
    b "I do"
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
    show pier normal
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
