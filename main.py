import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            width=100,
            height=100,
            bgcolor="red"
        )
    )
    
    
ft.app(target=main)