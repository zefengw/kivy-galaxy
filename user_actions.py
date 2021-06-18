
from kivy.uix.relativelayout import RelativeLayout


def keyboard_closed(self):
    #unbinds keyboard
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None

#Button is Pressed
def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':
        self.current_speed_x = self.speed_x
    elif keycode[1] == 'right':
        self.current_speed_x = -self.speed_x
    return True
#Button is released
def on_keyboard_up(self, keyboard, keycode):
    self.current_speed_x = 0
    return True
#tracks mouse pointer position when pressed
def on_touch_down(self, touch):
    # state_game_over = False
    # state_game_has_started = False
    if not self.state_game_over and self.state_game_has_started:
        if touch.x < self.width/2:
            self.current_speed_x = self.speed_x
        else:
            self.current_speed_x = -self.speed_x
    #relativelayout instead of mainwidget, then import the relative layout
    return super(RelativeLayout, self).on_touch_down(touch)
#sets speed to zero when mouse is released
def on_touch_up(self,touch):
    self.current_speed_x = 0
