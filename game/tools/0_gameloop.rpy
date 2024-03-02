init offset = -1

# Only one instantiation to this needed
default game_loop = GameLoop()

init python:
    import pygame, math

    # Inherit from this class
    class GameObject(object):
        # Called when the game object is created/instantiated. Note that usually this happens during the renpy init phase, so some renpy operations are not allowed
        def on_init(self, *args, **kwargs):
            pass

        # Called when GameLoop.start() is used. Usually used to initialise variables that will be used in the update loop
        def on_start(self):
            pass

        # Called when the GameLoop.stop() is used. Note that this is not called on destroy or disable
        def on_stop(self):
            pass

        # Called once per frame. If return True, restart the renpy interaction
        def on_update(self):
            return False
        
        # Called when set_enable(True) is used. This is not called on init or start
        def on_enable(self):
            pass
        
        # Called when set_enable(False) is used. This is not called on stop or destroy
        def on_disable(self):
            pass
        
        # Called when destroy() is called, or when player loads a save slot. Note: this is not called automatically if del is used, since GameLoop keeps a reference to all GameObjects
        def on_destroy(self):
            pass

        def __init__(self, *args, **kwargs):
            global game_loop
            if not self in game_loop.game_objects:
                game_loop.game_objects.append(self)
            if not self in game_loop.game_objects_enabled:
                game_loop.game_objects_enabled.append(self)
            self.on_init(*args, **kwargs)
            if game_loop.started:
                self.on_start()
                self.on_update()
        
        def destroy(self):
            global game_loop
            if self in game_loop.game_objects:
                game_loop.game_objects.remove(self)
            if self in game_loop.game_objects_enabled:
                game_loop.game_objects_enabled.remove(self)
            self.on_destroy()
        
        def set_enable(self, val):
            global game_loop
            if val is True and not self in game_loop.game_objects_enabled:
                game_loop.game_objects_enabled.append(self)
                self.on_enable()
                if game_loop.started:
                    self.on_update()
            elif val is False and self in game_loop.game_objects_enabled:
                game_loop.game_objects_enabled.remove(self)
                self.on_disable()

    class GameTransform(GameObject):
        ## TODO: implement hierarchal transform later. currently setting parents does nothing
        def __init__(self, trans=None, parent=None, *args, **kwargs):
            self.trans = trans
            if self.trans is None:
                self.trans = Transform()
            self.parent = parent
            if parent is not None:
                parent.children.append(self)
            self.children = []
            super().__init__(*args, **kwargs)

        def _transform_function(self, trans, st, at):
            self.trans = trans
            return 360000.0

        def _do_update(self):
            global game_loop
            if not self in game_loop.game_objects_enabled:
                return False
            restart_interaction = False
            if self.on_update() is True:
                restart_interaction = True
            for child in self.children:
                if child._do_update() is True:
                    restart_interaction = True
            return restart_interaction
        
        def get_transform(self):
            self.trans.function = self._transform_function
            return self.trans

        def set_parent(self, parent):
            if parent is self.parent:
                return
            if self.parent is not None:
                self.parent.children.remove(self)
            self.parent = parent
            if parent is not None:
                parent.children.append(self)

        def destroy(self):
            if self.parent is not None:
                self.parent.children.remove(self)
            self.parent = None
            super().destroy()

    class GameImage(GameTransform):
        def __init__(self, img, *args, **kwargs):
            self.img = img
            super().__init__(*args, **kwargs)

        def __str__(self):
            return "IMG:" + self.img

        def destroy(self):
            renpy.hide(self.img)
            super().destroy()

        def set_show(self, val, behind=None):
            if val is True:
                self.trans.function = self._transform_function
                renpy.show(self.img, at_list=[self.trans], behind=behind)
            else:
                renpy.hide(self.img)

        def is_completely_visible(self, check_x = True, check_y = True):
            bounds = renpy.get_image_bounds(self.img)
            if bounds is None:
                return False
            if check_x:
                if bounds[0] + bounds[2] > config.screen_width:
                    return False
                if bounds[0] < 0:
                    return False
            if check_y:
                if bounds[1] + bounds[3] > config.screen_height:
                    return False
                if bounds[1] < 0:
                    return False
            return True
        
        def is_partially_visible(self, check_x = True, check_y = True):
            bounds = renpy.get_image_bounds(self.img)
            if bounds is None:
                return False
            if check_x and not check_y:
                if bounds[0] >= 0 and bounds[0] <= config.screen_width:
                    return True
                if bounds[0] + bounds[2] >= 0 and bounds[0] + bounds[2] <= config.screen_width:
                    return True
            if check_y and not check_x:
                if bounds[1] >= 0 and bounds[1] <= config.screen_height:
                    return True
                if bounds[1] + bounds[3] >= 0 and bounds[1] + bounds[3] <= config.screen_height:
                    return True
            if check_x and check_y:
                if bounds[0] >= 0 and bounds[0] <= config.screen_width and bounds[1] >= 0 and bounds[1] <= config.screen_height:
                    return True
                if bounds[0] + bounds[2] >= 0 and bounds[0] + bounds[2] <= config.screen_width and bounds[1] + bounds[3] >= 0 and bounds[1] + bounds[3] <= config.screen_height:
                    return True
            return False
                
        def get_image(self):
            res = renpy.get_registered_image(self.img)
            while isinstance(res, ImageReference) or isinstance(res, LayeredImage):
                if isinstance(res, ImageReference):
                    res = renpy.get_registered_image(res.name)
                else:
                    res = renpy.get_registered_image(res.layers[0].image.name)
            return res

        def get_image_size(self):
            if self.size is None:
                self.size = renpy.image_size(self.get_image())
            if self.trans is None:
                self.trans = Transform()
            zoom = 1.0
            xzoom = 1.0
            yzoom = 1.0
            if self.trans.zoom is not None:
                zoom = self.trans.zoom
            if self.trans.xzoom is not None:
                xzoom = self.trans.xzoom
            if self.trans.yzoom is not None:
                yzoom = self.trans.yzoom
            return int(self.size[0] * zoom * xzoom), int(self.size[1] * zoom * yzoom)

    class GameLoop(object):
        # intentionally class variables so they don't get saved by renpy
        fps_counter_interval = 1.0
        max_fps = 0
    
        time_since_game_start = 0.0
        delta_time = 0
        current_fps = 0

        frames_count = 0
        last_update_fps = 0
        last_update_tick = 0

        def start():
            global game_loop
            if game_loop.started:
                return
            game_loop.started = True

            this_tick = pygame.time.get_ticks()
            GameLoop.time_since_game_start = this_tick / 1000.0
            GameLoop.delta_time = 0
            GameLoop.current_fps = 0
            GameLoop.frames_count = 0
            GameLoop.last_update_fps = this_tick
            GameLoop.last_update_tick = this_tick

            for go in game_loop.game_objects_enabled:
                go.on_start()
            GameLoop.main_loop()
            renpy.show_screen("GameLoopTicker")

        def stop():
            global game_loop
            if not game_loop.started:
                return
            game_loop.started = False

            renpy.hide_screen("GameLoopTicker")
            for go in game_loop.game_objects_enabled:
                go.on_stop()

        def main_loop():
            global game_loop

            if not game_loop.started:
                return

            this_tick = pygame.time.get_ticks()
            GameLoop.frames_count += 1
            if this_tick - GameLoop.last_update_fps > GameLoop.fps_counter_interval * 1000.0:
                GameLoop.current_fps = GameLoop.frames_count * 1000.0 / (this_tick - GameLoop.last_update_fps)
                GameLoop.frames_count = 0
                GameLoop.last_update_fps = this_tick

            GameLoop.delta_time = this_tick - GameLoop.last_update_tick
            GameLoop.last_update_tick = this_tick
            GameLoop.time_since_game_start = this_tick / 1000.0

            # if at least one returns true, then restart interaction
            restart_interaction = False
            for go in game_loop.game_objects_enabled:
                if isinstance(go, GameTransform):
                    if go.parent is None and go._do_update() is True:
                        restart_interaction = True
                else:
                    if go.on_update() is True:
                        restart_interaction = True

            if restart_interaction:
                renpy.restart_interaction()
            return
        
        def __init__(self):
            self.started = False
            self.game_objects = []
            self.game_objects_enabled = []
        
        # This is usually called when player loads a game which overrides the game_loop object
        def __del__(self):
            for go in self.game_objects:
                go.destroy()
            
            this_tick = pygame.time.get_ticks()
            GameLoop.time_since_game_start = this_tick / 1000.0
            GameLoop.delta_time = 0
            GameLoop.current_fps = 0
            GameLoop.frames_count = 0
            GameLoop.last_update_fps = this_tick
            GameLoop.last_update_tick = this_tick
    
    # needed to ensure game_loop exists during all init process, which default does not guarantee
    game_loop = GameLoop()

# Use GameLoop.start() to start running GameLoop updates
screen GameLoopTicker():
    if GameLoop.max_fps > 0:
        timer (1.0 / GameLoop.max_fps) repeat True action GameLoop.main_loop
    else:
        timer 0.001 repeat True action GameLoop.main_loop
