from yt_dlp import YoutubeDL

# url = "https://www.youtube.com/watch?v=dAOOTiNiF2w&ab_channel=%E3%81%BE%E3%81%8A%E3%81%9F%E3%82%93%E3%80%90M.A.O.%E3%80%91"
# url = "https://www.youtube.com/watch?v=ibGo_KCPrEQ&ab_channel=%E3%81%8B%E3%82%89%E3%81%9F%E3%81%A1"
# url = "https://www.youtube.com/watch?v=ioJrSH14ybo&ab_channel=%E3%80%90%E3%81%97%E3%82%87%E3%81%86%E3%81%B8%E3%81%84%E3%80%91AnyMusic"
# url = "https://www.youtube.com/watch?v=t3dQwj6YYXw&ab_channel=%E3%81%99%E3%83%BC%E3%81%95%E3%82%93%E3%81%AE%E3%82%AE%E3%82%BF%E3%83%BC%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB"
url = "https://www.youtube.com/watch?v=QwORP_EWmrI&ab_channel=%E3%81%82%E3%81%84%E3%82%8D%E3%81%AA"

ydl_opts = {
    "format": "best",
    "outtmpl": "data\%(title)s.%(ext)s",
}

with YoutubeDL(ydl_opts) as ydl:
    result = ydl.download([url])
