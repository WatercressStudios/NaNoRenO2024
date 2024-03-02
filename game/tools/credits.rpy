#
# Generate credits screen based on parameters below
#

label credits:
    call screen credits
    return

init python:
    credits_duration = 30.0
    credits_height = 3600
    credits_content = [
        ( "Developed for Winter Visual Novel Jam 2023",
            [
            ]
        ),
        ( "Story",
            [
                "Kevin Bomer",
                "Dana Reynolds",
                "Hamadyne",
            ]
        ),
        ( "Music & Sound Design",
            [
                "Paul Robins",
            ]
        ),
        ( "Voice Director",
            [
                "Ariane Marchese",
            ]
        ),
        ( "Voice Acting",
            [
                (
                    "Aldebrand",
                    "Nickeem",
                ),
                (
                    "Herleva",
                    "Gina Leigh Smith",
                ),
                (
                    "Glacia",
                    "Sara Seferian",
                ),
                (
                    "Pierre",
                    "Corey Katona",
                ),
                (
                    "Herald",
                    "Nathan Morrison",
                ),
                (
                    "Tavernkeep",
                    "Andreas S",
                ),
                (
                    "Passerby 1",
                    "Gary Yeung",
                ),
                (
                    "Passerby 2",
                    "RaycherVO",
                ),
            ]
        ),
        ( "Voice Editing",
            [
                "Brad \"EchoFrost\" Whitesell",
            ]
        ),
        ( "Art",
            [
                (
                    "Sprite Art",
                    "Hamu",
                ),
                (
                    "Mural CG",
                    "KartP",
                ),
                (
                    "BG Art",
                    "Likhos",
                ),
                (
                    "Character Concept",
                    "Dana Reynolds",
                ),
                (
                    "UI Design & Art",
                    "Sagittaeri",
                ),
            ]
        ),
        ( "Programming",
            [
                "Sagittaeri",
                "Brad \"EchoFrost\" Whitesell",
            ]
        ),
        ( "Scripting & Animation",
            [
                "Kevin Bomer",
                "Sagittaeri",
            ]
        ),
        ( "Special thanks to",
            [
                "Ren'py Tom",
                "The Lemmasoft Forum",
                "Organizers of Winter Visual Novel Jam 2023",
            ]
        ),

    ]


transform credits_roll(duration, dest):
    on show:
        alpha 0 pos (0, 0)
        parallel:
            linear duration ypos -dest
        parallel:
            linear 1 alpha 1
    on hide:
        linear 1 alpha 0

screen credits():
    timer credits_duration-2 action [Hide("credits"), Return()]
    key "dismiss" action [Hide("credits"), Return()]
    frame at credits_roll(credits_duration, credits_height):
        background None
        xsize 1.0
        xalign 0
        padding (0,0)
        margin (0,0)
        vbox:
            spacing 10
            xalign 0.5
            null height 1000
            for title, names in credits_content:
                null height 50
                text title:
                    text_align 0.5
                    xalign 0.5
                    font gui.name_text_font
                    size 50
                    color "#71ddf8"
                for name in names:
                    if type(name) == type(()):
                        hbox:
                            xalign 0.5
                            frame:
                                background None
                                padding (0,0)
                                margin (0,0)
                                xsize 900
                                text name[0]:
                                    text_align 1.0
                                    xalign 1.0
                                    # font gui.name_text_font
                                    size 30
                                    color "#fff"
                            null width 50
                            frame:
                                background None
                                padding (0,0)
                                margin (0,0)
                                xsize 900
                                vbox:
                                    for n in name[1:]:
                                        text n:
                                            text_align 0.0
                                            xalign 0.0
                                            # font gui.name_text_font
                                            size 30
                                            color "#fff"
                    else:
                        text name:
                            text_align 0.5
                            xalign 0.5
                            # font gui.name_text_font
                            size 30
                            color "#fff"
            null height 4000
