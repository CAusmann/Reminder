# Reminder
### Language: 
Python

### Description: 
A simple reminder app designed to create and customize reminders for a specific time in the day. Includes quick-add buttons for setting the time and a snooze function as well

## Usage
### Subject: 
-> This should be what the reminder is for (example: "Take cookies out of the oven")

### Time (HH:MM):
-> 24 Hour Format

-> This should be entered as the time of day the reminder should go off (example: 14:35)

### Quick-Add Buttons
 -> Add 5 Minutes: Adds 5 minutes to the time entered in the 'Time' field. Will also fill the 'Time' field if it's empty

 -> Add 15 Minutes: Adds 15 minutes to the time entered in the 'Time' field. Will also fill the 'Time' field if it's empty

 -> Add 30 Minutes: Adds 30 minutes to the time entered in the 'Time' field. Will also fill the 'Time' field if it's empty

 -> <3: This button was added as a development tool to add a single minute to the 'Time' field for testing purposes, but it's been more useful than I thought it would be so I'm leaving it in.

### Start Reminder
 -> Sets a reminder for the specified time 


## Snooze
 -> When the reminder is finished, an alert will prompt the user to select if they need additional time
 
 -> Quick-Add buttons will be displayed for the user to choose from. The reminder will be extended for that duration
