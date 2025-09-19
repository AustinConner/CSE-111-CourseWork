import pytest
import task as task


def test_load_and_find():
    """
    Tests loading from a real CSV and finding a value.
    This test assumes "test_data.csv" exists.
    """
    loaded_tasks = task.load("test_data.csv")
    assert len(loaded_tasks) == 2, f"Expected 2 tasks. Seen {len(loaded_tasks)}."

    found_task = task.find(loaded_tasks, "task_101")
    assert found_task["title"] == "First Task from File", f"Task title: 'First Task from File' not found."

def test_create_and_find():
    """Tests creating a new task and then finding it."""
    tasks = [{
    "taskID": "task_90210",
    "title": "Organize Digital Files",
    "priority": 3,
    "location": "Home Office",
    "preferred_start_time": "09:30 AM",
    "time_estimate": "2h 30m",
    "max_end_date": "2025-07-28",
    "max_end_time": "04:00 PM",
    "complete": ""
}]

    task.create(
        task_list=tasks, taskID="task_3", title="Newly Created Task",
        priority=2, location="New Location", preferred_start_time="11:00 AM",
        time_estimate="30m", max_end_date="2025-12-03", max_end_time="07:00 PM"
        )

    assert len(tasks) == 2

    found_task = task.find(tasks, "task_3")
    title = found_task["title"]
    priority = found_task["priority"]
    loc = found_task["location"]
    pst = found_task["preferred_start_time"]
    te = found_task["time_estimate"]
    med = found_task["max_end_date"]
    met = found_task["max_end_time"]

    # Assert that every value matches its expected state
    assert title == "Newly Created Task", f"Expected 'Newly Created Task', but got: {title}"
    assert priority == 2, f"Expected priority of 2, but got: {priority}"
    assert loc == "New Location", f"Expected location 'New Location', but got: {loc}"
    assert pst == "11:00 AM", f"Expected preferred start time '11:00 AM', but got: {pst}"
    assert te == "30m", f"Expected time estimate '30m', but got: {te}"
    assert med == "2025-12-03", f"Expected max end date '2025-12-03', but got: {med}"
    assert met == "07:00 PM", f"Expected max end time '07:00 PM', but got: {met}"

def test_delete_and_find():
    """Tests deleting a task and confirming it cannot be found."""
    tasks = [{"taskID": "task_1", "title": "Task to Delete"}]
    task_to_delete = task.find(tasks, "task_1")

    task.delete(tasks, task_to_delete)
    assert len(tasks) == 0, "task didn't get deleted"

    refound_task = task.find(tasks, "task_1")
    assert refound_task is None, "task was found after deleting it."

def test_edit_and_find():
    """Tests editing a task"s values."""
    tasks = [{
    "taskID": "task_2",
    "title": "Make PyTests",
    "priority": 2,
    "location": "In Da Cloud",
    "preferred_start_time": "09:30 AM",
    "time_estimate": "2h 30m",
    "max_end_date": "2025-07-28",
    "max_end_time": "04:00 PM",
    "complete": ""
}]

    task.edit(tasks, "task_2", "title", "newTitle")
    assert task.find(tasks, "task_2")["title"] == "newTitle", "Edited title doesn't match what was expected."

    task.edit(tasks, "task_2", "priority", "5")
    assert task.find(tasks, "task_2")["priority"] == 5, "Edited priority does't match what was expected"
pytest.main(["-v", "--tb=line", "-rN", __file__])