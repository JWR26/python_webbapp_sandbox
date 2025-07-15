from datetime import datetime
from nicegui import ui


class Action:

    def __init__(self, action: str, actor:str, date: datetime.date):
        self._action = action
        self._actor = actor
        self._date = date
        self._is_complete = False
        self._comments =[]

    def add_comment(self, comment: str) -> None:
        self._comments.append(comment)


class CreateActionDialogue(ui.dialog):

    def __init__(self):
        super().__init__()
        with self, ui.card().style('with: 360px'):
            self.text = ui.textarea(
                label='Enter action'
            ).style(
                'width: 320px'
            ).props(
                'clearable'
            )
            self.responsible = ui.input(
                label='Responsible',
                autocomplete=['Jonathan', 'Laure', 'Sarah', 'William']
            )
            with ui.input('Date') as self.date:
                with ui.menu().props('no-parent-event') as menu:
                    with ui.date().bind_value(self.date):
                        with ui.row().classes('justify-end'):
                            ui.button('Close', on_click=menu.close).props('flat')
                with self.date.add_slot('append'):
                    ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
            self.multiple_actions = ui.switch(text='Add another action...')
            with ui.row():
                ui.button('Create Action', on_click=self.create_action)
                ui.button('Close', on_click=self.close)

    def create_action(self):
        print("Creating an action")
        Action(
            self.text.value,
            self.responsible.value,
            self.date.value,
        )
        if self.multiple_actions.value:
            # clear the dialogue for a new entry
            self.text.set_value('')
            self.responsible.set_value('')
            self.date.set_value('')
        else:
            self.close()


class ViewActionDialogue(ui.dialog):

    def __init__(self):
        super().__init__()


class ActionListItem(ui.item):

    def __init__(self):
        super().__init__()


class ActionList(ui.list):

    def __init__(self):
        super().__init__()

    def update(self):
        self.clear()



ui.label("Action Manager").props('heading')
with ActionList() as action_list:
    with ActionListItem():
        with ui.item_section().props('avatar'):
            ui.icon('person')
        with ui.item_section():
            ui.item_label('Nice Guy')
            ui.item_label('name').props('caption')
        with ui.item_section().props('side'):
            ui.icon('chat')
ui.button("Create Action", on_click=lambda: CreateActionDialogue())

ui.run()