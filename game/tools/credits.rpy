#
# Generate credits screen based on parameters below
#

label credits:
    call screen credits
    return

init python:
    credits_duration = 30.0
    credits_height = 5000
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
                "Churlatte",
            ]
        ),
        ( "Audio",
            [
                "Paul Robins",
            ]
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
                (
                    "Additional Art",
                    "Alison \"Draz\" Huang",
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
                "Sagittaeri",
                "Paul Robins",
                "Brad \"EchoFrost\" Whitesell",
            ]
        ),
        ( "Quality Assurance",
            [
                "Churlatte",
                "Brad \"EchoFrost\" Whitesell",
                "Wolf",
                "Val Sørseth",
                "Sagittaeri",
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
            null height 1000
            for title, names in credits_content:
                null height 50
                text title:
                    text_align 0.5
                    xalign 0.5
                    font gui.name_text_font
                    size 50
                    color "#2879bb"
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
                                    color "#ccd1d5"
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
                                            color "#ccd1d5"
                    else:
                        text name:
                            text_align 0.5
                            xalign 0.5
                            # font gui.name_text_font
                            size 30
                            color "#ccd1d5"
            null height 4000
