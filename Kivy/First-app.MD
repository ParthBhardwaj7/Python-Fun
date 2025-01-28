# Made App first with Kivy MD
```
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabs, MDTabsBase
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.boxlayout import MDBoxLayout


class Tab(MDScreen, MDTabsBase):
    """Class for creating tabs."""
    def __init__(self, title, icon, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.icon = icon
        self.add_widget(MDLabel(
            text=f"Welcome to the {title} tab!",
            halign="center",
            theme_text_color="Primary",
            font_style="H5"
        ))

class MyKivyMDApp(MDApp):
    def build(self):
        screen = MDScreen()

        # Tab Manager
        tabs = MDTabs()

        # Adding tabs with titles and icons
        tabs.add_widget(Tab(title="Home", icon="home"))
        tabs.add_widget(Tab(title="Settings", icon="settings"))
        tabs.add_widget(Tab(title="Profile", icon="account"))

        # Add the tabs to the screen
        screen.add_widget(tabs)

        # Floating Action Button
        fab = MDFloatingActionButton(
            icon="plus",
            md_bg_color=self.theme_cls.primary_color,
            pos_hint={"center_x": 0.9, "center_y": 0.1},
            on_release=self.fab_action
        )
        screen.add_widget(fab)

        return screen

    def fab_action(self, instance):
        """Action for FAB click"""
        print("Floating Action Button Clicked!")
        # You can add actions here like navigating, showing messages, etc.


if __name__ == "__main__":
'''
