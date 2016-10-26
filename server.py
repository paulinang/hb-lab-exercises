"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)

from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
# So if you pass in an undefined variable
# Jinja doesn't just leave the field empty, it throws an error 
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template('homepage.html')


@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)


@app.route("/users/<user_id>")
def user_details(user_id):
    """Shows user details"""
    user = User.query.get(user_id)

    return render_template("user_details.html", user=user)


@app.route("/movies")
def movie_list():
    """Show list of movies."""

    movies = Movie.query.order_by(Movie.released_at).all()
    return render_template("movie_list.html", movies=movies)


@app.route("/movies/<movie_id>")
def movie_details(movie_id):
    """Shows movies details"""
    movie = Movie.query.get(movie_id)

    return render_template("movie_details.html", movie=movie)


@app.route("/register", methods=['GET'])
def register_form():
    """Show register form."""

    return render_template("register_form.html")


@app.route("/register", methods=['POST'])
def register_process():
    """Create user and redirect to homepage."""

    # get arguments from register_form
    email = request.form.get('email')
    password = request.form.get('password')
    age = int(request.form.get('age'))
    zipcode = request.form.get('zipcode')

    # check if user exists
    if not db.session.query(User).filter(User.email == email).first():
    # add user to db
        user = User(email=email,
                    password=password,
                    age=age,
                    zipcode=zipcode)
        print user
        db.session.add(user)
        db.session.commit()
        flash('Account successfully created.')
    else: 
        flash('Account with that email already exists.')

    # redirect to homepage

    return redirect('/')


@app.route("/login", methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login_form.html")


@app.route("/login", methods=['POST'])
def login_process():
    """Login user and redirect to homepage."""

    # get arguments from register_form
    email = request.form.get('email')
    password = request.form.get('password')


    user_query = db.session.query(User).filter(User.email==email).first()


    if not email or not password:
        flash('Nice try getting around our form, hacker.')

    elif user_query and user_query.password == password:
        session['user_id'] = user_query.user_id

        print '\n\n\n',session,'\n\n\n'
        flash('Log in successful')

        return redirect("/users/%s" % user_query.user_id)

    elif user_query:
        flash('YOU WRONG, FOOL')

    else:
        flash('YOU DON\'T EXIST, GO MAKE AN ACCOUNT')

    return redirect('/')

@app.route("/logout")
def logout_process():
    """Remove user_id from session"""

    if 'user_id' in session:
        user_id = session.pop('user_id')
        print session

        flash ('Logged Out')
    else: 
        flash ('Not logged in')
    return redirect('/')

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)


    
    app.run(port=5000)
