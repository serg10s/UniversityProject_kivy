from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

from db import get_all_info


class Authentication(MDScreen):
    def switch_to_second_screen(self, email, password):
        # Костыль
        email_right = 'a'
        password_right = 'a'
        if email == email_right and password == password_right:
            MDApp.get_running_app().root.current = "data"  
        else: 
            label = MDLabel(text='Error',  theme_text_color="Error", halign='center', valign='middle', font_size=18)

            self.add_widget(label)


class MDData(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.box_layout = MDBoxLayout(orientation="vertical", padding="10dp", spacing="24dp")
        # self.change_button = MDRaisedButton(text="Змінити статус", on_release=self.change_status)
        data = {
            '1': 'clock',
            '2': 'dots-horizontal-circle',
            '3': 'check-circle',
        }
        fab_speed_dial = MDFloatingActionButtonSpeedDial(
            data=data,
            root_button_anim=True,
            hint_animation=True,
            right_pad=True,
            size_hint=(1, .1)
        )

        info_list = get_all_info()
        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,

            column_data=[
                ("[size=14]№[/size]", dp(15)),
                ("[size=12]Назва продукту[/size]", dp(20)),
                ("[size=12]Примітка до замовлення[/size]", dp(30)),
                ("[size=12]Одиниця виміру[/size]", dp(20)),
                ("[size=12]Кількість[/size]", dp(20)),
                ("[size=12]Дата замовлення[/size]", dp(20)),
                ("[size=12]Вид[/size]", dp(20)),
                ("[size=12]Статус[/size]", dp(20)),
                ("[size=12]Створювач замовлення[/size]", dp(30)),
            ],
            row_data=[
                [
                    f"[size=12]{i + + 1}[/size]",
                    f'[size=12]{info_list[i][0]}[/size]',  # здесь можна изменять как звет так и розмер текста
                    f'[size=12]{info_list[i][1]}[/size]',
                    f'[size=12]{info_list[i][2]}[/size]',
                    f'[size=12]{info_list[i][3]}[/size]',
                    f'[size=12]{info_list[i][4]}[/size]',
                    f'[size=12]{info_list[i][5]}[/size]',
                    f'[size=12]{info_list[i][6]}[/size]',
                    f'[size=12]{info_list[i][7]}[/size]'] for i in range(len(info_list))

            ],
        )



        self.data_tables.bind(on_check_press=self.on_check_press)
        self.box_layout.add_widget(self.data_tables)
        self.box_layout.add_widget(fab_speed_dial)
        # self.box_layout.add_widget(fab_speed_dial)
        # self.box_layout.add_widget(self.change_button)

        self.add_widget(self.box_layout)

    def on_row_press(self, instance_table, instance_row):
        pass

    def on_check_press(self, instance_table, current_row):
        self.selected_row_index = int(current_row[0]) - 1
        print(self.selected_row_index)
        self.selected_row = current_row

    def change_status(self, instance_button):
        pass


class MainApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"


if __name__ == '__main__':
    MainApp().run()
