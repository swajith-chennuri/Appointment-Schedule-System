import os
from datetime import datetime
from userauth import UserAuth
from schedule import Schedule, Client

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause_and_clear():
    input("Press Enter to continue...")
    clear_screen()

def userlogin():
    user_auth = UserAuth()
    schedule = Schedule()

    while True:
        clear_screen()
        print("Welcome to the Appointment Scheduling System")
        print("\n1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            result = user_auth.login(username, password)
            print(result)
            pause_and_clear()
            if result == "Login successful.":
                user_menu(schedule)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(user_auth.add_user(username, password))
            pause_and_clear()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            pause_and_clear()

def user_menu(schedule):
    while True:
        clear_screen()
        print("\n1. Add Client")
        print("2. Schedule Appointment")
        print("3. View Appointments")
        print("4. Update Appointment")
        print("5. Cancel Appointment")
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                client_id = int(input("Enter Client ID: "))
                name = input("Enter Client Name: ")
                contact_info = input("Enter Contact Info: ")
                client = Client(client_id, name, contact_info)
                schedule.add_client(client)
                print("Client added successfully.")
            except Exception as e:
                print(f"An error occurred: {e}")
            pause_and_clear()
        elif choice == '2':
            try:
                client_id = int(input("Enter Client ID: "))
                appointment_date_str = input("Enter Appointment Date (YYYY-MM-DD): ")
                appointment_hour = int(input("Enter Appointment Hour (0-23): "))
                appointment_minute = int(input("Enter Appointment Minute (0-59): "))
                appointment_date = datetime.strptime(appointment_date_str, "%Y-%m-%d")
                print(schedule.schedule_appointment(client_id, appointment_date, appointment_hour, appointment_minute))
            except Exception as e:
                print(f"An error occurred: {e}")
            pause_and_clear()
        elif choice == '3':
            try:
                appointments = schedule.view_appointments()
                for appointment in appointments:
                    print(appointment)
            except Exception as e:
                print(f"An error occurred: {e}")
            pause_and_clear()
        elif choice == '4':
            try:
                appointment_id = int(input("Enter Appointment ID: "))
                new_time_str = input("Enter New Appointment Time (YYYY-MM-DD HH:MM) or press Enter to skip: ")
                new_time = datetime.strptime(new_time_str, "%Y-%m-%d %H:%M") if new_time_str else None
                new_client_id = input("Enter New Client ID or press Enter to skip: ")
                new_client_id = int(new_client_id) if new_client_id else None
                print(schedule.update_appointment(appointment_id, new_time, new_client_id))
            except Exception as e:
                print(f"An error occurred: {e}")
            pause_and_clear()
        elif choice == '5':
            try:
                appointment_id = int(input("Enter Appointment ID: "))
                print(schedule.cancel_appointment(appointment_id))
            except Exception as e:
                print(f"An error occurred: {e}")
            pause_and_clear()
        elif choice == '6':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
            pause_and_clear()
