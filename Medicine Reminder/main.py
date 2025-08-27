import tkinter as tk
from tkinter import messagebox
from db_helper import connect_db, insert_reminder
import threading
from reminder_checker import check_reminders

# Connect to the database
connect_db()

# Function to add reminder to database
def add_reminder():
    name = entry_name.get()
    time = entry_time.get()
    dose = entry_dose.get()
    
    if name == "" or time == "" or dose == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return
    
    insert_reminder(name, time, dose)
    messagebox.showinfo("Success", f"Reminder for '{name}' at {time} saved!")
    entry_name.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    entry_dose.delete(0, tk.END)

# GUI Window
app = tk.Tk()
app.title("Smart Medicine Reminder")
app.geometry("300x250")

tk.Label(app, text="Medicine Name").pack()
entry_name = tk.Entry(app)
entry_name.pack()

tk.Label(app, text="Time (HH:MM)").pack()
entry_time = tk.Entry(app)
entry_time.pack()

tk.Label(app, text="Dose").pack()
entry_dose = tk.Entry(app)
entry_dose.pack()

tk.Button(app, text="Add Reminder", command=add_reminder).pack(pady=10)

# Start background thread to check reminders
threading.Thread(target=check_reminders, daemon=True).start()

app.mainloop()
