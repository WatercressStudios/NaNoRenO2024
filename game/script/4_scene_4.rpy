label scene_4:
    ###Scene 4

    $ map_zoom = 3
    window hide
    show black onlayer fade:
        xpos 1.0
        linear 1 xpos 0
    pause 1
    play sound "sfx/Train Map.ogg"
    show screen map(10, True) with dissolve
    pause
    show screen map(11, True) with dissolve
    pause
    hide screen map with dissolve
    pause 0.5

    show black onlayer fade:
        xpos 0.0
        linear 1 xpos -1.0
    pause 1
    hide black
    
    "The squealing brakes of the train wake me from my impromptu nap as the conductor announces a fresh air break."

    "I nudge Ophi, rousing her."

    fre "Hey, wanna get some air?"

    "She sits up, taking a long, catlike stretch."

    oph "Hell yeah, let’s do it!"

    hide black onlayer foreground
    hide black onlayer fade
    show black onlayer fade with dissolve
    show station_empty onlayer foreground
    show text "{color=#FFFFFF}{size=70}{noalt}Alpine Station{/noalt}" onlayer foreground:
        align (0.49, 0.07)
    camera foreground:
        align (0.5, 0.0) zoom 3
    hide black onlayer fade with dissolve
    camera foreground:
        ease 2.0 align (0.5, 0.5) zoom 1.5
    pause 2
    play env "sfx/Remote Station.ogg" fadein 2.0
    "We clamber out of the train, and out onto the platform of the remote station."

    "Ophi continues stretching, taking advantage of the open space we don’t have inside the train."

    fre "Have a nice nap?"

    oph "Slept like a baby. Having such an amazing pillow certainly didn’t hurt."

    "I briefly make eye contact with Ophi, who matches my gaze and smiles deviously at first, then more sincerely."

    "I sheepishly break eye contact, drawing my eyes to our new surroundings."

    "The landscape changed drastically while we were napping. The temperate gulf coast climate that I’m used to is gone, replaced with rugged, hilly desert."

    oph "We’re not in Kansas anymore, are we?"

    oph "Hard to believe we’re still in the same state we started this leg in."

    fre "Wait, we’re still in Texas? Holy shit, this state is huge!"

    oph "And we still will be for at least another couple hours."

    oph "I know you’re probably not thrilled about that, of course."

    "For a moment, I don’t catch her meaning."

    fre "I’ve been enjoying—Oh!"

    oph "Yeah, that."

    fre "To be honest, I haven’t really thought that much about it. I’ve been basically done with my transition for like six years."

    fre "That and the fact that anything Texas can do, Florida can do worse."

    oph "You do have a point there, for sure."

    fre "I also never considered it, but the train keeps us pretty well insulated from any bullshit we might otherwise encounter."

    oph "The train does kinda have a culture all of its own."

    fre "Funny how a goddamn train has a better culture than half of this country."

    "The main street of the small town sits just across from the train station, characteristically complete with a saloon."

    "Many of the businesses have prominent signs in their windows, displaying their hateful politics in plain view, right alongside their merchandise."

    oph "Seeing these parts of the country always makes me depressed. Like, the people broadcast their shit so openly. To them, their hate for people like us is a point of pride. All that without ever really getting to know us."

    fre "I got lucky with my family. A lot of my trans friends have these people as their parents and grandparents. We don’t wanna hurt anyone, there isn't some evil agenda we're trying to enact, we’re just trying to exist as ourselves."

    fre "Looking back, I also got lucky with my transition. The timing was better than most could hope for. Before the bullshit trans panic that’s been going on for the last few years."

    fre "Trans kids now basically have to win the lottery to be allowed to be who they are. Have to have a family that accepts and supports you and live in a state that will do the same and back it up."

    "Ophi jolts my attention back to the present moment, surprising me with a hug."

    fre "What was that for?"

    oph "I just wanted to!"

    oph "Also they called all aboard like two minutes ago and I didn’t know how else to get your attention."

    fre "Oh, shit. My bad, let’s go."

    oph "Right behind you, Frey."

    "She definitely could have gotten my attention another way if she wanted."
    stop env fadeout 3.0
    ####Fade out, in
    show black onlayer fade with dissolve
    hide station_empty onlayer foreground
    hide text onlayer foreground
    camera foreground:
        zoom 1.01 align (0.5, 0.5)
    play env "sfx/Train.ogg" fadein 2.0
    "As we’re walking back to the room from dinner, a bend in the tracks throws me off balance."

    oph "I don’t remember you being such a lightweight. You sure that second vodka pineapple was a good idea?"

    fre "Fuck off Ophi, you know I used to be able to drink you under the table."

    "The train comes out of the turn, this time giving Ophi trouble."

    fre "You were saying?"

    oph "Yeah, whatever loser."

    "She jokingly sticks her tongue out at me and pushes me down along the train, past other rooms until we find our door."

    $ hide_sides = ['Freya', 'Ophelia']

    hide oph onlayer foreground
    hide fre onlayer foreground
    hide oph_shadow onlayer foreground
    hide fre_shadow onlayer foreground
    show oph_shadow onlayer foreground
    show oph normal onlayer foreground at oph_transform
    show fre_shadow onlayer foreground
    show fre normal onlayer foreground at fre_transform

    hide black onlayer fade with dissolve

    "As we stumble into our seats, Ophi digs through her bag."

    show oph happy onlayer foreground
    oph "Thank fuck, it’s in here."

    show oph e_smile onlayer foreground
    show fre happy onlayer foreground
    "Ophi holds up her phone, smiling."

    show fre cheeky onlayer foreground
    fre "I told you it would be. There’s basically nowhere else it could have been."

    show oph e_normal onlayer foreground
    show fre normal onlayer foreground
    "She flips through her camera app, readying some pictures to show me."

    show oph e_laugh onlayer foreground
    show fre e_smile onlayer foreground
    oph "Anyway, this is my baby Firetruck. I usually call him Fuckie or Asshole though."

    show black onlayer fade with dissolve

    "She passes me her phone, and I catch the briefest glimpse of an orange cat before the train rounds another bend."

    show black onlayer fade with hpunch

    "The sudden, if small, shift in momentum was more than enough to send Ophi’s phone tumbling to the floor—and Ophi herself tumbling right into my lap."

    "Clumsily catching her in my arms, we lock eyes. Ophi’s cheeks flush, just for a moment, and the look in her eyes is not a look I’ve seen her give me before."

    "I know what I hope that look is, but to be wrong would be a terrible mistake."

    "But the look persists, as if to confirm my suspicions."

    "Fighting against the fear and anxiety building in my chest, my heart beats so loudly and quickly that I’m sure Ophi can hear it."

    "I close my eyes, and, taking a deep breath, I lean in."
    play music "music/Track 8.ogg" fadein 2.0
    "Ophi meets me halfway, and we gently lock lips."

    "The kiss lasts for a short moment that feels like an eternity."

    "All those years I spent carrying these feelings for her, never thinking that this day might come."

    "But it’s just a kiss. It doesn’t necessarily mean anything."

    "But it’s a kiss. It could mean a lot."

    "She tastes like strawberries and gin."

    "The moment ends, and we both pull back."

    "Opening my eyes, I realize that Ophi is still looking at me the same as before the kiss."

    show oph embarrassed onlayer foreground
    show fre embarrassed_b onlayer foreground
    hide black onlayer fade with dissolve

    "I recognize the look now: longing."

    show oph embarrassed_mo onlayer foreground
    oph "I’ve been waiting all day for that."

    show fre embarrassed_mo onlayer foreground
    show oph embarrassed onlayer foreground
    "I can’t help but laugh in spite of myself."

    show fre e_happy onlayer foreground
    fre "All day, huh? Try waiting sixteen years."

    show fre e_embarrassed_mo onlayer foreground
    "I blush, realizing too late that I might have said too much, but Ophi is unphased."

    show oph devious onlayer foreground
    oph "You think I didn’t know?"

    show fre shocked onlayer foreground
    fre "I, uh…"

    show oph cheeky onlayer foreground
    oph "I figured it out in like, freshman year, you dork."

    show fre shocked_b onlayer foreground
    fre "Oh."

    "Oh shit, oh fuck, what the fuck?"

    show oph e_devious onlayer foreground
    show fre e_sad_mo onlayer foreground
    oph "But I never looked your way back then, and you knew why."

    show oph e_normal onlayer foreground
    show fre e_sad onlayer foreground
    oph "Then I heard about your transition from Grandma, and I was curious, but you were so far away, and I never knew what to say."

    show oph e_smile onlayer foreground
    show fre e_sad_smile onlayer foreground
    oph "Then I saw you on the platform back in Jacksonville."

    show oph e_smile_b onlayer foreground
    show fre e_smile onlayer foreground
    oph "I really {i}saw{/i} you."

    show oph e_laugh_b onlayer foreground
    show fre e_smile_b onlayer background
    oph "And I knew I loved you the way you used to love me. I just hoped you still felt the same way."

    "My mind is racing faster than the train, a hundred thoughts rush to the surface all at once, but I push them all down. I’ll think later."

    show oph e_smile_b onlayer foreground
    show fre e_embarrassed_mo onlayer background
    fre "I never stopped loving you."

    "I lean in and give her a quick kiss on the cheek."

    show oph e_laugh_b onlayer foreground
    show fre e_happy_b onlayer background
    fre "Not for a single second."
    stop music fadeout 4.0
    stop env fadeout 4.0
    jump scene_5
