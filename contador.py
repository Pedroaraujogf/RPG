import flet as ft
import sqlite3

class Contador:
    def __init__(self,page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.BLACK
        self.page.window_width = 350
        self.page.window_height = 450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = 'Contador App'
        self.task = ""
        self.db_execute('CREATE TABLE IF NOT EXISTS tasks(name, status)')
        self.results = self.db_execute('SELECT * FROM tasks')
        self.main_page()
    
    def db_execute(sel, query, params = []):
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()
            return cur.fetchall()

    def tasks_container(self):
        return ft.Container(
            height=self.page.height * 0.8,
            content = ft.Column(
                controls = [
                    ft.TextField(
                        # Revisar esssa parte, estão funcionando mas tem erros.
                        hint_text='HP', label=res[0], value = True if res[1] == 'complete' else False)
                    for res in self.results if res
                ]
            )
        )
    
    def set_value(self, e):
        self.task = e.control.value
        print(self.task)

    def add(self, e, input_task):
        name = self.task
        status = 'incomplete'

        if name:
            self.db_execute(query='INSERT INTO tasks VALUES(?,?)', params=[name, status])
            input_task.value=''
            self.results = self.db_execute('SELECT * FROM tasks')
            self.update_task_list()
    
    def update_task_list(self):
        tasks = self.tasks_container()
        self.page.controls.pop()
        self.page.add(tasks)
        self.page.updade()

    def main_page(self):
        input_task = ft.TextField(hint_text = 'Digite os nomes', expand=True, on_change=self.set_value)

        input_bar = ft.Row(
            controls= [
                input_task,
                ft.FloatingActionButton(icon=ft.icons.ADD,
                                        on_click=lambda e: self.add(e, input_task)
                )
            ]
        )

        tabs = ft.Tabs(
            selected_index=0,
            tabs=[
                ft.Tab(text='HP'),
                ft.Tab(text='Iniciativa'),
                ft.Tab(text='Caídos')
            ]
        )

        tasks = self.tasks_container()

        

        self.page.add(input_bar, tabs, tasks)

ft.app(target = Contador)