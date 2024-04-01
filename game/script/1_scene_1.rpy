label scene_1:
    stop music fadeout 2.0
    # AUDIO: ambience train station, not many people but can hear occasional train sounds

    #Scene 1 
    #Written by Wolf

    ###Large centered text on a pastel or watercolor background (if failing that, on a black bg)

    show text "{color=#FFFFFF}{size=50}It's been ten years since we last met.{/size}{/color}" with dissolve
    pause
    hide text with dissolve
   
    show text "{color=#FFFFFF}{size=50}And that's my fault.{/size}{/color}" with dissolve
    pause
    hide text with dissolve

    show text "{color=#FFFFFF}{size=50}I wonder...{/size}{/color}" with dissolve
    pause
    hide text with dissolve

    show text "{color=#FFFFFF}{size=50}Is there still some place for me in her life?{/size}{/color}" with dissolve
    pause
    hide text with dissolve

    play music "music/Track 3.ogg"
    play env "sfx/Quiet Platform.ogg" fadein 1.0
    ###Fade into intro CG (if applicable, if not, NVL)
    scene station_empty
    show text "{color=#FFFFFF}{size=50}{noalt}Jacksonville Station{/noalt}":
        align (0.49, 0.07)
    camera:
        align (0.5, 0.0) zoom 3
    show black
    hide black with Dissolve(2)
    show station_oph behind text:
        alpha 0
        linear 2 alpha 1
    camera:
        align (0.5, 0.0) zoom 3
        ease 2.0 align (0.0, 0.1) zoom 2
    pause 2
    "C'moooon, Freya. This is your last chance! You missed the funeral, you better not miss the fuckin' train."

    window hide
    ###Pace Ophelia's sprite back and forth
    camera:
        align (0.0, 0.1) zoom 2
        ease 1.5 align (1.0, 0.1) zoom 2
    pause 2
    camera:
        align (1.0, 0.1) zoom 2
        ease 1.5 align (0.0, 0.1) zoom 2
    pause 2

    "Aaaah... God! I hate this! The anticipation, the uncertainty, my hand in it all—I'm in for an {i}incredibly{/i} awkward cross-country trip if things keep going the way they are."

    camera:
        align (0.0, 0.1) zoom 2
        ease 30 align (0.5, 0.5) zoom 1

    "...Of all things, why did you have to miss {i}her{/i} funeral?"

    "We were family."

    "And now you're going to miss our train."

    "No no, reset—this is a reset. Remember your goals, Ophi!"

    "See my oldest friend. Bring her back from the shitshow that is Florida. Show her what real living looks like."

    "...Reconnect."

    "That's why I'm here, not for some emotional attack on her behavior. Open-minded, accepting, loving, affirming. And perhaps a little bit of gremlinery."

    "That's who I should be right now."

    "Slapping my face a bit, I stand up straight and put up my front."

    "Okay, Okay. Now, where could you be, Freya?"

    # AUDIO: train horn
    "The train horn blows, signaling the final call."

    "We have a few minutes at most, Freya. So... please be here this time."

    "An employee gives me one last warning, and I'm forced to make a decision."

    "Is it too late?"

    "...Was I too late?"

    "..."

    "I guess so."

    "Sighing, I grab my luggage tight and turn my back on Florida."

    stop music fadeout 2.0
    hide station_oph with Dissolve(2)

    "Well, goodbye, I guess."

    scene black with Dissolve(2)

    play music "music/Track 2.ogg"
    scene freya_intro_bg
    show freya_intro with hpunch:
        anchor (0.5, 0.5) pos (0.5, 0.3) zoom 1.5
        ease 5 ypos 0.4

    fre "O-Ophelia?"

    ###Ophelia's sprite should jump out of its skin right here

    oph "Yeack! Jesus fuck, you scared the shit outta me!"

    "My heart pounds in my chest, and not only from the start."

    "{i}She's here.{/i}"

    scene black with dissolve

    "In a rush, and for other more shameful reasons, I avoid looking at her and grab her by the wrist."

    oph "You're late, we gotta move!"
    stop env fadeout 1.0
    # AUDIO: running footsteps, cabin doors opening and closing
    "Pulling her—and her luggage—with me, we rush into our train car, down the aisle, and all the way back to our roomette."
    
    scene black with dissolve

    $ train_speed = 1.0
    scene skybox_white
    camera foreground at camera_transform_init

    $ test_movingpoles = MovingImage("test_movingobject1", ypos=0, min_interval=10000, max_interval=10000, init_xoffset=0, out_xoffset=None)
    $ test_movingpolesrandom = MovingImage("test_movingobject2", ypos=0, min_interval=0, max_interval=10000, init_xoffset=0, out_xoffset=None)
    $ test_movingtrain = MovingImage("test_movingtrain", ypos=0, min_interval=0, max_interval=0, init_xoffset=-500, out_xoffset=500)

    show bg2_closed onlayer foreground
    
    show black onlayer foreground:
        alpha 1.0
        linear 1 alpha 0.0
    pause 1
    hide black onlayer foreground

    "Still in a rush, I open the door and glance at what our bereavement bought us: A couple of seats foldable into a bed, a bunk up top, and a collapsed tray table in the wall between."

    "Quite the small room to share with someone I haven't seen in ten years."

    "Continuing to avoid eye contact with her, I put my luggage away and out of sight."

    oph "Whew, you startled the fuck out of me, ya know that?"

    "I look around the room again, finding it the same as it was five seconds ago."

    "I'm quickly losing things to distract myself with."

    "Hahh, okay. I guess this's it."

    show oph_shadow onlayer foreground:
        alpha 0.0
        linear 0.5 alpha 1
    show oph nervous onlayer foreground at oph_transform:
        alpha 0.0
        linear 0.5 alpha 1
    pause 0.5

    "Turning around and collapsing into my seat, I let my breath catch up to me. Freya is still stowing away her luggage."

    show freya_intro_bg onlayer foreground:
        alpha 0.0
        linear 0.5 alpha 1
    show freya_intro onlayer foreground:
        anchor (0.5, 0.5) pos (0.5, 0.3) zoom 1.5 alpha 0
        parallel:
            ease 0.5 alpha 1
        parallel:
            ease 10 yalign 0.0

    "Looking up at her, I first notice her cute, stylish jacket and romper. A casual fit, it's kinda cottage-core but I dig it. It fits the Freya that I knew."

    "It's still strange to see, considering the last time we talked, she was... well, not outwardly \"she\". But it fits her better than boy clothes ever did."

    "I finally meet my eyes with hers, and..."

    "{i}Oh no, she's {b}hot{/b}.{/i}"

    "Like, {i}very{/i}."

    "On days like these, it's a blessing that I'm so very gay."

    show fre_shadow onlayer foreground
    show fre j_sad_ec onlayer foreground at fre_transform
    show oph surprised_ec onlayer foreground
    hide freya_intro onlayer foreground
    hide freya_intro_bg onlayer foreground with hpunch

    "No! Focus, Ophelia! Now's not the time!"
    play sound "sfx/Train Leave.ogg"
    # AUDIO: train starts moving finally. is there a train horn again just before that?
    # AUDIO: eventually settle into ambience of train moving
    play env "sfx/Train.ogg" fadein 2.0
    $ test_movingpoles.set_show(True)
    $ test_movingpolesrandom.set_show(False)
    $ test_movingtrain.set_show(False)
    camera foreground at camera_transform(shake=1, zoom=1.01)
    
    show oph nervous onlayer foreground
    oph "It's, uhh, been a long time, hasn't it?"

    camera foreground at camera_transform(shake=0.5, zoom=1.01)

    show oph sad onlayer foreground
    fre "...Yeah. It has."

    show oph smile onlayer foreground
    oph "Well, I have to say, you look fucking {i}stunning{/i}."

    show fre j_embarrassed onlayer foreground
    "Freya awkwardly smiles, embarrassed by the compliment."

    show oph smile_ar onlayer foreground
    oph "Like, {i}really{/i}. You're more... {i}you{/i} than I've ever seen you."

    $ test_movingpoles.set_show(False)
    camera foreground at camera_transform(shake=0.1, zoom=1.01)

    show fre j_embarrassed_smile onlayer foreground
    "She curls up, trying to hide her happiness behind her closed hands."

    show fre j_embarrassed onlayer foreground
    "Cute."

    show oph nervous_b onlayer foreground
    oph "So, what've you been up to, over here in the \"sunshine state\"?"

    show fre j_scoff onlayer foreground
    "She scoffs, just as aware as I am that Florida is anything but."

    show fre j_nervous onlayer foreground
    fre "Enjoying what I can. Jacksonville... could be worse, I suppose."

    show oph disbelief onlayer foreground
    oph "Could it? Could it {i}really{/i}?"

    show fre j_smile onlayer foreground
    "Freya laughs, shaking her head."

    show fre j_normal onlayer foreground
    show oph normal onlayer foreground
    fre "No, I guess not."

    show oph sad onlayer foreground
    oph "You at least find something fun to pass the time?"

    show oph disbelief onlayer foreground
    show fre j_normal_ec onlayer foreground
    fre "Ehh, I've been serving for a while if that counts. It pays the bills at least."

    show fre j_normal onlayer foreground
    show oph disbelief_ec onlayer foreground
    oph "Oh dear."

    show oph normal onlayer foreground
    show fre j_normal_ec onlayer foreground
    "She shrugs."

    show fre j_scoff onlayer foreground
    show oph disbelief_ec onlayer foreground
    fre "Could be worse."

    show oph nervous_b onlayer foreground
    show fre j_scoff
    oph "You keep saying that."

    show oph normal onlayer foreground
    show fre j_sad onlayer foreground
    oph "Well, you'll be out of that place soon enough. I'm not going to lie to you—one of my goals here is to convince you to move to Oregon."

    show oph smile_ar onlayer foreground
    oph "It's better for you in many, many ways."

    show fre j_sad_ec onlayer foreground
    "She winces, retreating."

    fre "That's..."

    show fre j_nervous_b onlayer foreground
    show oph normal onlayer foreground
    oph "A big ask? I know. But if I have my way, all of your concerns will be addressed by the time we hit the ground in Portland."

    show oph cheeky onlayer foreground
    oph "And I'm confident that I can be pretty convincing..."

    show fre j_scoff onlayer foreground
    "I wink at her, and she rolls her eyes."

    show fre j_normal onlayer foreground
    show oph normal onlayer foreground
    fre "Good to see you haven't changed at all."

    show oph smile onlayer foreground
    oph "And neither have you. Well, outside of the obvious. Deep down, you're the Freya I've always loved. Just, now your outside matches what was always on the inside."

    show oph happy onlayer foreground
    show fre j_embarrassed onlayer foreground
    oph "But! Bathing you in compliments won't get you to stay with me."

    show fre j_embarrassed_ec onlayer foreground
    oph "Making up for lost time will."
    
    show fre j_embarrassed onlayer foreground
    "Right?"
    stop env fadeout 5.0
    ###End Scene 1
    jump scene_2
