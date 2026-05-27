define p = Character("[riley_name]", color="#000000")
define riley_first = "Riley"
define riley_last = "Papillion"
define riley_name = f"{riley_first} {riley_last}"

define b = Character("[beatrice_name]", color="#007788", image="beatrice")
define beatrice_name = "????"
define beatrice_first = "Beatrice"
define beatrice_last = "Morley"

define m = Character("[millie_name]", color="#aa8800", image="millie")
define millie_name = "????"
define millie_first = "Millie"
define millie_last = "Hayden"

define f = Character("[fry_name]", color="#8800aa", image="fry")
define fry_name = "????"
define fry_first = "Fry"
define fry_last = "Anthony"

define s = Character("[mattias_name]", color="#4e7c5c", image="mattias")
define mattias_first = "Mattias"
define mattias_last = "Sibyll"
define mattias_name = f"{mattias_first} {mattias_last}"

define l = Character("[butterfly_name]", color="#a0aa49", image="butterfly")
define butterfly_name = "Lycaenidae"

default last_chosen = None
default last_triggerer = None
default chosen_beatrice = False
default chosen_millie = False
default chosen_fry = False
default chosen_reverse = False
default chosen_fix = False
default chosen_leave = False

label start:
    jump intro

label intro:
    # start scene intro #######################################################################
    scene bg stairs
    # TODO: image of protag tripping on stairs
    p "AHHHHHHHHHH!"
    # TODO: image of everyone looking irreverent
    p "Really?? In front of everyone?? I'll be the laughingstock of the school!!"
    p "Oh, I guess people in college really are irreverent.
        It's not like my ability is invisibility or anything...
        Maybe I would almost prefer to be laughed at..."
    p "But maybe I'd prefer that invisibility were my ability.
     After all, being able to communicate with nature spirits and all that is kind of
      boring if they can't really outshine humans in the first place..."
    # TODO: image of protag looking up at spirits
    p "Yes, I'm talking to you all."
    p "Although, I guess versatility is a plus, but who cares if the spirits heal the scrape you got from
     tripping on the stairs {b}if they were the ones who grew the roots that tripped you{/b}..."
    show beatrice normal
    b "Um, who are you talking to?"
    # TODO: image of protag starting to walk away
    p "I have no idea what you're talking about."
    b "Wait! Can you talk to the spirits??!! That's sooooo cool!!!"
    b "What are they like?? What do they say?!
        I mean, we see them in drawings, but seeing them in reality is so interesting!
         And it's really rare too!!"
    # TODO: image of protag talking to beatrice
    $ temp = False
    menu:
        "like the spirits":
            p "Oh, um, I'm surprised you care that much about them. I mean, it can definitely
             be useful sometimes, but I usually need to work out deals with them. They're
              pretty kind, and they're cool to talk to!"
        "completely avoidant":
            p "Oh, I don't really like when people talk to me about them. It brings up some
             challenging stuff from my past."
            $ temp = True
        "sick of their shit":
            p "Oh, thanks, but they can be pretty inconvenient. For example, I recently had to
             give them a handmade water bottle holder in exchange for them growing a plant
              instantly. Some people can do that without having to talk to the spirits."
            p "And then there's the pranks... ({i}sigh{/i})"
    p "Anyway, my name is [riley_name]. I haven't met many people at this school yet, so it's
     nice to meet you!"
    $ beatrice_name = f"{beatrice_first} {beatrice_last}"
    if temp:
        b "Oh, my apologies. No need to dig too deep into our pasts – we just met!"
    else:
        b "Wow! That's incredibly fascinating, like you have a magic system all to yourself!
         I'm [beatrice_name], and I'm fairly new too! You're the first person I've really
          talked to..."
    b "I guess it's only fair that I tell you about my power too! Mine is Memory Viewing.
     If someone permits it, I can look at any memory they have. It's just like a movie!"
    b "It's not super helpful, but it's really cool!"
    # TODO: image of beatrice walking away
    b "Anyway, I've got to go to class. See you around, new friend!!"
    p "{i}Friend? Guess that works...{/i} See ya!"
    # TODO: image of protag walking away
    p "Wait, I'm late too! Oh no!"
    # end scene intro #########################################################################
    # start scene outside lecture hall ########################################################
    scene bg lecture outside
    "[riley_name] runs through campus, ignoring anyone they see on the way."
    p "Whew, made it on time. Just barely though..."
    p "Huh? Why is everyone still outside? Shouldn't everyone be inside already? Are we all late?!"
    show fry normal
    f "Well, well, well... I can see from your face that you seem confused.
        I shall illuminate your confusion!"
    $ fry_name = f"{fry_first} {fry_last}"
    f "You see, I am [fry_name], and I am taking every class I can with this professor, [mattias_name]."
    f "He's a visionary! The only person at this school who's even a little famous.
        His class just ended, and people are slowly leaving the lecture hall."
    f "It's only natural that they linger – they all want to speak with him!
        In fact, I would be there too, if I hadn't talked to him much in the past."
    p "Oh, um, hello. I'm [riley_name]."
    menu:
        "TODO: option 1":
            p "I'm glad I met someone who seems like they know what they're doing!
                The science of magic has always been so confusing to me,
                but it's required for my major in healing, so it would be great if you could help me!"
            f "Sure! I guess I can do that, as long as you actively try as well."
        "TODO: option 2":
            p "I was honestly expecting you to keep talking like you were a mad scientist...
                Anyway, I'm glad someone is talking to me."
            f "(Slightly embarrassed) Oh, that, um, I put that on to deter anyone who might be hostile to my interests.
                You see, my power is relatively lame... I can sense what's wrong with technology when it's broken."
    f "Part of the reason why I like Professor [mattias_last] so much is that, similar to me,
        his power doesn't have much use. Nobody even knows what it is!
        But he doesn't let that slow him down, and now he's known for being a genius! He inspires me a lot."
    p "Oh wow, that {i}is{/i} inspiring! I honestly expected this class to be boring, like high school... but now I'm excited!!!"
    f "I'm glad! Professor [mattias_last] is splendid. Let us enter now, my friend,
        and see if we can glean a fragment of his boundless wisdom! (Runs into lecture hall)"
    p "My name is Riley, by the way... (Hurriedly follows [fry_first] into lecture hall)"

    scene bg lecture
    show fry normal at left
    p "(Finally catches up with [fry_first]) What the heck... It won't be the end of the world if you're late, you know..."
    f "Nonsense, my friend! I had to get good seats!"
    hide fry
    show mattias normal
    s "Ahem! Welcome, class. I see we have a good showing today! I hate being this famous!!! Haha..."
    s "But that's not what you're here for. You... you're here to learn about magical technology!"
    s "Contrary to popular belief, technology and magic are more compatible than you might think."
    s "Magic tech has a reputation for being completely inaccessible to all but the most talented in both mind and magic.
        But although talent is important, pure determination is the true driving force."
    s "In fact, even those who lack raw power can use what is generated by others;
        as you may know, those who can generate electricity work with the bureaucrats to keep our lights on!"
    s "Any ability that affects the physical world, or generally creates things, can be used for this purpose."
    p "{i}With my power, I can't really change anything myself... so my power doesn't fall under this category...{/i}"
    s "We have taken the principles of science, particularly those related to electricity,
        and have applied them to all manner of abilities."
    s "By doing this, we found our baseline magical energy unit called Frederick Particles,
        named after the man who discovered them – my father! (Pause)"
    s "Anyway, these particles – and the energy they are a part of – are what is often referred to as \"magic,\"
        although they have less of a relation to \"true magic\" than you would think."
    s "Despite what intuition may imply, these particles are completely understandable through science.
        Very few abilities come close to resembling true magic. Relatively few are even able to interact with true magic at all,
        and they certainly can't attain the scale and impossibility of true magic."
    s "If you're lucky enough to generate positively charged mana particles, then your ability impacts the world."
    s "The reverse, negative particles are also useful, but all modern methods of conversion and technological interaction
        are currently known to utilize the positive particles, and their manifestations and creations in the physical world."
    s "However, abilities fueled with negative powers are more conceptual. Their capabilities do approach true magic,
        but they are still fundamentally rooted in science,
        and cannot affect the physical world beyond affecting the concepts of the physical world."
    p "By drawing and manipulating both of these particles,
        we can achieve feats of such magnitude that they put all currently known abilities to shame."
    p "Considering our gathering and storage methods, we can accomplish great things,
        closer than ever to recreating the miracles of spirits."
    p "And if one were to manipulate all types of these particles, have them work together,
        and then utilize them, they may even be able to produce and control true magic, the power of spirits."
    p "They will have the power to change the world entirely, to create miracles on a whim."
    s "Anyway, this is an introductory course, so don't worry about that yet! For now, we will return to the basics.
        I know all that can sound terrifying, but it will become more digestible with time."
    s "This course ultimately goes into depth on the interactions of magically produced electricity and normal electricity,
        and how we managed to merge the two."

    scene bg lecture outside
    show fry normal
    p "Wow, my brain hurts..."
    f "..."
    menu:
        "TODO: option 1":
            $ temp = True
            p "You ok?"
        "TODO: option 2":
            $ temp = False
            p "You've got to relax a little. I know he's an important person,
                but you're gonna run out of gas if you take everything too seriously."
    f "Oh! Yeah, I was just thinking... He was much more than I expected, but now he seems so much more human?"
    f "I guess... I've always been suspicious of people who seem like that... mortal, fallible.
        He was always above such things to me, but now I'm not so sure."
    f "No, I have to believe he is the legend I hold so close to my heart!"
    f "I find myself with much to ruminate on! I will have to bid you farewell."
    f "But know this, next time you see me, I will be unrecognizable, changed, enlightened further from my studies!"
    f "I pray you'll be able to recognize someone who considers you a friend! (Run away)"
    hide fry
    p "Aaaannndd he's gone..."
    if temp:
        p "Well, I asked him if he was okay, so I did the best I could."
    else:
        p "Well, I guess that makes him happy, best of both worlds, you know,
            both being normal with friends and insufferable to people he couldn't care less about..."
    p "I think it's time for me to go get food..."
    p "Why is today like this? Nothing today has made sense."
    p "I guess I'm glad I've met people though!"

    scene bg cafeteria inside
    p "Finally some food. I'm almost too exhausted to eat."
    p "I wonder where it would be good to sit?"
    show millie normal
    p "I guess here would work! Um, excuse me, is it okay to sit here?"
    m "Fine. Whatever."
    p "Thanks! Hmmmm... first we have a side of potato chips, quite the ordinary ones I suppose..."
    m "Ugh, I'm gonna kill them. I swear I'm going to kill them!"
    p "Then, I guess I'll be eating this sandwich next. Hmm, it appears to be turkey and cheddar...
        I guess ketchup on this is tolerable."
    m "How did I get roped into this again? Some stupid scholarship?
        Do they even know what could happen when you accumulate that much power?"
    m "Nukes are still barely safe!"
    p "Oh, I almost forgot about the fries... they actually look very tasty today!"
    m "What am I even doing? Holding the tools? Who do they think I am?! Some servant?
        They swear that eventually they will need me for something, but still."
    menu:
        "Talk to the girl":
            pass
        "Keep ignoring the girl":
            p "Oh, an oatmeal raisin cookie... spirits, you can have this one for free, okay?"
            m "I mean, this machine is clearly not doing anything to actually improve the situation outside!"
            m "Meaningless innovation as if the actual problems aren't interesting enough!"
            m "I've had {i}enough{/i}!!!"
    p "Sigh... honestly, I was going to ignore you,
        but at this point I feel obligated to ask why you aren't leaving."
    p "You don't sound like it's something you're getting any value out of."
    m "HUH? You think you could understand!"
    p "I can definitely try! Beats doing nothing for the rest of my break...
        I'm [riley_name], by the way."
    $ millie_name = f"{millie_first} {millie_last}"
    m "Oh, introductions. [millie_name]. Okay then, I'll tell you."
    m "It wasn't anything special. In fact, my life was straight-up common...
        for someone whose parents never were sure of their ability to keep me fed, at least."
    m "I survived, but was always aware of the newest technology, never being able to try it."
    m "It makes me wonder why they had advertisements where we were at all.
        There was nobody there who could even consider buying name brands."
    m "Anyway, I figured out I have this rare ability called \"reversal.\" I can reverse most things."
    m "Like making an ice cube hot temporarily,
        or sending the force of someone's punch right back at them – that kind of thing."
    m "Apparently, that's rare and useful, so they gave me a scholarship and I ended up here."
    m "Nobody knows how hard it was for my family and me."
    m "They just assume the world is okay because it doesn't affect them,
        while I have to hold my nose and work for them,
        in hopes of finally helping out the ones who placed their hopes in me."
    m "Do you get it now?"
    p "Honestly, I can empathize, but never truly understand. I do have my own share of problems, though."
    p "To make this session even, something about me is that I can talk to spirits...
        I may have had an easier childhood, but it made me a target throughout my life."
    p "You see, people started to realize what the spirits are capable of."
    p "Not the same... but I hope you believe me when I say that I understand life can be unfair."
    m "Oh, I see. It's been a while since someone's been this receptive to my complaints.
        Honestly, I'm hesitant to make new friends with someone so soon,
        but maybe we could at least talk some more?"
    m "I'm thinking of it like a proto-friendship situation."
    p "That sounds great! Honestly, it's almost a relief that I met someone who doesn't declare friendship instantly!"
    p "I'll look forward to talking with you some more!"
    p "Here is my phone number!"
    m "Oh, here's mine! I've got to get going, but I'll see you soon!"
    p "Talk to you later!"

    scene bg cafeteria inside
    show mattias normal
    p "{i}Oh? Is that Professor [mattias_last]? Maybe I should ask?{/i}"
    s "Sigh... are you going to keep staring or what?"
    p "Oh, um, sorry. I was just remembering your lecture,
        about how there are positive and negative Frederick particles, and I wanted to double-check my understanding."
    p "Specifically, I was wondering which category a spirit speaker would fall into?"
    s "Oh? Spirits, huh... interesting."
    s "Well, usually it's pretty easy to categorize abilities
        since the positive particles only really manifest when one is directly creating something with those particles."
    s "Anything that involves manipulating things that already exist, concepts, or mystical constructs
        tends to be negative-particle based..."
    s "Spirits may be the exception to that... To our knowledge, they don't actually use the particles.
        It's thought that whatever they use is similar, the same fundamental force per se,
        but theirs is a more inexplicable, primal form."
    s "That's what I've been calling true magic."
    s "Can I assume that your abilities involve spirits?"
    s "If so, if you have time, I would very much like for you to stop by my lab sometime!"
    s "I believe it could be helpful for our efforts!"
    menu:
        "TODO option 1":
            p "Oh, um, I guess that could be cool. Thank you for your help, Professor. I'll see you later!"
        "TODO option 2":
            p "I don't want to be used like a lab rat. I need some time to think about it, Professor."
    p "{i}It feels really odd that he's so eager... Are spirits that interesting?{/i}"
    p "{i}Sure, some of them are cool and mysterious, but most of them are annoying and childish,
        always asking for my hair to make trees and flowers grow...{/i} (Walk away)"

    scene bg cafeteria outside
    b "Oh, hi Riley! Didn't think I'd run into you here! What's up?"
    p "Huh, [beatrice_first]?"
    show beatrice normal
    p "Oh, hello!"
    b "How has your day been?"
    b "Do any super cool feats where you shocked everybody about how super cool you were?"
    menu:
        "Go along with the odd comment":
            p "Not quite... I did manage to meet quite a few people, but I haven't really done anything yet."
        "Respond with some uncertainty":
            p "It kind of sounds like you're making fun of me...
                No, unfortunately I have not shown everyone how \"super cool\" I am."
    b "Oh! I should have known, your hair looks the same way it did before,
        and I don't think you had time to make another type of offering either!"
    b "Spirits, if you can hear me, hang in there, I'm sure you'll have your fun soon."
    b "At the very least, I'll have Riley here, have you make me my own olive tree next time they get their haircut!"
    p "Haha, not a bad idea though, maybe then we can go volunteer in a hospital together or something,
        I'm sure they'll be happy to have access to your ability as well."
    p "Figuring out what actually happened to someone can be hard,
        and some feel less embarrassed if mind magic is used instead."
    b "Oh, you volunteer, that's so cool! Yeah, for sure, I'll look forward to it!"
    show millie normal at right
    m "Hey, Riley, who's this?"
    p "Oh, hi [millie_first], this is [beatrice_first]."
    m "Well then, hi [beatrice_first]! I assume you're pretty optimistic, right?"
    m "It must be tough in today's world... As they said, I'm [millie_first]."
    m "You probably shouldn't get too close with me... People never stuck around me for long at my last school
        since I love to challenge everyone's worldviews."
    b "Oh, well if my worldview wouldn't survive getting to know someone who seems as interesting as you,
        then it must be a pretty limited one anyway!"
    b "And what narrow-minded individuals there must've been at that school! I wonder where that was?"
    m "It was in the Wild Garden, named for its general ambience and nature of the students..."
    b "I see... I've actually heard that WG can be a cruel place without great education."
    b "So much darkness is targeted towards students that it now grows, with none caring enough to help."
    m "Well, you're right about the lack of care, but I think I'm proof enough that we aren't all bad."
    b "Of course, you indeed shine very brightly, more so than those you thought were like me, that's for sure!"
    b "We both know Riley too, so hopefully we can talk more!"
    m "Sure, whatever. Probably won't make a difference, though, but it couldn't hurt. Would be nice to see home too."
    show fry normal at left
    f "Aha! There you are, my faithful assistant!"
    f "I have to say I'm impressed... expanding your social network so well!"
    f "However, I, [fry_first], must ensure that these unknown agents are not devious Ne'er-do-wells, hoping to steal our confidential secrets!"
    p "Once again, my name is Riley, and since when was I your assistant?"
    m "Um, Riley, do you know this guy?"
    p "Oh, um, yes. This is [fry_first]... [fry_first], this is [millie_first] and [beatrice_first]... You can drop the act now."
    p "I'm sorry, he isn't always like this."
    p "{i}I have no idea what's going to happen today anymore.{/i}"
    p "{i}All of these... friends... who know each other through me. I could never have imagined this.{/i}"
    f "Ha, foolish assistant, what else would you be?"
    f "Anyway, in my fourth class of the day with Professor [mattias_last], he mentioned he met a very interesting Spirit Speaker!"
    f "May that be you, talented assistant?"
    p "Um, yeah, he seemed interested in that... No idea why, though."
    p "I can't believe he would mention it during class."
    m "[mattias_last], you mean the Professor?"
    m "I hate that man... maybe if he did more but gave vague directions,
        I would actually have something to do in his project I was drafted into..."
    f "GASP! You dare slander the visionary of our time?"
    m "Ha, any day of the week! If you're going to threaten my scholarship, you should at least have me do something!"
    m "If he would just let me, I could find a different position in an art lab or something."
    m "But no, for some reason, he can't seem to stand the idea of not having access to a resource he's claimed,
        regardless of whether that resource is a human!"
    f "If anything, you should be honored to be working with him. And besides, he isn't very powerful by himself,
        so you can barely blame him for having to utilize others!"
    f "If he is condemned for that, then I don't have a chance of achieving anything useful in my career."
    f "Unlike magic, technology is impartial, and anyone can use it!
        But in our present moment, people like him are starting to understand that we need technology to advance."
    f "That technology needs magic users, so excuse me if you feel like you're being treated unfairly!
        To me, it's unfair that your power is strong enough that you're useful to him! I would love to join his lab!"
    m "Technology is impartial blah blah blah... it may be equalizing for those who don't have useful abilities,
        but that doesn't mean it's fair."
    m "Do you know what kinds of technology the lower classes can use?"
    m "They're lucky if they can use something that's five years old!
        I would still be working long hours for little pay if I had a different power!"
    b "Um, maybe you could lay off each other a little bit...
        It seems to me your opinions are based on your personal experience."
    b "Which is completely understandable, but indicates that you may not reach a middle ground very soon."
    m "Yeah, sure whatever..."
    f "Hold up, you still haven't apologized for slandering Professor [mattias_last]. This injustice must be remedied!"
    b "Isn't it okay for people to have their opinions about other people... everyone's perspective is different, right?"
    f "I wouldn't expect a normie to understand!"
    b "Oh, um. I've just remembered I have something to do... see you later [riley_first] and [millie_first]..."
    hide beatrice
    p "Sigh... Hey [fry_first], I know you put this act on to protect yourself, but these are cool people.
        You don't have to drive them away."
    p "You've been antagonizing them to no end... Please, let it go for now."
    f "Oh, um, I see. I guess I'm sorry, [millie_first]."
    f "I still wish you could see how cool Professor [mattias_last] is, but I definitely was a bit out of line there."
    m "A bit? You literally caused [beatrice_first] to run away! Although, I guess I was a little combative as well...
        That doesn't mean I like you, but I won't disregard you entirely yet..."
    f "Oh, I see, thank you."
    m "Now, I think [fry_first] mentioned that you were approached by the annoying professor."
    m "I can show you to that lab... I think I'll be able to convince you not to even consider working with that man,
        especially once you see how it is there."
    p "Oh, okay, so interesting. Um, [fry_first], I'll talk to you later."
    f "Sounds good, I guess..."
    hide millie
    f "{i}Probably will be okay if I follow them, right? I want to see the lab!{/i}"

    scene bg lab entrance
    show millie normal
    m "Well, here we are. Welcome to the edge of despair. Sigh, I was really hoping not to be here today."
    p "Wow, this is like a sci-fi movie!"
    m "Ha, more like a supervillain's lab. Come here, I'll show you to the main event."
    m "Oh, but before that, I do want to clarify...
        While I don't really like them, the rest of the staff haven't really done anything wrong."
    m "It's just the white-coated narcissist."
    menu:
        "TODO option 1":
            p "Got it, and to be honest, I didn't really care for him either."
            p "When I was talking to him, it seemed like he just wanted to see whether I would be useful or not."
            m "Right? I'm glad you agree."
        "TODO option 2":
            p "If the rest of the staff are lovely, I wonder how bad he really is...
                Isn't he working on technology that's going to improve humanity forever?"
            m "Yes, I guess you could look at it that way..."
    m "Anyway, let's go see the machine."
    m "I assure you, if there is one thing you have to see here, it's that beautiful monstrosity."

    scene bg lab room
    show millie normal
    p "Whoa... you were right, I've never seen anything like this..."
    p "What does it do?"
    m "Well, that's the thing, we don't really know... he tells us some functions,
        and the team makes them work, but honestly, the larger role eludes all of us."
    m "We think that he might just be insane, and apparently, a large amount of it is built using his power."
    p "His power? Now that I think about it, I don't know what it is..."
    m "Believe it or not, it's swords. He can literally create magic swords."
    p "Wow, that is fascinating. So presumably, his swords have practical use outside of warfare..."
    m "I know, right? A surprising amount of the machine is made using the swords as parts."
    m "Which meanssss that currently no scientist knows what science is happening, if it's science at all.
        So I guess [fry_first] was right about one thing..."
    m "He does seem to be a visionary, even if those visions seem more like a manifestation of whatever anime he's watched
        rather than a bright future."
    show fry normal at right
    f "OH WOW WOW WOW, this place is so cool!"
    m "Oh no."
    f "I'm sorry I can't help myself... Is that what he's been working on?
        That's so cool, maybe it's a revolutionary form of computer that will advance us 50 years!"
    m "Why. Are. You. Here?"
    f "I just had to see! Is that a problem?"
    m "..."
    m "YES [fry_first], of course it's a major problem.
        The only reason I let Riley in was that they were recruited by the professor!"
    f "Oh, um, I didn't realize it would be a big deal. What now?"
    m "Sigh... Riley, you can leave. I'll figure something out."
    p "Oh, okay. Bye, I guess."

    scene bg lab outside
    p "Sigh."
    p "Finally, time to go home. Today has been a ride."
    show beatrice normal
    p "Wait, is that [beatrice_first]?"
    p "Hey, [beatrice_first], I thought you went home?"
    b "Oh, yeah, I did say that... I forgot something, and had to come back."
    p "I see, and by the way, I'm sorry about how [fry_first] acted earlier. That can't have been fun for you."
    b "Thank you, but I doubt it was fun for you either..."
    b "Besides, I'm aware that everyone has their moments like that!
        Honestly, I'm impressed that you're not still arguing..."
    b "Honestly, the reason I left wasn't that I was hurt,
        but because I could feel myself getting heated as well, and I don't have a reason to argue!"
    b "I'm glad you were there. Sometimes people need a guiding light to get them out of their anger."
    p "I didn't feel like I really did much, but thanks for those nice words regardless.
        I do need to head home, so I'll see you soon!"
    b "Sounds good. I'm still heading this way. Talk to you later!"

    scene bg stairs
    p "Almost out, I hope I can keep getting closer with everyone tomorrow. It seems like I'm on my way to a college friend group."
    p "I also wonder what will be for lunch tomorrow."
    "BOOM!"
    # TODO: There is a flash
    scene bg ruins
    p "{i}Ow? What the heck is that... Oh my!{/i}"
    # TODO: drawn art of riley looking at the ruined world
    p "{i}Why? How can it all be gone? Is this real??{/i}"
    p "{i}Ah! My head! It feels like it's splitting open... with power.{/i}"
    p "Everything... Everything is destroyed. How can humanity survive this?"
    show butterfly normal
    p "A butterfly? A Spirit?"
    p "Why? Why are you the only one I can hear?"
    p "..."
    p "Wha-What are you doing?"
    # TODO: drawing where butterfly is on a very scared riley's head
    # TODO: butterfly effect/sound plays

    jump branch_point

label branch_point:
    # TODO: Black screen with Earlier that day in white written
    scene bg cafeteria outside
    show fry normal at left
    show millie normal at right
    show beatrice normal
    f "However, I, [fry_first], must ensure that these unknown agents are not devious Ne'er-do-wells,
        hoping to steal our confidential secrets!"

    if chosen_reverse and chosen_leave and chosen_fix:
        jump final_reset

    $ route_count = int(chosen_beatrice) + int(chosen_millie) + int(chosen_fry)
    if route_count == 0:
        p "Huh? Why am I here again? The world is... still OK!"
        p "If I'm here, maybe I can actually prevent it from happening."
        p "But I don't think I have much time. I've got to hurry. Maybe that machine caused this to happen?"
    else:
        p "OK, I'm back."
    if route_count == 1:
        p "Was it really [last_triggerer]? Was it them the first time too?
            Anyway, regardless, I think I can do something to prevent the destruction,
            but maybe I should get more info first."
    elif route_count == 2:
        p "It was [last_triggerer] this time?"
        p "How is this possible... Should I try to stop the machine from destroying everything now,
            but I feel like there is still more I can learn."
    if route_count == 3:
        p "I think I've learned all I can, I wonder who set the machine off the first time...
            Anyway, I should focus on finding a way to stop this thing."
    else:
        p "I have to find a way that helps everyone, I can't accept the reality where something is still very wrong."

    f "Ha, an elementary mistake!"
    f "While the strategy to deal with those who might insult us is to act dramatically and all that, it does have to be based in reality."
    p "Oh, right, um, everyone, this is [fry_first]."
    f "Try not to antagonize them, these are good people."
    f "Oh... Is that so? Guess I can tone it down then..."
    m "I recognize you. You're that guy who's been following [mattias_first] around like a shadow, right?"
    m "I can't understand what you can see in the guy."
    p "Haha! A difference in opinion, surely there's no need to fight over this!"
    if route_count > 0:
        menu:
            p "{i}Actually, now might be a good time to try to prevent the disaster from happening again,
                and I think I need to get someone to help me.{/i}"
            "Convince [millie_first] to help" if chosen_millie:
                jump initial_reverse
            "Convince [beatrice_first] to help" if chosen_beatrice:
                jump initial_leave
            "Convince [fry_first] to help" if chosen_fry:
                jump initial_fix
            "Actually, there is more I want to investigate first":
                pass
    p "Actually, I'm quite interested in this lab. There's a cool machine in there, right?"
    m "Yeah, I guess so, if you could call anything that man contributes \"cool\"..."
    p "I wonder, I think I might try and take a look..."
    p "He mentioned me helping him, and I'd prefer to go look around before I make any decision."
    menu:
        p "{i}The person I should take with me to look around at the lab is...{/i}"
        "[millie_first]":
            jump millie_day
        "[beatrice_first]":
            jump beatrice_day
        "[fry_first]":
            jump fry_day

label millie_day:
    $ last_chosen = millie_first
    $ chosen_millie = True
    # TODO: black screen with \"INTENT\" Written in white appears
    p "[millie_first], you'd be able to take me, right?"
    m "I could take you... but I would caution you about doing anything related to that man."
    p "No, I think I need to do this. I need to get all the info I can, right?"
    p "[fry_first] and [beatrice_first], I'm sorry, but [millie_first] and I have got to go!"
    f "Oh, um, see ya later... Where?"
    p "The lab! Right [millie_first]?"
    m "Don't see why you're in such a rush! Surely it's not that urgent?"
    p "It {i}is{/i}! I need to figure it out, find out why,
        [mattias_first] must be hiding something about that machine!"
    m "Oh, OK... if you're looking for dirt, maybe we can look in his office - the professor's, I mean."
    p "That sounds like a great place to start!"

    scene bg office
    show millie normal
    m "So, what exactly are we looking for?"
    p "Anything, something that indicates why this machine actually exists..."
    m "Oh, well, none of us have any idea... I'm not sure information like that will be just laying around in his office."
    m "But I am interested, and it may make all the stress he puts me through worth it."
    p "Yeah, if it's something worthwhile, I might be tempted to work here as well,
        assuming that professor isn't too weird to me."
    m "You know, this place isn't nearly as bad with someone here for moral support.
        If I didn't want to keep you far away, then maybe it would be cool to work with you here."
    m "I've been so angry and alone recently, maybe things will be better with you and [beatrice_first]."
    p "I hope so too."
    p "He does seem like a lot, but I will see what he says.
        Having him as an ally would probably make it better for both of us."
    m "That's very kind of you. I guess we'll see how things go. It sounds crazy,
        but maybe if we hold you joining over his head, he will listen to reason and actually work with us some more."
    p "Haha, now we're talking! It would be nice to have some experience..."
    m "Well, that's more or less the lab. I am looking forward to seeing that man's face when
        I make his new resource contingent on being nice to me, the problem child!"
    p "Yeah, it seems like that would be cathartic for you! Do you want to talk about the specific work you do?
        So I can get a better idea before I consider things further."
    m "Oh, yeah, that would probably be f—"
    show mattias normal at right
    s "Ah, what do we have here? How convenient that you chose to come now!"
    m "Oh. It's you. Hello Professor."
    s "Sigh. Good day to you too, but unfortunately, you will not be the center of attention today [millie_first]."
    s "But really, Riley, I'm very glad you showed up. With your help, I'm sure my machine will be done in no time..."
    s "And no, you won't be leaving until then. We are just too close to greatness, and you are the key."
    menu:
        "Deny his authority":
            p "Um, I really would rather leave."
        "Play it cool while you try and slip out":
            p "Hahaha, I didn't know you were funny, Professor. But unfortunately, I should probably be goingggg."
    s "Well, you really don't get a choice. I am sorry, but I will be able to ensure you are treated well."
    p "That I'm treated well? What is going on? I have my phone, we can call someone to come get us."
    s "They simply will not be fast enough... You'll be grateful for me regardless. Besides, there won't be police anymore anyway!"
    p "What could you possibly mean by that?"
    s "It's simple. I'll be deleting all technology and reformatting the world to a different operating system, so to speak."
    s "One of castles instead of skyscrapers, where everyone's powers will be supercharged!"
    s "It will be just like an isekai!"
    m "There is no way... NO WAY that all this work, this oppressive working environment, the constant staff changes due to burnout,
        is to fulfill your dream of being a freaking anime power fantasy protagonist!"
    s "Well, as king, I'll be able to reward all of you. And besides, money will no longer be the main advantage people can have anymore!
        Isn't that the world you want?"
    m "Well, in a way. Even if that isn't the worst thing that could happen in theory,
        I want to improve this world! You can't just use a machine to make everything perfect. This is insanely dystopian."
    s "Well, if you think that you can just overthrow me! You'll probably be strong enough for it!
        Surely you don't mean that you can't see the upsides?"
    s "I know that I'm tired of technology at the very least!"
    show fry normal at left
    f "Professor [mattias_last]? What... What are you talking about?"
    s "Oh, it's you. Aren't you excited! Even your lame power will be boosted!"
    f "But technology, isn't that what equalizes us who don't have grand powers... Why..."
    s "I have my reasons, or are you doubting me? The student who adores me most also doubts my greatest idea.
        Just one click of that button and the systemic oppression will be flipped on its head, and you want to stop me?"
    f "No—I mean, I would never... and I'll prove it!"
    s "Wait—no it's not ready yet!"
    "[fry_first] presses the button."
    $ last_triggerer = fry_first
    p "That can't be good. [millie_first], we have to get out of here!"
    m "Let's hurry!"

    scene bg stairs
    show millie normal
    scene bg ruins
    show millie normal
    m "What... just happened?"
    p "It seems the machine wasn't functioning properly, and did... this."
    m "Oh my! Look at what they've done! Is this real? Is everything just... gone?
        Those idiots, they did it to us... all with their dumb technology!
        Did either of them think to give us a choice in the matter?!"
    m "Of course not, they never do."
    m "It angers me so much, the way that technology has become the domain of the rich and powerful,
        that only those who are lucky enough to afford it can utilize it,
        especially when the technology can help so many people."
    m "Yet it remained at a premium, exploited for profit, just like the less fortunate of us were."
    m "Everything has been reduced to dust now, it seems the machine erased instead of
        reformatting like the professor was planning..."
    m "I could have reversed it too, but I was scared, and part of me hoped for that world,
        where anyone can be powerful if they are lucky at birth."
    m "Maybe if I stopped relying on this power,
        I could have made more of a difference... but now it's too late."
    p "No, maybe this time, but next time, I will do better, I have to—"
    m "Next time?"
    show butterfly normal at left

    jump branch_point

label beatrice_day:
    $ last_chosen = beatrice_first
    $ chosen_beatrice = True
    p "[beatrice_first], could you come with me?
        I would like to talk to someone who is unrelated and unbiased."
    b "Oh, um, are you sure? I'm not sure that's a good idea."
    # TODO: A blank screen shows up, with nothing but the word \"Reality\" on it
    hide fry
    hide millie
    p "Beatrice, I alluded to this earlier, but I need your help with something."
    b "I see, I assume that will explain why you left them fighting..."
    b "How can I help?"
    p "Trust me, it hurts to see them go at each other for me too,
        but I need you to use your powers on me."
    b "Huh? Why could you possibly... OK, if you are so sure."
    b "Do you agree to let me in?"
    p "Yes."
    b "OK then, let's do it."

    scene bg ruins
    scene bg outside
    show beatrice normal
    b "What? How-How could you have these memories?"
    p "I don't know, there was a butterfly, I don't know what exactly happened,
        but it seemed like it originated from Professor [mattias_last]'s lab."
    b "I see, you were right, I knew you would be,
        but I'm glad you are in fact the type of person I thought you were."
    b "As painful as it must have been, leaving Fry and Millie arguing was probably the best move..."
    b "Come on then, let's go investigate this, I find it hard to believe that the professor
        would be so in the dark to want to destroy this beautiful planet."
    p "Right! It has to be a mistake, we just need to figure out why."

    scene bg office
    show beatrice normal
    b "Hmm, if I were a top-secret file that would help save the world, where would I be?"
    b "It seems like there's no information anywhere!"
    b "But that can't possibly be true, right?"
    p "Right, we're going to find this info!"
    b "Right!"
    b "Hey, there seems to be a hidden department on this desk..."
    p "There is! Seems like we managed to find something!"
    b "That's right, now let's see here, oh, there's something that is relevant to you..."
    b "\"The machine is a method for generating extreme amounts of true magic,
        the kind that spirits use to disobey the laws of physics.\""
    b "\"If I could gather a large amount of this energy,
        for example by utilizing my ability to generate and focus the particles,
        I could change this world without the need for interacting with notoriously finicky spirits.\""
    b "\"However, if I could recruit one, I wonder if they could help,
        they may even accelerate the accumulation process due to their presence.\""
    b "..."
    b "Oh no."
    p "What, what's wrong? It seems we've figured out how the machine functions."
    b "[riley_first], what if he forgot to add a limiter for the generation of true magic...
        What if the machine was activated before it was properly designed to channel the energy in a safe way..."
    b "What if this happened when the machine had way more true magic to utilize than designed,
        or the wild true magic was able to generate more true magic while neither were controlled?"
    b "True magic would have the potential to drastically affect the world
        even without the specific directions the machine would provide."
    p "That would not be good... Maybe that is the reason everything went so wrong,
        but why do you sound so somber?"
    b "Because the spirits are one way he describes how it could be supercharged,
        they could act as a catalyst to make the true magic rapidly generate,
        both in the cultivation phase and the guided release phase..."
    b "And you always have the spirits attracted to you, because you can see them,
        so they are interested in you."
    p "Oh."
    p "Oh no..."
    p "You think, I'm the reason that everything went so horribly wrong?"
    p "Because they activated the unfinished machine, when I had attracted more true magic to it..."
    b "It's the only thing that makes sense."
    p "Oh I, I mean, me? All of it, because of me... (Sob)"
    b "Hey, [riley_first], [riley_first], it's OK, you didn't know."
    p "But-but you've seen what I have, all that was because of me."
    p "How am I supposed to deal with that?"
    b "It may sound simple but you can never go back to not knowing anymore."
    b "And besides, what's most important is that you know now."
    b "I was in your head, I know, you didn't mean to, and you didn't know."
    b "And now, we can fix things, we can figure it out."
    b "And if we can't then next time, you now know what caused it, so if you do return again,
        then you know that at the very least that you can stay away."
    b "Assuming you don't come, the machine will just be normal broken, not a bomb."
    p "Oh, OK, I'm not sure how I feel. I probably won't be OK for a while, but you're right, we can figure this out,
        we can make sure this world of ours does continue."
    b "That's the spirit! I'm so glad you won't let this eat away at you!"
    b "Now, we just have to figure out how to disable the machine,
        it's probably past the point it will ever be safe already."
    p "You're right! Let's figure this out!"
    m "YOU HAVE GOT TO BE FREAKING KIDDING ME!"
    p "But first we should probably check to see what that is about."

    scene bg lab room
    show millie normal at right
    show fry normal at left
    show beatrice normal
    p "[millie_first]? What's going on? Why is [fry_first] here?"
    m "What's going on? I'll tell you what's going on!"
    m "This idiot just cost me my job!"
    p "[fry_first], what does she mean by that?"
    f "Oh, um, the scientists were really really impressed by the fact that
        I was able to map out a path for completing this machine, and so offered me a spot!"
    m "What he isn't telling you is that it's my spot,
        as they were already at the limit of student assistants."
    b "I don't understand, why is he even here, and don't you hate this job [millie_first]?"
    m "He begged me after he realized I worked here,
        but he just had to find a way to speak to Professor [mattias_last],"
    m "who unsurprisingly was more than happy to offer him {i}my{/i} spot after finding out
        he could figure out how to fix that dumb machine he's been having us build!"
    m "{i}Also{/i}, since I didn't have time to look for a job beforehand,
        if I don't find somewhere else to help out,
        then I effectively won't be able to go to this school anymore."
    f "You worry for nothing,
        working for Professor [mattias_last] will surely be a great benefit to your future work pursuits."
    m "He refused to write me a recommendation. I already asked, and he said NO!"
    m "He said that he's \"Too Busy.\" As if he's doing ANYTHING.
        Without his recommendation I have very little chance of finding something on time."
    b "[millie_first], it's OK! We'll figure something out, right [riley_first]?"
    p "Yes, of course we can!"
    m "No... I know what I need to do. If I make myself a part of this lab inextricably,
        if I had something to show for all those hours I put in, then they'll have to acknowledge me."
    m "Even the unfinished machine should still do something if we activate it,
        and I'll be recorded as the one who did it!"
    b "No! You don't understand, we'll figure something out. We promise.
        But you can't activate that machine!"
    # TODO: Sound/light effect to indicate it's been turned on
    "[millie_first] turns on the machine."
    $ last_triggerer = millie_first
    b "Oh no! I was too late. [riley_first], let's go."
    p "Oh. OK then... Why is this happening?"
    b "You can overthink later, for now we've got to get out of here!"

    scene bg ruins
    show beatrice normal
    b "It really happened."
    p "Again... It happened again! And it's all my fault! I'm responsible for the death of so many! How can I possibly cope with that!
        I'm evil... I must be evil, if I'm the reason this planet was destroyed."
    b "No, [riley_first], it's not your fault, you didn't do anything but exist,
        and you deserve to exist, [riley_first]..."
    b "If anyone, it was [millie_first]'s fault, for being too rash at hitting that darn button."
    p "No, she had her reasons... And she didn't know; I did. Besides, [millie_first] is good, I can tell,
        besides, she would have been right if I wasn't there!"
    b "No, no matter what, what [millie_first] did was selfish,
        an easy fix to the unknown she was facing... we would have been more than willing to help, right!"
    b "She's the one who made the choice to ignore us,
        to fall into the darkness she was facing to avoid having to rely on us for help."
    p "But, she's good, she didn't mean to—"
    b "I have a question for you. Are you one of those people who thinks humanity is good?
        I was spared from that delusion from birth, I've seen the minds of too many monsters."
    b "I'm not saying humanity is evil, or deserves to die, but do you really think we would be appreciative of the good
        that does exist if we thought it was our status quo..."
    b "I do my best, I don't pretend to be enlightened, but I try,
        I try to help people, to be the light that shines in the dark..."
    b "I think you're the same, you were so excited to help at that hospital,
        you didn't consider using the loop for your own gain, you just wanted to save everyone."
    b "Though humanity isn't good, some humans are... They matter, and maybe one day I'll be able to include myself with them."
    b "I've been inside people's heads, [riley_first], and the amount of darkness I can sense is immense..."
    b "Even those with good intentions, like [millie_first], can become blind to the fact they have become darkness as well."
    b "But you weren't like that, it's why I wanted to help you so much.
        You are one of those lights fry, and right now, you're needed."
    b "We can find a way out of this, me and you, whichever version of me ends up doing it with you, whether I reset too,
        without memories, or stay here as you go meet another me."
    b "I know you can solve it, solve how to make things better, and seize a brighter future."
    b "For no matter what, no matter what guilt you feel now,
        you are one of the people that make it worth it to look upon this planet that's as dark as the night sky."
    p "Beatrice, I—"
    b "It seems it's time to go, I hope I do get reset as well."
    b "Who knows, maybe that spirit butterfly of yours will figure out a way to restore our memories eventually,
        assuming I do get to come with, at least."
    b "The butterfly spirit must be gaining something from the world being flooded with true magic multiple times."
    b "Besides, now you know, things won't be as bad if you stay away from the lab, the machine won't function at all.
        You know at least one way to save this world, and it's as simple as doing nothing at all."
    show butterfly normal at left
    # TODO: scene is of Riley Standing back to back with beatrice, looking at the sky, with butterfly in frame
    # TODO: Butterfly effect sounds/images
    p "I see, you're right, it is time, I truly hope that I can talk to you again,
        that you do come with, even if you don't remember."
    b "Believe me, I do too."

    jump branch_point

label fry_day:
    $ last_chosen = fry_first
    $ chosen_fry = True
    p "{i}Of course! If it is because of the machine, like I suspect,
        then surely [fry_first] can help! He knows machines.{/i}"
    # TODO: Blank Screen with just the word mechanism
    p "[fry_first], would you come with me? I need to look into something..."
    f "Oh, um, sure! I'm sure I can help answer technical questions."
    m "Hey! I could answer those too!"
    p "Shh. I need him to distract [mattias_first] if he ends up showing up... I think his ability will be useful too,
        take the day off, I'll make sure there's nothing to do in there today anyway."
    m "OK, I see what you mean... Guess I'll take the day off!"
    p "Now [fry_first]! Aren't you excited to see your idol's lab?"
    f "Yep! I can't wait!"
    p "Then let's go!"

    scene bg lab room
    show fry normal
    p "Look, here is the machine the professor has been working on..."
    p "Is there any chance you can tell what it does? I'm a bit curious."
    f "Um, yeah, I can see if I can figure it out..."
    f "Huh, interesting... It seems to be essentially two parts, a condenser of magic and a utilizer."
    f "The condenser essentially uses the more science anchored Frederick Particles to generate true magic,
        which is the kind spirits like to use, which has less scientific explanations linked to it."
    f "However, it is explicitly designed to store this true magic up, and then channel it though an entirely separate set of technology."
    f "I can't tell what the final function of it would be, as it seems that several of the parts are based off these magic swords,
        which I can't analyze as well, but I can figure out that this is non-functional right now..."
    f "In fact, under the parameters of this machine, I believe the true magic would end up dissipating,
        or even return to the spirit side of reality."
    f "The spirits would be utterly unconcerned with having a bit extra around,
        as their side of reality is essentially flooded with the stuff anyway."
    p "Wait, they have access to that much power? Then why do I need to give them stuff then?"
    f "That... is unknown, the two explanations are they just like getting things,
        or maybe that they need a connection to this side to actually transmit a proportional amount of true magic, in any case..."
    f "This machine needs the guidance mechanism fixed... And I know how to do it."
    p "{i}Maybe that will fix things!{/i}"
    p "Then do it then!"
    f "Um, maybe, but I'll have to figure out what the mechanism does first...
        I wouldn't want to activate a machine that's aiming to destroy Canada or something like that."
    p "Maybe you could find the other workers in the lab, they might know more than [millie_first]..."
    f "Huh, when did [millie_first] have the time to tell you?"
    f "Well, anyway, I'll look for someone to ask, you stay here..."
    hide fry
    p "I wonder where that will lead... Hopefully he'll be able to figure that out."
    p "Because I very much know what will happen if this is not solved."
    show beatrice normal
    b "I finally found you!"
    b "Something's happened to [millie_first]! She fell down the stairs! Her leg is broken!"
    p "What, [millie_first]? How could this happen!"
    b "I don't know, but the spirits must be able to help, right? I can help you with the offering,
        but I'm worried about her... She'll never be able to afford the hospital bills if the ambulance finds her first!"
    p "Sorry, but could you wait just a moment? This machine - I have to help [fry_first] fix it, then I can go help [millie_first]."
    b "This machine? It can't be that urgent... We can leave [fry_first] a note, if you explain, I'm sure he'll understand!"
    b "And besides, even if it's about to explode or something, it has an off switch! See I can even switch it for you."
    # TODO: Machine activation effect/noise
    $ last_triggerer = beatrice_first
    p "Oh no... Beatrice, that was the \"On\" switch..."
    show fry normal at left
    f "Oh, hi... My fellow human! Um, are you doing OK... Because I can assist you if you require it of this genius scientist!"
    f "Oh whatever..."
    p "[fry_first], we have to go! Everyone runs!"
    b "Huh, oh, OK..."
    f "If you think that is the best course of action! If you don't mind assisting me with where to go...
        I will allow you to assist me in making my glorious escape!"
    p "Here, [fry_first], you can follow me, I can help you, [beatrice_first], you get out of here on your own."

    scene bg ruins
    show fry normal
    p "I see, it happened again."
    f "..."
    p "[fry_first], are you OK? I hope [beatrice_first] got out OK..."
    f "Yeah, I am, I can barely process what is going on right now."
    f "First of all, the machine shouldn't have done this, it just should have malfunctioned and broken..."
    f "Second, I heard some things from the other lab workers... that kind of rattled me..."
    f "They told me that they didn't know what the machine did either,
        Professor [mattias_last], [mattias_name], refused to tell them..."
    f "They had a general idea of the functions of the machine, but never the purpose..."
    f "They suggested using it to heal people, even extend the human lifespan, help the environment,
        but he always denied these causes."
    f "In fact, he told them \"You couldn't comprehend the actual solution, so I won't tell you.\""
    f "They all seemed so broken... and it sounds like Sibyll was the most broken of them all."
    f "He barely did any work, he just provided magic swords from his ability, and designed the utilizing section, nothing else."
    f "Apparently, he's always been that way, using big ideas, letting those below him do most of the work..."
    f "If I had known sooner, I would've strived to become better than him, instead of idolizing him."
    f "I never know what to do with broken people, my last hope is that the future wanted by the professor is truly one that is worth it all,
        but that doesn't prevent me from being scared..."
    f "Maybe by completing that project, I could have saved all those broken people, helped them start to heal,
        if that's even the solution at all."
    f "After all, the people in this world were always so broken, people are mean to them, so they are mean in turn."
    f "Something nobody can control, like a power that has utility, but is not flashy, is seen as an indicator of worth."
    f "And everybody always thinks everyone but themselves, who thinks differently from themselves, is broken as well."
    f "I've been guilty of this too."
    f "My power is to know how to fix what's broken... but it only works on machines... It didn't help when I looked all around,
        and saw everything that was broken, but it wasn't technology, I couldn't understand it..."
    f "If I could have chosen, if I could choose the objective of the machine, I would have chosen to create the miracle of understanding,
        of people seeing each other as themselves, and understanding their problems.
        I feel like I'm so close to understanding it, how to fix the broken parts of humanity,
        the parts of us that make everyone worse, that break more and more souls,
        but I'm not there yet..."
    f "At some point, a miracle would have done us some good, it might not have fixed things,
        but it might have started a process that leads to the solution."
    f "Make sure something changes, and out of that change maybe we could have
        figured out how to fix these ways of thinking we seem to be so stuck at."
    p "I understand [fry_first]..."
    # TODO: drawn scene Butterfly appears again, Riley looks at it, Fry looks down.
    p "I see, so I'll be able to try again. Maybe with [fry_first]'s help, I could figure something else out."
    # TODO: Butterfly effect sounds/images

    jump branch_point

label initial_reverse:
    $ chosen_reverse = True
    p "And anyway, now that I think about it, I have a question for Millie as well. Could you come with me for a moment?"
    hide fry
    hide beatrice
    p "Professor [mattias_last] had approached me earlier, and asked me to join the project.
        Could I get an opinion from you about that?"
    m "Um, sure, that would be fine! I will try to talk you out of even considering it though."
    p "I know! But I do want to discuss it in depth."

    scene bg lecture outside
    show millie normal
    m "[riley_first], is something up, are we not going to the lab?"
    p "So the machine [mattias_first] is building, I have a feeling that it might
        be about to cause everything to go horribly wrong."
    m "How could you possibly know that, I mean, I can't discount that possibility,
        but based on what I know about [mattias_first], he's not the kind to do that."
    p "It won't be intentional... Look, I can't tell you how, but I have information
        that shouldn't be possible for me to know."
    m "That's not terrifying at all... but I don't think you're the type to lie about that. Maybe a spirit told you?"
    p "Oh, yeah, it actually is something like that... Good guess."
    p "Anyway, his machine is broken, and I have to do something...
        After thinking about it, I think your power is the best way to do that."
    p "We need to reverse the directive of the machine, have it do the opposite of what was intended."
    p "But what that will end up doing is more or less erasing magic from the world..."
    m "What, what do you mean more or less... and why would that be acceptable to anyone?"
    p "Because the alternative is the destruction of everything... It's because the machine is broken..."
    p "Maybe we could fix it, but the options to do that, or to neutralize it, have problems..."
    p "I think this is the most reliable method."
    p "Not to mention even if we could fix it,
        [mattias_first] will use the results to become the king of everything."
    p "That is his goal, to eliminate technology and make himself king of a fantasy, isekai-like world."
    m "You are right that the options are limited... I can't believe eliminating magic is the best one..."
    p "Yeah, I know, it's not what I would call ideal either."
    p "However, I have an idea, it might make things better for you specifically,
        but that will be the reality for the world as a whole... but I'll let you know only if it works..."
    p "But it still should give you an advantage, maybe help your family rise out of the bit there in...
        but it will have a cost."
    m "We'll see... If it works out, you can tell me then, for now, let's get this done...
        Wouldn't want to let that stupid genius make himself a monarch while we deliberate."
    p "I don't think that's super likely, but we can certainly try."

    scene bg lab room
    show millie normal
    p "Are you ready?"
    m "As I'll ever be... let's condemn this world to being one of technology, where the rich undeniably rule."
    p "To save it from a fate where no one can live."
    m "Yes, of course."
    # TODO: Machine activate, and makes the visual and sound effects, but there is another new sound effect as well, to indicate reversal

    scene bg lab room machineless
    show millie normal
    m "Is it done?"
    p "I think so."
    m "Well then, best we figure out what to do in a world with only boring technology,
        they'll have to change our curriculum substantially, I think."
    p "Unfortunately, it's a bit more complicated than that."
    m "What do you mean?"
    p "What I tried worked, meaning there are still a couple more people with powers."
    m "What do you mean by that?"
    p "Using the machine itself as an offering, I strengthen the connections that spirit speakers use to communicate with spirits...
        I also gave you access to that connection."
    m "Wait, does that mean?"
    p "Yes, we still have ability-based magic even in this world without it."
    p "But that also means we'll have to hide it, we'll certainly be able to use it to our advantage,
        but we should probably stay in the shadows..."
    p "But regardless we can definitely help your family, but we certainly have to limit the people we have contact with."
    m "That's equally cool and very not cool, but I guess that's how things are, we have a responsibility too, right?
        To be the only kind of equalizer this world has, even if it means we have to hide to do it."
    p "Yes, I think Fry will be fine, though, and we can definitely find [millie_first] later,
        she's understanding enough to help us somehow..."
    m "I guess, but this world is still pretty bleak right, and I hate to have to hide in the shadows forever..."
    p "Unfortunately, our path is set, we probably will have an extended lifespan though!"
    p "I've heard spirit speakers live a really long time, to the point no one is sure how many of us are alive,
        despite being born every 100 years."
    m "I see. Guess we'll be lonely too. Oh well, guess that's just how things are."
    p "I guess so."

    jump initial_ending

label initial_leave:
    $ chosen_leave = True
    p "Or, you two can keep discussing if you really want to,
        [beatrice_first], could you come with me for a moment, I have a favor to ask."

    scene bg lecture outside
    show beatrice normal
    b "So, what's this mysterious favor! I hope it's something fun!"
    p "I think that I can trust you with this, but it's really important, it's a matter of life and death for the whole world..."
    p "I need you to go into Professor [mattias_last]'s lab, and turn on the machine there."
    b "Oh, why? And why can't you do it yourself?"
    p "It's a long story, but if I go there and do it myself, everything will end,
        this way, we can prevent that ever being a possibility."
    p "I don't think it can be used more than once, it's the kind of thing you only get one chance for,
        if I understand it correctly... even [mattias_first] couldn't gather up that much true magic again."
    b "True magic! Well, it sounds like it's important, I trust you, I will do it."
    p "Thank you so much, this means a lot to me."
    b "I won't let you down!"
    b "Oh, and if he gets mad... send him to me, I'll take responsibility."
    p "OK! Good to know."

    scene bg lecture outside
    show beatrice normal
    show mattias normal at left
    b "[riley_first] I did it! You should have seen the look on Fry and Millie's faces!
        It was hilarious! What was your plan now? [mattias_first] seemed very angry..."
    s "Angry... I see an apt description. You were the one who put her up to this, right [riley_first]?
        Why would you do that, I didn't think you had ever seen my machine."
    s "Actually, I don't want to know, I am friends with the principal, you know. You can both consider yourselves expelled."
    p "What? I understand me, but [beatrice_first] shouldn't be, I put her up to it,
        she didn't know what would happen."
    s "Life isn't fair kid, as you surely should know having ruined mine, that machine was everything..."
    s "I can tell you were expecting to be punished, and OK with it,
        so naturally to actually inconvenience you I have to do so to your friend as well."
    s "Maybe then you'll feel remorse. So long then, I will tell the principal myself."
    hide mattias
    p "[beatrice_first]... I don't know, I'm sorry..."
    b "It's not your fault, it's [mattias_first], what machine could possibly be worth this much anger?
        It still sucks regardless... We'll just have to figure something out then!"
    p "You... still want to be friends with me? Even if I got you expelled..."
    b "Yeah, of course, why wouldn't I... You had a good reason, right?
        Besides, we can definitely find something to do, with both our abilities..."
    b "We could do so much, like maybe a detective agency or something..."
    b "Although, we might not be able to do anything like healing for anything beyond simple things
        considering we're largely untrained still."
    p "Yeah, I still wish things could be better, but they could be worse, right?"
    p "Although [mattias_first] might end up recruiting [millie_first] and [fry_first],
        making them work on whatever he comes up with next."
    b "Honestly, I don't think [fry_first] will mind... And [millie_first] can probably handle herself."
    p "I still don't feel good about it though."
    b "There is not much we can do."
    p "I guess, let's go then!"

    jump initial_ending

label initial_fix:
    $ chosen_fix = True
    p "Anyway, I actually had a question about today's homework,
        and [fry_first] had agreed to help me earlier, so I guess I'll have to say goodbye.
        [beatrice_first], [millie_first], see you later!"
    m "OK, see ya!"
    b "Have a good rest of your day!"

    scene bg lecture outside
    show fry normal
    p "So, [fry_first], this is going to be a tough conversation to have... I'm going to need you to trust me..."
    f "What do you mean, I do trust you, but it depends on the thing."
    p "There are three things I need you to understand."
    p "First, I need you to fix the professor's machine."
    p "Second, I need you to understand that the professor has been lying, and has done little of his work himself."
    p "Third, I need you to fix the machine, and allow whatever it was he was planning to happen to happen."
    f "Huh? I don't understand... but I guess you don't have any reason to lie,
        I will confirm the stuff about him being bad, but, for now, I'll take you at your word."
    f "Besides, the things he has made are generally good, so I have no reason to suspect this one."
    f "I think I will be a bit broken when I find out the truth for sure, so I will fix the machine first,
        but I can definitely fix that machine, and trust that you know what you are doing."
    # TODO: If riley has seen different endings this can change, maybe they can think im not sure if it does what it actually does
    p "Thank you, I don't really know for sure what the machine does either."
    p "It will change the world, and I'm not sure if it will be a world you prefer,
        but the alternative is the end of the world, so I agree it's worth it."
    f "Yeah. Let's go then, no point waiting."

    scene bg lab room
    show fry normal
    f "OK, I think the machine is fixed now."
    p "Oh, is it?"
    p "I guess it must be about time to activate it then."
    f "Yeah, I guess it is..."
    p "See you on the other side, I guess."
    f "OK, I've also confirmed that it's true that [mattias_first] is not who I thought...
        As soon as we've settled down after the machine does whatever it does,
        I'll definitely need some time to think and accept that... but now it's time to activate this machine."
    p "Let's go!"
    # TODO: image and sound for machine activating

    scene bg forest
    show fry normal
    p "Oh, I see so this is the world we'll live in now."
    f "Wow. It seems to have changed everything... There's no more technology... What could I possibly do now?"
    p "I think my ability is much stronger. I think I'm generating my own true magic, that I'll be able to offer to the spirits..."
    p "I might not need offerings for doing some things anymore...
        and what I can do with the same offerings has been substantially increased."
    f "I see... I think mine is different too."
    f "I keep on looking at different things in this forest, and knowledge about how they can be used
        and combined with each is just flowing into my brain, like what used to happen with technology..."
    f "Am I an alchemist now? I guess that's not bad... not as cool as technology was, though."
    f "And I'm guessing that magic will become fundamentally more important, now that everything seems to approach true magic."
    f "There might even be monsters... dragons even."
    f "That's kind of terrifying..."
    f "At least with technology you could be mostly safe, even if you were unhappy."
    f "I for one don't think the slightly increased chance you can work for happiness worth it
        for the much increased chance of being eaten by a dragon."
    f "It's also fascinating that I know dragons exist, well I guess they must if ever root can be combined with their scales."
    p "I see. Not bad points."
    show mattias normal at left
    s "Hello denizens of this new world! It seems my machine activated, somehow, and a new world has been created."
    s "I made sure some of the magic would go to me, so I can announce my reign as King [mattias_name] the 1st!
        I know this must come as a shock, but I do have my reasons!"
    s "Challenge me if you can! Ha, as if you could!!!"
    p "So, [millie_first]'s definitely gonna do a revolution, right?"
    f "Honestly, I didn't talk to her much, but probably. I've seen her glares at the professor."
    p "Well, I guess we should find her, and [beatrice_first] too if we can...
        I wonder if we'll be able to survive in this world."
    f "Hopefully we can, although, I think next time we find rest, I'll need some time, you can go ahead."
    p "Are you kidding, I'm not going to get eaten by a dragon alone! I'm sure things aren't too mixed up from before,
        and I think Beatrice will move too far away from the ex-university area."
    p "She may even be looking for [millie_first] or me as we speak, and [millie_first] will be wherever [mattias_first] is,
        trying to kill him. We have to find them, we have to be able to work with somebody, but you're important too..."
    p "You'll have all the time you need to process, hopefully they'll be in the same place we end up anyway..."
    f "Thanks, though, it might be a while before I can truly accept that we'll never build a computer again."
    p "In this reality, we don't know if we'll be able to survive, or if the others will either.
        And assuming that, we might not meet up... but I don't want to give up hope."
    p "Even if it's hard sometimes, this is still hope here, and that's better than the alternative of everything being destroyed."
    p "{i}Things could be worse, I think I need to hold onto that, because our situation right now is very, unfortunate.{/i}"
    p "{i}But I guess it's what we got, so I'll make the most of it, especially if it means that the world is safe.{/i}"

    jump initial_ending

label initial_ending:
    menu:
        l "Are you truly OK with how things are now?
            Are you willing to brave your perilous day once more, to strive for a better ending?"
        "Yes":
            jump branch_point
        "No":
            $ renpy.run(MainMenu())
            jump initial_ending

label final_reset:
    p "WHY! Why, can things never end happily...
        I can't just accept that I need to make the sacrifice of leaving someone unhappy, just for the rest to be OK..."
    p "What should I do?"
    # TODO: Drawing of Riley Breaking down
    b "[riley_first]? What's wrong, what are you talking about?"
    m "Whatever it is, if I can help, I will. You've given me hope of a friend for the first time since I can remember..."
    f "I finally found someone I could trust to see me beyond just my power,
        who saw that I had value and wasn't to be pitied... Please, tell us what's wrong, I'm sure we can help."

    scene bg butterfly
    # no character appear because they should be drawn on the background image
    l "Don't despair, for it will be OK."
    l "I have finally gathered enough power, and [riley_first] has as well."
    l "Now, I can appear even to those without the sight... and help them as well."
    b "Are you... A spirit? How?"
    l "[riley_name] has gone through more than you could possibly know."
    l "For this reason, utilizing their gathered power, and their resolve to make everything right, as well as my own power,
        I can finally help [riley_first], and help you to help them."
    m "How... I don't even know what's wrong."
    l "I can remind you of the things you have lost, forgotten in the winds of the hurricane that brought [riley_first] to this point."
    l "Are you resolved to share this burden?"
    f "Anything for my valued assistant!"
    m "If I can help, if I can make things better for them, then I want to."
    b "Of course, I would never look away when someone needs help, especially [riley_first]."
    l "It seems that you are resolved then."
    l "Furthermore, it seems some part of each of you already remember."
    l "I am Lycaenidae, and by the small gust those memories leave in your souls, I shall awaken the rest,
        and the hurricane will be yours once more."
    # TODO: EFFECTS AND SOUNDS THAT SHOULD ACCOMPANY THIS.
    b "I actually remember! [riley_first]! I made it!"
    b "This is super weird though, like my memories are out of sync, but it does seem like they are unifying well enough,
        I do remember that happening vaguely before this though..."
    m "[millie_first], might I have a word?"
    m "I get what you mean within the memory stuff,
        though I don't know how you remember being with [riley_first], I was with them the whole time..."
    m "And it is very much Fry who needs to give an explanation, what the heck dude? You blew up the world?"
    f "Ha, that's unlikely, it was very much [beatrice_first] who blew up the world, why I do not know."
    b "Wait, was it not [millie_first]?... Oh."
    b "Oh no, [riley_first]..."
    b "You guys... Can't you see? All of our memories happened, [riley_first] went back all those times... Saw the world end all those times..."
    m "Now that you mention it... but I think I remember more than that too.
        I do remember a timeline where nothing got blown up, but it wasn't very happy for me either?"
    f "I do, I remember that it left me miserable..."
    b "Hmm, maybe that's how we got here. [riley_first] chose to go again, relive today even more times, but even when they saved everyone,
        they couldn't stand leaving any of us in a bad situation."
    b "They couldn't stand that anyone had to sacrifice anything."
    b "Oh [riley_first]... It's OK, we're with you now, we can figure this out... It will be OK."
    # TODO: A picture of a group hug, Riley at the center
    p "Everyone, thank you."
    p "With all of us together, maybe we have a chance."
    m "What have we learned anyway?"
    b "That the machine destroys the world because [riley_first] is too cool?
        And because the professor didn't think including a limiter would be worth it?"
    f "That the professor is actually an egomaniac who does no work,
        and also how he was so obsessed with whatever that machine does that he made."
    f "A miracle making machine and was so confident it would do what's best that he didn't listen to anyone's ideas?"
    m "Or the fact the machine itself is meant to turn the world into a isekai anime where he's the protagonist who becomes king?"
    p "With everything summarized like that it seems like [mattias_first] is the main source of the problems."
    p "Stopping him won't inherently fix anything, but we can certainly keep him from interfering while we figure out how to move forward."
    p "I don't remember any of the solutions being completely bad, especially compared to the apocalypse.
        They were definitely flawed, but maybe together we have a chance at finding something better?"
    m "More than a chance, we got this!"
    f "Yeah, just think, now I bet we can all agree to talk some sense into [mattias_first]!"
    m "Even you're against him now? What happened in those other loops?"
    f "Not important."
    m "If I remember the timing right, he should be in his office right about now, are you all ready? I know I am."
    p "Of course."
    b "I was steady since the reset, I won't let [riley_first] have more regrets!"
    f "Time to lecture a professor!"
    m "..."
    m "Whatever, I'll give that one to you."

    scene bg office
    $ left1 = Position(xpos=0, xanchor="left")
    $ left2 = Position(xpos=0.2, xanchor="left")
    $ left3 = Position(xpos=0.4, xanchor="left")
    show beatrice normal at left1
    show millie normal at left2
    show fry normal at left3
    show mattias normal at right
    m "We got you now! You old man!"
    m "We won't let you use that machine! Ever!"
    s "I don't think you, of all people, have a say in the matter... I can't stop now... I have to reform this world!"
    m "No one wants to worship your sorry ass, I'm sorry."
    m "If you were king, I would start a revolution myself!"
    p "I knew it! Right [fry_name]?"
    f "Oh yeah, in a fantasy world, yep. You read her super well!"
    m "Whatever! The point is that we know way more than you at this point, you old man!"
    s "Who ever said I was old? And I don't understand a word you're saying."
    b "I'm sorry, professor, but I do very much dislike you! You didn't even think that inviting [riley_first] would negatively impact the machine!
        It caused the world to blow up! Multiple times!"
    b "You're lucky [riley_first]'s powers were able to make use of that and for their mutually beneficial relationship with a time butterfly-thing.
        Sorry, Lycaenidae, I don't know what you are, and frankly, I am not sure you know either..."
    b "The point is, you've lost your vote to determine what happens to the world!"
    s "Time butterfly? Destroy the world? Multiple times? What the heck does any of this mean..."
    b "Sigh, it's probably easier to show you... Allow my memories into you, it will be a lot quicker."
    s "Oh, you can do that! That's interesting, yeah, maybe I can use that! I already have an idea on how we can utilize it!"
    m "He really can't help himself, can he?"
    b "All right! Here you go!"
    s "I can see now! I can see now? I EXPELLED you? Well, I can sort of understand that,
        even if it makes sense why you took your actions as well."
    s "Oh, it seems I may be a bit silly, in reflection."
    s "It sounded so good in my head, maybe I hyperfocused a bit too—"
    s "No! Now that we have this info, I can make a new plan! Utilize more true magic with [riley_first] help!
        I have to fix everything, make a world that actually makes sense to me!"
    s "Can't you see, it's my dream! I can be a benevolent ruler!  If you just give me a chance! I want people to adore me...
        but for what I do for them, not what thing I added to this world."
    s "Life has been made so complicated, I can ensure equality! Can't I do that! I'll be so strong I can stop oppression,
        and besides, the magic part of technology is better anyway."
    f "I disagree, technology might be a curse sometimes, how it can be used to manipulate, exploit, and distort,
        but I genuinely think that we can make technology not evil."
    f "Even then, I can admit the magic world might not be too bad either.
        IF we cooperate, that is... a king is too much for any stage of civilization."
    f "Even if the world is magic, why couldn't we just cooperate instead?"
    m "I mostly agree, even if I like magic, it's not like a magic world is all good either, I like being able to watch silly TV shows...
        those make me happy, even if I dislike the institutions that technology can make."
    m "In addition, people can find ways to live in an unequal world if they have to, and who's to say we can't start a revolution
        in a technological world as well, even if it's a different kind, one of words more so than violence."
    b "I don't think the shape of the world matters as much as the people in it,
        choosing to help each other, to counteract those who go astray..."
    b "I think it's best if we focus on the fact that no matter what humanity will be the same.
        There will always be some people who will be bad."
    b "Humanity as a whole could never be just one thing, and the amount of people who choose to do good things
        is depressingly few, but no matter what we can choose to be better ourselves."
    b "We can try to make the world one where it's easier to avoid going astray,
        and to make it easier for people to find their way back if we—"
    s "Why, why are you denying me my dreams, are you saying that having these dreams, a vision, makes me bad?"
    s "That these wants of mine, these goals that I believe would make the world better, are somehow inherently wrong?"
    p "Dreams are good, in fact, we need them... but we have to understand that not all of them can come true,
        it's the way we are, we yearn for what we cannot have, we hope for what will never come... because what if it does come?"
    p "If you have everything you ever wanted, and learned how to want no more... What's next?"
    p "Nothing but an eternal emptiness...even if your vision for the world came true, it wouldn't help,
        the most it will do is change things..."
    p "What really matters is what you do after. I don't think you thought about that at all, we will be stuck in our cycle of wants.
        We will always want what we can't have, if anything because we can't have it."
    p "Every decision leads to more decisions, new outcomes, new things to miss, to need, to want.
        We all have our own idea on what will solve everything, and we walk forward so we may eventually reach it...
        but you did. Would you be happy, I don't think so, you've dreamed so much that it's sure to be utterly disappointing."
    p "I don't know what's next, I don't know what's right, maybe nothing is, but I can make a choice, and that choice will do something,
        it may hurt some, kill some, save some, help some...
        but it won't change the fact that I'll be responsible no matter what, because that is my burden to bear..."
    b "Wait, you don't seriously think that, do you, it's mine too, I've seen what you have, and I agree."
    b "We have such beautiful dreams, but beauty is in the eye of the beholder. We think that we know what's right,
        and then dream a reality where that is true."
    b "But we deceive ourselves in thinking that it benifits everyone and not just us. That our dreams should be everyone's.
        That our understanding should be universal."
    b "But forcing your ideas, even if you think it's for the best, just stifles each other's dreams...
        we have to find a balance, a way to make everyone happy, but no one content...
        to have them keep dreaming, reaching for what's next, but not so angry that they snuff the light of others out."
    b "Because they are so, so convinced they are right, and if they are right then no one else can be.
        In this field of darkness, there is indeed light, but the dreams of others can easily snuff that light out."
    b "In their search for an ideal world, they choose to smother that light, thinking it will help them obtain their dreams...
        that's why one person can never be in control."
    b "This isn't an easy choice, but we'll make it together, and if we somehow snuff out the light by accident, then we can persist,
        and make sure there's at least a little left... a little that may reignite the light once again... that's what we can do together."
    b "As long as you haven't given yourself completely to serving only death, oppression and destruction,
        there is always hope that you can change, provide hope, care, and goodness to the world again."
    f "I'll join too, I haven't seen what you have, but I can see the world, how broken it is."
    f "People make such assumptions about others, based on what you can do, what abilities you have,
        what choices you make, and the values you hold."
    f "I resent it. I resent all of it, telling me what matters... We are so mean to each other...
        for what? To feel right, to feel superior."
    f "I see people being so mean to each other, and I need to do something, fix something, even if it isn't them right away."
    f "Ultimately, the only thing we can be sure to fix is our connections with those around us,
        there might not even be a cure-all for humanity, but we can certainly do something."
    f "Fix our own mistakes, no matter how terrible it is to face them, fix our ways of thinking, so we may understand those around us...
        but we can only do so much, maybe we can fix ourselves, maybe we can fix our bonds, but we can't fix others."
    f "We shouldn't want to fix others... Whenever we try, we always end up hurting them...
        because we could not possibly understand them enough to do so, we can only beg them to help themselves."
    f "If they don't, if they keep being destructive, trying to fix others, doing things that hurt them, hurt you.
        Then we can only stop them, and try to save others, hoping someday they will be reached."
    f "We may not truly fix anything, but it is a choice I can help make, to help my friends not have to break themselves as much,
        to provide my own strength, to let myself be broken as well."
    f "And maybe together, we can help each other fix ourselves in the new world we choose."
    m "I see we do have a choice, right? That's more than what can be said for many... we have access to this machine, this power."
    m "There is something that is unfair about it and inevitably our choice here will affect someone
        who would have made a different choice... but that doesn't change the situation we're in, does it?"
    m "Whenever possible, I want to make sure people are able to decide for themselves the life they want to live, but here,
        when all the answers are potentially correct, we inevitably have to make this choice,
        one that will decide the future path of humanity, completely by ourselves."
    m "However, I think as long as we don't make the choice with solely our own interests in mind."
    m "As long as we think about the effects on humanity as a whole, and those who had their choices taken away since they were born,
        like those in my hometown, then we can at least live with whatever comes of the choice we do make."
    p "First, let's review our options."
    p "The first choice is to activate the machine outright, and reformat technology into magic and fantasy...
        the major problems were we were separated, and therefore couldn't help each other and Mattias was on a power trip..."
    p "The second was to reverse the machine. This would erase magic and leave the world mostly magical,
        except for expanding the role of spirit speakers, and making anyone I want who's nearby at the moment a spirit speaker as well."
    p "Basically a mundane world where there are secret wizards, where we can do what we want,
        but probably end up finding ways to help people."
    p "Together we'll have a head start in figuring out how to manage that coexistence with the mundane world,
        and [fry_first] can be our link to technology."
    p "And then finally we could leave the machine be, embrace this world we already have, without its flaws,
        we can each make our way in our current world, and [beatrice_first] and I won't be expelled this time."
    p "Did I miss anything?"
    b "Nope, all of those sounds fine to me, and we can figure out what goes on from there... I think I will be making the same choice as you,
        but if I think of anything last minute, I'm not so nice that I'll let you make an objectively wrong choice!"
    m "Pretty much the same for me."
    f "Me as well."
    menu:
        "Keep the machine off":
            jump final_leave
        "Reverse the machine":
            jump final_reverse
        "Activate the machine properly":
            jump final_fix

label final_leave:
    p "Well, I think the correct answer is to just keep it off..."
    p "This world, is not so hopeless as to justify changing all of it."
    p "OK?"
    b "OK."
    f "OK."
    m "OK."
    s "I see now. I thought if you made this choice, I would be sad, but I only feel relief."

    s "You were right... all of you, my dreams, I disregarded everyone. I loved all of it, all that I saw...
        I thought that it would make everyone happier."
    s "But, I was letting my dreams decide what was best for others,
        making their choices for them... and it almost led to everyone dying."
    s "What now, what could I do now, how can I make amends for something
        no one will ever know about... and what will life be like for all of us."
    s "I can't imagine a future... where I can make up for any of it... I feel such guilt.... I can see now...
        but I can't guarantee I won't lose sight again, so, sorry you have to see this."
    s "He puts a sword into the ground, it starts draining him of energy."
    s "This will render me permanently comatose, but I'll be able to think, and perceive..."
    s "A self-imposed prison."
    s "This is what I deserve..."
    s "Do what you will. However you choose to further punish me, I'll deserve it."
    p "YOU IDIOT!"
    p "You're such an... idiot..."
    p "We don't want you gone!"
    m "What... What do we do?"
    b "I... I can't do anything... I can't ask his permission...
        and even if I could, understanding won't do anything here."
    f "I can't fix anything that is not a machine..."
    m "My reversal, is not working, it's a magic sword....he imbued too much power into it."
    p "I... might though..."
    p "Spirits, I beseech you thy aid."
    p "What will be the cost to save this man in the dark, to renew his soul, his life..."
    p "I see.... that's a fair price..."
    p "I agree."
    b "Wait! What did you agree to?"
    p "They'll take the machine, and my humanity..."
    m "WHAT?"
    f "Why... how?"
    p "It's not so bad... you three still be able to see me...
        but I will join them, as a nature spirit... I'll still look like myself though."
    p "That's the price, I will save everyone, at the cost of my human existence."
    p "The cost to heal was myself... the cost to remain here, for now, is the machine..."
    b "Oh, I see, how long will it take to save him, I mean..."
    p "It will be soon..."
    "[mattias_first]'s wound heals... he awakens again."
    s "What, why... how..."
    s "Where are they?"
    m "[riley_first] saved you."
    b "Hey professor, don't let what happened go to waste,
        you can still help others, find their dreams, and make new ones."
    f "You were my dream once, to be like you."
    f "Now, I want to work with you as myself, we can make things better,
        maybe some things will get worse, but things will change."
    f "That change, is human."
    m "I'm going to do what I always feared, I'll enter politics...
        make sure there are those who are on your side."
    m "Even if they don't understand, I'll make sure that you can help us."
    m "I'll support you, as you try to make this world of ours better. Maybe magic and technology combined...
        Maybe they can help us. Help us make something where no one is lesser, for their birth, or for who they are."
    m "Although we can still condemn choices they make that threaten others."
    m "We can make a world, where people's choices, their actions matter more than the circumstances they are in...
        and work to change this stagnating system that wronged me so."
    m "With the help of that technology you guys will make, that might someday become a guiding star to a proper world."
    m "But I will not hesitate to become your worst enemy if needed, if the technology you choose,
        your choices, try to harm people again, or harm this planet again."
    f "Let's go then, see if you can keep up with us....muwahaha, see if you can keep up with our great genius, look out world!!!
        You will never prepare yourself for the duo of the ages!!!"
    f "The dastardly duo who will improve your lives, and change the world into one no one dared dream of!!!"
    s "Oh boy, I need tylenol..."
    hide millie
    hide fry
    hide mattias
    b "That leaves us then."
    p "It... sure does..."
    b "Are you OK?"
    b "Maybe? I'll get used to it..."
    p "The question is, what now?"
    b "Let's help people."
    p "I see."
    p "We can do that."
    b "Then let's go, this world is hurting, and we can help, make this dark world a little brighter."
    b "Right, my friend?"
    p "Right."
    b "I won't give you my hair though!"
    p "Nor did I ask for it."

    scene bg end
    # TODO: Image of Beatrice with Riley floating nearby
    jump end

label final_reverse:
    p "As cool as magic is, maybe the world would be better off being mostly without it...
        after all, if [mattias_first] can make a world ending machine by accident, then others could theoretically do the same."
    p "I would prefer to largely erase magic from the world if it meant that it would continue!"
    m "Yeah, I think we could theoretically figure out how to avoid world ending machines,
        but it wouldn't be the worst thing not to worry about that either!"
    b "This works out for me! I can't wait to see all the cute spirits!"
    f "I don't need magic if I have technology, but I guess it's ok to join your secret wizards club as well."
    s "So, this is what you're going for... I suppose it will make the world more boring, I suppose,
        but are you truly prepared to live your lives in the shadows?"
    p "Actually, we might not need to... you make a pretty good villain Mattias! We can blame the whole magic removal thing on you,
        and then frame it as you did it to become a spirit speaker yourself... and then you can be like a supervillain!"
    p "Where us good Spirit Speakers would be there to stop your machinations!
        You don't even have to hurt anyone, as we could coordinate."
    p "Or you could also go all in with evil, either way works! We can also present the amount of spirit speakers increasing
        as a way of the world balancing everything... this might be pretty fun."
    p "We won't have to hide, as nobody will be bitter at the people with powers defending them."
    s "I see, but make no mistake, my pride won't allow it to be an act!
        Prepare yourself from stopping me from robbing all the banks!"
    m "All? That's so like you, we'll just have to stop you then!"
    b "This is kind of exciting! Though i'll be on support duty, [millie_first] and [fry_first] can do the fighting.
        And [riley_first] is already trained in support type stuff as well!"
    f "Woah, that sounds like a lot... I guess that's fine, as long as my public identity is of the millionaire tech genius sponsor!"
    p "Yeah, that should be fine, sounds like we're on the same page then!"
    m "Then let's do it! I'll reverse, [riley_first] you focus on the spirit stuff."
    p "Right."
    # TODO: Machine activation visual effects and sounds
    p "It's done!"
    b "Oh wow! The spirits are so cool! Some of them are really cute too!"
    p "Yeah. They do seem happy to see you."
    f "I can't wait to start my rise in this social economic system!"
    m "So is the main difference this time that [fry_first] is a dirty capitalist?"
    f "Not true! I promise to not become a billionaire, I will donate every penny above a billion if I have to!"
    m "I'm joking, you really aren't the evil type, I can tell...
        the good news is that now I can beat up [mattias_first] whenever he annoys me! So that's good."
    s "If you can, silly hero! You'll never stop me from robbing all the banks,
        be careful if you store your fortune in a bank [fry_first]!
        Because I'll rob it if you do! And other campy supervilliany things."
    b "You know, based on this and the whole king thing, you really have a flair for the dramatic, don't you?
        It's like your subconscious was always wanting you to be a villain."
    s "Um, no comment."
    p "Anyway, what will the rest of us do? We can't just be superheros."
    m "What if we formed a band, I can play guitar pretty well,
        and something tells me [beatrice_first] probably is at least a decent singer as well!"
    p "I can learn drums, if that works, I've studied a little bit and they do seem fun!"
    m "Great! Also, maybe when we're superhearing, we can focus on giving publicly and compassion
        towards my hometown, and any underadressed community."
    m "We can make sure this world doesn't eat them alive, now that magic is less of a factor."
    b "Of course, I know that they will appreciate that!"
    p "Right it's the least we can do."
    f "Ha, I will be a rebellious rich person! I will strive for wealth inequality."
    m "Ok tech bro."
    f "I'm not a tech bro!"
    m "Keep telling yourself that!"
    p "Anyway, it seems like our future is bright, this is going to be fun...
        though it's probably pretty chaotic right now in the world."
    b "Yep! But soon they'll face the wrath of the evil doctor [mattias_last]!"
    p "Of course, but we'll stop him every time!"

    scene bg end
    # TODO: Picture of everyone dressed as superheros, maybe just masks and capes though,
    # but Mattias is in full superfillain costumes
    jump end

label final_fix:
    p "Now that we have [mattias_first] cornered, there are a lot fewer negatives to the fantasy angle..."
    p "And in addition to that, this is probably the only way to completely reset power in this world."
    p "Assuming that we can avoid monarchies, we'll be able to construct a new system, one that is fair to everyone,
        and provides opportunities regardless if you were born with powers or not."
    p "In fact, we could normalize not using your abilities for personal gain,
        but to protect those who don't have abilities at all."
    m "Yeah, just because you have powers, doesn't mean we have to choose to use them to exploit...
        we can work together to ensure that those who would be vulnerable are safe, and don't get eaten by dragons."
    b "As I said, I think that as long as we're together, we'll be ok, so we can work together!
        Together, we can probably fight anything that would either oppress or eat those who want to live peaceful lives."
    f "I will miss technology, but that doesn't mean life will be bad... just different...
        and i can become super good with alchemy, and then teach those skills to others."
    f "Maybe eventually, though it may take awhile, I will be able to make alchemy the new equalizer in that world,
        or at least make it so the people who defend are able to have people working behind them to help in their own way."
    f "We can still ensure the safety of those who prefer a different way of life."
    p "Let's do it then, [fry_first], you know how to fix the machine right?"
    p "Could you also remove [mattias_first] king announcement while you're at it?"
    f "If I conceptualize fixing as including that, probably."
    p "Ok, let's go then! To adventure!"
    m "Sounds fun!"
    b "Let's protect people!"
    f "Let's get this started then."

    # TODO: Fade to black, and the machine starting sound and visual effects
    scene bg forest
    show beatrice normal at left1
    show millie normal at left2
    show fry normal at left3
    show mattias normal at right
    m "Woah! I can't believe that worked!"
    m "This is great!"
    b "I've never seen that kind of flower before! This is amazing!"
    f "I know I've seen this before... but I'm still awestruck..."
    s "So you need to use my machine anyway... What was all this for then?"
    p "To keep you from becoming just another oppressive force upon this world,
        nobody deserves to have absolute power over others."
    s "I suppose so... What do I do now then, will you arrest me for my flaws,
        and what you see as my mistakes?"
    m "Nope! You would just love to be able to laze around in jail all day, wouldn't you?"
    f "Yeah, you may have come up with ideas, but you did so little work on all of your creations!
        For once you should actually work to do something for other people!"
    b "Naturally there needs to be more protectors than just us! We may still have a massive grudge against you for
        what you accidentally were going to do to the world and what you wanted to do to become kind,
        but that doesn't mean you won't have a role of your own."
    b "Only we know what happened today... find people you can call friends as well! And use your powers,
        and help us keep people from being eaten by dragons!"
    s "I see... so that's the life I should live... maybe I can find fulfillment in that...
        or at the very least maybe I can find people who I can befriend as well."
    p "Yep! Now, let's do the first step which is to go and seek people panicking,
        and help them build or find an empty built town to live in,
        and start spreading the world of how we as humans can make our way in this world."
    m "And not get eaten by dragons?"
    b "I would very much prefer to avoid that."
    f "Yeah, me too!"
    p "Let's go... [mattias_first], you can stick with us for now until we find a place to settle for now...
        wouldn't want to leave you to the dragons anyway."
    s "Thank you, I too would not want to get first hand knowledge of a dragon's hunting rabbits."
    p "Right, then let's go! To this new world!"

    scene bg end
    # TODO: Image of Riley, Beatrice, Millie and Fry setting forth into a new world, Mattias is there too, not quite as eager
    jump end

label end:
    l "It seems you have found a future you're satisfied with, I'm happy for you."
    menu:
        l "But if any doubt remains, this path is not yet set in stone feel free to use my power once more, just remember to return here
            if you decide this is the path your heart desires. However the other memories won't come with this time."
        "Let's see what the other future look like":
            jump final_reset
        "My heart is content":
            $ renpy.run(MainMenu())
            jump end
