import flet as ft

class Contador:
    def __init__(self,page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.BLACK
        self.page.window_width = 350
        self.page.window_height = 450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = 'Contador App'
        self.main_page()

    def tasks_container(self):
        return ft.Container(
            height=self.page.height * 0.8,
            content = ft.Column(
                controls = [
                    ft.TextField(
                        hint_text='HP', label='Inimigo 1', width= 0.25
                    )
                ]
            )
        )

    def main_page(self):
        input_task = ft.TextField(hint_text = 'Digite os nomes', expand=True)

        input_bar = ft.Row(
            controls= [
                input_task,
                ft.FloatingActionButton(icon=ft.icons.ADD)
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