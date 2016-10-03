def print_ratings(filename):
    """Prints restaurant ratings from given file."""
    
    with open(filename) as text_file:

        # create dictionary of restaurant ratings
        restaurant_scores = {}

        for line in text_file:
            restaurant, rating = line.strip().split(":")
            restaurant_scores[restaurant] = rating

        # print sorted list of tuples containing restaurant info
        for restaurant, rating in sorted(restaurant_scores.iteritems()):
            print "{} is rated at {}.".format(restaurant, rating)

print_ratings('scores.txt')