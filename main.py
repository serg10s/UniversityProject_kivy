from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.datatables import MDDataTable
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
        self.change_button = MDRaisedButton(text="Change status", on_release=self.change_status)

        info_list = get_all_info()
        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            column_data=[
                ("Номер №", dp(30)),
                ("Назва продукту", dp(30)),
                ("Примітка до замовлення", dp(50)),
                ("Одиниця виміру", dp(30)),
                ("Кількість", dp(30)),
                ("Дата замовлення", dp(30)),
                ("Вид", dp(20)),
                ("Статус", dp(20)),
                ("Створювач замовлення", dp(50)),
            ],
            row_data=[
                [
                    f"{i + + 1}",
                    info_list[i][0],
                    info_list[i][1],
                    info_list[i][2],
                    info_list[i][3],
                    info_list[i][4],
                    info_list[i][5],
                    info_list[i][6],
                    info_list[i][7]] for i in range(len(info_list))

            ],
        )

        self.data_tables.bind(on_check_press=self.on_check_press)
        self.box_layout.add_widget(self.data_tables)
        self.box_layout.add_widget(self.change_button)

        self.add_widget(self.box_layout)

    def on_row_press(self, instance_table, instance_row):
        pass

    def on_check_press(self, instance_table, current_row):
        self.selected_row_index = int(current_row[0]) - 1
        print(self.selected_row_index)
        self.selected_row = current_row

    def modify_and_highlight_row(self):
        if self.selected_row[4] == '0':
            self.data_tables.row_data[self.selected_row_index][4] = '1'

            print(self.data_tables.row_data[self.selected_row_index])  # индекс таблицы

            self.data_tables.update_row_data(
                instance_data_table=self.data_tables, data=self.data_tables.row_data
            )

    def change_status(self, instance_button):
        self.data_tables.modify_and_highlight_row()


class MainApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"


if __name__ == '__main__':
    MainApp().run()
