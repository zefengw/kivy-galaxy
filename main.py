from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    #called when we attach widget to app
    def on_parent(self, widget, parent):
        pass
    #called when screen size changes
    def on_size(self, *args):
        print(str(self.width) + " " + str(self.height))
        self.perspective_point_x = self.width/2
        self.perspective_point_y = self.height * 0.75
    #calls when perspective_point_x/perspective_point_y is changed
    def on_perspective_point_x(self, widget, value):
        print("PX: " + str(value))
    def on_perspective_point_y(self, widget, value):
        print("PY: " + str(value))

class GalaxyApp(App):
    pass

GalaxyApp().run()