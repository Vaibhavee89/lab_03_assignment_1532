class Process:
    def __init__(self, p_id, process_name, start_time, priority):
        self.p_id = p_id
        self.process_name = process_name
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def sort_by_p_id(self):
        self.processes.sort(key=lambda process: process.p_id)

    def sort_by_start_time(self):
        self.processes.sort(key=lambda process: process.start_time)

    def sort_by_priority(self):
        priority_order = {"Low": 1, "MID": 2, "High": 3}
        self.processes.sort(key=lambda process: priority_order[process.priority])

    def print_table(self):
        print("P_ID\tProcess\tStart Time\tPriority")
        for process in self.processes:
            print(
                f"{process.p_id}\t{process.process_name}\t{process.start_time}\t{process.priority}"
            )

# Create instances of Process
processes_data = [
    ("P1", "VSCode", 100, "MID"),
    ("P23", "Eclipse", 234, "MID"),
    ("P93", "Chrome", 189, "High"),
    ("P42", "JDK 9", 9, "High"),
    ("P9", "CMD", 7, "High"),
    ("P87", "NotePad", 23, "Low"),
]

flight_table = FlightTable()
for data in processes_data:
    process = Process(*data)
    flight_table.add_process(process)

# User input for sorting parameter
print("Sorting options:")
print("1. Sort by P_ID")
print("2. Sort by Start Time")
print("3. Sort by Priority")
choice = int(input("Enter your choice: "))

# Sort and print based on user's choice
if choice == 1:
    flight_table.sort_by_p_id()
elif choice == 2:
    flight_table.sort_by_start_time()
elif choice == 3:
    flight_table.sort_by_priority()
else:
    print("Invalid choice")

flight_table.print_table()
