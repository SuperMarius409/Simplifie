from kivy.app import App
from kivy.lang import Builder


kv = """
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import Gradient kivy_gradient.Gradient

RelativeLayout:
    BoxLayout
        id: box
        on_kv_post: print(get_color_from_hex("7A8AFA"))
        canvas:
            Rectangle:
                size: self.size
                pos: self.pos
                texture: Gradient.horizontal(get_color_from_hex("7A8AFA"), get_color_from_hex("4958DC"))
"""


class Test(App):
    def build(self):
        return Builder.load_string(kv)

    def on_stop(self):
        self.root.ids.box.export_to_png("gradient.png")


Test().run()