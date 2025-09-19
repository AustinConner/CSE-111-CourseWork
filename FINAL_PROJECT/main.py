import task

TASK_PATH = "data/tasks.csv"

def main():
    tasks = task.load(TASK_PATH)
    print(tasks)
    task.create(tasks, "990", "Awesome task number 1", 4, "undeground", "10pm", "4hr", "12/22/22", "10pm")
    print(tasks)
    print()

        # Find and delete a task
    task_to_delete = task.find(tasks, "431")
    print(task_to_delete)
    # task.delete(tasks, task_to_delete)
    # print(f"\nAfter deleting task '26': {tasks}")
    # print(tasks)

    task.edit(tasks, "431", "priority", 5)
    print(tasks)
    # task.save(tasks, TASK_PATH)
main()