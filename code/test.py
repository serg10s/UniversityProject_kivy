from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, MDList


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.dialog = None

        # Создаем список настроек
        self.settings_list = MDList()
        settings_data = [
            "Настройка 1",
            "Настройка 2",
            "Настройка 3"
        ]
        for setting in settings_data:
            item = OneLineListItem(text=setting)
            item.bind(on_release=self.show_dialog)
            self.settings_list.add_widget(item)

        # Создаем кнопку закрытия окна настроек
        close_button = MDFlatButton(text="Закрыть", on_release=self.close_settings)

        self.add_widget(self.settings_list)
        self.add_widget(close_button)

    # Метод для отображения диалогового окна при выборе настройки
    def show_dialog(self, instance):
        if not self.dialog:
            self.dialog = MDDialog(title="Выбранная настройка",
                                   text=instance.text,
                                   buttons=[
                                       MDFlatButton(
                                           text="ОК", on_release=self.close_dialog
                                       )
                                   ],
                                   )
        self.dialog.open()

    # Метод для закрытия диалогового окна
    def close_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()

    # Метод для закрытия окна настроек
    def close_settings(self, *args):
        self.manager.current = "main"


class MainApp(MDApp):
    def build(self):
        # Создаем экраны и менеджер экранов
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "300"
        self.theme_cls.theme_style = "Light"

        self.screen_manager = ScreenManager()
        self.settings_screen = SettingsScreen(name="settings")
        self.main_screen = Screen(name="main")

        # Добавляем кнопку для открытия окна настроек
        button = MDFlatButton(text="Открыть настройки", pos_hint={'center_x': 0.5, 'center_y': 0.5})
        button.bind(on_release=self.open_settings)

        self.main_screen.add_widget(button)
        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.settings_screen)

        return self.screen_manager

    # Метод для открытия окна настроек
    def open_settings(self, *args):
        self.screen_manager.current = "settings"


if __name__ == "__main__":
    MainApp().run()
