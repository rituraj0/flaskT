from random import randint
import os
from flask import Flask, render_template, flash, session, redirect, url_for
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from flask.ext.wtf import Form
from flask.ext.wtf.recaptcha import RecaptchaField


DEBUG = True
SECRET_KEY = 'secret'

# keys for localhost. Change as appropriate.

RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'

app = Flask(__name__)
app.config.from_object(__name__)


class CommentForm(Form):

    comment = TextAreaField("Comment", validators=[DataRequired()])
    recaptcha = RecaptchaField()


@app.route("/")
def index(myform=None):
    if myform is None:
        myform = CommentForm()
    comments = session.get("comments", [])
    return render_template("index.html",
                           comments=comments,
                           myform=myform)


@app.route("/add/", methods=("POST",))
def add_comment():

    myform = CommentForm()
    if myform.validate_on_submit():
        comments = session.pop('comments', [])
        print( comments);
        comments.append(myform.comment.data)
        session['comments'] = comments
        flash("You have added a new comment")
        return redirect(url_for("index"))
    return index(myform)


if __name__ == "__main__":
    #port = int(os.environ.get('PORT', randint(5000,9999) ));
    port = int(6563);
    app.run(host='127.0.0.1', port=port)
