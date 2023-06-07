import pyrebase
from flask import Flask, render_template, request

config = {
   "apiKey": "AIzaSyAjPSCIDuaM5ZgDAfFxjQHUHrgS6bSUaOQ",
    "authDomain": "dbms-assignment-22mci0018.firebaseapp.com",
    "databaseURL": "https://dbms-assignment-22mci0018-default-rtdb.firebaseio.com",
    "projectId": "dbms-assignment-22mci0018",
    "storageBucket": "dbms-assignment-22mci0018.appspot.com",
    "messagingSenderId": "373393372838",
    "appId": "1:373393372838:web:59809a61ce8aa90562e667",
    "measurementId": "G-4V80BFJZ53"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_url_path='/static', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            donor_name = request.form['donor_name']
            gender = request.form['gender']
            blood_group = request.form['blood_group']
            city = request.form['city']
            donor_data = {
                'donor_name': donor_name,
                'gender': gender,
                'blood_group': blood_group,
                'city': city
            }
            db.child("donors").push(donor_data)
        elif request.form['submit'] == 'update':
            donor_id = request.form['donor_id']
            donor_name = request.form['donor_name']
            gender = request.form['gender']
            blood_group = request.form['blood_group']
            city = request.form['city']
            donor_data = {
                'donor_name': donor_name,
                'gender': gender,
                'blood_group': blood_group,
                'city': city
            }
            db.child("donors").child(donor_id).update(donor_data)
        elif request.form['submit'] == 'delete':
            donor_id = request.form['donor_id']
            db.child("donors").child(donor_id).remove()

    donors = db.child("donors").get()
    donor_list = []
    if donors.each():
        for donor in donors.each():
            donor_list.append({'id': donor.key(), 'data': donor.val()})
    return render_template('index.html', donors=donor_list)

if __name__ == '__main__':
    app.run(debug=True)
