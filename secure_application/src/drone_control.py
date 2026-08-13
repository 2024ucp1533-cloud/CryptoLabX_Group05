import os

logged_in = False
drone_logs = []


def login():
    global logged_in

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "drone123":
        logged_in = True
        print("Login successful!")
    else:
        print("Invalid credentials.")


def upload_waypoint():
    waypoint = input("Enter waypoint (latitude,longitude): ")

    # Improper input validation
    drone_logs.append("Waypoint uploaded: " + waypoint)
    print("Waypoint uploaded successfully.")


def execute_mission():
    command = input("Enter mission command: ")

    # Vulnerable command execution
    os.system(command)

    drone_logs.append("Mission executed: " + command)
    print("Mission execution completed.")


def view_telemetry():
    print("\n--- Drone Telemetry ---")
    print("Altitude: 120 meters")
    print("Speed: 35 km/h")
    print("Battery: 78%")
    print("GPS: Active")


def view_logs():
    print("\n--- Drone Logs ---")

    if not drone_logs:
        print("No logs available.")
    else:
        for log in drone_logs:
            print(log)


def main():
    while True:
        print("\n===== DRONE CONTROL SYSTEM =====")
        print("1. Login")
        print("2. Upload Waypoint")
        print("3. Execute Mission")
        print("4. View Telemetry")
        print("5. View Logs")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            upload_waypoint()
        elif choice == "3":
            execute_mission()
        elif choice == "4":
            view_telemetry()
        elif choice == "5":
            view_logs()
        elif choice == "6":
            print("Exiting Drone Control System.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
