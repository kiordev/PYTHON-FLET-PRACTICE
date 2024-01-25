import flet as ft

def main(page: ft.Page):
    page.title = "SwordGame"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    
    armor_column = ft.Row(
        [
            ft.ElevatedButton(text="Sword"),
            ft.ElevatedButton(text="Axe"),
            ft.ElevatedButton(text="Arrow"),
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND, vertical_alignment=ft.CrossAxisAlignment.END
        )
    
    view = ft.Container(bgcolor=ft.colors.DEEP_PURPLE_300, height=600, width=350, content=armor_column )
    

    page.add(ft.SafeArea(view))
    
ft.app(target=main)