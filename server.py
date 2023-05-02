from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def about(page_name):
    return render_template(page_name)

#lect 279
def write_to_file(data):
    with open('database.txt', mode = 'a') as db :
        email=data["email"] 
        sub=data["subject"] 
        msg=data["message"]
        file = db.write(f'\n{email}, {sub}, {msg}') 

#lect 280
def write_to_csv(data):
    with open('database.csv', newline='', mode = 'a') as db2 :
        email=data["email"] 
        sub=data["subject"] 
        msg=data["message"]
        csv_writer = csv.writer(db2, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, sub, msg]) 

#lect 278
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST' :
        data = request.form.to_dict()
        #write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')

    else :
        return 'Something went wrong. Try again'





