import csv
from datetime import datetime

std_list = [
    {'Name': 'Roman Reigns', 'ID': 1, 'Age': 38, 'Grade': 'A'},
    {'Name': 'Seth Rollins', 'ID': 2, 'Age': 37, 'Grade': 'A'},
    {'Name': 'CM Punk', 'ID': 3, 'Age': 45, 'Grade': 'B'},
    {'Name': 'Rey Mysterio', 'ID': 4, 'Age': 49, 'Grade': 'A'},
    {'Name': 'The Miz', 'ID': 5, 'Age': 43, 'Grade': 'B'},
    {'Name': 'Bray Wyatt', 'ID': 6, 'Age': 36, 'Grade': 'C'},
    {'Name': 'AJ Styles', 'ID': 7, 'Age': 46, 'Grade': 'A'},
    {'Name': 'Logan Paul', 'ID': 8, 'Age': 29, 'Grade': 'B'},
    {'Name': 'Jey Uso', 'ID': 9, 'Age': 38, 'Grade': 'B'},
    {'Name': 'Drew McIntyre', 'ID': 10, 'Age': 39, 'Grade': 'A'},
    {'Name': 'Damian Priest', 'ID': 11, 'Age': 41, 'Grade': 'B'},
    {'Name': 'Dominik Mysterio', 'ID': 12, 'Age': 26, 'Grade': 'C'},
    {'Name': 'Liv Morgan', 'ID': 13, 'Age': 29, 'Grade': 'B'},
    {'Name': 'Rhea Ripley', 'ID': 14, 'Age': 27, 'Grade': 'A'},
    {'Name': 'Bayley', 'ID': 15, 'Age': 34, 'Grade': 'A'},
    {'Name': 'Jacob Fatu', 'ID': 16, 'Age': 31, 'Grade': 'B'},
    {'Name': 'Solo Sikoa', 'ID': 17, 'Age': 30, 'Grade': 'B'},
    {'Name': 'Cody Rhodes', 'ID': 18, 'Age': 39, 'Grade': 'A'},
    {'Name': 'Sasha Banks', 'ID': 19, 'Age': 32, 'Grade': 'A'},
    {'Name': 'Bianca Belair', 'ID': 20, 'Age': 35, 'Grade': 'A'},
    {'Name': 'Iyo Sky', 'ID': 21, 'Age': 33, 'Grade': 'B'},
    {'Name': 'Finn Balor', 'ID': 22, 'Age': 42, 'Grade': 'B'},
    {'Name': 'Kevin Owens', 'ID': 23, 'Age': 40, 'Grade': 'B'},
    {'Name': 'Sami Zayn', 'ID': 24, 'Age': 39, 'Grade': 'B'},
    {'Name': 'Shinsuke Nakamura', 'ID': 25, 'Age': 44, 'Grade': 'C'},
    {'Name': 'LA Knight', 'ID': 26, 'Age': 41, 'Grade': 'B'},
    {'Name': 'Randy Orton', 'ID': 27, 'Age': 44, 'Grade': 'A'},
    {'Name': 'Gunther', 'ID': 28, 'Age': 36, 'Grade': 'A'},
    {'Name': 'Sheamus', 'ID': 29, 'Age': 46, 'Grade': 'B'},
    {'Name': 'Karrion Kross', 'ID': 30, 'Age': 39, 'Grade': 'C'},
]

def log_action(action):
    with open("log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {action}\n")

def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_age(age):
    return 15 <= age <= 50

def is_valid_id(ID_):
    return 1 <= ID_ <= 10000

def is_valid_grade(grade):
    return grade.upper() in ['A', 'B', 'C', 'D', 'F']

def add_std():
    print('\n=== Add Student ===')
    while True:
        name = input("Enter Name: ")
        if is_valid_name(name):
            break
        print("Invalid name!")

    while True:
        try:
            age = int(input("Enter Age (15-50): "))
            if is_valid_age(age):
                break
        except:
            pass
        print("Invalid age!")

    while True:
        try:
            ID_ = int(input("Enter ID (1-10000): "))
            if is_valid_id(ID_) and not any(s['ID'] == ID_ for s in std_list):
                break
        except:
            pass
        print("Invalid or duplicate ID!")

    while True:
        grade = input("Enter Grade (A-F): ").upper()
        if is_valid_grade(grade):
            break
        print("Invalid grade!")

    std_list.append({'Name': name, 'ID': ID_, 'Age': age, 'Grade': grade})
    log_action(f"Added: {name}, ID: {ID_}")
    print("Student added successfully!\n")

def show_records():
    print("\n=== All Students ===")
    for s in std_list:
        print(s)
    print()

def update_record():
    try:
        ID = int(input("Enter Student ID to update: "))
        for s in std_list:
            if s['ID'] == ID:
                print(f"Record Found: {s}")
                print("1. Name\n2. Age\n3. Grade")
                ch = int(input("Select field to update: "))
                if ch == 1:
                    name = input("Enter new name: ")
                    if is_valid_name(name):
                        s['Name'] = name
                        log_action(f"Updated Name for ID {ID}")
                elif ch == 2:
                    age = int(input("Enter new age: "))
                    if is_valid_age(age):
                        s['Age'] = age
                        log_action(f"Updated Age for ID {ID}")
                elif ch == 3:
                    grade = input("Enter new grade: ").upper()
                    if is_valid_grade(grade):
                        s['Grade'] = grade
                        log_action(f"Updated Grade for ID {ID}")
                return
        print("Record not found!\n")
    except:
        print("Invalid input.\n")

def delete_records():
    try:
        ID = int(input("Enter ID to delete: "))
        for s in std_list:
            if s['ID'] == ID:
                std_list.remove(s)
                log_action(f"Deleted ID {ID}")
                print("Record deleted.\n")
                return
        print("No record found.\n")
    except:
        print("Invalid input.\n")

def search_student():
    try:
        ID = int(input("Enter ID to search: "))
        for s in std_list:
            if s['ID'] == ID:
                print(f"Found: {s}")
                return
        print("Not found!\n")
    except:
        print("Invalid input.\n")

# Show stats
def show_stats():
    total = len(std_list)
    avg_age = sum(s['Age'] for s in std_list) / total
    grades = set(s['Grade'] for s in std_list)
    print(f"\nTotal Students: {total}\nAverage Age: {avg_age:.2f}\nGrades Present: {grades}\n")

# Export to CSV
def export_csv():
    with open("students.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "ID", "Age", "Grade"])
        writer.writeheader()
        writer.writerows(std_list)
    log_action("Exported data to students.csv")

# Main Menu
def main():
    while True:
        print("======= Student Management System =======")
        print("1. Add Student")
        print("2. Show Records")
        print("3. Delete Record")
        print("4. Update Record")
        print("5. Show Stats")
        print("6. Search Record")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        if choice == 1:
            add_std()
        elif choice == 2:
            show_records()
        elif choice == 3:
            delete_records()
        elif choice == 4:
            update_record()
        elif choice == 5:
            show_stats()
        elif choice == 6:
            search_student()
        elif choice == 7:
            export_csv()
            print("========Fi ImanAllah==========")
            break
        else:
            print("Invalid option. Please choose between 1 to 7.\n")

if __name__ == "__main__":
    main()
