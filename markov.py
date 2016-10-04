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

    # your code goes here
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


def make_text_n(chains, n=2):
    """Takes dictionary of markov chains;
    returns random text with specified n-grams."""

    return might mighty text

def make_chains_n(text_string, n=2):
     """Takes input text as string; returns _dictionary_ of markov chains
     with specified n-grams."""

     


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
# for key, value in chains.iteritems():
#     print key, value

# Produce random text
random_text = make_text(chains)

print random_text
