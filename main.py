from graph import (
    load_graph,
    display_all_courses,
    available_courses,
    get_all_completed
)

from cycle_detection import detect_cycle

from topo_sort import topological_sort

from semester_planner import semester_plan

from registration import (
    take_student_input,
    synchronization_demo
)


def main():

    print("=" * 70)
    print("CAMPUSPATH: SMART COURSE PREREQUISITE PLANNER")
    print("=" * 70)

    graph = load_graph("config/courses.txt")

    if detect_cycle(graph):

        print("\nERROR: Cycle detected!")

        return

    all_courses = list(graph.keys())

    print(f"\nTotal Courses Loaded: {len(graph)}")

    display_all_courses(graph)

    students = take_student_input(all_courses)

    topo_order = topological_sort(graph)

    for student in students:

        print("\n" + "=" * 70)

        print(f"STUDENT NAME : {student['name']}")
        print(f"USN          : {student['usn']}")
        print(f"BRANCH       : {student['branch']}")
        print(f"SEMESTER     : {student['semester']}")

        # AUTO COMPLETE PREREQUISITES

        completed = get_all_completed(
            graph,
            student["completed"]
        )

        print("\n===== COMPLETED COURSES =====\n")

        if completed:

            for c in completed:

                print("•", c)

        else:

            print("None")

        # AVAILABLE COURSES

        available = available_courses(
            graph,
            completed
        )

        print(
            "\n===== AVAILABLE COURSES "
            "FOR REGISTRATION =====\n"
        )

        if available:

            for c in available:

                print("-", c)

        else:

            print("No available courses.")

        # STUDENT-SPECIFIC REMAINING COURSES

        remaining = []

        for c in topo_order:

            if c not in completed:

                remaining.append(c)

        print(
            "\n===== VALID FUTURE COURSE ORDER =====\n"
        )

        for i, c in enumerate(remaining, 1):

            print(f"{i}. {c}")

        # STUDENT-SPECIFIC SEMESTER PLAN

        limit = int(

            input(
                f"\nEnter max courses per semester "
                f"for {student['name']}: "
            )
        )

        semesters = semester_plan(
            remaining,
            limit
        )

        print(
            f"\n===== FUTURE SEMESTER PLAN "
            f"FOR {student['name']} =====\n"
        )

        for sem_no, sem in enumerate(semesters, 1):

            print(f"Semester {sem_no}")

            for c in sem:

                print("  •", c)

            print()

    print("\n===== REGISTRATION PROCESS =====")

    synchronization_demo(students)

    print("\nProject Completed Successfully.")


if __name__ == "__main__":

    main()