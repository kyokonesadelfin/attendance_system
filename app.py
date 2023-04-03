import csv
import datetime
import tkinter as tk
from tkinter import messagebox
import smtplib


class AttendanceSystem(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Attendance System: Morning Oath")
        self.master.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        self.mark_attendance_button = tk.Button(
            self.master, text="Mark Attendance", command=self.mark_attendance)
        self.mark_attendance_button.pack(side="top", pady=10)

        self.view_attendance_button = tk.Button(
            self.master, text="View Attendance", command=self.view_attendance)
        self.view_attendance_button.pack(side="top", pady=10)

        self.quit_button = tk.Button(
            self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack(side="bottom", pady=10)

    def mark_attendance(self):
        self.mark_attendance_window = tk.Toplevel(self.master)
        self.mark_attendance_window.title("Mark Attendance")
        self.mark_attendance_window.geometry("400x200")

        self.roll_no_label = tk.Label(
            self.mark_attendance_window, text="Full Name: ")
        self.roll_no_label.pack(side="left", pady=10)

        self.roll_no_entry = tk.Entry(self.mark_attendance_window)
        self.roll_no_entry.pack(side="left", pady=10)

        self.submit_button = tk.Button(
            self.mark_attendance_window, text="Submit", command=self.submit_attendance)
        self.submit_button.pack(side="left", pady=10)

    def submit_attendance(self):
        roll_no = self.roll_no_entry.get()
        with open('attendance.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([roll_no, datetime.datetime.today()])
        messagebox.showinfo("Success", "Attendance marked successfully!")
        self.roll_no_entry.delete(0, tk.END)

   # Send email if attendance is present
        if self.check_attendance(roll_no):
            self.send_email(roll_no)


    def check_attendance(self, roll_no):
        with open('attendance.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == roll_no:
                    return True
        return False


    def send_email(self, roll_no):
        # Email information
        from_address = "ky-delfin@global-mobility-service.com"
        from_password = "Kobayashi123!!"
        to_address = "kyokonesa.delfin@gmail.com"

        # Create message
        subject = f"Attendance record: {roll_no}"
        body = f"Your attendance has been marked on {datetime.datetime.today()}"
        message = f"Subject: {subject}\n\n{body}"

        # Send email
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(from_address, from_password)
            smtp.sendmail(from_address, to_address, message)
        print(f"Email sent to {to_address}")

    def view_attendance(self):
        self.view_attendance_window = tk.Toplevel(self.master)
        self.view_attendance_window.title("View Attendance")
        self.view_attendance_window.geometry("300x100")

        self.roll_no_label = tk.Label(
            self.view_attendance_window, text="Full Name: ")
        self.roll_no_label.pack(side="left", pady=10)

        self.roll_no_entry = tk.Entry(self.view_attendance_window)
        self.roll_no_entry.pack(side="left", pady=10)

        self.submit_button = tk.Button(
            self.view_attendance_window, text="Submit", command=self.show_attendance)
        self.submit_button.pack(side="left", pady=10)

    def show_attendance(self):
        roll_no = self.roll_no_entry.get()
        attendance_dates = []
        with open('attendance.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == roll_no:
                    attendance_dates.append(row[1])
        attendance_message = f"Attendance for {roll_no}:\n"
        if attendance_dates:
            attendance_message += "\n".join(attendance_dates)
        else:
            attendance_message += "No attendance records found"
        messagebox.showinfo("Attendance Record", attendance_message)


root = tk.Tk()
app = AttendanceSystem(master=root)
app.mainloop()
