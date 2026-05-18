def topological_sort(graph):

    visited = set()

    stack = []

    def dfs(node):

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                dfs(neighbor)

        stack.append(node)

    for course in graph:

        if course not in visited:

            dfs(course)

    return stack