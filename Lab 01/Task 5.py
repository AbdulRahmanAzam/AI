# MADE WITH GPT WILL CHANGE LATER

import random
import time

# Define possible states
class HospitalEnvironment:
    def __init__(self):
        # Define the layout of the hospital
        self.rooms = {f"Room {i}": {"medicine": f"Medicine {i}", "scheduled_time": random.randint(1, 12)} for i in range(1, 6)}
        self.medicine_storage = {f"Medicine {i}": f"Medicine {i}" for i in range(1, 6)}  # Medicine stock
        self.staff_availability = ["Nurse A", "Nurse B", "Doctor C"]  # Available staff for alerts

    def get_patient_schedule(self):
        return self.rooms

    def get_available_staff(self):
        return self.staff_availability

# Define the delivery robot agent
class DeliveryRobot:
    def __init__(self, environment):
        self.environment = environment
        self.current_location = "Storage Area"
        self.delivered = []
        self.alerts = []
    
    def move(self, location):
        self.current_location = location
        print(f"Moving to {location}...")
    
    def pick_up_medicine(self, medicine):
        if medicine in self.environment.medicine_storage:
            print(f"Picking up {medicine} from storage.")
            return medicine
        else:
            print("Error: Medicine not available.")
            return None
    
    def scan_patient_id(self, room):
        print(f"Scanning patient ID in {room}...")
        return True  # Assume the scan is successful
    
    def deliver_medicine(self, medicine, room):
        print(f"Delivering {medicine} to {room}.")
        self.delivered.append((room, medicine))
        self.environment.rooms[room]["medicine"] = None
    
    def alert_staff(self, message):
        staff_member = random.choice(self.environment.get_available_staff())
        print(f"Alerting {staff_member}: {message}")
        self.alerts.append(f"Alerted {staff_member} with message: {message}")

    def check_if_goal_met(self, room, medicine):
        if self.environment.rooms[room]["medicine"] is None:
            print(f"Medicine {medicine} successfully delivered to {room}.")
            return True
        else:
            print(f"Delivery failed to {room}. Medicine not delivered.")
            return False

    def perform_task(self):
        patient_schedule = self.environment.get_patient_schedule()

        for room, details in patient_schedule.items():
            scheduled_time = details["scheduled_time"]
            medicine = details["medicine"]
            
            print(f"\nScheduled delivery for {room}: {medicine} at {scheduled_time} o'clock.")
            
            # Step 1: Move to medicine storage
            self.move("Medicine Storage")
            
            # Step 2: Pick up the medicine
            picked_medicine = self.pick_up_medicine(medicine)
            if not picked_medicine:
                continue  # If medicine is not available, skip the delivery task
            
            # Step 3: Move to patient room
            self.move(room)
            
            # Step 4: Scan patient ID
            if not self.scan_patient_id(room):
                print(f"Failed to scan patient ID for {room}. Aborting delivery.")
                continue
            
            # Step 5: Deliver medicine
            self.deliver_medicine(picked_medicine, room)
            
            # Step 6: Check if delivery goal is met
            if not self.check_if_goal_met(room, picked_medicine):
                self.alert_staff("Delivery issue occurred!")
                
            # Optional: Simulate a critical situation (for testing)
            if random.random() < 0.1:
                self.alert_staff(f"Critical issue at {room}: Need urgent assistance!")
            
            # Simulate time passing
            time.sleep(1)  # Simulating the time taken for each task
            
# Main simulation loop
def run_simulation():
    # Initialize the environment (hospital)
    hospital_env = HospitalEnvironment()
    
    # Initialize the delivery robot
    robot = DeliveryRobot(hospital_env)
    
    # Perform the delivery tasks
    robot.perform_task()

# Run the simulation
run_simulation()
