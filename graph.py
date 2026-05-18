def load_graph(filename):

    graph = {}

    with open(filename, 'r') as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            parts = line.split(":")

            course = parts[0].strip()

            if len(parts[1].strip()) == 0:
                prereqs = []

            else:
                prereqs = [x.strip() for x in parts[1].split(",")]

            graph[course] = prereqs

    return graph


def display_graph(graph):

    print("\nCourse Dependency Graph:\n")

    for course, prereqs in graph.items():

        print(f"{course} -> {prereqs}")