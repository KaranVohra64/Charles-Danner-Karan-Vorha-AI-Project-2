import urllib.request
import ssl
import re

def getLyrics(url):
	context = ssl._create_unverified_context()
	with urllib.request.urlopen(url, context=context) as url:
	    s = str(url.read())

	lyricBodyIndex = s.find("lyric-body-text")

	if(lyricBodyIndex != -1):
		lyricBodyStr = s[lyricBodyIndex:]
		lyricBodyStr= lyricBodyStr[lyricBodyStr.find(">"):lyricBodyStr.find("</pre>")]
		lyricBodyStr = re.sub("<(.|/n)*?>", "", lyricBodyStr)

		#is there a better solution to the replaces? Couldn't get regex to work for this...
		lyricBodyStr = lyricBodyStr.replace("\\r\\n\\r\\n","@@").replace("\\r\\n","@@").replace(";",",").replace("- ","").replace("\\","")
		lyricBodyStr = lyricBodyStr.split("@@")

		lyricalBreakdown = []

		for i in range(len(lyricBodyStr)):
			lyricalBreakdown.append(re.sub(r'[^\w & ^\s]', '', lyricBodyStr[i]))

		return(lyricalBreakdown)


def createURL(artistName, songNames): #This won't work, need to go to artist page and get url's from there...
	urls = []

	for i in songNames:
		urls.append("https://www.lyrics.com/lyric/29532703/Chance+the+Rapper/" + i.replace(" ", "+"))
		
	return(urls)