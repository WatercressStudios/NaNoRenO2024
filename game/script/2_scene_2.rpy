label scene_2:
    ######Map Transition - Jacksonville - Onboard map transition
    stop music fadeout 2.0
    # AUDIO: should we play an sfx while train map transitions from 1 station to another?

    $ map_zoom = 3
    window hide
    show black onlayer fade:
        xpos 1.0
        linear 1 xpos 0
    pause 1
    play sound "sfx/Train Map.ogg"
    show screen map(2, True) with dissolve
    pause
    show screen map(3, True) with dissolve
    pause
    hide screen map with dissolve
    pause 0.5

    show oph nervous onlayer foreground
    show fre j_sad_ec onlayer foreground
    camera foreground at camera_transform(shake=0.5, pos=(0.0, 0.66), zoom=2.01, duration=0.0)
    play music "music/Track 5.ogg" fadein 2.0
    show black onlayer fade:
        xpos 0.0
        linear 1 xpos -1.0
    pause 1
    hide black
    play env "sfx/Train.ogg" fadein 1.0
    $ test_movingpolesrandom.set_show(True)

    "So far, my plan hasn't been as successful as I hoped it'd be."

    camera foreground at camera_transform(shake=0.0, pos=(1.0, 0.7), zoom=2.01, duration=2.0)
    "It's been an hour and she's barely said a word. I know her more than anyone—even with her new face, I can tell she's terrified."

    camera foreground at camera_transform(shake=0.0, pos=(1.0, 0.7), zoom=2.01)
    $ test_movingpolesrandom.set_show(False)

    "...I have to wonder what's happened since I left. Grandma kept me updated, but there's only so much she could've done. Freya's more of a mystery than she ever has been, and that's deeply unsettling."

    "When we first sat down, it was like she had seen a ghost. I guess... I know I'm a ghost to her. So it makes sense. I outright stopped texting her. And I didn't stop for any good reason, either."

    camera foreground at camera_transform(shake=0.0, pos=(0.5, 0.5), zoom=1.01, duration=10.0)
    "Just distance."

    "Distraction."

    "Depression."

    "It's strange how loneliness can cause you to alienate yourself from those who would cure it most."

    "Still, that reaction hurt much more than I thought it would."

    "As kids up through high school, we were inseparable. Now, we might as well still be 3,000 miles away from each other."

    "Time for round two of \"Get Freya to open up to me.\". Operation: Bring Her Home won't succeed otherwise."

    "And I need her."

    "I just hope that she might need me, too."

    "With renewed resolve, I look up from my mindless social media swiping to find Freya doing the same."

    "This isn't what I wanted this to be. We're reconnecting after an entire decade. So why are we not taking advantage of this?"

    "No, this cannot continue."

    show oph smile onlayer foreground
    camera foreground at camera_transform(shake=0.0, pos=(0.0, 0.66), zoom=2.01, duration=1.0)
    oph "Yo, Freya, I have an idea. Shoot me down if you're not into it, but I think a bit of a social media detox could do us some good."

    oph "God knows it's all been a toxic shitshow for a while now, and hey. We could use the time to talk to each other."

    oph "Yeah?"

    show fre j_sad onlayer foreground
    camera foreground at camera_transform(shake=0.0, pos=(1.0, 0.7), zoom=2.01, duration=1.0)
    "Freya looks reluctant at first, giving furtive glances back to her phone, before relenting."

    show fre j_nervous onlayer foreground
    fre "You're right. Even though you've... we've..."

    "...Even though I haven't talked to her in so long? Even though I left her behind?"

    "She takes some time to mull over the words, avoiding what we both know she wants to say."

    fre "Regardless, it's not fair to anyone. I agree, let's put the phones down."

    fre "...Because I've missed you, Ophi, and I hope you've missed me, too."

    show oph cheeky onlayer foreground
    camera foreground at camera_transform(shake=0.0, pos=(0.0, 0.66), zoom=2.01, duration=1.0)
    pause 0.5
    oph "Hah! Of course I have, you have no idea!"

    camera foreground at camera_transform(shake=0.0, pos=(1.0, 0.7), zoom=2.01, duration=1.0)
    pause 1.0
    show fre j_sad onlayer foreground
    fre "Yeah... I don't."

    "Ouch."

    camera foreground at camera_transform(shake=0.0, pos=(0.5, 0.5), zoom=1.01, duration=2.0)
    show oph nervous onlayer foreground
    pause 1.8
    oph "Believe me, there's not a day that goes by without me thinking of you. You're my best friend, and you always will be!"

    oph "I had my reasons for not talking to you. Not the best reasons, but... I'll talk to you about it. Just not right now."

    show oph smile onlayer foreground
    oph "I want to enjoy our time together for a bit longer before things get heavy."

    oph "Just like we used to."

    "She opens her mouth to say something, then closes it, nodding. She knows that she fucked up, missing the funeral."

    "We both fucked up. I hate how relieved that makes me feel."

    show fre j_nervous onlayer foreground
    fre "That's fair."

    oph "So! Now that we've... temporarily? Cleared the air, there's something I've been dying to ask you."

    fre "Oh?"

    show oph devious onlayer foreground
    "I put on a devious smile."

    camera foreground at camera_transform(shake=0.0, pos=(0.0, 0.66), zoom=2.01, duration=0.0)
    oph "Ya single?"

    camera foreground at camera_transform(shake=0.0, pos=(1.0, 0.7), zoom=2.01, duration=0.0)
    show fre j_shocked_b onlayer foreground with hpunch
    "She coughs on her drink, the abrupt tonal shift taking her completely by surprise."

    fre "Good God Ophi, you really haven't changed one bit."

    camera foreground at camera_transform(shake=0.0, pos=(0.0, 0.66), zoom=2.01, duration=0.5)
    pause 0.5
    oph "Nope! Now answer the damned question!"

    camera foreground at camera_transform(shake=0.0, pos=(1.0, 0.7), zoom=2.01, duration=0.5)
    show fre j_embarrassed_smile onlayer foreground
    pause 0.5
    fre "Christ, give me a second, won't you?"

    "Gathering herself, she simply shakes her head."

    camera foreground at camera_transform(shake=0.0, pos=(0.0, 0.66), zoom=2.01, duration=1)
    pause 1
    oph "Ooooh?"

    camera foreground at camera_transform(shake=0.0, pos=(1.0, 0.7), zoom=2.01, duration=1)
    pause 1
    fre "I swear! Haven't been feeling it. The dating scene in Florida is messy enough, but for someone like me? No shot."

    show oph cheeky onlayer foreground
    camera foreground at camera_transform(shake=0.0, pos=(0.5, 0.5), zoom=1.01, duration=2)
    "I stop myself from smiling, laughing awkwardly instead."

    oph "Yeah, fuck Florida!"

    show fre j_nervous onlayer foreground
    fre "Fuck Florida."

    "I'm happy that she's single. Which... on the surface, sounds really shitty. But, I dunno. I always liked her, but I was never into her... when she wasn't \"her\" to me."

    "But now she is. And that makes me happy."

    camera foreground at camera_transform(shake=0.0, pos=(1.0, 0.7), zoom=2.01, duration=1)
    show fre j_cheeky onlayer foreground
    pause 1
    fre "So? You think you can get away with asking that and not returning the favor?"

    camera foreground at camera_transform(shake=0.0, pos=(0.0, 0.66), zoom=2.01, duration=1)
    show oph surprised_ec onlayer foreground
    pause 1
    oph "Oh, no, no one. I was far too busy for a while. And recently, well... I haven't been in the headspace for it."

    camera foreground at camera_transform(shake=0.0, pos=(1.0, 0.7), zoom=2.01, duration=1)
    pause 1
    fre "Hmm."

    camera foreground at camera_transform(shake=0.0, pos=(0.0, 0.66), zoom=2.01, duration=1)
    show oph surprised onlayer foreground with hpunch
    pause 1
    oph "Oh don't you \"hmm\" me!"

    camera foreground at camera_transform(shake=0.0, pos=(1.0, 0.7), zoom=2.01, duration=1)
    pause 1
    fre "Hmm~"

    camera foreground at camera_transform(shake=0.0, pos=(0.0, 0.66), zoom=2.01, duration=0.0)
    show oph surprised onlayer foreground with hpunch
    oph "Hey!"

    camera foreground at camera_transform(shake=0.0, pos=(0.5, 0.5), zoom=1.01, duration=1.0)
    show fre j_nervous onlayer foreground
    pause 1
    fre "Well, that's good to hear."

    "Wha?"

    oph "Wha?"

    "It's her turn to smile devilishly at me."

    show fre j_cheeky onlayer foreground
    fre "If you succeed in getting me to stay in Oregon, you're going to need a good wingwoman."

    fre "Not that I'm saying I will make the move. But if I do, you're going to need all the help you can get."

    oph "Hey!"

    show fre j_smile onlayer foreground
    fre "I mean, look at you. What are you, a bassist in an early 2000's alternative rock band?"

    oph "Oh don't you judge me Ms. \"Cottage isn't just a lifestyle\". And I was in a band! As the lead guitarist, no less!"

    fre "And whatever happened to that, then? Break the wrong girl's heart?"

    oph "Hah! No."

    show fre j_cheeky onlayer foreground
    "She arches her brow, knowing that under normal circumstances I wouldn't stop there. But, again, keep it light. Heavy can come later."

    "I quickly switch topics."

    show oph cheeky onlayer foreground
    oph "Anyway, I'm hungry, and we haven't checked out the dining car. How're you feeling?"

    "She shrugs."

    show fre j_smile onlayer foreground
    fre "I could go for some food right now, sure."

    "Getting up, I reach my hand out and pull her up beside me."

    hide oph_shadow onlayer foreground
    hide oph onlayer foreground with dissolve
    hide fre_shadow onlayer foreground
    hide fre onlayer foreground with dissolve

    "Even though we've had a few hang ups here and there, I'm willing to accept this truce of ours. We've lost too much time to waste it now."

    "I pull her along with me to enjoy our first meal of the trip."
    stop music fadeout 5.0
    stop env fadeout 3.0
    window hide
    show black onlayer fade:
        xpos 1.0
        linear 1 xpos 0
    pause 1
    play sound "sfx/Train Map.ogg"
    show screen map(4, True) with dissolve
    pause
    hide screen map with dissolve

    show black onlayer fade:
        xpos 0.0
        linear 1 xpos -1.0
    pause 1
    hide black

    ####If we ever want to expand the story, here's an opportunity to do so.

    ####Transition to windows closed.
    play env "sfx/Train.ogg" fadein 2.0
    "Arriving back to our room, I enjoy one last stretch before sitting back down."

    show oph_shadow onlayer foreground:
        alpha 0.0
        linear 0.5 alpha 1
    show oph cheeky onlayer foreground at oph_transform:
        alpha 0.0
        linear 0.5 alpha 1
    pause 0.5

    show fre_shadow onlayer foreground:
        alpha 0.0
        linear 0.5 alpha 1
    show fre j_smile onlayer foreground at fre_transform:
        alpha 0.0
        linear 0.5 alpha 1
    pause 0.5

    oph "You know, I didn't expect train food to be that good. I mean, my only point of reference was plane food, which is pretty fuckin' garbage."

    oph "Even when you're in first class, it just doesn't compare. Here? Really filling."

    show fre j_shocked onlayer foreground
    fre "You've flown first class?"

    show oph normal onlayer foreground
    oph "A bit, yeah. I never really liked it though, even if it's more comfy. Just feels wrong, ya know? I never felt like I belonged up there."

    show oph surprised_ec onlayer foreground
    oph "Felt like I was betraying my roots."

    show fre j_scoff onlayer foreground
    fre "We weren't exactly poor growing up, Ophi."

    show oph disbelief_ec onlayer foreground
    oph "But we weren't rich, either. Just solidly in the middle. I dunno, separating things by how much money you make? Kinda shitty."

    show fre j_yawn onlayer foreground
    "She yawns, nodding."

    show fre j_smile onlayer foreground
    fre "True."

    show oph smile onlayer foreground
    "Ah, yeah. We should get the beds ready, huh? I was having too much fun, I forgot we still have to sleep."

    show oph sad onlayer foreground
    "Shame we can't sleep together."

    fre "What's wrong?"

    oph "Hmm?"

    fre "You're frowning."

    show oph surprised_ec onlayer foreground
    oph "Oh! Nothing, nothing. Let's get the beds sorted. Top, or bottom?"

    show fre j_embarrassed_smile onlayer foreground
    fre "Umm..."

    oph "Of course you're bottom. I'll take the top."

    fre "Y-Yeah."

    hide oph_shadow onlayer foreground
    hide oph onlayer foreground with dissolve
    hide fre_shadow onlayer foreground
    hide fre onlayer foreground with dissolve

    "I look around the top bunk, trying to find a way to fold it down. It should be pretty simple..."

    "Finding a latch, I pull—no luck."

    "I look around, making sure that this is the right device, and yep. It is. Trains, especially in the south, are shittier than out west, so maybe I just need to give it more oomph."

    "I pull as hard as I can, bracing myself with my foot on the seat next to me. When that doesn't work, I put my entire weight on it—nothing."

    "Ahh, fuck."

    $ hide_sides = []

    oph sad "I think it's broken."

    fre "Should we get someone?"

    oph cheeky "Nah, it's late. I don't want to bother 'em with this. Let's just share!"

    "I promise, I pulled as hard as I could! I'm just lucky, I guess."

    fre j_nervous "Are you sure?"

    oph "Hey, we used to all the time back in the day."

    fre j_embarrassed_ec "Things are a little different now!" with hpunch

    oph "Yeah, now people can't claim we're some closeted het couple."

    fre "Our parents really did want us to get together."

    oph "Right? I never understood why some parents want their kids to hook up so much. And Christ, did it take them a long time to understand what gay meant."

    fre j_smile "I think they thought I was the gayer one."

    oph devious "Are you not?"

    fre "Well, {i}now{/i}, sure. But they were sure you'd end up with some boy."

    oph disbelief "Fuckin' gross."

    fre "Hey, guys aren't so bad."

    "I shake my head."

    oph "I'm not on that queer+ subscription."

    "She laughs, shaking her head right back."

    fre "No, you're not."

    oph cheeky "So! Let's sleep together!"

    "She rolls her eyes and helps me set up the bottom bunk."

    "This one unfolds rather easily, the two seats coming together into one bed. It's... well, going to be a very {i}cozy{/i} fit."

    "Freya looks to me, waiting for me to take the lead. I accept the side towards the wall, climbing in and fluffing out the blanket."

    "She climbs in next to me, trying to keep some distance between us, half hanging off the bed in the process."

    oph "Oh, c'mon, you can't sleep like that."

    "I reach out, pulling her closer."

    fre j_shocked "Ack!" with hpunch

    fre j_embarrassed_smile "Hey!" with hpunch

    oph surprised_ec "Just rip off the bandaid already! It's not like I have cooties."

    fre "Yeah, but..."

    oph "What, afraid of a little spooning with your dear old friend?"

    fre "No, of course not."

    "Seeing that as an invitation to pick on her more, I pull her as close as I can, arm wrapped around her stomach."

    oph "Of course not, eh?"

    "She grumbles a nonresponse."

    "I always loved picking on her. Glad to see that's just as fun as it used to be."

    "More fun, now, honestly."

    "Nustling my head into my pillow and against hers, her hair tickles my nose."

    "Freeing my hand, I gently push her hair away and reclaim my place around her waist."

    fre "How long are you going to torture me?"

    oph "Your hair smells good. What product do you use?"

    fre "Ophi!"

    oph "Yeah yeah, I gotta roll over anyway. But hey, if you ever wanna spoon {i}me{/i}, by all means."

    "She lays still, feigning sleep."

    "Not brave enough, eh?"

    "But I probably should lay off a bit. Fucking with her is fun, but I don't want to be overbearing."

    "I can't forget my goal. Bring her to a safer place. A place she can belong."

    "More than anything else, I need to bring her home."

    #Scene 2 End
    stop env fadeout 4.0
    jump scene_3