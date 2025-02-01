class Backup:
    def __init__(self, name):
        self.name = name
        self.status = random.choice(["Completed", "Failed"])

class BackupAgent:
    def __init__(self, tasks):
        self.BackupTasks = tasks

    def scans(self):
        for task in self.BackupTasks:
            print(f"Task: {task.name} is {task.status}")

        print("\nNow retrying")

        for task in self.BackupTasks:
            if task.status == "Failed":
                task.status = "Completed"
                print(f"Task {task.name} retries and {task.status}")
        print("\n")


    def display(self):
        print("Updated status of tasks")
        for task in self.BackupTasks:
            print(f"Task: {task.name} is {task.status}")

        print("\n")


back = [Backup(f"Task {i+1}") for i in range(5)]

backAg = BackupAgent(back)
backAg.scans()
backAg.display()
