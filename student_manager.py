import json
import csv
import pickle
import os

DATA_FILE = "students.json"
CSV_FILE = "students.csv"
PICKLE_FILE = "students.pkl"

students = []

# ---------- File Load ----------
def load_students():
    global students
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            students = json.load(f)
        print(f"📖 Loaded {len(students)} student(s).")
    else:
        print("ℹ️ No data file found, starting fresh.")

# ---------- File Save ----------
def save_students():
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=2)

    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "Skill"])
        for s in students:
            writer.writerow([s["name"], s["age"], s["skill"]])

    with open(PICKLE_FILE, "wb") as f:
        pickle.dump(students, f)

    print("💾 Data saved to JSON, CSV, and Pickle.")

# ---------- Add ----------
def add_student():
    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    skill = input("Enter skill: ").strip()

    student = {"name": name, "age": int(age), "skill": skill}

    if student in students:
        print("⚠️ Student already exists!")
        return

    students.append(student)
    print(f"✅ Added: {student}")

# ---------- List ----------
def list_students():
    if not students:
        print("⚠️ No students yet.")
        return
    print("\n--- Students ---")
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']} | Age: {s['age']} | Skill: {s['skill']}")

# ---------- Search ----------
def search_student():
    name = input("Enter name to search: ").strip()
    found = [s for s in students if s["name"].lower() == name.lower()]
    if found:
        print("🔍 Found:")
        for s in found:
            print(f"- {s['name']} | Age: {s['age']} | Skill: {s['skill']}")
    else:
        print("❌ Student not found.")

# ---------- Delete ----------
def delete_student():
    name = input("Enter name to delete: ").strip()
    global students
    new_list = [s for s in students if s["name"].lower() != name.lower()]
    if len(new_list) < len(students):
        students = new_list
        print(f"🗑️ Deleted student(s) with name: {name}")
    else:
        print("❌ No matching student found.")

# ---------- Menu ----------
def menu():
    load_students()
    while True:
        print("\n===== Student Manager =====")
        print("1. Add Student")
        print("2. List Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            save_students()
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again.")

if __name__ == "__main__":
    menu()
