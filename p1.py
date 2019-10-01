from flask import Flask, render_template,request,json 
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='Bookmyshow',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
app = Flask(__name__)

# @app.route('/',methods=['POST', 'GET'])
# def loginup():
    # return render_template('login.html')

# @app.route('/' ,methods=['POST','GET'])
# def home():
#     if request.method == 'POST':
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM ...")
#             data = cursor.fetchall() 
#     return render_template("home.html" , data = data)


@app.route('/',methods=['POST', 'GET'])
def login():
    if request.method == 'POST' :
        email = request.form['email']
        password = request.form['password']
        category = request.form['category']
        try:
            if category == 'coustmer':
                with connection.cursor() as cursor:
                    cursor.execute('SELECT * FROM coustmer_info WHERE email_id = %s AND password = %s', (email, password))
                    account = cursor.fetchone()

                    if account:
                        session['email'] = account['email_id']
                        msg = 'Logged successful'
                    else:
                        msg = 'Incorrect username/password'
            
            elif category == 'theater_owner':
                with connection.cursor() as cursor:
                    cursor.execute('SELECT * FROM theater_owner_info WHERE email_id = %s AND password = %s', (email, password))
                    account = cursor.fetchone()

                    if account:
                        session['email'] = account['email_id']
                        msg = 'logged successful'
                    else:
                        msg = 'Incorrect username/password'
            else:
                # Admin ...
                pass
        
        except:
            print('a')
    return render_template('login.html')


@app.route('/signUp',methods=['POST', 'GET'])
def signUp():
    if request.method=='POST':
        name = request.form['name']
        print(name)
        email=request.form['email']
        password=request.form['psw']
        category = request.form['category']
        try:

            if category == 'customer':
                with connection.cursor() as cursor:
                    print(email,password)
                  # Read a single record
                    sql = "INSERT INTO  customer_info (name,email_id,password) VALUES (%s,%s, %s)"
                   
                    cursor.execute(sql, (name, email,password))
                    connection.commit()
            elif category == 'theater_owner':
                with connection.cursor() as cursor:
                    print(email,password)
                  # Read a single record
                    sql = "INSERT INTO  theater_owner_info (name,email_id,password) VALUES (%s,%s, %s)"
                   
                    cursor.execute(sql, (email,password))
                    connection.commit()
            else:
                print(admin)
        finally:
            connection.close()
            return "saved successfully."
    return render_template('signupform.html')
       

if __name__ == "__main__":
    app.run(debug=True)

