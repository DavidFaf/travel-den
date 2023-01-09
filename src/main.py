from models import setup_db, FormMessage, db_drop_and_create_all
from flask import Flask, request
from flask_cors import CORS
from models import db


from flask import render_template, url_for, flash, redirect
from forms import AddMessageForm
from models import FormMessage


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
setup_db(app)  
db_drop_and_create_all(app)

@app.route("/",methods=['GET', 'POST'])
@app.route("/home" ,methods=['GET', 'POST'])
def home():

    form = AddMessageForm()

    # print("before validation")
    # print("------")
    # print(form.fullname.data)


    if form.validate_on_submit():
        create_message = FormMessage(fullname=form.fullname.data, 
        email=form.email.data, countries=form.countries.data,)

        db.session.add(create_message)
        db.session.commit()

        flash('Form has been submitted',category='success')
        # print(form.email.data)

        # if not form.fullname.data:
        #     flash('Fullname is required!')
        # elif not form.email.data:
        #     flash('Email is required!')
        # elif not form.countries.data:
        #     flash('Countries is required!')
        # else:

        return redirect(url_for('home'))

    return render_template('form.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)

