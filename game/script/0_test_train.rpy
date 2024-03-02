# define config.layers = ['background', 'master', 'transient', 'screens', 'overlay' ]

init python:
    import random
    class MovingImage(GameImage):
        def __init__(self, img, ypos, min_interval, max_interval, *args, **kwargs):
            self.ypos = ypos
            self.interval = (min_interval, max_interval)
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

transform cabin_transform_shake(intensity=1.0):
    anchor (0.5, 0.5) zoom 1.1 pos (0.5, 0.5)
    block:
        ease 0.2 offset (round(4*intensity), round(-3*intensity))
        ease 0.2 offset (round(2*intensity), 0)
        ease 0.2 offset (round(-1*intensity), round(1*intensity))
        ease 0.2 offset (0, round(-4*intensity))
        ease 0.2 offset (round(-1*intensity), round(2*intensity))
        ease 0.2 offset (round(3*intensity), 0)
        repeat

image test_movingobject1 = "test_movingobject"
image test_movingobject2 = "test_movingobject"

label test_train:
    $ train_speed = 1.0
    scene test_backlayer
    $ test_movingobject1 = MovingImage("test_movingobject1", ypos=0.25, min_interval=0, max_interval=5000)
    $ test_movingobject2 = MovingImage("test_movingobject2", ypos=0.3, min_interval=0, max_interval=5000)
    $ test_movingobject1.set_show(True)
    $ test_movingobject2.set_show(True)
    show test_frontlayer at cabin_transform_shake(1)
    show black:
        alpha 1.0
        linear 1 alpha 0.0
    pause 1
    hide black

    "Testing train"
    return