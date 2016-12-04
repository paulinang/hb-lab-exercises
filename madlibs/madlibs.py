from random import choice, sample
from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

MADLIBS = [
    'madlib.html', 'madlib2.html', 'madlib3.html'
]

@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)

@app.route('/game')
def show_madlib_form():
    """madlib game """

    play_game = request.args.get("play-game")

    if play_game == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html") 

@app.route('/madlib')
def show_madlib():
    """finished madlib"""

    
    person = request.args.get("name")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjectives = request.args.getlist("adjectives")

    random_madlib = choice(MADLIBS)

    return render_template(random_madlib,
                            name=person,
                            color=color,
                            noun=noun,
                            adjectives=adjectives,
                            )

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
