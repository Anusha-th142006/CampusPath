def load_graph(filename):

    graph = {}

    with open(filename, "r") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            parts = line.split(":")

            course = parts[0].strip()

            prereqs = []

            if len(parts) > 1 and parts[1].strip():

                prereqs = [
                    x.strip()
                    for x in parts[1].split(",")
                ]

            graph[course] = prereqs

    return graph


def display_all_courses(graph):

    print("\n===== ALL AVAILABLE COURSES =====\n")

    for course in graph:

        print("-", course)


def get_all_completed(graph, completed_courses):

    final_completed = set(completed_courses)

    def dfs(course):

        for prereq in graph.get(course, []):

            if prereq not in final_completed:

                final_completed.add(prereq)

                dfs(prereq)

    for course in completed_courses:

        dfs(course)

    return list(final_completed)


def available_courses(graph, completed_courses):

    available = []

    for course, prereqs in graph.items():

        if course not in completed_courses:

            valid = True

            for prereq in prereqs:

                if prereq not in completed_courses:

                    valid = False
                    break

            if valid:

                available.append(course)

    return available