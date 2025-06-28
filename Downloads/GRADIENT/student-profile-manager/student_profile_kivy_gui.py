import threading
import uvicorn
import requests

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

Window.clearcolor = (1, 1, 1, 1)

class WhiteBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

def run_fastapi():
    import main
    uvicorn.run(main.app, host="127.0.0.1", port=8001, reload=False)

def show_popup(title, message):
    label = Label(
        text=message,
        color=(0, 0, 0, 1),
        font_size='18sp',
        halign='center',
        valign='middle'
    )
    label.bind(size=label.setter('text_size'))

    popup = Popup(
        title=title,
        content=label,
        size_hint=(None, None),
        size=(450, 300),
    )
    popup.open()

def show_scrollable_popup(title, content_text):
    layout = WhiteBoxLayout(orientation='vertical')
    scroll = ScrollView(size_hint=(1, 1))
    label = Label(
        text=content_text,
        size_hint_y=None,
        valign='top',
        color=(0, 0, 0, 1),
        font_size='16sp',
        halign='left',  # align text to the left
    )
    label.bind(
        texture_size=label.setter('size'),
        width=lambda instance, value: setattr(label, 'text_size', (label.width, None))
    )
    scroll.add_widget(label)
    layout.add_widget(scroll)
    popup = Popup(
        title=title,
        content=layout,
        size_hint=(0.95, 0.95),
    )
    popup.open()
class StudentEntryForm(WhiteBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)

        self.fields = {}
        grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        # Name
        self.add_field(grid, "Name", TextInput(multiline=False, size_hint_y=None, height=40))

        # Age
        self.add_field(grid, "Age", TextInput(multiline=False, size_hint_y=None, height=40, input_filter='int'))

        # Roll Number
        self.add_field(grid, "Roll Number", TextInput(multiline=False, size_hint_y=None, height=40))

        # Email
        self.add_field(grid, "Email", TextInput(multiline=False, size_hint_y=None, height=40))

        # Year - Spinner
        year_spinner = Spinner(
            text='Select Year',
            values=["B.Tech Year 1", "B.Tech Year 2", "B.Tech Year 3", "B.Tech Year 4", "MBA Year 1", "MBA Year 2"],
            size_hint_y=None,
            height=40
        )
        self.add_field(grid, "Year", year_spinner)

        # Branch - Spinner
        branch_spinner = Spinner(
            text='Select Branch',
            values=["CSE", "ECE", "EEE", "MECH", "CIVIL", "IT", "AI&DS", "MBA"],
            size_hint_y=None,
            height=40
        )
        self.add_field(grid, "Branch", branch_spinner)

        # Subject - Spinner
        subject_spinner = Spinner(
            text='Select Subject',
            values=["Python", "DBMS", "OS", "CN", "AI", "ML", "Maths", "Management"],
            size_hint_y=None,
            height=40
        )
        self.add_field(grid, "Subject", subject_spinner)

        # Grade - Spinner
        grade_spinner = Spinner(
            text='Select Grade',
            values=["O", "A+", "A", "B+", "B", "C", "P", "F"],
            size_hint_y=None,
            height=40
        )
        self.add_field(grid, "Grade", grade_spinner)

        self.add_widget(grid)

        add_btn = Button(
            text="Add Student",
            background_color=(0.3, 0.6, 0.9, 1),
            color=(1, 1, 1, 1),
            font_size='18sp',
            size_hint_y=None,
            height=50
        )
        add_btn.bind(on_press=self.submit_student)
        self.add_widget(add_btn)

    def add_field(self, grid, label_text, widget):
        label = Label(
            text=f"{label_text}:",
            size_hint_x=None,
            width=120,
            color=(0, 0, 0, 1),
            font_size='16sp',
            halign='right',
            valign='middle'
        )
        label.bind(size=label.setter('text_size'))
        grid.add_widget(label)
        grid.add_widget(widget)
        self.fields[label_text.lower()] = widget

    def submit_student(self, instance):
        try:
            name = self.fields["name"].text.strip()
            age_text = self.fields["age"].text.strip()
            roll_number = self.fields["roll number"].text.strip()
            email = self.fields["email"].text.strip()
            year_label = self.fields["year"].text.strip()  # original spinner text
            branch = self.fields["branch"].text.strip()
            subject = self.fields["subject"].text.strip()
            grade = self.fields["grade"].text.strip()

            # Validation
            if not name or not roll_number or not email or not year_label or not branch or not subject or not grade:
                show_popup("Error ⚠️", "All fields are required.")
                return
            if '@' not in email or '.' not in email:
                show_popup("Error ⚠️", "Invalid email format.")
                return
            age = int(age_text) if age_text.isdigit() else 18
            if age < 10 or age > 100:
                show_popup("Error ⚠️", "Age must be between 10 and 100.")
                return

            # Map year label to numeric value
            year_mapping = {
                "B.Tech Year 1": 1,
                "B.Tech Year 2": 2,
                "B.Tech Year 3": 3,
                "B.Tech Year 4": 4,
                "MBA Year 1": 1,
                "MBA Year 2": 2,
            }
            year_value = year_mapping.get(year_label, None)
            if year_value is None:
                show_popup("Error ⚠️", f"Invalid year selected: {year_label}")
                return

            student_data = {
                "name": name,
                "roll_number": roll_number,
                "email": email,
                "age": age,
                "year": year_value,  # send the numeric year
                "branch": branch,
                "subject": subject,
                "grade": grade,
            }

            print("🚀 Sending student data:", student_data)
            res = requests.post("http://127.0.0.1:8001/students/", json=student_data)
            if res.status_code == 200:
                show_popup("Success ✅", "Student added successfully.")
                for field in self.fields.values():
                    if isinstance(field, TextInput):
                        field.text = ""
                    elif isinstance(field, Spinner):
                        field.text = field.values[0] if field.values else "Select"
            else:
                show_popup("Error", f"{res.status_code}: {res.text}")

        except Exception as e:
            show_popup("Error ⚠️", str(e))

class ViewTab(WhiteBoxLayout):
    def __init__(self, endpoint, title, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        self.endpoint = endpoint
        self.title = title

        btn = Button(
            text=f"View {title}",
            font_size='20sp',
            size_hint_y=None,
            height=55,
            background_color=(0.75, 0.85, 1, 1),
            color=(0, 0, 0, 1)
        )
        btn.bind(on_press=self.view_data)
        self.add_widget(btn)

    def view_data(self, instance):
        try:
            res = requests.get(f"http://127.0.0.1:8001/{self.endpoint}/")
            if res.status_code == 200:
                response = res.json()
                if not response:
                    content = f"No {self.title} found."
                else:
                    content = f"{self.title} List:\n\n"
                    for idx, item in enumerate(response, 1):
                        content += f"{idx}. " + " | ".join(f"{k.capitalize()}: {v}" for k, v in item.items()) + "\n\n"
                show_scrollable_popup(f"{self.title}", content)
            else:
                show_popup("Error", f"{res.status_code}: {res.text}")

        except Exception as e:
            show_popup("Error ⚠️", str(e))

class StudentProfileManagerApp(App):
    def build(self):
        threading.Thread(target=run_fastapi, daemon=True).start()

        root = WhiteBoxLayout(orientation='vertical')

        title_label = Label(
            text='Student Profile Manager API – Gradient',
            size_hint_y=None,
            height=70,
            color=(0, 0, 0, 1),
            font_size='24sp',
            halign='center',
            valign='middle'
        )
        root.add_widget(title_label)

        tabs = TabbedPanel(do_default_tab=False)
        tabs.add_widget(TabbedPanelItem(text="Add Student", content=StudentEntryForm()))
        tabs.add_widget(TabbedPanelItem(text="View Students", content=ViewTab("students", "Students")))
        tabs.add_widget(TabbedPanelItem(text="View Subjects", content=ViewTab("subjects", "Subjects")))
        tabs.add_widget(TabbedPanelItem(text="View Grades", content=ViewTab("grades", "Grades")))
        tabs.add_widget(TabbedPanelItem(text="View Branches", content=ViewTab("branches", "Branches")))
        tabs.add_widget(TabbedPanelItem(text="View Years", content=ViewTab("years", "Years")))

        root.add_widget(tabs)
        return root

if __name__ == '__main__':
    StudentProfileManagerApp().run()
