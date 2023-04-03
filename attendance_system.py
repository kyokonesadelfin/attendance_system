import csv
import datetime

# Function to mark attendance for a student
def mark_attendance():
    full_name = input("Enter your full name: ")
    with open('attendance.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([full_name, datetime.datetime.now()])

# Function to view attendance for a student
def view_attendance():
    full_name = input("Enter your full name: ")
    with open('attendance.csv', 'r') as file:
        reader = csv.reader(file)
        print(f"Attendance for Roll No. {full_name}:")
        for row in reader:
            if row[0] == full_name:
                print(row[1])

# Main function to run the attendance system
def main():
    print("Welcome to Attendance System")
    while True:
        print("\n1. Mark Attendance\n2. View Attendance\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            mark_attendance()
        elif choice == 2:
            view_attendance()
        elif choice == 3:
            print("Thank you for using Attendance System")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
