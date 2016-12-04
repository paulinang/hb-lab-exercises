from sys import argv
from collections import Counter

filename = argv[1]
#filename = 'twain.txt'

#open text file to object
with open(filename) as txt_file:

    #initialize empty dictionary
    word_count = {}
    counter_wordlist = []

    #fill dictionary with word count 
    for line in txt_file:
        words = line.lower().strip().split()
        for word in words:
            # check for non-alphabets and remove from start and end of word
            if not word[-1].isalpha():
               word = word[:-1]
            
            if len(word) and not word[0].isalpha():
                word = word[1:]

            word_count[word] = word_count.get(word, 0) + 1
            
            counter_wordlist.append(word)

    other_word_count = Counter(counter_wordlist)

    #iterate through dictionary and print each pair
    for word, count in word_count.iteritems():
        print word, count

    print 'USING COUNTER'

    for word, count in other_word_count.iteritems():
        print word, count
