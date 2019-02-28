import urllib.request
import ssl
import re


class Lyrics():

	def getLyrics(url):
		context = ssl._create_unverified_context()
		try:
			conn = urllib.request.urlopen(url, context=context)
		except urllib.error.HTTPError as e:
			print('HTTPError: {}'.format(e.code))
			return e.code

		except urllib.error.URLError as e:
			print('URLError: {}'.format(e.reason))
			return e.reason
		else:
			with urllib.request.urlopen(url, context=context) as url:
				s = str(url.read())
				return AZLyrics(s)


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

	def createAZLyricsUrl(artistName, songName):#AZLyrics.com
		return "https://www.azlyrics.com/lyrics/" + artistName.replace(" ", "") + "/" + songName.replace(" ", "") + ".html"





