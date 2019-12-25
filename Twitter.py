# Kathleen Hablutzel
# Twitter.py
# CSC 111 Assignment 7
# 1 Nov 2019
#
# Given a text file of tweets, 'Tweets_Thu24Oct2019_100s.txt', this program
# asks the user for a string to count within the tweet text, prints this count,
# and then prints the 10 most-frequent hashtags from all the tweets.
# (An exercise on reading data from text files and using dictionaries.)

def dCounts(Lst):
    '''creates dictionary of tallies of items in Lst'''
    d = {}
    for tag in Lst:
        # add to tally if tag in d
        if tag in d:
            d[tag] += 1
        # add tag with tally one if tag not in d yet
        else:
            d[tag] = 1
            
    return d

def sortPrintD(d, n):
    '''sorts dictionary d of tallies and prints top n from most- to nth
    most-frequent'''
    count = 0
    # code given in assignment - sort d.items() in reverse and print key:value
    for key, value in sorted(d.items(), reverse=True, key=lambda item: item[1]):
        print(key, ':', value)
        count += 1
        # stop at nth most-frequent
        if count == n:
            break

def main():
    '''runs analysis of twitter feed data, counting a specific word (as indicated
    by user input) and printing top 10 most frequent hashtags'''
    # open and read whole file to get line count
    f = open('Tweets_Thu24Oct2019_100s.txt', 'r')
    tweets = f.read()
    # assume every line, including end, has \n at end
    nLines = tweets.count('\n')
    f.close()

    # word to count
    print(30*'=')
    word = input('Enter search string: ')
    word = word.lower() # case-insensitive

    # word counter and tag tracker
    wCount = 0
    allTags = []

    # open file again to go line-by-line
    f = open('Tweets_Thu24Oct2019_100s.txt', 'r')

    # read every line
    for i in range(nLines):
        line = f.readline()
        
        # for 'text: ' lines:
        if line[0:6] == 'text: ':
            # remove 'text: ' and ending '\n'
            line = line[6:-1]
            # remove 'RT ' if present
            if line[0:3] == 'RT ':
                line = line[3:]
            # case-insensitive
            line = line.lower()
            # add count of word within line
            wCount += line.count(word) 

        # for 'hashtags: ' lines:
        elif line[0:10] == 'hashtags: ':
            # remove 'hashtags: ' and ending '\n'
            # note '\n' is one character, not two
            line = line[10:-1]
            # make list
            tags = eval(line)
            # append tags list to big tag list
            allTags += tags 

    f.close()

    # print word search result
    print('The string', word, 'occurs in tweets', wCount, 'times.')
    print(30*'=')

    # create dictionary of hashtags and their counts
    d = dCounts(allTags)

    # print top 10 dictionary entries sorted by most to least frequent
    sortPrintD(d, 10)

main()
