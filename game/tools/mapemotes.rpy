# Instructions:
# 1. Run game in Renpy and press Shift+S to bring up Dynamic Sprite Viewer
# 2. Create the emote and click on the preview window on the left to copy the code
# 3. Paste the MapEmote code in this file and give the new emote a sensible name
# 4. Use with `show mc normal`, or even have it inline with dialogue with `mc normal "Hello world."`

init python:
    DefineImages("images/test")
    DefineImages("cgs")
    DefineImages("bgs")
    DefineImages("sprites", composite=True, overrideLayerOrder=['base', 'mouth', 'eyes', 'brow', 'blush', 'sweat',],
        zooms={'oph': 1.2, 'fre': 1.1}, sides=['oph', 'fre'])

    # Optional layers: blush, sweat
    # NOTE: optional layers don't need to be explicitly defined here because they can be added in script e.g. "show oph e_normal blush sweat"

    ##### OPHELIA #####
    MapEmote('oph normal', 'oph default base md_default ed_default brow_default')
    

    ##### FREYA #####
    # j_ = with jacket
    MapEmote('fre normal', 'fre default basejacket md_default ed_default brow_default')
    MapEmote('fre j_normal', 'fre default jacket md_default ed_default brow_default')
