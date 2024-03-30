define fre = Character("Freya")
define oph = Character("Ophelia")
define gra = Character("Grandma")
define n = Character(None, kind=nvl, what_color="#ffffff")
define f = Character("Freya", kind=nvl)
define o = Character("Ophelia", kind=nvl)
define g = Character("Grandma", kind=nvl)

label start:
    $ GameLoop.start()
    menu:
        "Start game normally":
            jump scene_1
        "Test moving train BG":
            jump test_train

return
