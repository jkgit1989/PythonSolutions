# # #
# #
# #
# # from pytube import Playlist
# # from pytube import YouTube
# #
# # playlist = Playlist('https://www.youtube.com/watch?v=Hxe362w66GI&list=RDEMI2BCFFo10vdkjwqBMuZb7Q')
# # YouTube('https://www.youtube.com/watch?v=Hxe362w66GI&list=RDEMI2BCFFo10vdkjwqBMuZb7Q').streams.first().download()
# # print('Number of videos in playlist: %s' % len(playlist.video_urls))
# # playlist.download_all()
#
#
#
# import youtube_dl #module required to download youtube videos
# y= {}
# while (1):
#     link= input("https://www.youtube.com/watch?v=Hxe362w66GI&list=RDEMI2BCFFo10vdkjwqBMuZb7Q")
#     youtube_dl.YoutubeDL(y).download([link])
#     f=input("\nENETR YES(Y) TO CONTINUE DOWNLOADING VIDEOS \nELSE NO(N) TO STOP\n")
#     if f=="N" or f=="n":
#         break