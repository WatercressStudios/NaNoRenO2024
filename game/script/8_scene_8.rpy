label scene_8:
    ##Scene 8

    $ map_zoom = 3
    window hide
    show black onlayer fade:
        xpos 1.0
        linear 1 xpos 0
    pause 1
    play sound "sfx/Train Map.ogg"
    show screen map(21, True) with dissolve
    pause
    show screen map(22, True) with dissolve
    pause
    show screen map(23, True) with dissolve
    pause
    hide screen map with dissolve
    pause 0.5

    hide black
    hide black onlayer foreground

    # show fre_shadow onlayer foreground
    # show fre normal onlayer foreground at fre_transform

    # show oph_shadow onlayer foreground
    # show oph normal onlayer foreground at oph_transform
    play music "music/Track 6.ogg" fadein 2.0
    show black onlayer fade:
        xpos 0.0
        linear 1 xpos -1.0
    pause 1
    hide black onlayer fade

    "About an hour after we finish dinner, our last meal on the train before reaching Portland, the train pulls into Eugene for the final fresh air break of the journey."

    "Before the train has a chance to come to a complete stop, Ophi grabs me by the hand, pulling me toward the exit."

    oph "It's only a ten minute stop, but it's finally familiar territory!"

    fre "Eugene, huh?"

    fre "What's familiar about it? I thought we had three more hours to go."

    "Stepping down from the train car, Ophi looks up to the sky, eyes closed, breathing in deeply. The orange light of the setting sun lights up her hair like fire."

    "Finally, she exhales."

    oph "I went to school here — the University of Oregon."

    "A solemn, yet contented look washes over her face."

    oph "Lived here for, what, five years?"

    oph "Got a lot of memories in this town, both good and bad."

    oph "Experienced a lot of firsts. First tattoo. First queer bar. First drag show. First time in a band..."

    oph "First time a friend died. First time being cheated on."

    oph "But I took the good with the bad. There was always more good than bad anyway, and it was always worth it."

    oph "My time in this town means a lot to me, I'll always love it."

    fre "I'm kinda envious, if I'm honest. You got to have different experiences in different places. For me, every first I've ever had has been in Jacksonville."
    
    "Ophi gently grabs my face, placing a strawberry-flavored kiss on my lips."

    oph "First kiss in your new home state!"

    oph "And there are plenty of new firsts to be had."

    "Count on Ophi to always give me a new perspective."

    fre "Has anyone ever told you how great you are?"

    oph "Once or twice, now that you mention it."

    "I suddenly feel my arms prick with goosebumps as a wave of bittersweet realization washes over me."

    fre "The trip's almost over."

    "Ophi must recognize my melancholy tone."

    oph "This trip will always have a special place in my heart, kinda like Eugene does."

    oph "The good with the bad, it was all more than worth it."

    oph "I wouldn't trade it for anything."

    oph "I'm glad you showed up on the platform back in Jacksonville."

    fre "It's only been a few days, but looking back..."

    fre "...taking this trip with you, it means everything to me."

    "As the sun disappears behind the evergreen-dotted mountains, all aboard is called."

    "In the beautiful twilight, Ophi gives me my second kiss in my new home state."

    ###Map transition - Portland

    $ map_zoom = 3
    window hide
    show black onlayer fade:
        xpos 1.0
        linear 1 xpos 0
    pause 1
    show screen map(24, True) with dissolve
    pause
    hide screen map with dissolve
    pause 0.5

    hide black
    hide black onlayer foreground

    # show fre_shadow onlayer foreground
    # show fre normal onlayer foreground at fre_transform

    # show oph_shadow onlayer foreground
    # show oph normal onlayer foreground at oph_transform

    show black onlayer fade:
        xpos 0.0
        linear 1 xpos -1.0
    pause 1
    hide black onlayer fade

    "As the train slowly rolls into the station in Portland, Ophi and I gather up our belongings checking every corner of the tiny room to make sure we don't leave anything behind."

    oph "You got your phone charger, right?"

    fre "Yup, already packed it in my backpack."

    oph "Then what's this?"

    "Ophi holds up a cable."

    fre "I dunno, not mine."

    oph "Wait, shit, that's {i}my{/i} phone charger!"

    "I laugh to myself as Ophi stuffs the charger into her bag."

    fre "Got everything?"

    "She takes one last, long glance around."

    oph "Yep, that's everything."

    oph "Let's roll."

    "We make our way out of the room and down the corridor one final time."

    "As we exit the train car, the crisp evening air greets us."

    oph "Ah, home sweet home!"

    "She stretches her arms out, yawning."

    oph "Oh, right—"

    oph "You'll get to meet Fuckie when we get home!"

    fre "What an honor!"

    "Ophi snorts."

    oph "Yeah, it's anything but. He may put on a friendly facade, but remember, he's got that name for a reason."

    fre "I'll be sure to keep it in mind."

    oph "Maybe once you move in, we can get another cat? A little sibling for Firetruck?"

    fre "I'd like that."

    oph "Hell yeah, it's a plan!"

    oph "Now then, let's get home, I'm beyond excited to sleep in my own bed tonight."

    "Ophi looks at me, smiling devilishly."

    oph "And I bet you are, too."

    "Her meaning isn't lost on me, and I return her devious glance in turn."

    fre "I can't wait."

    oph "Another first for you tonight! Imagine that."

    fre "First night with the love of my life?"

    fre "How could I not be excited?"

    "After everything the two of us have been through, these beautiful, awful, wonderful, torturous past ten years..."

    "I think it was what needed to happen. For us to end up here, together."

    "After all of it, the distance between us is gone, bringing us closer together than ever before in the best way possible."

    "Portland, huh?"

    "I think I'm gonna like it here."

    ##End Scene 8

    $ quick_menu = False
    window hide
    call screen credits
    stop music fadeout 5.0
    return
