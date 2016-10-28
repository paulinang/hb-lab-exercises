"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy
from correlation import pearson

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """User of ratings website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id,
                                               self.email)

    def similarity(self, other_user):
        """Compare a user's rating to another user's """
        u_ratings = self.ratings

        u_dict = {}
        for r in u_ratings:
            u_dict[r.movie_id] = r

        # other_ratings = Rating.query.filter_by(movie_id = m.movie_id).all()
        # other_users = [r.user for r in other_ratings]

        matched_scores = []
        for o_r in other_user.ratings:
            u_rating = u_dict.get(o_r.movie_id)

            if u_rating:
                matched_scores.append((u_rating.score, o_r.score))

        if matched_scores:
            return pearson(matched_scores)

        return 0


    def predict_rating(self, movie):
        """Predict user's rating of a movie."""

        other_ratings = movie.ratings

        similarities = [
            (self.similarity(r.user), r)
            for r in other_ratings
        ]

        similarities.sort(reverse=True)

        positive = sum([r.score * sim for sim, r in similarities
                        if sim > 0])

        negative = sum([abs(r.score - 6) * abs(sim) for sim, r in similarities
                        if sim < 0])

        if not similarities:
            return None

        numerator = positive + negative
        denominator = sum([abs(sim) for sim, r in similarities])

        return numerator/denominator




# Put your Movie and Rating model classes here.

class Movie(db.Model):
    """Movies of ratings website."""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    released_at = db.Column(db.DateTime, nullable=True)
    imdb_url = db.Column(db.String(256), nullable=True)

class Rating(db.Model):
    """Ratings of ratings website."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    movie_id = db.Column(db.Integer,
                         db.ForeignKey('movies.movie_id'),
                         nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    score = db.Column(db.Integer, nullable=False)

    user = db.relationship("User",
                            backref=db.backref("ratings",
                                                order_by=rating_id))
    movie = db.relationship("Movie",
                             backref=db.backref("ratings",
                                                 order_by=rating_id))

    def __repr__(self):
        """Provide helpful representation when printed."""

        s = "<Rating rating_id=%s movie_id=%s user_id=%s score=%s>"
        return s % (self.rating_id, self.movie_id, self.user_id,
                    self.score)

##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ratings'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
