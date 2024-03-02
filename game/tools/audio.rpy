init python:
    renpy.music.register_channel("env", mixer="sfx", loop=True, stop_on_mute=True, tight=False, buffer_queue=True, movie=False)
    renpy.music.register_channel("env2", mixer="sfx", loop=True, stop_on_mute=True, tight=False, buffer_queue=True, movie=False)
    renpy.music.register_channel("sound2", mixer="sfx", loop=False, stop_on_mute=True, tight=False, buffer_queue=True, movie=False)

    voicefile_template = 'voice/{filename}-{charname}-{charlinenum}.ogg'
    # Ex. voice/scene_1-ald-44.ogg"
    #
    # {filename} the script file name
    # {filenum} the number in the script file name
    # {labelname} the name of the current label
    # {charname} the character short name
    # {filelinenum} the line number in the file
    # {labellinenum} the line number in the label
    # {charlinenum} the line number for the character in the file
    # {charlabellinenum} the line number for the character in the label
    #

    voices = {}
    voices['her'] = '#Herleva (Gina Leigh Smith)'
    voices['ald'] = '#Aldebrand (Nickeem)'
    voices['pie'] = '#Pierre (Corey Katona)'
    voices['gla'] = '#Glacia (Sara Seferian)'
    voices['hrd'] = '#Herald (DNathan Morrisont)'
    voices['tav'] = '#Tavernkeep (Andreas S)'
    voices['pb1'] = '#Passerby 1 (Gary Yeung)'
    voices['pb2'] = '#Passerby 2 (RaycherVO)'
    # To do VA parsing after filling the above:
    # 1. Run the game in Ren'Py
    # 2. Call the console with 'shift+o'
    # 3. Type 'ParseVoices()' or 'ParseVoices(comment_out_if_missing=True)' and hit enter
    #
    # Use the 'comment_out_if_missing=True' version if you want the script to comment out
    # the line automatically if the VA file doesn't exist
    #

define Battle_Theme = "music/Battle_Theme.ogg"
define Emotional = "music/Emotional.ogg"
define Nighfall = "music/Nighfall.ogg"
define Traveling = "music/Traveling.ogg"
define Upbeat = "music/Upbeat.ogg"
