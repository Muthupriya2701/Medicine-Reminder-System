from db_helper import fetch_reminders
from voice_alert import speak
import time
from datetime import datetime

triggered_today = set()

def check_reminders():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        reminders = fetch_reminders()
        
        for reminder in reminders:
            reminder_id = reminder[0]
            name = reminder[1]
            time_to_ring = reminder[2]
            dose = reminder[3]
            
            unique_key = f"{reminder_id}-{current_time}"
            
            if current_time == time_to_ring and unique_key not in triggered_today:
                speak(f"It's time to take your medicine: {name}, {dose}")
                triggered_today.add(unique_key)

        time.sleep(10)  # Check every 10 seconds
