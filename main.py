from dataclasses import dataclass
from typing import List
from nicegui import app, ui

app.add_static_files('/img', 'img')

with ui.row().classes('w-full items-center'):
    ui.label('Hello NiceGUI!')
    result = ui.label().classes('mr-auto')
    with ui.button(icon='menu'):
        with ui.menu() as menu:
            ui.menu_item('Menu item 1', lambda: result.set_text('Selected item 1'))
            ui.menu_item('Menu item 2', lambda: result.set_text('Selected item 2'))
            ui.menu_item('Menu item 3 (keep open)',
                         lambda: result.set_text('Selected item 3'), auto_close=False)
            ui.separator()
            ui.menu_item('Close', menu.close)


button = ui.button(icon=r'img:/img\notification-2-line.png',on_click=lambda: badge.set_text(int(badge.text) + 1))

ui.button('update the badge...', on_click=lambda: badge.set_text(int(badge.text) + 1))

with button:
    badge = ui.badge('0', color='red').props('floating')


ui.mermaid('''
graph LR;
    A --> B;
    A --> C;
    C --> D;
''')

with ui.dialog() as dialog, ui.card().style('width: 360px'):
    ui.label('Enter some text...')
    ui.textarea(label='Comment', placeholder='enter comment here').style('width: 320px')
    ui.button('Close', on_click=dialog.close)

ui.button('Open a dialog', on_click=dialog.open)


@dataclass
class Contact:
    name: str
    number: str


contacts: List[Contact] = [
    Contact("David", "12345"),
    Contact("Jonathan", "312343"),
    Contact("Laure", "145498")
]

with ui.list().props('bordered separator'):
    ui.item_label('Contacts').props('header').classes('text-bold')
    ui.separator()
    for c in contacts:
        with ui.item():
            with ui.item_section().props('avatar'):
                ui.icon('person')
            with ui.item_section():
                ui.item_label(f'{c.name}')
                ui.item_label(f'{c.number}').props('caption')
            with ui.item_section().props('side'):
                ui.icon('chat')

ui.run()