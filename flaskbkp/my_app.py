from flask import flash, Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from dao.ContatoDao import ContactDAO
from model import Contact

#create app
app = Flask(__name__)

app.secret_key = 'teste'

#connection db

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='123456'
app.config['MYSQL_DB']='aula_bd'
app.config['MYSQL_PORT']=3306

db = MySQL(app)

dao = ContactDAO(db)

#routes
@app.route('/home')
def find():
    contact_list = dao.find()
    return render_template('list.html', title='Contacts', list=contact_list)

@app.route('/new_contact')
def new_contact():
    return render_template('create.html', title='Create Contact')

@app.route('/create', methods=['POST',])
def create():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    date_of_birth = request.form['date_of_birth']

    contact = Contact(name, phone, email, date_of_birth)
    dao.create(contact)
    return redirect('/home')

@app.route('/edit/<int:id>')
def edit(id):
    contact = dao.findOne(id)
    return render_template('edit.html', titulo="Update Contact", contact=contact)

@app.route('/update', methods=['POST',])
def update():
    id = request.form['id']
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    date_of_birth = request.form['date_of_birth']

    contact = Contact(name, phone, email, date_of_birth, id)
    dao.create(contact)
    return redirect('/home')

@app.route('/delete/<int:id>')
def delete(id):
    contact = dao.delete(id)
    flash('Contact deleted was succesfully.')
    return redirect('/home')

app.run(debug=True)
