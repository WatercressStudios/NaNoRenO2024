define config.layers = ['background', 'master', 'foreground', 'transient', 'screens', 'overlay' ]

init python:
    import random
    class MovingImage(GameImage):
        def __init__(self, img, ypos, min_interval, max_interval, init_xoffset, out_xoffset, *args, **kwargs):
            self.ypos = ypos
            self.interval = (min_interval, max_interval)
            self.init_xoffset = init_xoffset
            if out_xoffset is None:
                self.out_xoffset = 0
            else:
                self.out_xoffset = out_xoffset
            super().__init__(img, *args, **kwargs)

        def on_start(self):
            print "start"
            self.trans.xpos = 1.0
            self.trans.ypos = self.ypos

        def on_update(self):
            # print "update"
            if not self.trans.xoffset:
                self.trans.xoffset = self.init_xoffset
            self.trans.xoffset -= int(GameLoop.delta_time * train_speed * 10)
            if self.trans.xoffset < self.out_xoffset and not self.is_partially_visible(check_x=True, check_y=False):
                rand = random.random()
                val = self.interval[0] + (self.interval[1]-self.interval[0]) * rand
                self.trans.xoffset = self.init_xoffset + int(val)
            return True
    train_speed = 1.0

    fre_pos = (1.0, 0.7)
    oph_pos = (0.0, 0.66)

image test_movingobject1 = "test_movingobject"
image test_movingobject2 = "test_movingobject"

image skybox_white = "#FFFFDC"
image skybox_yellow = "#ffdd88"
image skybox_dark = "#1c1065"

image oph_shadow = im.Flip("bgs/shadow.png", horizontal=True)
image fre_shadow = "shadow"

transform camera_transform_init():
    anchor (0.5, 0.5) zoom 1.01 pos (0.5, 0.5)

transform camera_transform(shake=1.0, pos=(0.5, 0.5), zoom=1.01, duration=0.5):
    ease duration pos pos zoom zoom
    block:
        ease 0.2 offset (round(4*shake), round(-3*shake))
        ease 0.2 offset (round(2*shake), 0)
        ease 0.2 offset (round(-1*shake), round(1*shake))
        ease 0.2 offset (0, round(-4*shake))
        ease 0.2 offset (round(-1*shake), round(2*shake))
        ease 0.2 offset (round(3*shake), 0)
        repeat

transform oph_transform:
    anchor (0.5, 0.5) pos (0.62, 0.68)
transform fre_transform:
    anchor (0.5, 0.5) pos (0.325, 0.71)

label test_train:
    $ train_speed = 1.0
    scene skybox_white
    camera foreground at camera_transform_init

    $ test_movingpoles = MovingImage("test_movingobject1", ypos=0, min_interval=10000, max_interval=10000, init_xoffset=0, out_xoffset=None)
    $ test_movingpolesrandom = MovingImage("test_movingobject2", ypos=0, min_interval=0, max_interval=10000, init_xoffset=0, out_xoffset=None)
    $ test_movingtrain = MovingImage("test_movingtrain", ypos=0, min_interval=0, max_interval=0, init_xoffset=-500, out_xoffset=500)

    show bg1_closed onlayer foreground

    # NOTE: Be sure to show oph shadow whenever her sprite is shown
    show oph_shadow onlayer foreground
    show oph a_normal onlayer foreground at oph_transform
    
    # NOTE: Be sure to show fre shadow whenever her sprite is shown
    show fre_shadow onlayer foreground
    show fre normal onlayer foreground at fre_transform
    
    show black onlayer foreground:
        alpha 1.0
        linear 1 alpha 0.0
    pause 1
    hide black

    "No camera shake"

    camera foreground at camera_transform(shake=1, pos=(0.5, 0.5), zoom=1.01)
    "Camera shake at 1"

    camera foreground at camera_transform(shake=2)
    "Camera shake at 2"

    camera foreground at camera_transform(shake=2, pos=(1.0, 0.7), zoom=2.01)
    "Pan to Freya"

    camera foreground at camera_transform(shake=2, pos=(0.0, 0.66), zoom=2.01)
    "Pan to Ophelia"

    camera foreground at camera_transform(shake=0.5)
    "Camera shake at 0.5"

    $ test_movingpoles.set_show(True)
    $ test_movingpolesrandom.set_show(False)
    $ test_movingtrain.set_show(False)
    "Poles moving at fixed intervals."

    $ test_movingpoles.set_show(False)
    $ test_movingpolesrandom.set_show(True)
    $ test_movingtrain.set_show(False)
    "Poles moving at random intervals. Trees?"

    $ test_movingpoles.set_show(False)
    $ test_movingpolesrandom.set_show(False)
    $ test_movingtrain.set_show(True)
    $ train_speed = 2.0
    "Larger shadows. Was supposed to be trains, but might be better fit for buildings?"
    return