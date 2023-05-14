from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivymd.app import MDApp
from kivymd.uix.progressbar import MDProgressBar

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: '48dp'
    spacing: '48dp'

    GridLayout:
        cols: 2
        row_force_default: True
        row_default_height: '60dp'
        spacing: '12dp'
        padding: '12dp'

        MDProgressBar:
            id: pie1
            value: app.progress1
            max: 100
            type: 'pie'
            color: app.color1

        MDProgressBar:
            id: pie2
            value: app.progress2
            max: 100
            type: 'pie'
            color: app.color2

    GridLayout:
        cols: 2
        row_force_default: True
        row_default_height: '60dp'
        spacing: '12dp'
        padding: '12dp'

        MDProgressBar:
            id: pie3
            value: app.progress3
            max: 100
            type: 'pie'
            color: app.color3

        MDProgressBar:
            id: pie4
            value: app.progress4
            max: 100
            type: 'pie'
            color: app.color4
'''

class ChartApp(MDApp):
    progress1 = NumericProperty(80)
    progress2 = NumericProperty(60)
    progress3 = NumericProperty(40)
    progress4 = NumericProperty(20)
    color1 = [1, 0, 0, 1]  # red
    color2 = [0, 1, 0, 1]  # green
    color3 = [0, 0, 1, 1]  # blue
    color4 = [1, 1, 0, 1]  # yellow

    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    ChartApp().run()
