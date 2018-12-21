from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL
from collections import OrderedDict

# from collections import OrderedDict
url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)

raw_data = conn.read()

page_content = raw_data.decode("utf8")

soup = BeautifulSoup(page_content, "html.parser")


section = soup.find("section", "section chart-grid")
div = section.find("div", "section-content")
ul = section.find("ul")
li_list = ul.find_all("li")
# print(li_list)

list_song = []
for li in li_list:
    a =li.h3.a
    a1 = li.h4.a
    names = a.string
    artists = a1.string
    # print(Names)
    # print(Artists)
    news = OrderedDict({
        "Names": names,
        "Artists": artists
    })
   
    options = {
        'default_search': 'ytsearch',  # tell downloader to search instead of directly downloading
        'max_downloads':1 # Tell downloader to download only the first entry (video)
    }
    dl = YoutubeDL(options)
    dl.download([names + artists])

    list_song.append(news)

pyexcel.save_as(records= list_song , dest_file_name="itunes.xlsx")
