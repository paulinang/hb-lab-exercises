# filename = 'test.txt'
filename = 'twain.txt'

#open text file to object
txt_file = open(filename)

#initialize empty dictionary
word_count = {}

#fill dictionary with word count 
for line in txt_file:
    words = line.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

#iterate through dictionary and print each pair
for word, count in word_count.iteritems():
    print word, count
