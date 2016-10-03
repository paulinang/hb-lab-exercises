def print_ratings(filename):
    """Prints restaurant ratings from given file."""

    with open(filename) as text_file:

        # create dictionary of restaurant ratings
        restaurant_scores = {}

        for line in text_file:
            restaurant, rating = line.strip().split(":")
            restaurant_scores[restaurant] = int(rating)

        # get new restaurant and rating from user
        new_name = raw_input('Enter restaurant name: ')
        new_rating = int(raw_input('Enter the rating: '))
        restaurant_scores[new_name] = new_rating

        # print sorted list of tuples containing restaurant info
        for restaurant, rating in sorted(restaurant_scores.iteritems()):
            print "{} is rated at {}.".format(restaurant, rating)

print_ratings('scores.txt')

