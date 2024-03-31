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
    MapEmote('oph nervous', 'oph default guarded md_default ed_sad brow_default sweat')
    MapEmote('oph surprised', 'oph default guarded mdo_surprised ed_surprised brow_default blush sweat')
    MapEmote('oph surprised_ec', 'oph default guarded mdo_surprised ec_default brow_default blush sweat')
    MapEmote('oph nervous_b', 'oph default base md_default ed_sad brow_default sweat')
    MapEmote('oph disbelief', 'oph default base mdo_surprised ed_default brow_relaxed')
    MapEmote('oph disbelief_ec', 'oph default base mdo_surprised ec_default brow_relaxed sweat')
    MapEmote('oph smile', 'oph default base md_smile ed_default brow_default')
    MapEmote('oph smile_ar', 'oph default armrest md_smile ed_default brow_default')
    MapEmote('oph cheeky', 'oph default base md_smile ec_smile brow_default')
    MapEmote('oph sad', 'oph default guarded md_default ed_sad brow_sad sweat')
    MapEmote('oph happy', 'oph default base mdo_surprised ec_smile brow_default')



    ##### FREYA #####
    # j_ = with jacket
    MapEmote('fre normal', 'fre default base md_default ed_default brow_default')
    MapEmote('fre normal_ec', 'fre default base md_default ec_default brow_default')
    MapEmote('fre sad', 'fre default guarded md_sad ed_sad brow_sad sweat')
    MapEmote('fre sad_ec', 'fre default guarded md_sad ec_default brow_sad sweat')
    MapEmote('fre embarrassed', 'fre default guarded md_smile ed_sad brow_sad sweat')
    MapEmote('fre embarrassed_ec', 'fre default guarded md_smile ec_default brow_sad sweat')
    MapEmote('fre embarrassed_smile', 'fre default guarded md_smile ec_smile brow_sad blush sweat')
    MapEmote('fre scoff', 'fre default guarde mdo_surprised ec_default brow_relaxed')
    MapEmote('fre nervous', 'fre default guarded md_smile ed_default brow_sad')
    MapEmote('fre nervous_b', 'fre default base md_sad ed_sad brow_sad sweat')
    MapEmote('fre smile', 'fre default base md_smile ec_smile brow_relaxed')

    MapEmote('fre j_normal', 'fre default basejacket md_default ed_default brow_default')
    MapEmote('fre j_normal_ec', 'fre default basejacket md_default ec_default brow_default')
    MapEmote('fre j_sad', 'fre default guardedjacket md_sad ed_sad brow_sad sweat')
    MapEmote('fre j_sad_ec', 'fre default guardedjacket md_sad ec_default brow_sad sweat')
    MapEmote('fre j_embarrassed', 'fre default guardedjacket md_smile ed_sad brow_sad sweat')
    MapEmote('fre j_embarrassed_ec', 'fre default guardedjacket md_smile ec_default brow_sad sweat')
    MapEmote('fre j_embarrassed_smile', 'fre default guardedjacket md_smile ec_smile brow_sad blush sweat')
    MapEmote('fre j_scoff', 'fre default guardedjacket mdo_surprised ec_default brow_relaxed')
    MapEmote('fre j_nervous', 'fre default guardedjacket md_smile ed_default brow_sad')
    MapEmote('fre j_nervous_b', 'fre default basejacket md_sad ed_sad brow_sad sweat')
    MapEmote('fre j_smile', 'fre default basejacket md_smile ec_smile brow_relaxed')
