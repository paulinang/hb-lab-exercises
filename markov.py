import random, sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as src_file:
        full_text = src_file.read()

    return full_text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

    for index in range(0, len(words) - 2):
        chains_key = (words[index], words[index + 1])

        chains[chains_key] = chains.get(chains_key, []) # Creating the dictionary key value      
        chains[chains_key].append(words[index + 2]) # Appending value/word to dictionary

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    current_key = random.choice(chains.keys()) # Selects the first key

    # Starts the text with the first item in the first key.
    text += (current_key[0] + " ") 

    while True:
        try:
            """ First iteration:
            # add_word = current_key[0]
            # current_key_list = chains[current_key]
            # next_tuple = (current_key[1], random.choice(current_key_list))
            # current_key = next_tuple
            # text += (add_word + ' ')
            """

            # continues text with 2nd item in current_key
            text += (current_key[1] + " ") 
            # Defines the list that we can choose from for the next word in the text.
            current_key_list = chains[current_key]
            # Re-defines current_key for next loop. 
            current_key = (current_key[1], random.choice(current_key_list))
            


        except KeyError:
            #Stops while loop for non-existent keys (ie, end of text)
            break

    return text


def make_chains_n(text_string, n=2):
    """Takes input text as string; returns _dictionary_ of markov chains
    with specified n-grams."""

    chains = {}
    words = text_string.split()

    for index in range(0, len(words) - n):
        # Creates chains key for arbitrary amount of words
        chains_key = tuple(words[index: index + n])

        # Creates empty list if dictionary key did not exist
        chains[chains_key] = chains.get(chains_key, [])
        # Append word to value of dictionary key
        chains[chains_key].append(words[index + n])

    return chains


def id_start_chains(chains):
    """Returns starter chains that have beginning capital letter"""

    starter_chains = []

    # creates list of chains with first word starting with capital letter
    for chain in chains:
        if chain[0][0].isupper():
            starter_chains.append(chain)

    # NOTE FOR LATER: try list comprehensions

    return starter_chains


def make_text_n(chains):
    """Takes dictionary of markov chains;
    returns random text with specified n-grams."""

    text = ""

    current_key = random.choice(id_start_chains(chains)) # Selects first key

    # Adds first to second last words of current key to text
    text += (' '.join(current_key[:-1]) + " ")

    while True:
        try:
            # Adds last word of current key to text
            text += (current_key[-1] + " ")
            # Define list of options for next key given current key
            current_key_list = chains[current_key]
            # Turn slice of current key tuple into temp list
            temp_list = list(current_key[1:])
            # Appends random word to end of temp list
            temp_list.append(random.choice(current_key_list))
            # Redefines current key as tuple of temp list
            current_key = tuple(temp_list)

        except KeyError:
            # Breaks while loop when current key does not exist in chains
            break

    return text



input_path = sys.argv[1]
n = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
# chains = make_chains(input_text)
# for key, value in chains.iteritems():
#     print key, value

# Produce random text
# random_text = make_text(chains)

n_chains = make_chains_n(input_text, n)

print make_text_n(n_chains)
# print
# print random_text
