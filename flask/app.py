from flask import Flask, render_template, request
import pandas as pd
import os
import pymysql

app = Flask(__name__)
conn = pymysql.connect('localhost','root','','nstrudb')

@app.route("/")
def index():
    info = {
        'title' : 'My first python web appliaction'
    }
    return render_template('index.html', data=info)

@app.route("/province")
def province_index():
    df = pd.read_excel("province.xlsx")

    area_min = df['area'].min()
    area_max = df['area'].max()

    province_min = df[df['area']==area_min]
    province_max = df[df['area']==area_max]

    info = {
        'title' : 'Thailand Province',
        'path' : os.path.join(''),
        'detail' : {
            'province_min' : province_min[['province']],
            'province_max' : province_max[['province']],
            'area_min' : area_min,
            'area_max' : area_max,
        }
    }
    return render_template('view.html', data=info)

@app.route("/student")
def student_index():
    with conn:
        cur=conn.cursor()
        cur.execute("select * from student")        
        rows=cur.fetchall()
        info = {
            'title' : 'Student',
            'path' : os.path.join(''),
            'detail' : {
                'student' : rows
            }
        }    
        return render_template('student.html', data=info)

@app.route("/student/edit/<int:student_id>", methods=['GET', 'POST'])
def student_edit(student_id):
    with conn:       
        cur=conn.cursor()

        if request.method == "POST":
            form_data = {
                'student_code' : request.form['student_code'],
                'first_name' : request.form['first_name'],
                'last_name' : request.form['last_name'],
            }

            sql = """update student set 
                first_name = '{}',
                last_name = '{}'
                where student_code='{}'
            """.format(form_data['first_name'], form_data['last_name'], form_data['student_code'])

            #cur=conn.cursor()
            cur.execute(sql) 
            row = []

        else:
            form_data = {}
            sql = "select * from student where student_code='{}'".format(student_id)
            cur.execute(sql)        
            row=cur.fetchone()

        info = {
            'title' : 'Student',
            'path' : os.path.join(''),
            'detail' : {
                'sql' : sql,
                'post_data' : form_data,
                'student' : row
            }
        }    
        return render_template('student_edit.html', data=info)        

if __name__ == "__main__":
    app.run(debug=True)