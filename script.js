const courses = [

    "Programming",
    "Math",
    "Statistics",
    "DSA",
    "DBMS",
    "OS",
    "CN",
    "AI",
    "ML",
    "Compiler Design",
    "Cloud Computing",
    "Cyber Security",
    "Big Data",
    "Distributed Systems",
    "Data Mining",
    "Blockchain",
    "IoT",
    "Software Engineering",
    "Web Development",
    "Mobile App Dev",
    "Computer Graphics",
    "AR/VR"
];

const courseList =
    document.getElementById("courseList");

courses.forEach(function(course) {

    const span =
        document.createElement("span");

    span.innerText = course;

    courseList.appendChild(span);
});

function createStudentForms() {

    const count = parseInt(

        document.getElementById(
            "studentCount"
        ).value
    );

    let forms = "";

    for (let i = 1; i <= count; i++) {

        forms += `

        <div class="card">

            <h3>Student ${i}</h3>

            <input type="text"
                   id="name${i}"
                   placeholder="Enter Name">

            <input type="text"
                   id="usn${i}"
                   placeholder="Enter USN">

            <input type="text"
                   id="branch${i}"
                   placeholder="Enter Branch">

            <input type="number"
                   id="semester${i}"
                   placeholder="Current Semester">

            <label style="font-weight:bold; margin-top:10px; display:block;">

    Enter Completed Courses

</label>

<textarea
    id="completed${i}"
    placeholder="Example: DSA, Math, Programming">
</textarea>

            <input type="number"
                   id="limit${i}"
                   placeholder="Max courses per semester">

        </div>
        `;
    }

    forms += `

    <button onclick="generatePlans(${count})">

        Generate Plans

    </button>
    `;

    document.getElementById(
        "studentForms"
    ).innerHTML = forms;
}

function generatePlans(count) {

    let finalOutput = "";

    for (let i = 1; i <= count; i++) {

        const name =
            document.getElementById(
                `name${i}`
            ).value;

        const usn =
            document.getElementById(
                `usn${i}`
            ).value;

        const branch =
            document.getElementById(
                `branch${i}`
            ).value;

        const semester =
            document.getElementById(
                `semester${i}`
            ).value;

        const completedInput =
            document.getElementById(
                `completed${i}`
            ).value;

        const limit = parseInt(

            document.getElementById(
                `limit${i}`
            ).value
        );

        let completed = completedInput

            .split(",")

            .map(function(course) {

                return course
                    .trim()
                    .toLowerCase();
            });

        let completedCourses = [];

        courses.forEach(function(course) {

            if (

                completed.includes(
                    course.toLowerCase()
                )
            ) {

                completedCourses.push(course);
            }
        });

        let remainingCourses = [];

        courses.forEach(function(course) {

            if (

                !completedCourses.includes(course)
            ) {

                remainingCourses.push(course);
            }
        });

        let semesters = [];

        for (

            let j = 0;

            j < remainingCourses.length;

            j += limit
        ) {

            semesters.push(

                remainingCourses.slice(
                    j,
                    j + limit
                )
            );
        }

        finalOutput += `

        <div class="output-card">

            <h2>Student ${i}</h2>

            <p><b>Name:</b> ${name}</p>

            <p><b>USN:</b> ${usn}</p>

            <p><b>Branch:</b> ${branch}</p>

            <p><b>Semester:</b> ${semester}</p>

            <h2>Completed Courses</h2>

            <ul>

                ${completedCourses.map(function(course) {

                    return `<li>${course}</li>`;

                }).join("")}

            </ul>

            <h2>Future Course Order</h2>

            <ol>

                ${remainingCourses.map(function(course) {

                    return `<li>${course}</li>`;

                }).join("")}

            </ol>

            <h2>Future Semester Plan</h2>
        `;

        semesters.forEach(function(sem, index) {

            finalOutput += `

            <div class="semester">

                <h3>
                    Semester ${index + 1}
                </h3>

                <ul>

                    ${sem.map(function(course) {

                        return `<li>${course}</li>`;

                    }).join("")}

                </ul>

            </div>
            `;
        });

        finalOutput += `</div>`;
    }

    document.getElementById(
        "output"
    ).innerHTML = finalOutput;
}