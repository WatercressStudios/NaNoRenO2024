init python:
    DefineImages("images/test")
    DefineImages("cgs")
    DefineImages("bgs")
    DefineImages("sprites", composite=True, overrideLayerOrder=['base', 'mouth', 'eyes', 'brow', 'blush', 'sweat',],
        zooms={'oph': 1.2, 'fre': 1.1}, sides=['oph', 'fre'])

    # Optional layers: blush, sweat
    # NOTE: optional layers don't need to be explicitly defined here because they can be added in script e.g. "show oph e_normal blush sweat"

    ##### OPHELIA #####
    # e_ = engaged pose, g_ = guarded pose, a_ = armrest pose
    MapEmote('oph normal', 'oph default base md_default ed_default brow_default')
    MapEmote('oph e_normal', 'oph engaged base md_default ed_default brow_default')
    MapEmote('oph g_normal', 'oph default guarded md_default ed_default brow_default')
    MapEmote('oph a_normal', 'oph default armrest md_default ed_default brow_default')


    ##### FREYA #####
    MapEmote('fre normal', 'fre base md_default ed_default brow_default')

