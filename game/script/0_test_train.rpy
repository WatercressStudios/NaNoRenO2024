# define config.layers = ['background', 'master', 'transient', 'screens', 'overlay' ]

init python:
    import random
    class MovingImage(GameImage):
        def __init__(self, img, ypos, interval, *args, **kwargs):
            self.ypos = ypos
            self.interval = interval
            super().__init__(img, *args, **kwargs)

        def on_start(self):
            print "start"
            self.trans.xpos = 0.0
            self.trans.ypos = self.ypos

        def on_update(self):
            # print "update"
            if not self.trans.xoffset:
                self.trans.xoffset = 0
            self.trans.xoffset += int(GameLoop.delta_time * train_speed * 4.0)
            if self.trans.xoffset > 0 and not self.is_partially_visible():
                rand = random.random()
                val = self.interval[0] + (self.interval[1]-self.interval[0]) * rand
                self.trans.xoffset = -int(val)
            return True
    train_speed = 1.0

label test_train:
    $ train_speed = 1.0
    scene test_backlayer
    $ test_movingobject1 = MovingImage("test_movingobject", 0.25, (0, 5000))
    $ test_movingobject1.set_show(True, behind="background")
    show test_frontlayer
    show black:
        alpha 1.0
        linear 0.5 alpha 0.0
    hide black

    "Testing train"
    return