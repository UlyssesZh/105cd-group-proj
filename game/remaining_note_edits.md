# Remaining Note-Driven Edits for `script.rpy`

These are proposed edits based on the unaddressed comments in `Ren'py written script "The Papillion Effect".txt`.

They are **not applied yet**. Each item is numbered so you can approve, reject, or modify specific edits.

## Text Edits

### 1. Intro menu labels
```diff
-         "like the spirits":
+         "Open up about the spirits":

-         "completely avoidant":
+         "Avoid the topic":

-         "sick of their shit":
+         "Complain about the spirits":
```

### 2. Fry introduction menu labels
```diff
-         "TODO: option 1":
+         "Ask for help with class":

-         "TODO: option 2":
+         "Tease his whole vibe":
```

### 3. Riley reintroducing their name to Fry
```diff
-     p "My name is Riley, by the way... (Hurriedly follows [fry_first] into lecture hall)"
+     p "{i}He really doesn't slow down, does he?{/i} (Hurriedly follows [fry_first] into lecture hall)"
```

### 4. Post-lecture menu labels
```diff
-         "TODO: option 1":
+         "Check on him":

-         "TODO: option 2":
+         "Tell him to relax":
```

### 5. Riley's "best of both worlds" line
```diff
-         p "Well, I guess that makes him happy, best of both worlds, you know,
-             both being normal with friends and insufferable to people he couldn't care less about..."
+         p "Well, I guess that works for him.
+             He gets to be normal with friends and dramatic with everyone else..."
```

### 6. Millie conversation pacing
```diff
      p "I can definitely try! Beats doing nothing for the rest of my break...
          I'm [riley_name], by the way."
+     p "You don't have to tell me everything, but if you want to vent, I can listen."
      $ millie_name = f"{millie_first} {millie_last}"
```

### 7. Riley's "session even" line
```diff
-     p "To make this session even, something about me is that I can talk to spirits...
+     p "To make this conversation fair, something about me is that I can talk to spirits...
         I may have had an easier childhood, but it made me a target throughout my life."
```

### 8. Mattias cafeteria menu labels
```diff
-         "TODO option 1":
+         "Agree to visit the lab":

-         "TODO option 2":
+         "Push back on the invitation":
```

### 9. "Lab rat" response
```diff
-             p "I don't want to be used like a lab rat. I need some time to think about it, Professor."
+             p "I don't want to be treated like an experiment. I need some time to think about it, Professor."
```

### 10. Beatrice's haircut/offering line
```diff
-     b "Oh! I should have known, your hair looks the same way it did before,
-         and I don't think you had time to make another type of offering either!"
+     b "Oh! I should have known, your hair looks the same way it did before,
+         so I guess you haven't had time to make another spirit offering either!"
```

### 11. Beatrice's "hang in there" line
```diff
-     b "Spirits, if you can hear me, hang in there, I'm sure you'll have your fun soon."
+     b "Spirits, if you can hear me, be patient, I'm sure Riley will have an offering for you soon."
```

### 12. Olive tree line
```diff
-     b "At the very least, I'll have Riley here, have you make me my own olive tree next time they get their haircut!"
+     b "At the very least, maybe I can ask Riley to help me grow my own olive tree next time they get their haircut!"
```

### 13. Hospital follow-up line
```diff
-     p "Haha, not a bad idea though, maybe then we can go volunteer in a hospital together or something,
-         I'm sure they'll be happy to have access to your ability as well."
+     p "Haha, not a bad idea. Maybe we really could volunteer at a hospital together sometime,
+         I'm sure they'd be glad to have access to your ability too."
```

### 14. Beatrice's worldview line about Millie
```diff
-     b "Oh, well if my worldview wouldn't survive getting to know someone who seems as interesting as you,
-         then it must be a pretty limited one anyway!"
+     b "Oh, well if being friends with Riley means getting to know interesting people like you,
+         then I think that's a good thing anyway!"
```

### 15. Millie's "see home too" line
```diff
-     m "Sure, whatever. Probably won't make a difference, though, but it couldn't hurt. Would be nice to see home too."
+     m "Sure, whatever. Probably won't make a difference, though, but it couldn't hurt.
+         Would be nice to feel a little closer to home too."
```

### 16. Riley defending Fry
```diff
-     p "I'm sorry, he isn't always like this."
+     p "I'm sorry, he's not always this intense."
```

### 17. Millie's "equalizing" line
```diff
-     m "Technology is impartial blah blah blah... it may be equalizing for those who don't have useful abilities,
-         but that doesn't mean it's fair."
+     m "Technology is impartial blah blah blah... it may level the playing field for people who don't have useful abilities,
+         but that doesn't mean it's fair."
```

### 18. Lab entrance menu labels
```diff
-         "TODO option 1":
+         "Agree that Mattias is the problem":

-         "TODO option 2":
+         "Defend the lab's mission":
```

### 19. Riley processing the first reset
```diff
      if route_count == 0:
          p "Huh? Why am I here again? The world is... still OK!"
+         p "No... no, I was just outside. I saw everything destroyed."
+         p "I really am back. Somehow, I'm back."
          p "If I'm here, maybe I can actually prevent it from happening."
          p "But I don't think I have much time. I've got to hurry. Maybe that machine caused this to happen?"
```

### 20. Branch-point investigative option
```diff
-             "Actually, there is more I want to investigate first":
+             "I still need to investigate more first":
                pass
```

### 21. Beatrice route background name
```diff
-     scene bg outside
+     scene bg lecture outside
```

### 22. Beatrice's "lights fry" typo/clarity issue
```diff
-     b "But you weren't like that, it's why I wanted to help you so much.
-         You are one of those lights fry, and right now, you're needed."
+     b "But you weren't like that, it's why I wanted to help you so much.
+         You are one of those lights, [riley_first], and right now, you're needed."
```

### 23. Fry machine-analysis line
```diff
-     f "I can't tell what the final function of it would be, as it seems that several of the parts are based off these magic swords,
-         which I can't analyze as well, but I can figure out that this is non-functional right now..."
+     f "I can't tell what its final function is. Several of the parts are based on these magic swords,
+         so I can't analyze those as well, but I can tell the machine is non-functional right now..."
```

### 24. Fry's long "miracle of understanding" passage
```diff
-     f "If I could have chosen, if I could choose the objective of the machine, I would have chosen to create the miracle of understanding,
-         of people seeing each other as themselves, and understanding their problems.
-         I feel like I'm so close to understanding it, how to fix the broken parts of humanity,
-         the parts of us that make everyone worse, that break more and more souls,
-         but I'm not there yet..."
+     f "If I could have chosen the machine's purpose, I would have chosen a miracle of understanding,
+         of people seeing each other clearly and understanding each other's pain.
+         I feel like I'm close to understanding how to mend the broken parts of humanity,
+         the parts of us that keep hurting each other, but I'm not there yet..."
```

### 25. Initial reverse: "directive"
```diff
-     p "We need to reverse the directive of the machine, have it do the opposite of what was intended."
+     p "We need to reverse the function of the machine, have it do the opposite of what was intended."
```

### 26. Initial reverse: unclear "bit there in" line
```diff
-     p "But it still should give you an advantage, maybe help your family rise out of the bit there in...
-         but it will have a cost."
+     p "But it still should give you an advantage, maybe even help your family climb out of the situation they're in...
+         but it will have a cost."
```

### 27. Initial fix: Fry's confidence before seeing the machine
```diff
-     f "I think I will be a bit broken when I find out the truth for sure, so I will fix the machine first,
-         but I can definitely fix that machine, and trust that you know what you are doing."
+     f "I think I will be a bit broken when I find out the truth for sure, so I will fix the machine first.
+         Once I see it, I should be able to fix it, and for now I'll trust that you know what you're doing."
```

### 28. Initial fix: dragons line
```diff
-     f "It's also fascinating that I know dragons exist, well I guess they must if ever root can be combined with their scales."
+     f "It's also fascinating that I know dragons exist. I guess they must if every root can be combined with their scales."
```

### 29. Final reset: broken miracle-machine sentence
```diff
-     f "That the professor is actually an egomaniac who does no work,
-         and also how he was so obsessed with whatever that machine does that he made."
-     f "A miracle making machine and was so confident it would do what's best that he didn't listen to anyone's ideas?"
+     f "That the professor is actually an egomaniac who does no work,
+         and that he was so obsessed with what that machine could do that he made"
+     f "a miracle-making machine and was so confident it would know best that he didn't listen to anyone else's ideas?"
```

### 30. Beatrice's "universal" line
```diff
-     b "But we deceive ourselves in thinking that it benifits everyone and not just us. That our dreams should be everyone's.
-         That our understanding should be universal."
+     b "But we deceive ourselves into thinking it benefits everyone and not just us. That our dreams should be everyone's.
+         That everyone should understand the world the way we do."
```

### 31. Final leave: Riley's spirit-price line
```diff
-     p "It's not so bad... you three still be able to see me...
+     p "It's not so bad... you three will still be able to see me...
         but I will join them, as a nature spirit... I'll still look like myself though."
```

### 32. Final reverse: spirit-speaker sentence
```diff
-     p "Where us good Spirit Speakers would be there to stop your machinations!
-         You don't even have to hurt anyone, as we could coordinate."
+     p "Where we good spirit speakers would be there to stop your machinations!
+         You don't even have to hurt anyone, since we could coordinate."
```

### 33. Final reverse: "superhearing"
```diff
-     m "Great! Also, maybe when we're superhearing, we can focus on giving publicly and compassion
-         towards my hometown, and any underaddressed community."
+     m "Great! Also, maybe when we're doing hero work, we can focus on public giving and compassion
+         toward my hometown, and any underaddressed community."
```

### 34. Final fix: "become kind"
```diff
-     b "Naturally there needs to be more protectors than just us! We may still have a massive grudge against you for
-         what you accidentally were going to do to the world and what you wanted to do to become kind,
-         but that doesn't mean you won't have a role of your own."
+     b "Naturally there needs to be more protectors than just us! We may still have a massive grudge against you for
+         what you accidentally were going to do to the world and what you wanted to do to become king,
+         but that doesn't mean you won't have a role of your own."
```

### 35. Final fix: "spreading the world"
```diff
-     p "Yep! Now, let's do the first step which is to go and seek people panicking,
-         and help them build or find an empty built town to live in,
-         and start spreading the world of how we as humans can make our way in this world."
+     p "Yep! Now, let's do the first step, which is to go find people who are panicking,
+         help them build or find an empty town to live in,
+         and start spreading the word of how we as humans can make our way in this world."
```

## Implementation / Structure Edits

These are still note-driven edits, but they are not just dialogue swaps.

### 36. Replace remaining `TODO` menu labels throughout `script.rpy`
Affected areas:
- Fry intro choice
- post-lecture Fry choice
- Mattias cafeteria invitation choice
- lab entrance choice

### 37. Decide and implement the repeated title-card / transition comments
Affected `TODO`s:
- `Earlier that day`
- `INTENT`
- `Reality`
- `mechanism`
- fade / flash / butterfly reset transitions

### 38. Standardize the thought presentation rule
Current issue:
- some internal thoughts use italics
- some use plain dialogue
- some stage directions are embedded in dialogue text

Proposed direction:
- use italics only for thoughts
- convert embedded actions like `(Runs into lecture hall)` and `(Walk away)` into narration/stage lines where useful

### 39. Resolve the reset-route explanation UX
Current issue:
- the notes ask for clearer handling of what the "investigate more first" option does
- the first reset needs a stronger comprehension beat

Proposed direction:
- keep edit 19
- add a short one-line prompt before the branch menu explaining Riley is choosing between intervention and more investigation

### 40. Clean up remaining non-art `TODO`s that are really script issues
Examples:
- `scene bg butterfly` / `scene bg end` assume backgrounds that may not exist in the current project
- route comments like `# TODO: If riley has seen different endings this can change...` should be resolved or removed
- any non-visual TODO that changes meaning should either be implemented or deleted
