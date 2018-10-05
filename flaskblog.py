from flask import Flask, render_template, url_for, flash, redirect
import datetime
from forms import RegistrationForm, LoginForm

# url_for is a function that can find the location of routes. We used it in main.css to find and map static folder and related css file.

app = Flask(__name__)  # __name__ = __main__ when we run this script directly

app.config['SECRET_KEY'] = '123456789'

posts = [
    {
        'author': 'Abhi',
        'title': "blog post",
        'content': "first post",
        "date_posted": datetime.datetime.now(),
    },
    {
        'author': 'Corey Schafer',
        'title': "blog post",
        'content': "second post",
        "date_posted": datetime.datetime.now(),
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts) # value in post will be available to html template.

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    """flash function accepts a second argument that is called category, we are passing "Success", the name of bootstrap class to this fucntion"""
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Account created for {}!".format(form.username.data), 'success')
        return redirect(url_for('home')) # home is the name of the function above. we will be using layout template to pop up message on any page
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("you Have Been Logged In!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check credentials", "danger")
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
