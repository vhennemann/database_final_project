from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
 
 
app.secret_key = 'Project2021'
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Seas2023!!LETSGO'
app.config['MYSQL_DB'] = 'university'
 
 
mysql = MySQL(app)


#seas


@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print('In post')    
        c = mydb.cursor()
        print('here')
        user = request.form["email"]
        session['user'] = request.form["email"]
         
        print('user name obtained')
        password = request.form["password"]
        c.execute(
                'SELECT UID FROM student WHERE email = %s and password = %s', (user, password))
        result = c.fetchone()
        
       
        print(result)
        c.close()
        if result is None:
            return render_template('index.html', session=session['user'])
        
        return render_template('home.html')
    print("rendering login")      
    return render_template('index.html')

@app.route('/keywordSearch', methods=["GET", "POST"])
def keywordSearch():
    if request.method == "POST":
        
            print("here")
            c = mydb.cursor()
            keyword = request.form['searchKeyword']
            print(keyword)
            
            c.execute(
                'SELECT * FROM courseCatalog WHERE title LIKE  %s', ("%" + keyword + "%",))
                
            keyword = c.fetchall()
            print(keyword)
            return render_template("addDrop.html", result = keyword)

            
                        
    return render_template("sections.html")

@app.route('/add/<id>')
def add(id):

    courses = session['my_courses']
    c = mydb.cursor()        
    c.execute(
        'SELECT * FROM courseCatalog WHERE CRN = %s', (id,))  
                
    course = c.fetchall()

    for i in course:
        Subject = i[2]
        CourseNumber = i[1]
        CourseTitle = i[3]
        CourseCredit= i[4]
    
   
    courses.append([Subject, CourseNumber, CourseTitle, CourseCredit])

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
    user = session['user']
    print("USER:")
    print( user)
    if user is not NULL:
        c = mydb.cursor()       
        c.execute(
            'SELECT UID FROM student WHERE email = %s', (user,))  
        students = c.fetchone()

        print("STUDENT")
        print(students)
        student = students[0]

        c.execute(
            'SELECT * FROM my_Courses WHERE UID = %s', (student,)) 

        courses= c.fetchall()

        print("COURSES")
        print(courses)
        return render_template("transcripts.html", courses=courses)
    return render_template("transcripts.html")

@app.route('/searchSections')
def searchSections():
    session['my_courses'] = []
    if request.method == "POST":
        c = mydb.cursor()
        if request.form['courseSubject'] or request.form['courseNumber'] or request.form['courseTitle'] or request.form['searchKeyword']:
            courseSubject = request.form['courseSubject']
            c.execute(
                'SELECT * FROM courseCatalog WHERE courseSubject = %s' , (courseSubject, ))
            subject = c.fetchall()

            courseNumber = request.form['courseNumber']
            c.execute(
                'SELECT * FROM courseCatalog WHERE courseNumber = %s' , (courseNumber, ))
            number = c.fetchall()
        
            courseTitle = request.form['courseTitle']
            c.execute(
                'SELECT * FROM courseCatalog WHERE courseTitle = %s' , (courseTitle, ))
            title = c.fetchall()
      
            keyword = request.form['searchKeyword']
            c.execute(
                "SELECT * FROM courseCatalog WHERE title LIKE 's%'",(keyword,))
            keyword = c.fetchall()
            

            
                        
    return render_template("sections.html")

@app.route('/submit')
def addClass():
    user = session['user']
    courses = session['my_courses']
    if user is not NULL:
        c = mydb.cursor()       
        c.execute(
            'SELECT UID FROM student WHERE email = %s', (user,))  
        students = c.fetchone()

        print("STUDENT")
        print(students)
        student = students[0]

        for i in courses:

            c.execute('INSERT INTO `my_Courses` (UID, subject, courseNum, Title, Credits, Term, Year, Grade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', 
                    (student, i[0], i[1], i[2],i[3], 'Fall', '2020', 'IP'))

            mydb.commit()
        return render_template("transcripts.html", courses=courses)


if __name__ == "__main__":
    app.run()

