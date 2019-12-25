# Kathleen Hablutzel
# TwitterExtra2.py
# CSC 111 Assignment 7 Extra Credit - Part 2
# 2 Nov 2019
#
# This extension on Twitter.py finds and prints the ten most common retweets
# From the given data in the 'Tweets_Thu24Oct2019_100s.txt' file

def dCounts(Lst):
    '''creates dictionary of tallies of list items'''
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
    '''runs analysis of twitter feed data, counting a word from the user and
    the hashtags of the tweets'''
    # open and read whole file to get line count
    f = open('Tweets_Thu24Oct2019_100s.txt', 'r')
    tweets = f.read()
    # assume every line, including end, has \n at end
    nLines = tweets.count('\n')
    f.close()

    # word counter and tag tracker
    allLines = []

    # open file again to go line-by-line
    f = open('Tweets_Thu24Oct2019_100s.txt', 'r')

    # read every line
    for i in range(nLines):
        line = f.readline()
        
        # for 'text: ' lines:
        if line[0:6] == 'text: ':
            # remove 'text: ' and ending '\n'
            line = line[6:-1]
            # only use if it's a 'RT '
            if line[0:3] == 'RT ':
                line = line[3:]
                # case-insensitive
                allLines += [line]

    f.close()

    # create dictionary of lines and their counts
    d = dCounts(allLines)

    # print top 10 dictionary entries sorted by most to least frequent
    sortPrintD(d, 10)

    print(d)

main()
