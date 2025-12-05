from flask import render_template, request, redirect, flash

from dao.ContatoDao import ContactDAO
from model import Contact
from flaskApp.utils.valida_dados import ValidaDados
def init_contato_routes(app, db):
    dao = ContactDAO(db)

    # routes
    @app.route('/home')
    def find():
        contact_list = dao.find()
        return render_template('list.html', title='Contacts', list=contact_list)

    @app.route('/new_contact')
    def new_contact():
        return render_template('create.html', title='Create Contact', contact = None)

    @app.route('/create', methods=['POST', ])
    def create():
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        contact = Contact(name, phone, email, date_of_birth)

        if ValidaDados.eh_telefone(phone):

            dao.create(contact)
            flash('Contato criado com sucesso.')
            return redirect('/home')
        else:
            flash('Contato Inválido.')
            return render_template('create.html', title='Create Contact', contact=contact)

    @app.route('/edit/<int:id>')
    def edit(id):
        contact = dao.findOne(id)
        return render_template('edit.html', titulo="Update Contact", contact=contact)

    @app.route('/update', methods=['POST', ])
    def update():
        id = request.form['id']
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']

        contact = Contact(name, phone, email, date_of_birth, id)
        dao.create(contact)
        flash('Contato atualizado com sucesso')
        return redirect('/home')

    @app.route('/delete/<int:id>')
    def delete(id):
        contact = dao.delete(id)
        flash('Contato deletado com sucesso.')
        return redirect('/home')