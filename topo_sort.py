def topological_sort(graph):

    visited = set()

    stack = []

    def dfs(node):

        visited.add(node)

        for prereq in graph[node]:

            if prereq not in visited:

                dfs(prereq)

        stack.append(node)

    for course in graph:

        if course not in visited:

            dfs(course)

    return stack