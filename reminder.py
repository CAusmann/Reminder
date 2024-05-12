#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import datetime

# Global variable to store the alert ID
alert_id = None

def set_reminder():
    """Function to set a reminder."""
    global alert_id

    # Check if a reminder is already set
    if alert_id:
        messagebox.showinfo("Reminder", "Reminder already set!")
        return

    subject = subject_entry.get()
    reminder_time = time_entry.get()

    try:
        # Reminder time
        hour, minute = map(int, reminder_time.split(':'))
        now = datetime.datetime.now()
        reminder_datetime = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

        # Calculate time difference
        delta = (reminder_datetime - now).total_seconds()
        if delta <= 0:
            raise ValueError("Reminder time should be in the future")

        # Confirmation message
        messagebox.showinfo("Success", "Reminder set successfully!")

        # Wait until reminder time
        alert_id = root.after(int(delta * 1000), lambda: show_reminder(subject))

    except ValueError as e:
        messagebox.showerror("Error", str(e))

def show_reminder(subject):
    """Function to display the reminder alert."""
    global alert_id 

    # Display reminder alert and ask if the user wants to extend the reminder time
    reminder_text = f"Reminder: {subject}"
    extend_time = messagebox.askyesno("Reminder", reminder_text + "\n\nWould you like to extend the reminder time?")
    
    if extend_time:
        extend_reminder_window(datetime.datetime.now())
    else:
        alert_id = None

def extend_reminder_window(reminder_time):
    """Function to display the window for extending the reminder."""
    def close_window():
        root.destroy()

    root = tk.Tk()
    root.title("Extend Reminder")

    def add_minutes(minutes):
        new_time = reminder_time + datetime.timedelta(minutes=minutes)
        root.destroy()
        set_reminder_at(new_time)
        messagebox.showinfo("Success", "Reminder extended successfully!")

    five_minutes_button = tk.Button(root, text="Add 5 Minutes", command=lambda: add_minutes(5))
    five_minutes_button.pack(pady=5)

    fifteen_minutes_button = tk.Button(root, text="Add 15 Minutes", command=lambda: add_minutes(15))
    fifteen_minutes_button.pack(pady=5)

    thirty_minutes_button = tk.Button(root, text="Add 30 Minutes", command=lambda: add_minutes(30))
    thirty_minutes_button.pack(pady=5)

    cancel_button = tk.Button(root, text="Cancel", command=close_window)
    cancel_button.pack(pady=5)

    root.mainloop()

def set_reminder_at(reminder_datetime):
    """Function to set reminder at a specific time."""
    delta = (reminder_datetime - datetime.datetime.now()).total_seconds()
    alert_id = root.after(int(delta * 1000), lambda: show_reminder(subject_entry.get()))
    return alert_id

def add_minutes(minutes):
    """Function to add minutes to the time entry."""
    current_time = time_entry.get()
    if current_time == "":
        now = datetime.datetime.now()
        new_time = now + datetime.timedelta(minutes=minutes)
        time_entry.delete(0, tk.END)
        time_entry.insert(0, f"{new_time.hour:02d}:{new_time.minute:02d}")
    else:
        try:
            hour, minute = map(int, current_time.split(':')) #I'm going to try and explain what I'm doing with the math because I'm sure there was a much easier way to do it, but this is what my brain did
            new_minute = (minute + minutes) % 60  # Increment minute by specified minutes and handle rollover
            new_hour = hour + (minute + minutes) // 60  # Increment hour if minute exceeds 59
            new_hour %= 24  # Handle rollover of hours
            time_entry.delete(0, tk.END)
            time_entry.insert(0, f"{new_hour:02d}:{new_minute:02d}")
        except ValueError:
            pass  # Ignore if current time is not in correct format

# Create the main window
root = tk.Tk()
root.title("Reminder App")

# Subject input
subject_label = tk.Label(root, text="Subject:")
subject_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
subject_entry = tk.Entry(root)
subject_entry.grid(row=0, column=1, padx=5, pady=5)

# Time input
time_label = tk.Label(root, text="Time (HH:MM):")
time_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=1, padx=5, pady=5)

# Create the "Add One Minute" button
add_one_minute_button = tk.Button(root, text="<3", command=lambda: add_minutes(1))
add_one_minute_button.grid(row=0, column=3, padx=5, pady=5, sticky="ne")

# Set reminder button
set_reminder_button = tk.Button(root, text="Start Reminder", command=set_reminder)
set_reminder_button.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

# Quick time buttons
quick_times_frame = tk.Frame(root)
quick_times_frame.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

five_minutes_button = tk.Button(quick_times_frame, text="Add 5 Minutes", command=lambda: add_minutes(5))
five_minutes_button.pack(side="left", padx=5)

fifteen_minutes_button = tk.Button(quick_times_frame, text="Add 15 Minutes", command=lambda: add_minutes(15))
fifteen_minutes_button.pack(side="left", padx=5)

thirty_minutes_button = tk.Button(quick_times_frame, text="Add 30 Minutes", command=lambda: add_minutes(30))
thirty_minutes_button.pack(side="left", padx=5)

# Text at the bottom to cancel the reminder
cancel_text_label = tk.Label(root, text="(To cancel the reminder, close the program)", anchor="center")
cancel_text_label.grid(row=4, column=0, columnspan=4, padx=5, pady=(10, 5))

# Start the GUI main loop
root.mainloop()
