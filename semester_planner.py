def semester_plan(course_order, max_courses=4):

    semesters = []

    for i in range(0, len(course_order), max_courses):

        semester = course_order[i:i + max_courses]

        semesters.append(semester)

    return semesters