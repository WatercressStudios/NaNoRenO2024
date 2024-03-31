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
    # e_ = engaged
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
    MapEmote('oph devious', 'oph default guarded mdo_happy ed_anger brow_default')
    MapEmote('oph laugh', 'oph default base mdo_happy ec_smile brow_default')

    MapEmote('oph e_normal', 'oph engaged base md_default ed_default brow_default')
    MapEmote('oph e_smile', 'oph engaged base md_smile ed_default brow_default')
    MapEmote('oph e_devious', 'oph engaged base mdo_happy ed_anger brow_default')
    MapEmote('oph e_devious_relaxed', 'oph engaged base mdo_happy ed_anger brow_relaxed')
    MapEmote('oph e_devious_smile', 'oph engaged base md_smile ed_anger brow_default')
    MapEmote('oph e_embarrassed_p', 'oph engaged base md_pout ed_default brow_sad blush sweat')
    MapEmote('oph e_sigh', 'oph engaged base mdo_default ec_default brow_default')
    MapEmote('oph e_sad', 'oph engaged base mdo_default ed_sad brow_sad')
    MapEmote('oph e_sad_mo', 'oph engaged base mdo_default ed_sad brow_sad')
    MapEmote('oph e_surprised', 'oph engaged base mdo_surprised ed_surprised brow_default')
    MapEmote('oph e_laugh', 'oph engaged base mdo_happy ec_smile brow_default')



    ##### FREYA #####
    # j_ = with jacket
    # e_ = engaged
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
    MapEmote('fre shocked', 'fre default armrest mdo_surprised ed_surprised brow_relaxed sweat')
    MapEmote('fre cheeky', 'fre default guarded md_smile ed_anger brow_default')
    MapEmote('fre yawn', 'fre default basejacket mdo_default ec_default brow_relaxed')
    MapEmote('fre pout', 'fre default guarded md_pout ed_unimpressed brow_relaxed')

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
    MapEmote('fre j_shocked', 'fre default armrestjacket mdo_surprised ed_surprised brow_relaxed sweat')
    MapEmote('fre j_cheeky', 'fre default guardedjacket md_smile ed_anger brow_default')
    MapEmote('fre j_yawn', 'fre default basejacket mdo_default ec_default brow_relaxed')

    MapEmote('fre e_normal', 'fre engaged base md_default ed_default brow_default')
    MapEmote('fre e_smile', 'fre engaged base md_smile ed_default brow_relaxed')
    MapEmote('fre e_smile_ec', 'fre engaged base md_smile ec_smile brow_relaxed')
    MapEmote('fre e_happy', 'fre engaged base mdo_happy ec_smile brow_relaxed')
    MapEmote('fre e_happy_b', 'fre engaged base mdo_happy ec_smile brow_relaxed blush')
    MapEmote('fre e_sad', 'fre engaged base md_default ed_sad brow_sad')
    MapEmote('fre e_sad_mo', 'fre engaged base mdo_default ed_sad brow_sad')
    MapEmote('fre e_sad_smile', 'fre engaged base md_smile ed_sad brow_sad')
    MapEmote('fre e_devious', 'fre engaged base md_smile ed_anger brow_default')
