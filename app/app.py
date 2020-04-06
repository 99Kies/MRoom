from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length
from werkzeug.security import check_password_hash, generate_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')

bootstrap = Bootstrap(app)

password = generate_password_hash("123456")

class UserForm(FlaskForm):
    userid = PasswordField("User ID", validators=[DataRequired(), Length(8,30)])
    submit = SubmitField("登入")

@app.route("/", methods=["GET","POST"])
def index():
    form = UserForm()
    if form.validate_on_submit():
        userid = form.userid.data
        if check_password_hash(password, "123456"):
            return redirect(url_for("server"))
        flash("账号或者密码错误！")
    return render_template("index.html", form=form)



@app.route('/server')
def server():
    return render_template("server.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=33420)
