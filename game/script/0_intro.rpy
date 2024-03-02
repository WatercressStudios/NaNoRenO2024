define e = Character("Eileen")

label start:
    $ GameLoop.start()
    menu:
        "Test moving train BG":
            jump test_train

    return
