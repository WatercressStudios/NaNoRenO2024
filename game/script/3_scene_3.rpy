label scene_3:
    ###Map Transition - Houston

    $ map_zoom = 3
    window hide
    show black onlayer fade:
        xpos 1.0
        linear 1 xpos 0
    pause 1
    show screen map(5, True) with dissolve
    pause
    show screen map(6, True) with dissolve
    pause
    show screen map(7, True) with dissolve
    pause
    show screen map(8, True) with dissolve
    pause
    hide screen map with dissolve
    pause 0.5

    show black onlayer fade:
        xpos 0.0
        linear 1 xpos -1.0
    pause 1
    hide black

    ###Scene 3

    "As the morning light creeps through a small gap in curtains, the train gently trekking along, I open my eyes."

    "I sit up, careful not to disturb Ophi, and stretch. I slept better than I would have thought, all things considered."

    "Ophi, still fast asleep next to me, rolls over. It’s weird being around her again so suddenly. God, I was an awkward mess yesterday."

    "But she didn’t care. She treated me just like she always used to. So much has changed, but Ophi is just like I remember."

    "I have to be better today. I think things were improving last night. Ophi’s trying to pick things up where we left them, I owe it to her to try to do the same."

    "Gingerly slipping out of bed, I leave the room and head to the bathroom to freshen up."

    "By the time I make it back to our room, Ophi has woken up. Sitting up, still wrapped in a blanket, she sleepily rubs her eyes."

    oph cheeky "Mornin'."

    "She reaches up to her messy hair, pulling it away from her face and back off her shoulders."

    "She’s so fucking cute I can’t—"

    oph "Hello in there? Earth to Freya!"

    fre smile "Oh, good morning! Sorry for spacing, I must still be half asleep."

    oph "You sure about that? You were sleeping like a baby."

    oph "I, on the other hand, struggled my way through the night. Sleeping on trains isn’t easy. Tell me your secret."

    fre "No secrets here, I don’t know what to tell you. I just went to sleep last night and woke up this morning."

    oph "Hmph, well I guess you’re just a lucky bitch then."

    "I crack a stupid smile at the friendly insult."

    fre "I guess I am."

    "Ophelia clambers out of bed, and pushes past me, sticking her tongue out at me."

    "While she’s gone to the bathroom, I work on getting the bed folded away. With a little effort, the bed is transformed back into our seats."

    "Ophi slips back into the room just as I’m finishing up."

    oph "Wanna get some breakfast?"

    fre "Sounds good, I’m starving."

    #NOTE: I'm leaving the previous text unscripted (for now) since they belong to the as-of-yet unfinished bed CG.
    #If I get everything else done, I'll wrap around and do some basic scripting.
    #~Wolf

    window hide
    show black onlayer fade:
        xpos 1.0
        linear 1 xpos 0
    pause 1

    hide bg2_closed onlayer foreground
    show bg1_open onlayer foreground

    show fre_shadow onlayer foreground
    show fre normal onlayer foreground at fre_transform
    show oph_shadow onlayer foreground
    show oph normal onlayer foreground at oph_transform


    show black onlayer fade:
        xpos 0.0
        linear 1 xpos -1.0
    pause 1
    hide black

    show fre normal onlayer foreground
    show oph normal onlayer foreground
    "Sitting down in the same dining car booth as yesterday, I look out the window, getting my bearings straight on just where we are."

    show oph e_smile onlayer foreground
    "Vast pine woods flicker by, bringing a surge of memories from our early high school days."
    
    show fre e_smile onlayer foreground
    fre "Remember cutting through the woods to go to the cafe?"

    show oph e_devious_smile onlayer foreground
    "Ophi snorts."

    show oph e_devious onlayer foreground
    show fre e_smile_ec onlayer foreground
    oph "To skip P.E.? Yeah. In hindsight, you hating P.E. makes too much sense."

    show fre e_smile onlayer foreground
    show oph e_smile onlayer foreground
    fre "Right? God, I was so dense."
    
    show oph e_devious_relaxed onlayer foreground
    oph "I also remember you running away from that gator you almost stepped on."

    show oph laugh onlayer foreground
    show fre normal onlayer foreground
    "Ophi giggles."

    show fre pout onlayer foreground
    show oph e_smile onlayer foreground
    fre "Yeah, yeah, very funny."

    show fre e_devious onlayer foreground
    show oph surprised onlayer foreground
    fre "But I distinctly remember another time you tripped over a root and ate shit."

    show oph e_embarrassed_p onlayer foreground
    "Ophi covers her face in embarrassment."

    show fre e_happy onlayer foreground
    show oph e_sigh onlayer foreground
    oph "Ugh, don’t remind me. I was covered from head to toe in mud!"

    show fre sad onlayer foreground
    show oph sad onlayer foreground
    fre "You know, I tried going after you left. After a couple times going alone, it just started feeling…"

    show fre sad_ec onlayer foreground
    fre "I don’t know, hollow."

    show fre sad onlayer foreground
    show oph e_sad onlayer foreground
    oph "You know I would have been there if I could."

    show fre e_sad_mo onlayer foreground
    show fre nervous_b onlayer foreground
    fre "Of course. Your Dad didn’t really give you a choice."

    show fre e_sad onlayer foreground
    show oph e_sad_mo onlayer foreground
    oph "It was hard. The worst days of my life. I lost my Mom, and then I lost my best friend."

    show oph e_sad
    "I want to tell her I didn’t die, that she could have kept in touch, but I think better of it."

    "I don’t want to sour the mood. It’s been a great day so far, and I want to make the most of the time I have with Ophi."

    "Instead, I steer the conversation back to our good memories."

    show fre e_sad_smile onlayer foreground
    fre "Remember when Grandma accidentally gave us your Mom’s edibles?"

    show oph e_surprised onlayer foreground
    show fre e_normal onlayer foreground
    oph "Oh my god, I forgot about that! What were we, twelve?"

    show fre e_smile onlayer foreground
    show oph e_normal onlayer foreground
    fre "She was freaking the fuck out when she realized what happened."

    show oph e_laugh onlayer foreground
    show fre e_happy onlayer foreground
    oph "She made us promise not to tell Mom! Oh, she would have been livid if she had ever found out."

    "As we laugh and reminisce, the conductor announces our arrival into San Antonio."

    show fre normal onlayer foreground
    show oph e_normal onlayer foreground
    "We gather our things and get off the train. I check the notice boards and find our connecting train."

    show oph normal onlayer foreground
    show fre e_normal onlayer foreground
    fre "I think we have a few hours before the next train."

    show oph e_normal onlayer foreground
    oph "If you want, we could drop our bags in the sleeper passenger lounge and explore the city a bit."

    show fre e_happy onlayer foreground
    fre "I’m down!"

    $ map_zoom = 3
    window hide
    show black onlayer fade:
        xpos 1.0
        linear 1 xpos 0
    pause 1
    show screen map(9, True) with dissolve
    pause
    hide screen map with dissolve
    pause 0.5

    hide black onlayer fade
    hide black onlayer foreground
    show black onlayer foreground

    ###Map Transition - San Antonio
    ###Jared’s San Antonio Exploration Scene
    ###Should have a title card as such: "Side Story: San Antonio"

    show text "{color=#FFFFFF}{size=50}A Brief Aside: \nSan Antonio{/size}{/color}" onlayer foreground
    with dissolve
    pause
    hide text onlayer foreground with dissolve

    n "The station itself is strikingly Tex-Mex in design. I guess it's a fitting omen to say we still have half the state left to get through. We're pretty deep in it at this point."
    
    n "\"Oh hey, the Alamo. I remember that place!\" I proclaim sarcastically."
    
    n "Ophelia cocks an eyebrow in my direction, smiling and shaking her head as she walks away and stretches on the platform. I blush as I try not to stare."
    
    n "I think I'm pretty clever for only a moment. As we walk into the bright open streets, we can't help but notice the stadium down the road."
    
    n "\"What do you think that place is?\" I ask."
    
    n "Ophelia whips out her phone, pulling up a map faster than I can blink. \"It's the Alamodome.\""
    
    n "My expression drops, my ego shattered. The Alamo.. Dome? There's an Alamo DOME?" 
    
    n "I curl up into a ball on the sidewalk as I realize that I am no better than any of the thousands of tourists who enter this place and make that exact same joke, blissfully unaware of their unoriginality."
    
    n "It's baked into the very sand, and I am nothing but a single grain."
    
    n "\"Come on,\" Ophi bumps against me, shaking me from my drama. \"Are we gonna check out the city or not?\""
    
    n "I leap to my feet, dusting myself off. \"Alright, alright. What do they even have here?\""
    
    n "Ophi gets in close, smiling. \"That's the thing, Freya. We gotta go find it.\""
    
    n "She leads the way, with me just a couple steps behind her. And like some kind of spell, we don't even notice we've found our way to the path that follows the river through the downtown area."
    
    n "It's a lively walkway, with restaurants and bridges and gardens decorating the way. Everything centered on the river."
    
    n "I guess people don't really change that much, even over the course of hundreds of years. We're always drawn back to water."
    
    n "We don't really have a plan. Well, I sure don't, and Ophi doesn't seem to have much of one either."
    
    n "We stick close to the water, seeing where it leads us."
    
    n "Occasionally, we stray to investigate whatever catches our eye as the river leads us from one side of the city to another, over and under bridges as they come and go."
    
    n "I remind us that we need to circle back around soon so we don't miss the train. Ophi shrugs, saying she's keeping track of the time."
    
    n "We pick a spot to eat, a largely authentic-looking Mexican restaurant to really run home the Texas experience."  
    
    n "And with perfect timing, we make it back to the station with just a few minutes to spare. I'm satisfied with the tour, ready to get back on the train."
    
    n "\"What the fuck is that?\" Ophelia asks, looking just down the road. Across the tracks, there's a run-down building with a winding slide coming out of it."
    
    n "I guarantee sliding down it would give you tetanus and four other diseases with cryptic names. Just being near it would be a health hazard. It's perfect. The most punk thing we've seen for miles."
    
    n "\"I want to go take pictures under that.\""
    
    n "\"Oh my god, yes!\""
    
    n "Ophelia jumps expertly from one rail to the next as she crosses the tracks, leaving me a couple steps behind as I make sure I don't trip over anything."
    
    n "We take some cute pics under the rusty slide, doing our best to look like cowboys who are about to drop the best indie rock album you've ever heard."
    
    n "It isn't long until we're laughing uncontrollably, and for a tiny moment, our memories from years ago don't seem quite so far away."   
    
    n "The train blows its whistle and we're startled into action."
    
    n "We make off for the train like Bonnie and Clyde, hopping the tracks while still giggling amongst ourselves until we're back in our cabin, huffing to catch our breath."

    nvl clear
    pause 0.5

    ###End Jared's San Antonio Scene

    $ train_speed = 1.0
    scene skybox_white
    camera foreground at camera_transform_init

    $ test_movingpoles = MovingImage("test_movingobject1", ypos=0, min_interval=10000, max_interval=10000, init_xoffset=0, out_xoffset=None)
    $ test_movingpolesrandom = MovingImage("test_movingobject2", ypos=0, min_interval=0, max_interval=10000, init_xoffset=0, out_xoffset=None)
    $ test_movingtrain = MovingImage("test_movingtrain", ypos=0, min_interval=0, max_interval=0, init_xoffset=-500, out_xoffset=500)

    show bg2_closed onlayer foreground
    hide black onlayer foreground
    show black onlayer fade:
        xpos 0.0
        linear 1 xpos -1.0
    pause 1
    hide black onlayer fade

    "A final all aboard call is made for our ride to LA as we hurriedly shuffle up the steps and into the sleeper car."

    "We find our room, and I drop off my bags and circle back to the hallway, in desperate need of the bathroom."

    "When I make it back to the room, I find Ophi working on folding our bed down. She points up to the other bed."

    ####All of the below is side sprites, and a missing CG. TBD
    ####~Wolf
    $ hide_sides = []

    oph sad "Looks like the top bunk isn’t stuck this time!"

    "I can’t help being disappointed by the apparent news that Ophi and I will be sleeping in separate beds tonight. I can’t let her see it though."

    fre nervous "Maybe you’ll sleep better tonight."

    oph "One could hope. And speaking of which, I was thinking of taking a nap down here for now. That cool with you?"

    fre "For sure. I’m not really tired though, so I’m just gonna chill."

    oph "Of course you’re not tired, you got a full eight hours last night!"

    fre "Yeah, I know, I’m a lucky bitch."

    "Ophi laughs sweetly at my sarcastic teasing and lays down. I sit down on the bed with my back next to the window, legs pointed toward the door."

    "She shuffles a bit, trying in vain to fluff up the lumpy pillow."

    "After her failed attempts, she looks across to me, and down to my legs. Without hesitation, she flips around, plonking her head right down onto my lap."

    "I’m glad Ophi’s eyes are closed, I would die if she saw how red my cheeks definitely are right now."

    oph "I really did miss you, you know. So much more than I knew at the time."

    fre "I missed you too, more than you could ever know."

    fre "I’m glad we’re taking this trip together."

    "I look back down at her, my checks finally having returned to their normal color, and see Ophi peacefully snoozing."

    fre "It’s not fair."

    "I keep my words to a soft whisper."

    fre "You’re just as beautiful as ever. As adorable and incredible and wonderful."

    fre "I wish we had more time. A few days isn’t enough."

    "I run my fingers through her gorgeous, flowing hair, pushing it behind her ear."

    fre "I could stay like this forever."

    $ hide_sides = ['Freya, Ophelia']

    ###End Scene 3
    jump scene_4

