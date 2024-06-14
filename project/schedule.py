from collections import deque
from datetime import datetime

class Client:
    def __init__(self, client_id, name, contact_info):
        self.client_id = client_id
        self.name = name
        self.contact_info = contact_info

    def __repr__(self):
        return f"Client(ID: {self.client_id}, Name: {self.name}, Contact: {self.contact_info})"

class Appointment:
    def __init__(self, appointment_id, client, appointment_time):
        self.appointment_id = appointment_id
        self.client = client
        self.appointment_time = appointment_time

    def __repr__(self):
        return (f"Appointment(ID: {self.appointment_id}, "
                f"Client: {self.client.name}, "
                f"Time: {self.appointment_time.strftime('%Y-%m-%d %H:%M')})")

class Schedule:
    def __init__(self):
        self.clients = {}
        self.appointments = {}
        self.appointment_requests = deque()
        self.next_appointment_id = 1

    def add_client(self, client):
        self.clients[client.client_id] = client

    def schedule_appointment(self, client_id, appointment_date, appointment_hour, appointment_minute):
        client = self.clients.get(client_id)
        if not client:
            return "Client not found."
        for appointment in self.appointments.values():
            if appointment.appointment_time.date() == appointment_time.date():
                if appointment.appointment_time.hour == appointment_time.hour and appointment.appointment_time.minute == appointment_time.minute:
                    return "Appointment slot on the same day and time is already booked. Please choose another time."
        appointment_time = datetime(appointment_date.year, appointment_date.month, appointment_date.day, appointment_hour, appointment_minute)
        appointment = Appointment(self.next_appointment_id, client, appointment_time)
        self.appointments[self.next_appointment_id] = appointment
        self.next_appointment_id += 1
        return f"Appointment scheduled successfully. Appointment ID: {appointment.appointment_id}"

    def view_appointments(self):
        return [repr(appointment) for appointment in self.appointments.values()]

    def update_appointment(self, appointment_id, new_time=None, new_client_id=None):
        appointment = self.appointments.get(appointment_id)
        if not appointment:
            return "Appointment not found."
        if new_time:
            appointment.appointment_time = new_time
        if new_client_id:
            new_client = self.clients.get(new_client_id)
            if not new_client:
                return "New client not found."
            appointment.client = new_client
        return "Appointment updated successfully."

    def cancel_appointment(self, appointment_id):
        appointment = self.appointments.pop(appointment_id, None)
        if not appointment:
            return "Appointment not found."
        return "Appointment cancelled successfully."
