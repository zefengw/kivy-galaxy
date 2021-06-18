#called when we attach widget to app
def on_parent(self, widget, parent):
    pass
#called when screen size changes
#update function will resize anyways

#calls when perspective_point_x/perspective_point_y is changed
def on_perspective_point_x(self, widget, value):
    # print("PX: " + str(value))
    pass
def on_perspective_point_y(self, widget, value):
    # print("PY: " + str(value))
    pass
def on_size(self, *args):
        # print(str(self.width) + " " + str(self.height))
        self.perspective_point_x = self.width/2
        self.perspective_point_y = self.height * 0.75
        # self.update_vertical_lines()
        # self.update_horizontal_lines()