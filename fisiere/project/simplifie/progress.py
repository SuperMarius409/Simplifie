# Import Kivy modules
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.lang import Builder


# Define the main screen
class MainScreen(Screen):
    notes_layout = ObjectProperty(None)

    # Method to add a note to the notes_layout
    def add_note(self, note):
        note_label = Label(text=note, size_hint_y=None, height=40)
        note_button = Button(text="Edit", size_hint_x=None, width=80)
        note_button.bind(on_release=self.edit_note)
        note_layout = BoxLayout(size_hint_y=None, height=40)
        note_layout.add_widget(note_label)
        note_layout.add_widget(note_button)
        self.notes_layout.add_widget(note_layout)

    # Method to go to the editor screen
    def goto_editor(self):
        self.manager.current = "editor"

    # Method to edit a note
    def edit_note(self, instance):
        note_layout = instance.parent
        note_label = note_layout.children[0]
        note_text = note_label.text
        editor_screen = self.manager.get_screen("editor")
        editor_screen.load_note_text(note_text)
        self.manager.current = "editor"


# Define the editor screen
class EditorScreen(Screen):
    note_input = ObjectProperty(None)

    # Method to load a note into the note_input
    def load_note_text(self, note_text):
        self.note_input.text = note_text

    # Method to save a note and go back to the main screen
    def save_note_and_goto_main(self):
        note_text = self.note_input.text.strip()
        if note_text:
            main_screen = self.manager.get_screen("main")
            main_screen.add_note(note_text)
        self.note_input.text = ""
        self.manager.current = "main"


# Define the screen manager
class NoteApp(ScreenManager):
    pass


# Load the .kv file as a string
kv_string = '''
<MainScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Notes"
            size_hint_y: None
            height: 40
        ScrollView:
            BoxLayout:
                id: notes_layout
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
        Button:
            text: "Add Note"
            size_hint_y: None
            height: 40
            on_release: root.goto_editor()

<EditorScreen>:
    BoxLayout:
        orientation: "vertical"
        TextInput:
            id: note_input
            size_hint_y: None
            height: 200
        Button:
            text: "Save"
            size_hint_y: None
            height: 40
            on_release: root.save_note_and_goto_main()
'''

# Load the .kv string
Builder.load_string(kv_string)


# Define the app class
class MyApp(App):
    def build(self):
        return NoteApp()


# Run the app
if __name__ == "__main__":
    MyApp().run()
