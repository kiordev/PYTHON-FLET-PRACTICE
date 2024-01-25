import flet as ft

def main(page: ft.Page):
    page.title = "Testing Login Form"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.DEEP_PURPLE_500
    
    # Header
    hello_text = ft.Text(
        "Welcome!", 
        size=40,
        color=ft.colors.DEEP_PURPLE_500,
        weight = ft.FontWeight.BOLD,
        )
    
    # Text Fields
    login = ft.TextField(
        label="Login",
        bgcolor=ft.colors.DEEP_PURPLE_300,
        width=280,
        border_radius=20,
        )
    
    password = ft.TextField(
        label="Password", 
        password=True, 
        bgcolor=ft.colors.DEEP_PURPLE_300,
        width=280,
        border_radius=20,
        )
    
    # Buttons
    entry_button = ft.ElevatedButton(
        "Sign In",
        bgcolor=ft.colors.DEEP_PURPLE_500,
        color=ft.colors.DEEP_PURPLE_100
        )
    
    # Main Column
    column = ft.Column(
        [hello_text, login, password, entry_button],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=40,
        )
    
    # Main Container
    main = ft.Container(
        content=column,
        height=400,
        width=300,
        border_radius=25,
        bgcolor=ft.colors.DEEP_PURPLE_100,
    )
    
    page.add(main)

ft.app(main)
