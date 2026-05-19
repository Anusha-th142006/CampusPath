import threading
import time

seats = 1

lock = threading.Lock()


def register_without_lock(student):

    global seats

    if seats > 0:

        print(f"\n{student['name']} is registering...")

        time.sleep(1)

        seats -= 1

        print(f"{student['name']} registered successfully.")

    else:

        print(f"{student['name']} failed to register.")


def register_with_lock(student):

    global seats

    with lock:

        if seats > 0:

            print(f"\n{student['name']} is registering...")

            time.sleep(1)

            seats -= 1

            print(f"{student['name']} registered successfully.")

        else:

            print(f"{student['name']} failed to register.")


def take_student_input(valid_courses):

    print("\n===== STUDENT REGISTRATION =====")

    total_students = int(
        input("\nEnter number of students registering: ")
    )

    students = []

    for i in range(total_students):

        print(f"\n===== ENTER DETAILS FOR STUDENT {i+1} =====")

        name = input("Enter Name: ")

        usn = input("Enter USN: ")

        branch = input("Enter Branch: ")

        semester = input("Enter Current Semester: ")

        completed = input(
            "\nEnter completed courses separated by comma: "
        )

        entered_courses = [
            x.strip()
            for x in completed.split(",")
            if x.strip()
        ]

        completed_courses = []

        for course in entered_courses:

            matched = False

            for valid in valid_courses:

                if course.lower() == valid.lower():

                    completed_courses.append(valid)

                    matched = True
                    break

            if not matched:

                print(f"\nERROR: '{course}' is not valid.")

                return take_student_input(valid_courses)

        student = {

            "name": name,
            "usn": usn,
            "branch": branch,
            "semester": semester,
            "completed": completed_courses
        }

        students.append(student)

    return students


def synchronization_demo(students):

    global seats

    if len(students) == 1:

        print("\nOnly one student registering.")
        print("Synchronization not required.")

        return

    print("\n===== MULTIPLE STUDENTS DETECTED =====")

    print("\n===== WITHOUT SYNCHRONIZATION =====")

    seats = 1

    threads = []

    for student in students:

        t = threading.Thread(
            target=register_without_lock,
            args=(student,)
        )

        threads.append(t)

        t.start()

    for t in threads:

        t.join()

    print("\nRemaining Seats:", seats)

    print("\n===== WITH SYNCHRONIZATION =====")

    seats = 1

    threads = []

    for student in students:

        t = threading.Thread(
            target=register_with_lock,
            args=(student,)
        )

        threads.append(t)

        t.start()

    for t in threads:

        t.join()

    print("\nRemaining Seats:", seats)