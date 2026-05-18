from graph import load_graph, display_graph
from cycle_detection import detect_cycle
from topo_sort import topological_sort
from registration import run_registration_demo
from semester_planner import semester_plan


def main():

    print("=" * 60)
    print("CAMPUSPATH: SMART COURSE PREREQUISITE PLANNER")
    print("=" * 60)

    graph = load_graph("config/courses.txt")
    print(f"\nTotal Courses Loaded: {len(graph)}")

    display_graph(graph)

    print("\nChecking for cycles...\n")

    if detect_cycle(graph):

        print("ERROR: Invalid course configuration detected due to cyclic dependencies.")

        return

    print("No cycles found.\n")

    order = topological_sort(graph)

    print("Valid Course Order:\n")

    for i, course in enumerate(order, 1):

        print(f"{i}. {course}")

    completed = input("\nEnter completed courses: ")

    completed_courses = [x.strip() for x in completed.split(",")]

    remaining = [c for c in order if c not in completed_courses]

    print("\nRemaining Courses:\n")

    for course in remaining:

        print(course)

    limit = int(input("\nEnter maximum courses per semester: "))

    semesters = semester_plan(remaining, limit)
    print("\n===== SEMESTER PLAN =====\n")

    for i, semester in enumerate(semesters, 1):

        print(f"Semester {i}")

        for course in semester:

            print("-", course)

        print()

    run_registration_demo()


if __name__ == "__main__":

    main()