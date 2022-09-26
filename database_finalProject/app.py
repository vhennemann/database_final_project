from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3 as sql


app = Flask(__name__)
app.secret_key = 'seas'



# def get_db_connection():
#     conn = sqlite3.connect('finalproject.db')
#     conn.row_factory = sqlite3.Row
#     return conn


@app.route('/')
def index():
    if not session.get("user"):
        redirect("/login")
    return "You are not logged in <br><a href = '/login'>" + "click here to log in </a>"


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        user = request.form["email"]
        password = request.form["password"]
        print(user)
        print(password)
        connection = sql.connect("finalproject.db")
        cursor = connection.cursor()

        cursor.execute(
                'SELECT UID, role FROM users WHERE email = ? and password = ? ', (user, password))
        # print("after execute")
        result = cursor.fetchall() 
        print(result)
        role = result[0][1]; 
        UID = result[0][0];   
        print(UID)  
        cursor.close()
        if result is None:
            return render_template('index.html') 

        session['username'] = request.form['email']
        if role == 'student':
            return render_template('addDrop.html')
        elif role == 'falculty':
            connection = sql.connect("finalproject.db")
            cursor = connection.cursor()
            cursor.execute(
        '       SELECT * FROM classes WHERE UID = ?', (UID,))
            result = cursor.fetchall()
            return render_template('falculty_home.html', courses = result)

    return render_template('index.html')


@app.route('/insertGrades', methods=["GET", "POST"])
def insertGrades():
    return render_template("grades.html")

@app.route('/courseSearch', methods=["GET", "POST"])
def courseSearch():  
    print("In correct route")
    if request.method == "POST":
        if request.form['Subject'] or request.form['Number'] or request.form['courseTitle']:
            courseSubject = request.form['Subject']
            courseNumber = request.form['Number']
            courseTitle = request.form['Title']
            connection = sql.connect("finalproject.db")
            cursor = connection.cursor()
            cursor.execute(
        '       SELECT firstname, lastname, UID,Grade,  Subject, courseNum, Title, CRN FROM list_students WHERE subject = ? and courseNum =? and Title=? ', (courseSubject, courseNumber, courseTitle))
            result = cursor.fetchall()
            print(result)
            
        return render_template("insertGrades.html", students = result)
    return render_template("grades.html")


@app.route('/changeGrade/<id>/<CRN>', methods=["GET", "POST"])
def changeGrade(id, CRN): 
    print(id)
    print(CRN)
    if request.method == "POST": 
        print("IN REQUEST")
        grade = request.form.get("grade", None)
        print(grade)
        connection = sql.connect("finalproject.db")
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE my_Courses SET Grade = ? WHERE UID = ? and CRN = ?', (grade,id,CRN))
        connection.commit()
        
    
    print("NOT REQUEST")
    return render_template("grades.html")
    

@app.route('/CRN', methods=["GET", "POST"])
def CRN_search():  
    print("In correct route")
    if request.method == 'POST':
        CRN = request.form["CRN"]

    

@app.route('/courseCatalog', methods=["GET", "POST"])
def catalog():


    connection = sql.connect("finalproject.db")
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM courseCatalog')
                
    courses = cursor.fetchall()

    return render_template("courseCatalog.html", courses = courses)

@app.route('/keywordSearch', methods=["GET", "POST"])
def keywordSearch():
    if request.method == "POST":
        
            print("here")
            connection = sql.connect("finalproject.db")
            cursor = connection.cursor()
            keyword = request.form['searchKeyword']
            
            cursor.execute(
                'SELECT * FROM courseCatalog WHERE title LIKE  ?', ("%" + keyword + "%",))
                
            keyword = cursor.fetchall()
            print(keyword)
            return render_template("addDrop.html", result = keyword)

            
                        
    return render_template("sections.html")

@app.route('/add/<id>')
def add(id):

    courses = session['my_courses']
    connection = sql.connect("finalproject.db")
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM courseCatalog WHERE CRN = ?', (id,))  
                
    course = cursor.fetchall()
    print(course)

    for i in course:
        CRN = i[0]
        Subject = i[2]
        CourseNumber = i[1]
        CourseTitle = i[3]
        CourseCredit= i[4]
    
   
    courses.append([CRN, Subject, CourseNumber, CourseTitle, CourseCredit])

    session["my_courses"] = courses
    
    return render_template("addDrop.html", course = session['my_courses'])

@app.route('/drop/<index>')
def drop(index):

    courses = session['my_courses']
    
    courses.pop(int(index))
    
    
    session['my_courses']=courses

    return render_template("addDrop.html", courses=courses, course=session['my_courses'])



@app.route('/transcripts')
def transcripts():
    user = session['username']
    print("IN TRANSCRIPT")
    print(user)
    
    connection = sql.connect("finalproject.db")
    cursor = connection.cursor()     
    cursor.execute(
            'SELECT UID FROM users WHERE email = ?', (user,))  
    students = cursor.fetchone()

    student = students[0]

    cursor.execute(
        'SELECT * FROM my_Courses WHERE UID = ?', (student,)) 

    courses= cursor.fetchall()

    return render_template("transcripts.html", courses=courses)
   

@app.route('/searchSections')
def searchSections():
    session['my_courses'] = []
    if request.method == "POST":
        connection = sql.connect("finalproject.db")
        cursor = connection.cursor()
        if request.form['courseSubject'] or request.form['courseNumber'] or request.form['courseTitle'] or request.form['searchKeyword']:
            courseSubject = request.form['courseSubject']
            cursor.execute(
                'SELECT * FROM courseCatalog WHERE courseSubject = ?' , (courseSubject, ))
            subject = cursor.fetchall()

            courseNumber = request.form['courseNumber']
            cursor.execute(
                'SELECT * FROM courseCatalog WHERE courseNumber = ?' , (courseNumber, ))
            number = cursor.fetchall()
        
            courseTitle = request.form['courseTitle']
            cursor.execute(
                'SELECT * FROM courseCatalog WHERE courseTitle = ?' , (courseTitle, ))
            title = cursor.fetchall()
      
            keyword = request.form['searchKeyword']
            cursor.execute(
                "SELECT * FROM courseCatalog WHERE title LIKE '?'",(keyword,))
            keyword = cursor.fetchall()
            

            
                        
    return render_template("sections.html")

@app.route('/dropCourse')
def dropCourse():
    user = session['username']
    print("IN TRANSCRIPT")
    print(user)
    
    connection = sql.connect("finalproject.db")
    cursor = connection.cursor()     
    cursor.execute(
            'SELECT UID FROM users WHERE email = ?', (user,))  
    students = cursor.fetchone()

    student = students[0]

    cursor.execute(
        'SELECT * FROM my_Courses WHERE UID = ?', (student,)) 

    courses= cursor.fetchall()
    print(courses)
    return render_template("drop.html", courses = courses)


@app.route('/dropClass/<CRN>')
def dropClass(CRN):
    print(CRN)
    user = session['username']
    print("IN DROP CLASS")
    print(user)
    
    connection = sql.connect("finalproject.db")
    cursor = connection.cursor()     
    cursor.execute(
            'SELECT UID FROM users WHERE email = ?', (user,))  
    students = cursor.fetchone()

    student = students[0]


    cursor.execute(
        'DELETE FROM my_Courses WHERE UID = ? and CRN = ?', (student, CRN)) 
    connection.commit()

    cursor.execute(
        'SELECT * FROM my_Courses WHERE UID = ?', (student,)) 

    courses= cursor.fetchall()
    return render_template("drop.html", courses = courses)


@app.route('/submit')
def addClass():
    print("HERE")
    user = session['username']
   
    courses = session['my_courses']
    print(courses)
    
    connection = sql.connect("finalproject.db")
    cursor = connection.cursor() 
    cursor.execute(
            'SELECT UID FROM users WHERE email = ?', (user,))  
    students = cursor.fetchone()
    print(students)
    student = students[0]
    print(student)
    
    
    for i in courses:
        cursor.execute(
            'SELECT * FROM my_Courses WHERE CRN = ?', (i[0],))  
        result = cursor.fetchall()
        if len(result) == 0:
            cursor.execute('INSERT INTO my_Courses (CRN, UID, Subject, courseNum, Title, Credits, Term, Year, Grade) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                    (i[0], student, i[1], i[2], i[3],i[4], 'Spring', '2020', 'IP'))

            connection.commit()
        else:
            return render_template("addDrop.html", messages = "Class already added")
    return render_template("addDrop.html")

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect('/login')

@app.route("/test")
def test():
    username = 'john'
    password = 'test'
    id = '1'
   
    connection = sql.connect("finalproject.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users(UID, username, password) VALUES (%s, %s, %s)", (id, username, password))
    connection.commit()
    cursor.close()
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)