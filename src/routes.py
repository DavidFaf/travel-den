from flask import render_template, url_for, flash, redirect
from src import app
from src.forms import AddMessageForm
from src import db
from src.models import FormMessage


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
    app.run(debug=True, port=3000)