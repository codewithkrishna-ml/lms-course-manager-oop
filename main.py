#PROJECT-Online Course / LMS System
class CourseDetails:
    def __init__(self, course_id, course_name, instructor):
        self.course_id = int(course_id)
        self.course_name = course_name
        self.instructor = instructor
        self.enrolled_students = []

    def __str__(self):
        return f"Course ID: {self.course_id} | Title: {self.course_name} | Instructor: {self.instructor} | Enrolled: {len(self.enrolled_students)}"


class LMSManager:
    def __init__(self):
        self.course_db = {}
        self.id_counter = 101

    def add_course(self, course_name, instructor):
        if course_name == "" or instructor == "":
            print("Error: Course name or Instructor cannot be blank.")
            return False

        current_id = self.id_counter
        new_course = CourseDetails(current_id, course_name, instructor)
        
        self.course_db[current_id] = new_course
        self.id_counter += 1

        print(f"Course created successfully with ID: {current_id}")
        return True

    def enroll_student(self, course_id, student_name):
        if course_id not in self.course_db:
            print("Error: This course ID does not exist.")
            return False

        if student_name == "":
            print("Error: Student name cannot be empty.")
            return False

        course = self.course_db[course_id]

        if student_name in course.enrolled_students:
            print(f"Error: {student_name} is already enrolled in this course.")
            return False

        course.enrolled_students.append(student_name)
        print(f"Success! {student_name} has been enrolled in '{course.course_name}'.")
        return True

    def view_all_courses(self):
        if len(self.course_db) == 0:
            print("No courses available currently.")
            return

        print("\n----------------------------- AVAILABLE COURSES ---------------------------------------")
        for c_id in self.course_db:
            print(self.course_db[c_id])
        print("----------------------------------------------------------------------------------------")

    def view_course_roster(self, course_id):
        if course_id not in self.course_db:
            print("Error: Course ID not found.")
            return

        course = self.course_db[course_id]
        print(f"\n-------- Student Roster for Course ID {course_id} ({course.course_name}) -----------")
        if len(course.enrolled_students) == 0:
            print("No students have enrolled in this course yet.")
            return

        for student in course.enrolled_students:
            print(f"-> {student}")

    def export_data_csv(self):
        if len(self.course_db) == 0:
            print("No course records found to export.")
            return False

        try:
            file = open("lms_course_ledger.csv", mode="w")
            file.write("CourseID,CourseName,Instructor,TotalStudents\n")
            for c_id in self.course_db:
                course = self.course_db[c_id]
                file.write(f"{course.course_id},{course.course_name},{course.instructor},{len(course.enrolled_students)}\n")
            file.close()
            print("LMS logs successfully exported to 'lms_course_ledger.csv'")
            return True
        except:
            print("Error: writing data matrix to csv storage.")
            return False


manager = LMSManager()

while True:
    print("\n---------------------- ONLINE COURSE / LMS MENU ----------------------------")
    print("1. Add New Course")
    print("2. View All Available Courses")
    print("3. Enroll Student in a Course")
    print("4. View Registered Students for a Specific Course")
    print("5. Export LMS Data to CSV")
    print("6. Exit")

    choice = input("Select an option (1-6): ").strip()

    if choice == "1":
        c_title = input("Enter Course Name: ").strip()
        i_name = input("Enter Instructor Name: ").strip()
        manager.add_course(c_title, i_name)

    elif choice == "2":
        manager.view_all_courses()

    elif choice == "3":
        try:
            c_id = int(input("Enter target Course ID: ").strip())
            s_name = input("Enter Student Full Name: ").strip()
            manager.enroll_student(c_id, s_name)
        except ValueError:
            print("Error: Course ID must be a valid number.")

    elif choice == "4":
        try:
            c_id = int(input("Enter Course ID to view roster: ").strip())
            manager.view_course_roster(c_id)
        except ValueError:
            print("Error: Course ID must be a valid number.")

    elif choice == "5":
        manager.export_data_csv()

    elif choice == "6":
        print("Safely shutting down LMS portal. Goodbye!")
        break
    else:
        print("Invalid choice! Please select an entry index between 1 and 6.")

