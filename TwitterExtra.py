# Kathleen Hablutzel
# TwitterExtra.py
# CSC 111 Assignment 7 Extra Credit - Part 1
# 1 Nov 2019
#
# This extension on Twitter.py creates a bar graph of mentions of each Democratic
# candidate (using candidates as of November 1, 2019).

import matplotlib.pyplot as plt
# Also depends on 'Tweets_Thu24Oct2019_100s.txt' file

def nameCount(name, nLines):
    '''Return count of name in text of tweets from Twitter file.
    Needs nLines to know line length of file.'''
    
    # word counter
    wCount = 0

    # names that are too common to count alone
    common = ['michael', 'steve', 'john',  'andrew', 'amy', 'tom', '']

    # case-insensitive
    for i in range(len(name)):
        name[i] = name[i].lower()

    # open file again to go line-by-line
    f = open('Tweets_Thu24Oct2019_100s.txt', 'r')

    # read every line
    for i in range(nLines):
        line = f.readline()
        
        # for 'text: ' lines:
        if line[0:6] == 'text: ':
            # first, filter text:
            # remove 'text: ' and ending '\n'
            line = line[6:-1]
            # remove 'RT ' if present
            if line[0:3] == 'RT ':
                line = line[3:]
            # case-insensitive and replace accented 'á' with 'a'
            line = line.lower()
            line.replace('á', 'a')

            # now, count candidate name:
            # count of full name within line
            tally = line.count(name[0] + ' ' + name[1])
            # if full name not in line, try adding counts of first and last
            # names separately
            if tally == 0:
                # add last name
                tally += line.count(name[1])
                # add first name if not too common a first name
                if name[0] not in common:
                    tally += line.count(name[0]) 

            # track total mentions
            wCount += tally

    f.close()

    return wCount

def chart(d):
    '''Charts frequency of each key in a dictionary where values are tallies'''
    # x-coordinates of left sides of bars  
    left = list(range(1, len(d.items()) + 1))

    names = []
    tallies = []
    # lists of names and tallies in popularity order
    for key, value in sorted(d.items(), reverse = True, key=lambda item: item[1]):
        names += [key]
        tallies += [value]
      
    # plotting a bar chart 
    plt.bar(left, tallies, tick_label = names, width = 0.8, color = ['blue', 'green']) 
      
    # naming the x-axis 
    plt.xlabel('Candidate') 
    # naming the y-axis 
    plt.ylabel('Mentions') 
    # plot title 
    plt.title('Tally of Democratic Candidate mentions in Twitter feed') 
      
    # function to show the plot 
    plt.show() 

def main():
    '''Runs analysis of twitter feed data, charting counts of democratic
    candidate mentions'''
    # open and read whole file to get line count
    f = open('Tweets_Thu24Oct2019_100s.txt', 'r')
    tweets = f.read()
    # assume every line, including end, has \n at end
    n = tweets.count('\n')
    f.close()

    # words to count - most presidential candidate names in alphabetical order
    candidates = ['Michael', 'Bennet', 'Cory', 'Booker', 'Steve', 'Bullock', \
                  'Pete', 'Buttigeig', 'Julian', 'Castro', 'John', 'Delaney', \
                  'Tulsi', 'Gabbard', 'Kamala', 'Harris', 'Amy', 'Klobuchar', \
                  'Wayne', 'Messam', 'Bernie', 'Sanders', 'Tom', 'Steyer', \
                  'Elizabeth', 'Warren', 'Marianne', 'Williamson', 'Andrew', 'Yang']
    
    # dictionary of counts
    counts = {}

    # for each candidate in regular list
    # store under last name in dictionary of counts, and count name
    for i in range(1, len(candidates), 2):
        counts[candidates[i]] = nameCount(candidates[i-1: i+1], n) # count of last name

    # count 'Joe' as Biden, not Sestak
    counts['Sestak'] = nameCount(['', 'Sestak'], n)
    counts['Biden'] = nameCount(['Joe', 'Biden'], n)

    # show chart of counts
    chart(counts)

main()
