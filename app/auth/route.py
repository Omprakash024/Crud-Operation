from crypt import methods
from dataclasses import dataclass
from flask import redirect, render_template, request,flash, url_for
from app.auth.forms import LoginForm, Registration
from app.auth import authentication as at

from app.auth.models import UserCredential

from flask_login import current_user, login_required, login_user, logout_user

@at.route("/register", methods=['GET','POST'])
def registration_func():
    name = None
    email = None
    if current_user.is_authenticated:
        flash('your are already registered')
        return redirect(url_for('main.home'))

    form = Registration()
    # if request.method == "POST":
    #     # print(form)        # <app.auth.forms.Registration object at 0x7f8eac1b8dc0>
    #     name = form.name.data
    #     email = form.email.data
    #     # print(name,email)
    if form.validate_on_submit():
        UserCredential.create_user(
            name = form.name.data,
            email = form.email.data,
            password= form.password.data
        )
        flash("Register Successully!")
        return redirect(url_for('authentication.login_func'))
    return  render_template('registration.html', form=form,name=name,email=email)



@at.route("/login", methods=['GET','POST'])
def login_func():
     
    if current_user.is_authenticated:
        flash('your are already Logged in')
        return redirect(url_for('main.home'))

    form = LoginForm()
    print(form.password.data)
    if form.validate_on_submit():
        user = UserCredential.query.filter_by(user_email = form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash("Invalid Credentials. Please try again!")
            return redirect(url_for('authentication.login_func'))
        login_user(user,form.stay_loggedin.data)
        return redirect(url_for('main.home'))
    return render_template('login.html',form=form)

@at.route("/logout", methods=['GET','POST'])
@login_required
def logout_func():
    logout_user()
    return redirect(url_for('main.home'))


@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404