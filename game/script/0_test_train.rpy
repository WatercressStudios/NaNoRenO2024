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

transform cabin_transform_shake(intensity=1.0):
    anchor (0.5, 0.5) zoom 1.01 pos (0.5, 0.5)
    block:
        ease 0.2 offset (round(4*intensity), round(-3*intensity))
        ease 0.2 offset (round(2*intensity), 0)
        ease 0.2 offset (round(-1*intensity), round(1*intensity))
        ease 0.2 offset (0, round(-4*intensity))
        ease 0.2 offset (round(-1*intensity), round(2*intensity))
        ease 0.2 offset (round(3*intensity), 0)
        repeat

image test_skybox_beige = "#FFFFDC"
image test_movingobject1 = "test_movingobject"
image test_movingobject2 = "test_movingobject"

label test_train:
    $ train_speed = 1.0
    scene test_skybox_beige
    camera foreground at cabin_transform_shake(0)

    $ test_movingpoles = MovingImage("test_movingobject1", ypos=0, min_interval=10000, max_interval=10000, init_xoffset=0, out_xoffset=None)
    $ test_movingpolesrandom = MovingImage("test_movingobject2", ypos=0, min_interval=0, max_interval=10000, init_xoffset=0, out_xoffset=None)
    $ test_movingtrain = MovingImage("test_movingtrain", ypos=0, min_interval=0, max_interval=0, init_xoffset=-500, out_xoffset=500)

    show test_frontlayer onlayer foreground
    show test_charleft onlayer foreground
    show test_charright onlayer foreground
    show black onlayer foreground:
        alpha 1.0
        linear 1 alpha 0.0
    pause 1
    hide black

    "No camera shake"

    camera foreground at cabin_transform_shake(1)
    "Camera shake at 1"

    camera foreground at cabin_transform_shake(2)
    "Camera shake at 2"

    camera foreground at cabin_transform_shake(0.5)
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
    "Larger shadows. Trains?"
    return