from youtube_dl import YoutubeDL

#1: Download a singleyoutube video
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])

#2: Download multiple youtube videos
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])

#3: Download audio
# options = {
#     'format':'bestaudio/audio' # Tell the downloader to download only the best quality of audio
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])

# 4: Search and then download the first video
options = {
    'default_search': 'ytsearch',  # tell downloader to search instead of directly downloading
    'max_downloads':1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download(['con điên TAMKA PKL'])

# 5: Search and then download the first audio
# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1, # Tell downloader to download only the first entry (audio)
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['Nhớ mưa sài gòn lam trường'])
