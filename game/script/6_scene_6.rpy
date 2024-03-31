label scene_6:
    ##Scene 6

    window hide
    show black onlayer fade:
        xpos 1.0
        linear 1 xpos 0
    pause 1

    hide black
    hide black onlayer foreground

    show bg2_closed onlayer foreground

    show fre_shadow onlayer foreground
    show fre smile onlayer foreground at fre_transform

    show oph_shadow onlayer foreground
    show oph smile onlayer foreground at oph_transform

    show black onlayer fade:
        xpos 0.0
        linear 1 xpos -1.0
    pause 1
    hide black onlayer fade
    play music "music/track 3.ogg" fadein 2.0
    $ hide_sides = ['Freya', 'Ophelia']

    "Taking our seats in our roomette, we bask in the glow of the west coast."

    "It's fantastic. Beautiful. So utterly... home."

    "For {i}me{/i}."

    "But that can be {i}us{/i}. I have the power to change that."

    "Time to enact the final step in my plan. Time to bring her home."

    
    camera foreground at camera_transform(shake=0.0, pos=(0.0, 0.66), zoom=2.01, duration=1.0)
    pause 1
    oph "Enjoying the best coast so far?"

    camera foreground at camera_transform(shake=0.0, pos=(1.0, 0.7), zoom=2.01, duration=1.0)
    pause 1
    fre "Oh my God, yes. It's amazing here."

    show oph e_smile onlayer foreground
    camera foreground at camera_transform(shake=0.0, pos=(0.0, 0.66), zoom=2.01, duration=1.0)
    pause 1
    oph "Right?? I wasn't sold at first, either. But after seeing it, after being here, I learned that there was no better place to be."

    oph "And that's doubly true for you."

    show fre nervous_b onlayer foreground
    camera foreground at camera_transform(shake=0.0, pos=(1.0, 0.7), zoom=2.01, duration=1.0)
    "Freya shifts uncomfortably in her seat. She knows where this's going."

    fre "Yeah, but..."

    show oph e_normal onlayer foreground
    camera foreground at camera_transform(shake=0.0, pos=(0.5, 0.5), zoom=1.01, duration=1.0)
    pause 1
    oph "Freya."

    show fre e_normal onlayer foreground
    fre "Ophelia?"

    oph "Realistically, why do you live in Florida?"

    show fre e_sad onlayer foreground
    fre "Huh?"

    oph "Think. Why Florida? Dig down and find the core reason."

    "A moment passes before she finds her answer."

    show fre e_normal onlayer foreground
    fre "Uhh... Honestly, because I do. I realize that's not a good answer, but life sort of ended up that way. I was born there, and my family is there, therefore I'm there."

    oph "Right."

    show oph cheeky onlayer foreground
    oph "So move to Oregon with me."

    show fre e_sad_smile onlayer foreground
    fre "It's not that simple—"

    show oph normal onlayer foreground
    oph "What's keeping you in Florida? What future do you imagine, there in Jacksonville?"

    show fre e_sad onlayer foreground
    fre "Just my family, really. It's not like I have any job prospects there, any career holding me down. My life has been in a sort of... holding pattern ever since you left."

    "She furrows her brow, really examining my question."

    show oph e_smile onlayer foreground
    oph "Frey, all you have there is your family. There's nothing else that Florida offers, and in fact, Oregon offers all of that and then some."

    oph "Think. You'd be accepted for who you are. You'd have more job opportunities, opportunities to work with and for people who'd enjoy you unconditionally."

    oph "So why not?"

    show fre sad onlayer foreground
    "She leans back, considering it all. I can tell that she's been thinking the same thing this entire trip, but making that leap is terrifying."

    "But she knows that, with me being on the other end, logistics aren't the problem."

    "That, as a server, she'd have plenty of opportunity, so finances wouldn't be a problem."

    "And that the only thing holding her down—her family—isn't something she can tie herself to forever."

    fre "You're right."

    oph "You can video call your family any time you want. Fly home for holidays—we'd fly home together."

    show fre smile onlayer foreground
    fre "That'd be very nice, actually."

    oph "And think. You'd be able to live with me! Something we used to dream about. Plus, if you want to go back and get a degree, there's a lovely bunch of universities right in the area."

    "She nods, silent."

    show oph smile onlayer foreground
    oph "You don't have to make a decision today. Just... sleep on it, okay?"

    fre "Okay. I'll sleep on it."

    "With that, our busy day finally catches up to us, and we make our bed with haste."

    "Tomorrow'll be the day."

    "Tomorrow, the rest of my life will be decided."
    stop music fadeout 4.0
    ##End Scene 6

    jump scene_7
