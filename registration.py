import threading
import time

seats = 1

lock = threading.Lock()


def register_without_lock(student):

    global seats

    if seats > 0:

        print(f"{student} is registering...")

        time.sleep(1)

        seats -= 1

        print(f"{student} registered.")

    else:

        print(f"{student} failed.")


def register_with_lock(student):

    global seats

    with lock:

        if seats > 0:

            print(f"{student} is registering...")

            time.sleep(1)

            seats -= 1

            print(f"{student} registered.")

        else:

            print(f"{student} failed.")


def run_registration_demo():

    global seats

    print("\nWITHOUT SYNCHRONIZATION")

    seats = 1

    t1 = threading.Thread(target=register_without_lock, args=("Student A",))
    t2 = threading.Thread(target=register_without_lock, args=("Student B",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Remaining Seats:", seats)

    print("\nWITH SYNCHRONIZATION")

    seats = 1

    t3 = threading.Thread(target=register_with_lock, args=("Student A",))
    t4 = threading.Thread(target=register_with_lock, args=("Student B",))

    t3.start()
    t4.start()

    t3.join()
    t4.join()

    print("Remaining Seats:", seats)