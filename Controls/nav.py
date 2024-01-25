import flet as ft

def main(page: ft.Page):
    page.title = "MyShop"
    
    def navigation(e):
        index = page.navigation_bar.selected_index
        page.clean()
        
        if index == 0: 
            page.add(ft.SafeArea(green_box))
            
        elif index == 1:
            page.add(ft.SafeArea(red_box))
            
        elif index == 2:
            page.add(ft.SafeArea(blue_box))
        
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.SHOP),
            ft.NavigationDestination(icon=ft.icons.MONEY),
            ft.NavigationDestination(icon=ft.icons.SHOPPING_BASKET)
        ], on_change=navigation
    )
    
    green_box = ft.Container(width=100, height=100, bgcolor='green')
    red_box = ft.Container(width=100, height=100, bgcolor='red')
    blue_box = ft.Container(width=100, height=100, bgcolor='blue')
    
    page.add(ft.SafeArea(green_box))

ft.app(target=main)