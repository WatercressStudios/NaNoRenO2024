define fre = Character("Freya", callback=speaker("fre"), image="fre")
define oph = Character("Ophelia", callback=speaker("oph"), image="oph")
define gra = Character("Grandma")
define n = Character(None, kind=nvl, what_color="#ffffff")
define f = Character("Freya", kind=nvl, what_color="#ffffff")
define o = Character("Ophelia", kind=nvl, what_color="#ffffff")
define g = Character("Grandma", kind=nvl, what_color="#ffffff")

default hide_sides = ['Freya', 'Ophelia']

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
