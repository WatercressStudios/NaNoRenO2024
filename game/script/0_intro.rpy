﻿define fre = Character("Freya")
define oph = Character("Ophelia")
define gra = Character("Grandma")

label start:
    $ GameLoop.start()
    menu:
        "Start game normally":
            jump scene_1
        "Test moving train BG":
            jump test_train

    return
