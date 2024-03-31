define fre = Character("Freya", callback=speaker("fre"))
define oph = Character("Ophelia", callback=speaker("oph"))
define gra = Character("Grandma")
define n = Character(None, kind=nvl, what_color="#ffffff")
define f = Character("Freya", kind=nvl, what_color="#ffffff")
define o = Character("Ophelia", kind=nvl, what_color="#ffffff")
define g = Character("Grandma", kind=nvl, what_color="#ffffff")

label start:
    $ GameLoop.start()
    menu:
        "Start game normally":
            jump scene_1
        "Test moving train BG":
            jump test_train

return
