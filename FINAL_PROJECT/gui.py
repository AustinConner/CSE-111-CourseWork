# YOU MIGHT NEED TO INSTALL PYWEBUI IN ADDITION TO NICEGUI! 
# I was prompted to install it when running the nicegui window natively (as a system window instead of a broswer window)
# If you don't want to install it, you could just comment and uncomment the specified lines at the bottom of the program.
from nicegui import ui
import task as task
import time
TASK_PATH = "tasks.csv"
tasks = task.load(TASK_PATH) 

# homepage title
ui.label("Task Buddy")

@ui.page("/edit/{task_id}")
def edit_task(task_id: str):
    current_tasks_list = task.load(TASK_PATH)
    original_task = task.find(current_tasks_list, task_id)

    # check to see if task was found
    if not original_task:
        ui.label(f'Task with ID {task_id} not found.').classes('text-h4')
        ui.button('Back', on_click=ui.navigate.back)
        return

    # Delete popup
    with ui.dialog() as delete_dialog, ui.card():
        ui.label('Are you sure you want to delete this task?')
        with ui.row().classes('w-full justify-center'):
            ui.button('Yes', on_click=lambda: delete_dialog.submit('Yes'), color='red')
            ui.button('No', on_click=lambda: delete_dialog.submit('No'))
    
    # Complete popup
    with ui.dialog() as complete_dialog, ui.card():
        ui.label('Are you sure you want to complete this task?')
        with ui.row().classes('w-full justify-center'):
            ui.button('Yes', on_click=lambda: complete_dialog.submit('Yes'), color='green')
            ui.button('No', on_click=lambda: complete_dialog.submit('No'))

    # wait for delete yes/no
    async def delete_conf():
        delete_dialog.open()
        result = await delete_dialog
        if result == "Yes":
            all_tasks = task.load(TASK_PATH)
            task_to_delete = task.find(all_tasks, task_id)
            if task_to_delete:
                task.delete(all_tasks, task_to_delete)
                task.save(all_tasks, TASK_PATH)
            ui.notify(f'Task {task_id} deleted.', type='positive')
            ui.navigate.to('/')

    # wait for complete
    async def complete_conf():
        complete_dialog.open()
        result = await complete_dialog
        if result == "Yes":
            all_tasks = task.load(TASK_PATH)
            task.edit(all_tasks, task_id, "complete", "Complete")
            task.save(all_tasks, TASK_PATH)
            ui.notify('Task marked as complete!', type='positive')
            ui.navigate.to('/')
    # ui elements
    ui.label(f"Editing Task ID: {task_id}").classes('text-h4')
    title = ui.input("Title", value=original_task.get("title"))
    priority = ui.number('Priority', value=original_task.get('priority'))
    location = ui.input('Location', value=original_task.get('location'))
    time_estimate = ui.input('Time Estimate', value=original_task.get('time_estimate'))
    date_input = ui.date(value=original_task.get('max_end_date')).props('label="Max End Date"')
    end_time_input = ui.input('Max End Time', value=original_task.get('max_end_time'))

    def save_changes(): # handles task editing
        all_tasks = task.load(TASK_PATH)
        task_to_update = task.find(all_tasks, task_id)
        
        new_values = {
            'title': title.value, 'priority': priority.value, 'location': location.value,
            'time_estimate': time_estimate.value, 'max_end_date': date_input.value,
            'max_end_time': end_time_input.value,
        }

        for key, new_value in new_values.items():
            if str(task_to_update.get(key)) != str(new_value):
                task.edit(all_tasks, task_id, key, new_value)
        
        task.save(all_tasks, TASK_PATH)
        ui.notify("Changes saved!", type='positive')
        ui.navigate.to('/')

    # --- BUTTONS ---
    with ui.row():
        ui.button('Save', on_click=save_changes)
        ui.button('Cancel', on_click=lambda: ui.navigate.to('/'))
        ui.button("DELETE", color="red", on_click=delete_conf)
        ui.button("COMPLETE!", color="green", on_click=complete_conf)

@ui.page("/")
def create_task_table():
    ui.label("Task Buddy").classes('text-h4')
    task_columns = [
        {"label":'Task ID', "field":"taskID"},
        {"label":'Title', "field":"title"},
        {"label":'Priority', "field":"priority"},
        {"label":'Location', "field":"location"},
        {"label":'Preferred Start Time', "field":"preferred_start_time"},
        {"label":'Time Estimate', "field":"time_estimate"},
        {"label":'Max End Date', "field":"max_end_date"},
        {"label":'Max End Time', "field":"max_end_time"},
        {"label": "Completion Status", "field":"complete"}
    ]

    # Create the table
    task_table = ui.table(columns=task_columns, rows=[], row_key='taskID').classes('w-full')
    task_table.on('rowClick', handle_row_click)
    ui.button('Add New Task', on_click=lambda: ui.navigate.to('/add'))


    def update_table_content():
        tasks = task.load(TASK_PATH) # Reload tasks every time the page is built/refreshed
        task_table.rows.clear() #clears the table so when it loads data in, it's not appended to the old.
        for item in tasks:
            task_to_import = {
                "taskID": item.get("taskID"),
                "title": item.get("title"),
                "priority": item.get("priority"),
                "location": item.get("location"),
                "preferred_start_time": item.get("preferred_start_time"),
                "time_estimate": item.get("time_estimate"),
                "max_end_date": item.get("max_end_date"),
                "max_end_time": item.get("max_end_time"),
                "complete": item.get("complete")
            }
            task_table.rows.append(task_to_import)
        task_table.update() 

    # Call the update function immediately when the page is opened
    update_table_content()

def handle_row_click(e):
    task_data = e.args[1]
    task_id = task_data['taskID']
    ui.navigate.to(f'/edit/{task_id}')
    

@ui.page("/add")
def add_task_page():
    global tasks
    ui.label("Add New Task").classes('text-h4')

    new_title = ui.input("Title")
    new_priority = ui.number('Priority', value=1)
    new_location = ui.input('Location')
    new_time_estimate = ui.input('Time Estimate')
    new_date_input = ui.date().props('label="Max End Date"')
    new_end_time_input = ui.input('Max End Time')
    new_preferred_start_time = ui.input('Preferred Start Time')

    def save_new_task():
        if not new_title.value:
            ui.notify("Title is required.", type='negative')
            return

        # Generate task title based off current machine time
        new_task_id = f"task_{int(time.time())}" 

        new_task_data = {
            'taskID': new_task_id,
            'title': new_title.value,
            'priority': new_priority.value,
            'location': new_location.value,
            'preferred_start_time': new_preferred_start_time.value,
            'time_estimate': new_time_estimate.value,
            'max_end_date': new_date_input.value,
            'max_end_time': new_end_time_input.value,
        }
        
        task.create(tasks, new_task_data["taskID"], new_task_data["title"], new_task_data["priority"], new_task_data["location"], new_task_data['preferred_start_time'], new_task_data["time_estimate"], new_task_data["max_end_date"], new_task_data['max_end_time'])
        task.save(tasks, TASK_PATH)
        ui.notify("New task added!", type='positive')
        ui.navigate.to('/')

    with ui.row():
        ui.button('Save New Task', on_click=save_new_task)
        ui.button('Cancel', on_click=lambda: ui.navigate.to('/'))

ui.run(native=True) # Comment this out if you DO NOT want to install pywebui 

#ui.run() # UNCOMMENT this if you DO NOT want to install pywebui