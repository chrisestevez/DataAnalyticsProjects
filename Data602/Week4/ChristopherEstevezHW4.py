import urllib2
import bs4
import re
import IBMCredentials as IBM # This module contains my Alchemy credentials.
from watson_developer_cloud import AlchemyLanguageV1
import sys

# The program just process this HTML web page.
url = "http://www.recode.net/2017/2/24/14727106/faceebook-mark-zuckerberg-manifesto-government-news-media-power"
try:
    # I start by using beautiful soup and urllib2 in order to pass the url and target paragraphs in the article.

    page = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(page, 'html.parser')
    information = soup.find_all('p', {'id': re.compile("^")})

    # I force the results into a string in order to run regex and remove HTML tags etc.

    info = str(information)
    cleanData = re.sub(r"<.*?>","",info)
    cleanData = re.sub(r"\\u\d*\D", " ", cleanData)
    cleanData = re.sub(r"\s", " ", cleanData)
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

print "-"*100
print "Clean Data"
print cleanData
print "-"*100

"######################## Please change API key in order to function properly##############################"

Key_API = IBM.apikey
alchemy_language = AlchemyLanguageV1(api_key=Key_API)

words = alchemy_language.keywords(text=cleanData, max_keywords=10)

print "Alchemy Results"
print words
print "-"*100

print "Top 10 Keywords with Relevance"
print "-"*100

print "Keyword".center(50," ") + "Relevance".center(5," ")

if words['status'] == 'OK':
    for Result in words['keywords']:
        print "".center(20) + Result['text'] + "".center(10)+Result['relevance']
else:
    print "An Error has occurred trying to extract keywords"
