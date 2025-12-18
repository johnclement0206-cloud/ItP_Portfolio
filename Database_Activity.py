import numpy

students = [
    {"student_id": 1001, "first_name": "Azel", "mid_name": "Edryan", "last_name": "Bulanadi", "fbt_id": 250044, "dob": "7/14/2007", "age": 18, "email": "azelbulanadi677@gmail.com", "nationality": "Filipino", "phone_no": "0502911671", "course": "Cybersecurity", "com_indus": 87, "itp": 92, "digi_for": 85},
    {"student_id": 1002, "first_name": "Nathaniel", "mid_name": "Josemari", "last_name": "Talens", "fbt_id": 250019, "dob": "01/28/2007", "age": 18, "email": "josemartalens@gmail.com", "nationality": "Filipino", "phone_no": "0538946672", "course": "Cybersecurity", "com_indus": 91, "itp": 88, "digi_for": 79},
    {"student_id": 1003, "first_name": "Abdulaziz", "mid_name": "", "last_name": "Tejada", "fbt_id": 250002, "dob": "01/02/2008", "age": 17, "email": "azizst08@gmail.com", "nationality": "Filipino", "phone_no": "0510269673", "course": "Cybersecurity", "com_indus": 84, "itp": 90, "digi_for": 86},
    {"student_id": 1004, "first_name": "Mohammed", "mid_name": "Abrar", "last_name": "Khan", "fbt_id": 250068, "dob": "11/16/2006", "age": 19, "email": "Kabrar997@gmail.com", "nationality": "Indian", "phone_no": "0538936918", "course": "Cybersecurity", "com_indus": 89, "itp": 85, "digi_for": 92},
    {"student_id": 1005, "first_name": "John", "mid_name": "Clement", "last_name": "Ibrahim", "fbt_id": 250027, "dob": "02/02/2006", "age": 19, "email": "johnclement0206@gmail.com", "nationality": "Filipino", "phone_no": "0557446148", "course": "Cybersecurity", "com_indus": 93, "itp": 87, "digi_for": 91},
    {"student_id": 1006, "first_name": "Diego", "mid_name": "", "last_name": "Catal", "fbt_id": 250051, "dob": "04/25/2007", "age": 18, "email": "cataldiego5@gmail.com", "nationality": "Filipino", "phone_no": "0547698579", "course": "Cybersecurity", "com_indus": 82, "itp": 89, "digi_for": 84},
    {"student_id": 1007, "first_name": "Yadha", "mid_name": "", "last_name": "Villanueva", "fbt_id": 250063, "dob": "01/15/2008", "age": 17, "email": "yadhavillanueva@gmail.com", "nationality": "Filipino", "phone_no": "0533581447", "course": "Cybersecurity", "com_indus": 88, "itp": 91, "digi_for": 87},
    {"student_id": 1008, "first_name": "Deen", "mid_name": "", "last_name": "Tanaei", "fbt_id": 250033, "dob": "07/07/2003", "age": 22, "email": "deentanaei@gmail.com", "nationality": "Filipino", "phone_no": "0564529805", "course": "Cybersecurity", "com_indus": 85, "itp": 86, "digi_for": 90},
    {"student_id": 1009, "first_name": "Amir", "mid_name": "Abdullah", "last_name": "Tanaei", "fbt_id": None, "dob": "03/24/2007", "age": 19, "email": "", "nationality": "Filipino", "phone_no": "", "course": "Cybersecurity", "com_indus": 90, "itp": 84, "digi_for": 88},
    {"student_id": 1010, "first_name": "Justine", "mid_name": "Noel", "last_name": "Dicuangco", "fbt_id": 250004, "dob": "10/15/2007", "age": 18, "email": "justinedicuangco@gmail.com", "nationality": "Filipino", "phone_no": "0566932280", "course": "Cybersecurity", "com_indus": 86, "itp": 92, "digi_for": 83},
    {"student_id": 1011, "first_name": "Princess", "mid_name": "Gefren", "last_name": "Calisaan", "fbt_id": 250062, "dob": "10/20/2006", "age": 19, "email": "m.y.gswaeg@gmail.com", "nationality": "Filipino", "phone_no": "", "course": "Cybersecurity", "com_indus": 91, "itp": 88, "digi_for": 89},
    {"student_id": 1012, "first_name": "Muhammad", "mid_name": "Umar", "last_name": "Ayubb", "fbt_id": 250030, "dob": "09/12/2005", "age": 19, "email": "omerayoub123456789@gmail.com", "nationality": "Pakistan", "phone_no": "0598606719", "course": "Cybersecurity", "com_indus": 87, "itp": 85, "digi_for": 91},
    {"student_id": 1013, "first_name": "Muhammad", "mid_name": "Basil", "last_name": "Shahid", "fbt_id": 250065, "dob": "03/11/2005", "age": 20, "email": "mbsawan2005@gmail.com", "nationality": "Pakistan", "phone_no": "0508089027", "course": "Cybersecurity", "com_indus": 89, "itp": 90, "digi_for": 86},
    {"student_id": 1014, "first_name": "Augustus", "mid_name": "Vidal", "last_name": "Sales", "fbt_id": 200015, "dob": "5/6/2007", "age": 18, "email": "augustusvldalsales@gmail.com", "nationality": "Filipino", "phone_no": "0508211324", "course": "Cybersecurity", "com_indus": 84, "itp": 87, "digi_for": 92},
    {"student_id": 1015, "first_name": "Emmanuel", "mid_name": "", "last_name": "Dicuangco", "fbt_id": 250003, "dob": "8/29/2006", "age": 19, "email": "emmanuelejoshua@gmail.com", "nationality": "Filipino", "phone_no": "0540083894", "course": "Cybersecurity", "com_indus": 92, "itp": 89, "digi_for": 85},
    {"student_id": 1016, "first_name": "Ma. Jessica", "mid_name": "Paula", "last_name": "Cabato", "fbt_id": 250020, "dob": "02/07/2007", "age": 18, "email": "cabatojessica01@gmail.com", "nationality": "Filipino", "phone_no": "0570764453", "course": "Cybersecurity", "com_indus": 88, "itp": 91, "digi_for": 87},
    {"student_id": 1017, "first_name": "Mark", "mid_name": "Rowel", "last_name": "Druja", "fbt_id": None, "dob": "06/15/2007", "age": 18, "email": "markdruja@gmail.com", "nationality": "Filipino", "phone_no": "0543219876", "course": "Cybersecurity", "com_indus": 83, "itp": 86, "digi_for": 90},
    {"student_id": 1018, "first_name": "Hassen", "mid_name": "Abduljalil", "last_name": "Wabe", "fbt_id": None, "dob": "09/03/2006", "age": 19, "email": "hassenwabe@gmail.com", "nationality": "Filipino", "phone_no": "0578901234", "course": "Cybersecurity", "com_indus": 89, "itp": 91, "digi_for": 85},
    {"student_id": 1019, "first_name": "Wossan", "mid_name": "", "last_name": "Kadi", "fbt_id": None, "dob": "12/25/2005", "age": 20, "email": "wossankadi@gmail.com", "nationality": "Filipino", "phone_no": "0589012345", "course": "Cybersecurity", "com_indus": 85, "itp": 84, "digi_for": 88},
    {"student_id": 1020, "first_name": "Khalid", "mid_name": "Waleed", "last_name": "Suliman", "fbt_id": None, "dob": "04/18/2006", "age": 19, "email": "khalidsuliman@gmail.com", "nationality": "Filipino", "phone_no": "0590123456", "course": "Cybersecurity", "com_indus": 91, "itp": 87, "digi_for": 92}
]

def add_student():
    if students:
        student_id = max(student['student_id'] for student in students) + 1
    else:
        student_id = 1001
    
    first_name = input("Enter first name: ")
    mid_name = input("Enter middle name: ")
    last_name = input("Enter last name: ")
    fbt_id = int(input("Enter FBT ID: "))
    dob = input("Enter date of birth (DD/MM/YY): ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")
    nationality = input("Enter nationality: ")
    phone_no = input("Enter phone number: ")
    course = input("Enter course: ")
    com_indus = int(input("Enter Computer Industry grade: "))
    itp = int(input("Enter ITP grade: "))
    digi_for = int(input("Enter Digital Forensics grade: "))
    
    new_student = {
        "student_id": student_id,
        "first_name": first_name,
        "mid_name": mid_name,
        "last_name": last_name,
        "fbt_id": fbt_id,
        "dob": dob,
        "age": age,
        "email": email,
        "nationality": nationality,
        "phone_no": phone_no,
        "course": course,
        "com_indus": com_indus,
        "itp": itp,
        "digi_for": digi_for
    }
    
    students.append(new_student)
    print(f"Student added! ID: {student_id}")
    return new_student

def find_student():
    try:
        student_id = int(input("Enter student ID: "))
        for student in students:
            if student['student_id'] == student_id:
                print(f"\n{'='*50}")
                print(f"Student ID: {student['student_id']}")
                print(f"Name: {student['first_name']} {student['mid_name']} {student['last_name']}")
                print(f"FBT ID: {student['fbt_id']}")
                print(f"Date of Birth: {student['dob']}")
                print(f"Age: {student['age']}")
                print(f"Email: {student['email']}")
                print(f"Nationality: {student['nationality']}")
                print(f"Phone: {student['phone_no']}")
                print(f"Course: {student['course']}")
                print(f"Grades - CI: {student['com_indus']}, ITP: {student['itp']}, DF: {student['digi_for']}")
                print(f"{'='*50}")
                return student
        print("Student not found!")
        return None
    except ValueError:
        print("Please enter a valid ID number!")
        return None

def change_grade():
    student = find_student()
    if student:
        print("\n1. Computer Industry")
        print("2. ITP") 
        print("3. Digital Forensics")
        
        try:
            choice = int(input("Select subject (1-3): "))
            new_grade = int(input("Enter new grade: "))
            
            if choice == 1:
                student['com_indus'] = new_grade
                print("Computer Industry grade updated!")
            elif choice == 2:
                student['itp'] = new_grade
                print("ITP grade updated!")
            elif choice == 3:
                student['digi_for'] = new_grade
                print("Digital Forensics grade updated!")
            else:
                print("Invalid choice!")
        except ValueError:
            print("Please enter valid numbers!")

def display_all_students():
    print("\n" + "="*100)
    print("ALL STUDENTS")
    print("="*100)
    for student in students:
        print(f"ID: {student['student_id']} | {student['first_name']} {student['mid_name']} {student['last_name']}")
        print(f"  FBT ID: {student['fbt_id']} | DOB: {student['dob']} | Age: {student['age']}")
        print(f"  Email: {student['email']} | Phone: {student['phone_no']}")
        print(f"  Nationality: {student['nationality']} | Course: {student['course']}")
        print(f"  Grades - Computer Industry: {student['com_indus']}, Intro to Programming: {student['itp']}, Digital Forensics: {student['digi_for']}")
        print("-"*100)

def calculate_average_grades():
    if students:
        com_indus_avg = sum(student['com_indus'] for student in students) / len(students)
        itp_avg = sum(student['itp'] for student in students) / len(students)
        digi_for_avg = sum(student['digi_for'] for student in students) / len(students)
        
        print(f"\nAverage Grades - CI: {com_indus_avg:.2f}, ITP: {itp_avg:.2f}, DF: {digi_for_avg:.2f}")
    else:
        print("No students in database!")

def main_menu():
    while True:
        print("\n" + "="*40)
        print("STUDENT DATABASE SYSTEM")
        print("="*40)
        print("1. Add Student")
        print("2. Find Student") 
        print("3. Change Grade")
        print("4. Show All Students")
        print("5. Show Average Grades")
        print("6. Exit")
        print("="*40)
        
        choice = input("Choose option (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            find_student()
        elif choice == '3':
            change_grade()
        elif choice == '4':
            display_all_students()
        elif choice == '5':
            calculate_average_grades()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
