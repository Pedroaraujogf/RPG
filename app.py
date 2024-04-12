import flet as ft

def main(page: ft.Page):
    page.title = "Cadastro nome"

    txt_nome = ft.Text('Nome do personagem:')
    nome = ft.TextField(label="Digite o nome...", text_align=ft.TextAlign.LEFT)
    txt_classe_nivel = ft.Text('Classe e nivel de personagem:')
    classe_nivel = ft.TextField(label="Digite a classe e o nível...", text_align=ft.TextAlign.LEFT)
    txt_raça = ft.Text('Raça do personagem:')
    raça = ft.TextField(label="Digite a raça do personagem", text_align=ft.TextAlign.LEFT)
    btn_gerar = ft.ElevatedButton('Gerar')

    page.add(
        txt_nome,
        nome,
        txt_classe_nivel,
        classe_nivel,
        txt_raça,
        raça,
        btn_gerar,
   )

ft.app(target=main)



