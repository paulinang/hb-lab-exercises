"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session, jsonify)

from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db

from correlation import pearson


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

    # all movies except the one with id 267 (has unknown title and release date)
    movies = Movie.query.filter(Movie.movie_id != 267).order_by(Movie.title).all()
    return render_template("movie_list.html", movies=movies)


@app.route("/movies/<movie_id>")
def movie_details(movie_id):
    """Shows movies details"""
    movie = Movie.query.get(movie_id)

    user_id = session.get('user_id')

    if user_id:
        user_rating = Rating.query.filter_by(
            movie_id=movie_id, user_id=user_id).first()

    else:
        user_rating = None

    # Get average rating of movie

    rating_scores = [r.score for r in movie.ratings]
    avg_rating = float(sum(rating_scores)) / len(rating_scores)

    prediction = None

    # Prediction code: only predict if the user hasn't rated it.

    if (not user_rating) and user_id:
        user = User.query.get(user_id)
        if user:
            prediction = user.predict_rating(movie)

    return render_template(
        "movie_details.html",
        movie=movie,
        user_rating=user_rating,
        average=avg_rating,
        prediction=prediction
        )


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


@app.route("/rate_movie", methods=['POST'])
def rate_movie():
    """Rates movie"""

    # movie_id is hidden input in form, user_id is from session
    # you can only access this route if you are logged in/ user_id exists in session
    movie_id = request.form.get('movie-id')
    score = request.form.get('rating')
    user_id = session['user_id']

    # get the rating record with that movie and user (return None if there's none)
    rating_query = db.session.query(Rating).filter(Rating.movie_id == movie_id,
                                                   Rating.user_id == user_id).first()

    # if rating_query exists
    if rating_query:
        # update score
        old_score = rating_query.score
        rating_query.score = score
        flash('Existing rating of %s updated to %s successfully.' % (old_score, score))
    else:
        # instantiate new rating and add to db
        new_rating = Rating(movie_id=movie_id, user_id=user_id, score=score)
        db.session.add(new_rating)
        flash('New rating of %s added successfully.' % score)

    db.session.commit()

    # redirect to details of movie you updated
    return redirect('/movies/%s' % movie_id)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)


    
    app.run(port=5000)
