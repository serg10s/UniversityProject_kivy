from kivy.metrics import dp
from kivymd.app import MDApp

from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

from kivymd.uix.menu import MDDropdownMenu

from kivy.properties import StringProperty
from kivymd.uix.list import OneLineIconListItem

from db import get_all_info


class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class Authentication(MDScreen):

    def switch_to_second_screen(self, email, password, error_label):
        # Костыль
        email_right = 'a'
        password_right = 'a'
        if email == email_right and password == password_right:
            MDApp.get_running_app().root.current = "data"
        else:
            error_label.text = 'Error'
            error_label.theme_text_color = "Error"


class MDData(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        info_list = get_all_info()  # get info from database

        self.box_layout = MDBoxLayout(orientation="vertical", padding="5dp", spacing="24dp")
        # self.change_button = MDRaisedButton(text="Змінити статус", on_release=self.change_status)

        self.button_menu = MDRaisedButton(text="Змінити статус", on_release=self.menu_open)

        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            background_color_header="#f0f0f0",
            column_data=[
                ("[size=12]№[/size]", dp(20)),
                ("[size=12]Назва продукту[/size]", dp(20)),
                ("[size=12]Примітка до замовлення[/size]", dp(35)),
                ("[size=12]Одиниця виміру[/size]", dp(20)),
                ("[size=12]Кількість[/size]", dp(20)),
                ("[size=12]Дата замовлення[/size]", dp(20)),
                ("[size=12]Вид[/size]", dp(20)),
                ("[size=12]Статус[/size]", dp(20)),
                ("[size=12]Створювач замовлення[/size]", dp(35)),
            ],
            row_data=[
                [
                    f"[size=10]{i + + 1}[/size]",
                    f'[size=10]{info_list[i][0]}[/size]',  # здесь можна изменять как звет так и розмер текста
                    f'[size=10]{info_list[i][1]}[/size]',
                    f'[size=10]{info_list[i][2]}[/size]',
                    f'[size=10]{info_list[i][3]}[/size]',
                    f'[size=10]{info_list[i][4]}[/size]',
                    f'[size=10]{info_list[i][5]}[/size]',
                    f'[size=10]{info_list[i][6]}[/size]',
                    f'[size=10]{info_list[i][7]}[/size]'] for i in range(len(info_list))

            ],
        )

        self.data_tables.bind(on_check_press=self.on_check_press)
        self.box_layout.add_widget(self.data_tables)
        self.box_layout.add_widget(self.button_menu)
        self.add_widget(self.box_layout)

    def on_row_press(self, instance_table, instance_row):
        pass

    def on_check_press(self, instance_table, current_row):
        self.selected_row_index = int(current_row[0].split(']')[1].split('[')[0]) - 1
        print(self.selected_row_index)
        self.selected_row = current_row

    def change_status(self, instance_button):  # здесь я буду менять статус продукта
        pass

    def menu_open(self, instance):

        data = {'Статус 1': 'clock',
                'Статус 2': 'dots-horizontal-circle',
                'Статус 3': 'check-circle'}

        menu_items = [
            {
                "text": i[0],
                "viewclass": "IconListItem",
                "icon": i[1],
                "on_release": lambda x=f"{i[0]}": self.menu_callback(x),

            } for i in data.items()
        ]

        menu = MDDropdownMenu(
             caller=instance,
             items=menu_items,
             width_mult=3,
             max_height=dp(178),
             radius=[12, 12, 12, 12],
        )

        menu.open()

    def menu_callback(self, text_item):
        if text_item == 'Статус 1':
            print('Скоро тут буду функціонал')


class MainApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"


if __name__ == '__main__':
    MainApp().run()
