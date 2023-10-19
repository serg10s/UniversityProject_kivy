from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

from db import get_all_info


class WindowManager(ScreenManager):
    pass


class Authentication(MDScreen):
    pass


class MDData(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
            # row_data=[
            #       [f"{i + + 1}", "info", "hehe", "Gojo", "0", "Satoro"] for i in range(0, 51) # work with db
            # ],
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

            ]
        )

        self.data_tables.bind(on_check_press=self.on_check_press)
        self.add_widget(self.data_tables)

    def on_row_press(self, instance_table, instance_row):
        pass

    def on_check_press(self, instance_table, current_row):
        self.selected_row_index = int(current_row[0]) - 1
        print(self.selected_row_index)
        self.selected_row = current_row

    def modify_and_highlight_row(self):
        if self.selected_row[4] == '0':
            self.data_tables.row_data[self.selected_row_index][4] = '1'
            print(self.data_tables.row_data[self.selected_row_index])
            self.data_tables.update_row_data(
                instance_data_table=self.data_tables, data=self.data_tables.row_data
            )


class MainApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "Orange"
        self.table_screen = MDData()

    def change_status(self, instance_button):
        self.table_screen.modify_and_highlight_row()

    def switch_to_second_screen(self):
        self.root.current = "data"

    def test(self, instance):
        email_text = self.root.ids.email_input.text
        password_text = self.root.ids.password_input.text
        print(email_text)
        print(password_text)


if __name__ == '__main__':
    MainApp().run()
