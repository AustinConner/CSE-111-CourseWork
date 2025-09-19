# Module that handles the creation, deletion, and editing of tasks.
import csv
import os
TASK_DATA_HEADERS = "taskID", "title", "priority", "location", "preferred_start_time", "time_estimate", "max_end_date", "max_end_time", "complete"

def load(filepath: str):
    """Loads the tasks from CSV file.

    Args:
        filename (str): The filepath for the saved tasks csv
    """
    try:
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, skipinitialspace=True)
            return list(reader)

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found creating a new task file...")

        directory = os.path.dirname(filepath)
        if directory:
            print(f"The '{directory}' directory doesn't exist. Making it.")
            os.makedirs(directory, exist_ok=True)

        header_items = TASK_DATA_HEADERS
        with open(filepath, 'w', newline="") as tasks:
            writer = csv.DictWriter(tasks, fieldnames=header_items)
            writer.writeheader()
            return []

def find(task_list, task_id):
    """Gets task info from main list using task id

    Args:
        task_list (list): list w/ dictonary entries for the current tasks
        task_id (str): ID of task
    """
    for task in task_list:
        if task.get("taskID") == task_id:
            return task
    return None

def create(task_list: list,
                taskID: str,
                title: str,
                priority: int,
                location: str,
                preferred_start_time: str,
                time_estimate: str,
                max_end_date: str,
                max_end_time: str):
    """Takes user information and creates task for the user.
    Args:
        task_list (list): list w/ dictonary entries for the current tasks
        taskID (str): ID for task
        title (str): name of the task
        priority (int): where the task ranks in imporance (1-5)
        preferred_start_time (str)(opt.): a good time to start the task
        time_estimate (str)(opt.): estimate length of time it will take to complete the task
        max_end_date (str)(opt.): the last date that the task can be completed
        max_end_time (str)(opt.): the last moment in time that the task can be completed 
    
    Returns:
        dict: task dictonary with the newly added task.
    """
    if find(task_list, taskID) is not None:
        """Searchs task list for task that corresponds with task ID. Returns results.

        Args:
            task_list (list): list w/ dictonary entries for the current tasks
            taskID (str): ID of the task
        """
        print(f"Error: Task ID '{taskID}' already exists. Cannot create a duplicate.")
        return # stop
    
    new_task = {} 
    new_task["taskID"] = taskID
    new_task["title"] = title
    new_task["priority"] = priority
    new_task["location"] = location
    new_task["preferred_start_time"] = preferred_start_time
    new_task["time_estimate"] = time_estimate
    new_task["max_end_date"] = max_end_date
    new_task["max_end_time"] = max_end_time
    new_task["complete"] = ""


    task_list.append(new_task)

    return task_list

def delete(task_list: list,
                task_to_delete: str):
    """Removes task from task list.
    Args:
        task_list (list): list w/ dictonary entries for the current tasks
        taskID (str): the unique ID for the task that you want to remove.
    """
    if task_to_delete in task_list:
        task_list.remove(task_to_delete)

def edit(task_list: list,
              taskID: str,
              item_to_edit: str,
              new_value: str):
    """Edits task in task list.

   Args:
        task_list (list): list w/ dictonary entries for the current tasks
        taskID (str): the unique for the task that you want to edit.
    """
    for task in task_list:
        if task["taskID"] == taskID:
            if item_to_edit == "priority":
                task[item_to_edit] = int(new_value)
                break
            else:
                task[item_to_edit] = new_value

def save(task_list: list,
              filepath: str):
    """Saves tasklist dictonary to tasklist csv file.

    Args:
        task_list (list): list w/ dictonary entries for the current tasks
        filepath (str): filepath of task.csv file
    """
    try:
        with open(filepath, 'w', newline="") as tasks_file:
            writer = csv.DictWriter(tasks_file, fieldnames=TASK_DATA_HEADERS)
            writer.writeheader()
            writer.writerows(task_list)
        print(f"\nTasks successfully saved to '{filepath}'.")
    except IOError as e:
        print(f"Error saving tasks to '{filepath}': {e}")

if __name__ == "__main__":
    print("oof")