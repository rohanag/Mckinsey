"""
Given an array of integers, write some code to find all the integers that appear more than once in the array, sorted by which appears most often to least often (once)
"""

from collections import defaultdict
from operator import itemgetter

if __name__ == '__main__':
    hash = defaultdict(int)
    try:
        f = open('in.txt', 'r')
    except IOError:
        print 'File in.txt does not exist, put the file in the same directory as the python file'
        exit()
    for lines in f:
        hash[int(lines)] += 1

    sortedTuple = sorted(hash.iteritems(), key = itemgetter(1), reverse = True)
    for i,j in sortedTuple:
        if j > 1:
            print i
        else:
            break
    f.close()