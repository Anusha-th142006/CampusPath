def semester_plan(courses, limit):

    semesters = []

    temp = []

    for course in courses:

        temp.append(course)

        if len(temp) == limit:

            semesters.append(temp)

            temp = []

    if temp:

        semesters.append(temp)

    return semesters