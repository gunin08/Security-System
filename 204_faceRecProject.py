import sqlite3
import sys

import sqlite3
import sys

def create_database():
    conn = sqlite3.connect('employee_database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employee (
            [Employee ID] INTEGER PRIMARY KEY,
            Beard BOOLEAN,
            Mustache BOOLEAN,
            Spectacles BOOLEAN,
            [Skin colour] TEXT,
            [Eye colour] TEXT,
            [Hair colour] TEXT,
            [Authorization Level] INTEGER
        )
    ''')

    employees = [
         (1, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (2, 1, 0, 1, 'tan', 'brown', 'brown', 2),
    (3, 0, 0, 0, 'dark', 'green', 'black', 1),
    (4, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (5, 0, 0, 1, 'fair', 'blue', 'blonde', 1),
    (6, 1, 0, 1, 'tan', 'brown', 'brown', 2),
    (7, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (8, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (9, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (10, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (11, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (12, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (13, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (14, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (15, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (16, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (17, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (18, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (19, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (20, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (21, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (22, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (23, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (24, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (25, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (26, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (27, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (28, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (29, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (30, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (31, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (32, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (33, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (34, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (35, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (36, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (37, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (38, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (39, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (40, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (41, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (42, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (43, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (44, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (45, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (46, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (47, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (48, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (49, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (50, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (51, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (52, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (53, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (54, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (55, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (56, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (57, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (58, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (59, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (60, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (61, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (62, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (63, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (64, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (65, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (66, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (67, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (68, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (69, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (70, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (71, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (72, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (73, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (74, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (75, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (76, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (77, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (78, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (79, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (80, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (81, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (82, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (83, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (84, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (85, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (86, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (87, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (88, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (89, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (90, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (91, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (92, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (93, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (94, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (95, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    (96, 1, 1, 0, 'tan', 'hazel', 'brown', 1),
    (97, 0, 0, 1, 'dark', 'brown', 'black', 1),
    (98, 0, 1, 0, 'fair', 'blue', 'blonde', 1),
    (99, 1, 0, 1, 'tan', 'green', 'blonde', 2),
    (100, 0, 1, 0, 'fair', 'brown', 'brown', 1),
    ]

    cursor.executemany('INSERT OR IGNORE INTO Employee VALUES (?, ?, ?, ?, ?, ?, ?, ?)', employees)
    conn.commit()

    return conn

def add_new_employee(conn, authorisation_level):
    print("\nAdding a new employee:")
    
    try:
        new_employee_id = int(input("Enter the new Employee ID: "))
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employee WHERE [Employee ID] = ?", (new_employee_id,))
        
        if cursor.fetchone():
            print("Employee ID already exists. Please choose a different ID.")
            return

        # Additional boolean inputs
        beard = int(input("Does the new employee have a beard? (1 for Yes, 0 for No): "))
        mustache = int(input("Does the new employee have a mustache? (1 for Yes, 0 for No): "))
        spectacles = int(input("Does the new employee wear spectacles? (1 for Yes, 0 for No): "))
        skin_colour = input("Enter the skin colour of the new employee: ")
        eye_colour = input("Enter the eye colour of the new employee: ")
        hair_colour = input("Enter the hair colour of the new employee: ")

        # Authorization level for the new employee
        if authorisation_level == 2:
            auth_level_new_employee = int(input("Enter authorization level for the new employee (1 or 2): "))
            if auth_level_new_employee not in [1, 2]:
                print("Invalid authorization level. Setting to default (1).")
                auth_level_new_employee = 1
        elif authorisation_level == 3:
            auth_level_new_employee = int(input("Enter authorization level for the new employee (1, 2, or 3): "))
            if auth_level_new_employee not in [1, 2, 3]:
                print("Invalid authorization level. Setting to default (1).")
                auth_level_new_employee = 1

        # Insert new employee into the database
        cursor.execute('''
            INSERT INTO Employee VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (new_employee_id, beard, mustache, spectacles, skin_colour, eye_colour, hair_colour, auth_level_new_employee))
        conn.commit()

        print("New employee added successfully!")

    except ValueError:
        print("Invalid input. Please enter valid details.")

def initiate_system_meltdown():
    response = input("Are you sure you want to initiate a system meltdown? (yes/no): ").lower()
    return response == 'yes'

def authenticate_user(conn, error_limit=3):
    error_count = 0
    error_flag = 0

    while error_count < error_limit:
        try:
            employee_id = int(input("Enter Employee ID: "))
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Employee WHERE [Employee ID] = ?", (employee_id,))
            employee = cursor.fetchone()

            if not employee:
                print("Employee not found. Please try again.")
                error_count += 1
                continue

            # Additional boolean inputs
            sleepy = int(input("Is the person sleepy? (1 for Yes, 0 for No): "))
            intoxicated = int(input("Is the person intoxicated? (1 for Yes, 0 for No): "))
            sufficient_light = int(input("Is there sufficient light? (1 for Yes, 0 for No): "))
            one_person_in_frame = int(input("Is there only one person in the frame? (1 for Yes, 0 for No): "))
            face_clear = int(input("Is the face clear? (1 for Yes, 0 for No): "))
            face_front = int(input("Is the face looking in front? (1 for Yes, 0 for No): "))

            # Check boolean conditions
            if sleepy or intoxicated:
                print("Security Alert! Employee is sleepy or intoxicated. Access denied.")
                sys.exit()  # Exit the program immediately
            elif not sufficient_light or not one_person_in_frame or not face_clear or not face_front:
                print("Access Denied. Conditions not met. Please try again.")
                error_count += 1
            else:
                # Ask for employee details only if conditions are met
                print("Initial Access Granted!")
                # Employee details input
                # Additional boolean inputs
                beard = int(input("Does the person have a beard? (1 for Yes, 0 for No): "))
                mustache = int(input("Does the person have a mustache? (1 for Yes, 0 for No): "))
                spectacles = int(input("Does the person wear spectacles? (1 for Yes, 0 for No): "))
                skin_colour = input("Enter the skin colour of the person: ")
                eye_colour = input("Enter the eye colour of the person: ")
                hair_colour = input("Enter the hair colour of the person: ")

                # Check if employee details match
                if (
                    employee[1] == beard
                    and employee[2] == mustache
                    and employee[3] == spectacles
                    and employee[4] == skin_colour
                    and employee[5] == eye_colour
                    and employee[6] == hair_colour
                ):
                    print("Employee details match. Access Granted!")

                    # Additional functionality for authorization levels
                    if employee[7] == 2:
                        response = input("Do you want to add a new employee? (yes/no): ").lower()
                        if response == 'yes':
                            add_new_employee(conn, 2)
                    elif employee[7] == 3:
                        response = input("Do you want to add a new employee or initiate system meltdown? (employee/meltdown/no): ").lower()
                        if response == 'employee':
                            add_new_employee(conn, 3)
                        elif response == 'meltdown':
                            if initiate_system_meltdown():
                                print("System meltdown initiated. Goodbye!")
                                sys.exit()
                            else:
                                print("System meltdown aborted.")
                    return

                print("Employee details do not match. Access Denied.")
                error_count += 1

        except ValueError:
            print("Invalid input. Please enter a valid Employee ID.")

    # Security Alert
    print("Security Alert! Too many incorrect attempts. Access denied.")
    sys.exit()  # Exit the program immediately

if __name__ == "__main__":
    conn = create_database()
    authenticate_user(conn)
