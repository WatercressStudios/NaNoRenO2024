label scene_7:
    ###Map Transition - Oakland

    $ map_zoom = 3
    window hide
    show black onlayer fade:
        xpos 1.0
        linear 1 xpos 0
    pause 1
    play sound "sfx/Train Map.ogg"
    show screen map(17, True) with dissolve
    pause
    show screen map(18, True) with dissolve
    pause
    show screen map(19, True) with dissolve
    pause
    show screen map(20, True) with dissolve
    pause
    hide screen map with dissolve
    pause 0.5

    hide black
    hide black onlayer foreground

    hide fre_shadow onlayer foreground
    hide fre onlayer foreground
    hide oph_shadow onlayer foreground
    hide oph onlayer foreground

    # show fre_shadow onlayer foreground
    # show fre normal onlayer foreground at fre_transform

    # show oph_shadow onlayer foreground
    # show oph normal onlayer foreground at oph_transform

    show black onlayer fade:
        xpos 0.0
        linear 1 xpos -1.0
    pause 1
    hide black onlayer fade

    # $ hide_sides = ['Freya', 'Ophelia']


    play env "sfx/Train.ogg" fadein 2.0
    ###Scene 7

    "I awaken to the familiar rattling of the tracks as the miles continue to pass by."

    "Flipping over, I find myself alone in the roomette. I take advantage of the space, stretching my arms and back."

    "I wonder where..."

    "My train of thought is interrupted as the door gently creaks open. Ophi gingerly steps inside, quietly closing the door again behind her."

    "Her slightly damp hair reveals where she's been."

    play music "music/Track 4.ogg" fadein 2.0
    
    fre "Hey, you."

    $ hide_sides = []

    fre smile "Hey, you."
    oph smile "Morning! I didn't wake you, did I?"

    fre "Nope, but I did just wake up a couple minutes ago."

    oph "Damn, that means you didn't have time to miss me."

    "A dose of Ophi's teasing first thing in the morning."

    "I wouldn't have it any other way."

    fre "I did have time, actually. Just barely, though."

    fre cheeky "But to be fair, I've had nothing {i}but{/i} time to miss you for the last ten years."

    oph cheeky "In that case, I'd better make sure you never miss me again!~"

    "Ophi smiles at me sweetly as she leans in to kiss me."

    fre embarrassed_b "I hope you don't mind morning breath."

    oph embarrassed "As long as I get kisses, it doesn't matter to me!"

    "I move to meet her lips, savoring the moment. Eventually, the kiss breaks off."

    fre smile "So, what's on the agenda today?"

    oph cheeky "We've got a whole day of tracks ahead of us, with home waiting for us at the end. God, I can't wait to sleep in my own bed again."

    fre embarrassed "Home, huh?"

    oph "Yup. Your home too, if you want it!"

    fre "So you keep saying."

    "I can't deny that it would be good to finally get the fuck outta Florida. And with things the way they are now... I can't really justify not staying in Portland."

    "I want to be with Ophi, and the only way that works is if I make the move."

    "And she's right—long term, I don't have a future in Jacksonville. I'll miss my family, but I know I won't miss them as much as I've missed Ophi these past ten years."

    "I have to do it."

    "For her."

    "For us."

    fre cheeky "And you're right."

    oph devious "Of course I'm right—"

    oph surprised "Wait, does that mean—!?"

    fre embarrassed_smile "I'll move to Portland."

    "Ophi's face lights up like I've never seen, which is saying something, considering how long we've known each other."

    "The genuine joy on her face is unmistakable, and her huge smile is contagious."

    oph laugh "Fuck yes!" with hpunch

    ###Ophi channeling her inner Karlach

    "She doesn't bother to fight back the tears welling in her eyes."

    fre smile "I just have one condition."

    oph disbelief "Don't you fucking dare ruin this for me right now, I swear to God—"

    fre "I get to be your girlfriend."

    oph laugh "UGH! You fucker, you had me worried for a second." with hpunch

    oph cheeky "For the record, I thought of you as my girlfriend from the moment you kissed me."

    fre embarrassed_b "I-I..."

    "Hearing her say those words after all these years of holding a candle for her... It's blissfully cathartic. My heart is full, my soul is happy."

    "It's like I'm getting a happy ending I never thought I could, that I never deserved."

    window hide
    show black onlayer fade:
        xpos 1.0
        linear 1 xpos 0
    pause 1

    hide bg2_closed onlayer foreground
    show bg1_open onlayer foreground

    show fre_shadow onlayer foreground
    show fre smile onlayer foreground at fre_transform
    show oph_shadow onlayer foreground
    show oph laugh onlayer foreground at oph_transform

    show black onlayer fade:
        xpos 0.0
        linear 1 xpos -1.0
    pause 1
    hide black onlayer fade

    $ hide_sides = ['Freya', 'Ophelia']

    oph "Another delicious meal on the train, holy shit!"

    fre "For real, I've had worse home cooked burgers before." 

    "I gaze out the window, taking in the view as we climb through the northern end of California's Central Valley."

    "A few more hours, and we'll be in Portland. It's weird to think about. After four days on the rails, it was starting to feel normal. I think I'll miss it."

    show oph e_smile onlayer foreground
    oph "Heya, Frey?"

    "The sweet call of Ophi's voice pulls my eyes back inside the train."

    oph "I'm curious, and now seems like a safe enough time to ask—was there ever anyone else?"

    show fre e_smile onlayer foreground
    fre "Nope. Ever since I've known what a crush is, what it is to love someone, it's always been you."

    show oph e_smile_b onlayer foreground
    "Ophi blushes and smiles adorably."

    oph "Well isn't that gay of you?"

    show fre e_smile_b onlayer foreground
    fre "Yes, yes it absolutely is."

    "My own curiosity is piqued. She's had other girlfriends of course. There were a handful in middle school and high school, most of which ended horribly."

    show fre e_smile onlayer foreground
    fre "What about you? After you left?"

    show oph smile onlayer foreground
    "Ophi considers the question for a minute." 

    oph "Yeah, there have definitely been a few since I've been in Oregon."

    oph "It is, like, the lesbian Mecca, though."

    oph "Let's see..."

    "She looks out the window, her eyes not really fixed on anything in particular."

    show oph disbelief_ec onlayer foreground
    oph "There were a few girls in my college days at U of O. None of them achieved girlfriend status though. Most of those bitches ended up being straight girls using the closest lesbian as an experiment for their own sexuality."

    show oph normal onlayer foreground
    oph "And then there were a handful of other girlfriends over the years since then. Only one of them was actually serious."

    show oph sad onlayer foreground
    oph "Naomi."

    oph "We were together in the band era. That relationship ended tragically, just like everything else did those days."

    show oph normal onlayer foreground
    oph "I've been single since then, I guess for two or three years. You know the rest."

    "Ophi looks back to me, a loving look of determination on her face."

    show oph cheeky onlayer foreground
    oph "With all of those relationships in hindsight, I {b}know{/b} that what we have is different. I don't know if I have the right words for it—stronger, more meaningful, whatever."

    oph "I know that whatever the future holds, I wanna face it with you by my side. Like it used to be, but more than that, like it always should have been."

    show oph e_smile onlayer foreground
    oph "I love you."

    "In spite of the seriousness of the moment, I can't resist the urge to tease her."

    show fre sad_ec onlayer foreground
    fre "Damn, that's crazy..."

    "I immediately regret my decision as Ophi's eyes flash with the fury of a thousand suns."

    show oph e_furious onlayer foreground
    oph "You better fuckin' say it back!"

    "In the end, I fold like paper, just as I always have."

    show fre e_happy_b onlayer foreground
    fre "I love you too, Ophi."

    fre "And I get what you're trying to say about us. I feel the same."

    fre "I know that if I had nothing left in the world, I'd still have you."

    oph "You're Goddamn right."

    fre "Knowing that we have a future together... I dunno."

    fre "It's like it flipped a switch in my head, like now I'm allowed to have hope again."

    show oph laugh onlayer foreground
    "Ophi snorts, laughing at my sappy recovery."

    oph "God, you're so fuckin' gay."

    show fre smile onlayer foreground
    fre "That's rich, coming from you, of all people."

    "She shrugs."

    show oph cheeky onlayer foreground
    oph "What can I say? I was born this way."

    ###End scene 7
    stop music fadeout 4.0
    stop env fadeout 4.0
    jump scene_8
