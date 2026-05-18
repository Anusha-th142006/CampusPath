def detect_cycle(graph):

    visited = set()
    rec_stack = set()

    def dfs(node):

        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                if dfs(neighbor):
                    return True

            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)

        return False

    for course in graph:

        if course not in visited:

            if dfs(course):
                return True

    return False