
from typing import List
from nicegui import ui


tasks: List[str] = ["Task 1", "Task 2", "Task 3"]

def get_task_row(label: str) -> ui.row:
    with ui.row() as row:
        ui.label(str)
        ui.separator()
        ui.button('Done')
    return row

with ui.card() as card:
    ui.label("To Do List:")
    for t in tasks:
        row = get_task_row(t)
        row.move(card)

with ui.dialog() as dialog, ui.card().style('width: 360px'):
    text = ui.textarea(
        label= 'Enter the task to complete',
        placeholder='describe task here'
        ).style(
            'width: 320px'
        ).props(
            'clearable'
        )
    def add_task() -> None:
        tasks.append(text.value)
        new_task = get_task_row(text.value)
        new_task.move(card)
        dialog.close()
        print(tasks)
    
    with ui.row():
        ui.button('Add', on_click=add_task)
        ui.button('Close', on_click=dialog.close)



ui.button("Add Task", on_click=dialog.open)


ui.run()

