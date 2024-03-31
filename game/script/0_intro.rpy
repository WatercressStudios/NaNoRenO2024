define fre = Character("Freya", callback=speaker("fre"), image="fre")
define oph = Character("Ophelia", callback=speaker("oph"), image="oph")
define gra = Character("Grandma")
define n = Character(None, kind=nvl, what_color="#ffffff")
define f = Character("Freya", kind=nvl, what_color="#ffffff")
define o = Character("Ophelia", kind=nvl, what_color="#ffffff")
define g = Character("Grandma", kind=nvl, what_color="#ffffff")

default hide_sides = ['Freya', 'Ophelia']

label splashscreen:
    scene black
    show splash1 with Dissolve(1):
        align (0.5, 0.5) zoom 0.2
    pause 2
    hide splash1 with Dissolve(1)
    show splash2 with Dissolve(1):
        align (0.5, 0.5) zoom 0.6
    pause 2
    hide splash2 with Dissolve(1)
    show logo with Dissolve(1):
        align (0.5, 0.5) zoom 0.1
    pause 2
    hide logo with Dissolve(1)
    return

label start:
    $ GameLoop.start()
    $ hide_sides = ['Freya', 'Ophelia']
    jump scene_1
    # menu:
    #     "Start game normally":
    #         jump scene_1
    #     "Test moving train BG":
    #         jump test_train

return
