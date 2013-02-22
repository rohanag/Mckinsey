"""
Create an app that will be executed in terminal or from the command line. The app should accept a hashtag as an argument and should only print out unique urls found in the 100 most recent tweets that matched the hashtag.
"""
import urllib, urllib2
import json
import re
import sys

class HeadRequest(urllib2.Request):
    def get_method(self): return "HEAD"

#Converting URLs from t.co/tinyurl-form to expanded url
def get_real(url):
    res = urllib2.urlopen(HeadRequest(url))
    return res.geturl()
    
def searchTweets(query):
    search = urllib.urlopen("http://search.twitter.com/search.json?q="+query+"&rpp=100")
    dict = json.loads(search.read())
    results = []
    for result in dict["results"]:
        results.append(result["text"].encode('utf8'))
    return results

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'One argument is needed, i.e the hashtag to be searched'
        exit()
    tag = sys.argv[1]
    if tag[0] != '#':
        tag = '#' + tag
        
    tweets = searchTweets(tag)
    
    ans = set()
    for t in tweets:
        ans.update(get_real(i) for i in re.findall('(?:http://|www.)[^"\' ]+', t))

    print 'The unique URL\'s are '
    print

    for i in ans:
        print i
        print
