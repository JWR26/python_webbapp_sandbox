from nicegui import ui


# mockup of an "app portal" - a page with links to different application modules

class AppButton(ui.button):

    def __init__(self, in_maintenance: bool = False):
        super().__init__()
        with self:
            with ui.row():
                ui.image(r'D:\Users\Jonathan\Documents\python\webapp\logo_placeholder.png').classes('w-32')
                with ui.column():
                    ui.label('App 1!').style('font-size: 200%; font-weight: bold')
                    ui.label('This is the text discription for App 1!')
                    if in_maintenance:
                        ui.label('Currently Under Maintenance').style('color: #ff5815;')
            if in_maintenance:
                with ui.badge(color='#ff5815').props('floating'):
                    ui.icon('construction').classes('w-8')

ui.page_title('JWR Portal')

with ui.header().style(
    'background-color: #001a71;'
):
    ui.space()
    ui.label("Portal")
    ui.space()

with ui.row().classes('w-full justify-center'):
    ui.label("Bienvenu au Portail JWR26!")

with ui.column().classes('fixed-center'):
    AppButton()
    AppButton()
    AppButton(True)

with ui.footer().style(
    'background-color: #ffffff;'
):
    ui.image(r'D:\Users\Jonathan\Documents\python\webapp\logo_placeholder.png').classes('w-16')
    ui.label('Copyright JWR 26').style(
        'color: #000000;'
    )


ui.run()