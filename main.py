from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import smtplib
app = Flask("__name__")
Bootstrap(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
EMAIL = "admin@gmail.com"
PASSWORD = "password"



class Form(FlaskForm):
    name = StringField("Your Name", [DataRequired()])
    email = StringField("Your Email", [DataRequired()])
    message = StringField("Message", [DataRequired()])
    submit = SubmitField("Send")


@app.route('/')
def profile():
    return render_template("index.html", page="profile")


@app.route('/contact', methods=["POST", "GET"])
def contact():
    form = Form()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        print(f"{name}, {email}, {message}")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # connection.connect("smtp.gmail.com", 465)
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject: {name} has sent you a message!\n\n{message}\n\nEmail: {email}")
        return render_template("sent.html", page="contact")
    return render_template("contact.html", page="contact", name="Mail!", form=form)










if __name__ == "__main__":
    app.run(debug=True)