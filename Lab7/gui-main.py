import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

# File paths
csv_file = 'students.csv'
log_file = 'log.txt'

# Load students from CSV
def load_students():
    students = []
    if os.path.exists(csv_file):
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({
                    'Name': row['Name'],
                    'ID': int(row['ID']),
                    'Age': int(row['Age']),
                    'Grade': row['Grade']
                })
    return students

# Save students to CSV
def save_students():
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ['Name', 'ID', 'Age', 'Grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in std_list:
            writer.writerow(student)

# Log event to log file
def log_event(event):
    with open(log_file, mode='a') as log:
        log.write(event + '\n')

# Load initial student data
std_list = load_students()

def add_student_ui():
    def save_student():
        name = name_entry.get()
        age = age_entry.get()
        student_id = id_entry.get()
        grade = grade_entry.get().upper()

        if not name.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Invalid name!")
            return
        if not age.isdigit() or not (15 <= int(age) <= 50):
            messagebox.showerror("Error", "Invalid age!")
            return
        if not student_id.isdigit():
            messagebox.showerror("Error", "Invalid ID!")
            return
        if grade not in ['A', 'B', 'C', 'D', 'F']:
            messagebox.showerror("Error", "Invalid grade!")
            return

        std_list.append({
            'Name': name,
            'ID': int(student_id),
            'Age': int(age),
            'Grade': grade
        })
        save_students()
        log_event(f"Added student: {name} (ID: {student_id})")
        messagebox.showinfo("Success", "Student Added!")
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add Student")

    tk.Label(add_window, text="Name").grid(row=0, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Age").grid(row=1, column=0)
    age_entry = tk.Entry(add_window)
    age_entry.grid(row=1, column=1)

    tk.Label(add_window, text="ID").grid(row=2, column=0)
    id_entry = tk.Entry(add_window)
    id_entry.grid(row=2, column=1)

    tk.Label(add_window, text="Grade").grid(row=3, column=0)
    grade_entry = tk.Entry(add_window)
    grade_entry.grid(row=3, column=1)

    tk.Button(add_window, text="Add", command=save_student).grid(row=4, column=0, columnspan=2, pady=10)

def show_students_ui():
    show_window = tk.Toplevel(root)
    show_window.title("Student Records")

    for i, student in enumerate(std_list):
        info = f"{student['ID']} | {student['Name']} | Age: {student['Age']} | Grade: {student['Grade']}"
        tk.Label(show_window, text=info).pack(anchor="w")

def delete_student_ui():
    def delete_student():
        student_id = id_entry.get()

        if not student_id.isdigit():
            messagebox.showerror("Error", "Invalid ID!")
            return

        student_id = int(student_id)
        found = False
        for student in std_list:
            if student['ID'] == student_id:
                std_list.remove(student)
                save_students()
                log_event(f"Deleted student: {student['Name']} (ID: {student_id})")
                found = True
                messagebox.showinfo("Success", f"Student ID {student_id} deleted!")
                delete_window.destroy()
                break

        if not found:
            messagebox.showerror("Error", f"Student ID {student_id} not found!")

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Student")

    tk.Label(delete_window, text="Enter Student ID to delete:").grid(row=0, column=0)
    id_entry = tk.Entry(delete_window)
    id_entry.grid(row=0, column=1)

    tk.Button(delete_window, text="Delete", command=delete_student).grid(row=1, column=0, columnspan=2, pady=10)

# Main window
root = tk.Tk()
root.title("Student Management System")

tk.Button(root, text="Add Student", width=30, command=add_student_ui).pack(pady=10)
tk.Button(root, text="Show Students", width=30, command=show_students_ui).pack(pady=10)
tk.Button(root, text="Delete Student", width=30, command=delete_student_ui).pack(pady=10)
tk.Button(root, text="Exit", width=30, command=root.quit).pack(pady=10)

root.mainloop()
