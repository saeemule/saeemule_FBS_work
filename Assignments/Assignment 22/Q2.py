import pickle
import os

FILENAME = "emp_data.dat"


class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def __str__(self):
        return f"ID: {self.eid}, Name: {self.ename}, Basic: {self.basic}"


def AddRecord():
    with open(FILENAME, "ab") as f:
        eid = int(input("Enter Employee ID: "))
        ename = input("Enter Employee Name: ")
        basic = float(input("Enter Basic Salary: "))
        emp = Emp(eid, ename, basic)
        pickle.dump(emp, f)
        print("Record added successfully.")


def SearchRecord():
    search_id = int(input("Enter Employee ID to search: "))
    found = False
    if os.path.exists(FILENAME):
        with open(FILENAME, "rb") as f:
            while True:
                try:
                    emp = pickle.load(f)
                    if emp.eid == search_id:
                        print("Record found:")
                        print(emp)
                        found = True
                        break
                except EOFError:
                    break
    if not found:
        print("Record not found.")


def DeleteRecord():
    del_id = int(input("Enter Employee ID to delete: "))
    records = []
    found = False

    if os.path.exists(FILENAME):
        with open(FILENAME, "rb") as f:
            while True:
                try:
                    emp = pickle.load(f)
                    if emp.eid != del_id:
                        records.append(emp)
                    else:
                        found = True
                except EOFError:
                    break

    if found:
        with open(FILENAME, "wb") as f:
            for emp in records:
                pickle.dump(emp, f)
        print("Record deleted successfully.")
    else:
        print("Record not found.")


def EditRecord():
    edit_id = int(input("Enter Employee ID to edit: "))
    records = []
    found = False

    if os.path.exists(FILENAME):
        with open(FILENAME, "rb") as f:
            while True:
                try:
                    emp = pickle.load(f)
                    if emp.eid == edit_id:
                        print("Current record:", emp)
                        emp.ename = input("Enter new Name: ")
                        emp.basic = float(input("Enter new Basic Salary: "))
                        found = True
                    records.append(emp)
                except EOFError:
                    break

    if found:
        with open(FILENAME, "wb") as f:
            for emp in records:
                pickle.dump(emp, f)
        print("Record updated successfully.")
    else:
        print("Record not found.")


def DisplayAllRecords():
    if os.path.exists(FILENAME):
        with open(FILENAME, "rb") as f:
            print("=" * 40)
            count = 0
            while True:
                try:
                    emp = pickle.load(f)
                    print(emp)
                    count += 1
                except EOFError:
                    break
            print("=" * 40)
            if count == 0:
                print("No records found.")
    else:
        print("No records found.")


def Menu():
    while True:
        print("\n----- EMPLOYEE RECORD MENU -----")
        print("1. Add a record")
        print("2. Search for a record using ID")
        print("3. Delete a record using ID")
        print("4. Edit a record using ID")
        print("5. Display all records")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            AddRecord()
        elif choice == '2':
            SearchRecord()
        elif choice == '3':
            DeleteRecord()
        elif choice == '4':
            EditRecord()
        elif choice == '5':
            DisplayAllRecords()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


# ---- Run the menu ----
if __name__ == "__main__":
    Menu()