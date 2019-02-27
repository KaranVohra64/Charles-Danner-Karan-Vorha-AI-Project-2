import urllib.request
import ssl
import re

# def getLyrics(url): #lyrics.com
# 	context = ssl._create_unverified_context()
# 	with urllib.request.urlopen(url, context=context) as url:
# 	    s = str(url.read())

# 	lyricBodyIndex = s.find("lyric-body-text")

# 	if(lyricBodyIndex != -1):
# 		lyricBodyStr = s[lyricBodyIndex:]
# 		lyricBodyStr= lyricBodyStr[lyricBodyStr.find(">"):lyricBodyStr.find("</pre>")]
# 		lyricBodyStr = re.sub("<(.|/n)*?>", "", lyricBodyStr)

# 		#is there a better solution to the replaces? Couldn't get regex to work for this...
# 		lyricBodyStr = lyricBodyStr.replace("\\r\\n\\r\\n","@@").replace("\\r\\n","@@").replace(";",",").replace("- ","").replace("\\","")
# 		lyricBodyStr = lyricBodyStr.split("@@")

# 		lyricalBreakdown = []

# 		for i in range(len(lyricBodyStr)):
# 			lyricalBreakdown.append(re.sub(r'[^\w & ^\s]', '', lyricBodyStr[i]))

# 		return(lyricalBreakdown)


# def createURL(): #This won't work, need to go to artist page and get url's from there...
# 	context = ssl._create_unverified_context()
# 	with urllib.request.urlopen("https://www.lyrics.com/artist/Chance-the-Rapper", context=context) as url:
# 	    s = str(url.read())

# 	print(s[s.find("/lyric/"):])

# createURL()

#make one for azlyrics.com (easier)

def getLyrics(url):
	context = ssl._create_unverified_context()
	with urllib.request.urlopen(url, context=context) as url:
	    s = str(url.read())
	
	if(s.find("It's a place where all searches end!") == -1):
		return AZLyrics(s)
	else:
		return -1


def AZLyrics(s): #AZLyrics.com
	lyricBodyStart = s.find("<!-- Usage of azlyrics.com")
	lyricBody = s[lyricBodyStart:]
	lyricBody = lyricBody[:lyricBody.find("</div>")]
	lyricBody = re.sub("<(.|/n)*?>", "", lyricBody) #Remove HTML
	lyricBody = re.sub("[\(\[].*?[\)\]]", "", lyricBody) #Remove intervals
	lyricBody = lyricBody.replace("\\r\\n", "").replace("\\n\\n", "@@").replace("\\n", "@@").replace("\\", "").replace("&quot;", "\"").replace("...", " ") #remove sequences
	lyricBody = lyricBody.split("@@")

	lyricBodyData = []

	for i in range(len(lyricBody)):
		if(lyricBody[i] != ""):
			lyricBodyData.append(re.sub(r'[^\w & ^\s]', '', lyricBody[i]).lower())

	return lyricBodyData

def createAZLyricsUrl(artistName, songName):
	return "https://www.azlyrics.com/lyrics/" + artistName.replace(" ", "") + "/" + songName.replace(" ", "") + ".html"


def main():
	url = createAZLyricsUrl("asap rocky", "been around the world")
	lyrics = getLyrics(url)

	for i in lyrics:
		print(i)

main()





