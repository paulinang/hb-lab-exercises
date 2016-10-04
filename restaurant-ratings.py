import random

def make_ratings_dict(filename):
    """Prints restaurant ratings from given file."""

    with open(filename) as text_file:

        # create dictionary of restaurant ratings
        restaurant_scores = {}

        for line in text_file:
            restaurant, rating = line.strip().split(":")
            restaurant_scores[restaurant] = int(rating)

    return restaurant_scores


def add_rating(restaurant_scores):
    """ Adds new restaurant to ratings dictionary."""

    # get new restaurant and rating from user
    new_name = raw_input('Enter restaurant name: ')
    new_rating = int(raw_input('Enter the rating: '))
    restaurant_scores[new_name] = new_rating


def change_random_rating(restaurant_scores):
    """Changes a random restaurant rating"""

    random_restaurant, random_rating = random.choice(restaurant_scores.items())    
    print "{} has rating {}.".format(random_restaurant, random_rating)
    
    new_rating = int(raw_input('Enter the new rating: '))
    restaurant_scores[random_restaurant] = new_rating


def print_ratings(restaurant_scores):
    """ Prints sorted restaurant ratings. """

    # print sorted list of tuples containing restaurant info
    print
    for restaurant, rating in sorted(restaurant_scores.iteritems()):
        print "{} is rated at {}.".format(restaurant, rating)


ratings_dict = make_ratings_dict('scores.txt')

while True:
    print
    print "1) View ratings. 2) Add rating. 3) Edit random rating. 4) Quit. "
    user_choice = raw_input("Enter 1, 2, 3, or 4: ")

    if user_choice == "4":
        break
    elif user_choice == "3":
        change_random_rating(ratings_dict)
        print_ratings(ratings_dict)
    elif user_choice == "2":
        add_rating(ratings_dict)
        print_ratings(ratings_dict)
    elif user_choice == "1":
        print_ratings(ratings_dict)
    else:
        print "That was not a choice."