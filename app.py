class OnlineCourseRegistrationSystem:
    def __init__(self):
        self.users = {}
        self.courses = {}

    def register_user(self, username, password, is_admin=False):
        
        if username not in self.users:
                 self.users[username] = {'password': password, 'is_admin': is_admin, 'enrolled_courses': []}
                 print(f"User {username} registered successfully.")
        else:
                 print(f"Username {username} is already taken. Please choose a different one.")

    def login(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            print(f"Welcome, {username}!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def add_course(self, code, title, instructor, capacity):
        if code not in self.courses:
            self.courses[code] = {'title': title, 'instructor': instructor, 'capacity': capacity, 'enrolled_students': []}
            print(f"Course {code}: {title} added successfully.")
        else:
            print(f"Course {code} already exists. Please use a different course code.")

    def view_courses(self):
        print("\nAvailable Courses:")
        for code, course in self.courses.items():
            print(f"{code}: {course['title']} - {course['instructor']} - Capacity: {course['capacity']}")

    def enroll_course(self, username, course_code):
        if username in self.users and course_code in self.courses:
            user = self.users[username]
            course = self.courses[course_code]

            if len(user['enrolled_courses']) < 3 and len(course['enrolled_students']) < course['capacity']:
                user['enrolled_courses'].append(course_code)
                course['enrolled_students'].append(username)
                print(f"{username} enrolled in {course_code}: {course['title']}")
            else:
                print("Enrollment failed. Check course capacity or user's course limit.")
        else:
            print("Invalid username or course code.")
    def choice(self,d):
        if d==1:
                num= int(input('enter number of courses u want to enter: '))
                for i in range(0,num):
                            code= str (input('Enter course code: '))
                            name = str(input('Enter course name: '))
                            ins= str(input('Instructor name: '))
                            cap= int(input('Enter capacity: '))
                            system.add_course(code,name, ins, cap)
                            i=+1  
                            print( "programs added successfully. \n")
                return True
        
        if d ==2:
                system.view_courses()
                print('\n')
                return True

        if d==3:
            system.view_courses()

            enroll= str(input('Enter course code u want to enroll: '))
            system.enroll_course(user, enroll)
            print('\n')
            return True
        
        else:
            print('System exits.')
            print('\n')
            return False
              
                

# Example Usage
system = OnlineCourseRegistrationSystem()

user = str(input("enter the user name: "))
passw = str(input("put password: "))
system.register_user(user, passw)
print('\n')

loguser = str(input("user name : "))
logpass= str(input('password: '))
c= system.login(loguser, logpass)
print('\n')

if c==True:
    a= int(input('Enter: 1 for registering new course . \n       2 for enrolling into a course. '))
    if a==1:
            num= int(input('enter number of courses u want to enter: '))
            for i in range(0,num):
                            code= str (input('Enter course code: '))
                            name = str(input('Enter course name: '))
                            ins= str(input('Instructor name: '))
                            cap= int(input('Enter capacity: '))
                            system.add_course(code,name, ins, cap)
                            i=+1  
                            print( "programs added successfully. \n")
                            
    else:        
                    system.view_courses()

                    enroll= str(input('Enter course code u want to enroll: '))
                    system.enroll_course(user, enroll)

    d= int(input('1. Enter 1 to if want to add more courses.\n2. Enter 2 to view courses.\n3. Enter 3 to view courses and enroll in course.\n4. Enter 4 to exit. '))
    e= system.choice(d)
