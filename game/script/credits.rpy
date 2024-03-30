#
# Generate credits screen based on parameters below
#

init python:
    credits_duration = 40.0
    credits_height = 4900
    credits_content = [
        ( "Developed for Nanoreno 2024.",
            [
            ]
        ),
        ( "Creative Director",
            [
                "Wolf",
                "Val Sørseth",
            ]
        ),

        ( "Writing & Editing",
            [
                "Wolf",
                "Val Sørseth",
                "Zodai",
                "Jared Jensen",
            ]
        ),
        ( "Audio",
            [
                "Wolf",
                "Val Sørseth",
            ]
            # [
            #     (
            #         "Music Director",
            #         "Paul Robins",
            #     ),
            #     (
            #         "Music",
            #         "Paul Robins",
            #     ),
            #     # (
            #     #     "Sound Design",
            #     #     "Maddie Anderson",
            #     # ),
            #     # (
            #     #     "Sound Editing",
            #     #     "Paul Robins",
            #     #     "Tristan \"Wolf\" Barber",
            #     # ),
            # ]
        ),
        ( "Art",
            [
                (
                    "Art Director",
                    "Alison \"Draz\" Huang",
                ),
                (
                    "Sprite Art",
                    "Plate",
                ),
                (
                    "BG Art",
                    "Imagibeat Studio",
                ),
                (
                    "Concept Art",
                    "Shahar \"Voiderling\" Hod",
                ),
                (
                    "UI Design and Art",
                    "Brad \"EchoFrost\" Whitesell",
                ),
                (
                    "Logo Design",
                    "Imagibeat Studio",
                ),
            ]
        ),
        ( "Code",
            [
                (
                    "Coding Director",
                    "Sagittaeri",
                ),
                (
                    "UI",
                    "Brad \"EchoFrost\" Whitesell",
                ),
            ]
        ),

        ( "Ren'py Scripting",
            [
                "Wolf",
                "Val Sørseth",
                "Sagittaeri",
                "Brad \"EchoFrost\" Whitesell",
            ]
        ),
        ( "Marketing",
            [
                "Wolf",
                "Val Sørseth",
            ]
        ),
        ( "Special thanks to",
            [
                "Ren'py Tom",
                "The Lemmasoft Forum",
                "Our Fans",
                "Aniki",
                # "r/egg_irl",
                # "NASA Jet Propulsion Laboratory",
            ]
        ),
        ( "A thank you to all of our Patrons, including",
            [
                "Jonas Lee",
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
            null height 1500
            for title, names in credits_content:
                null height 50
                text title:
                    text_align 0.5
                    xalign 0.5
                    font gui.name_text_font
                    size 50
                    color gui.accent_color
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
            null height 5000
