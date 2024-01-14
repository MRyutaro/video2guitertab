from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=dAOOTiNiF2w&ab_channel=%E3%81%BE%E3%81%8A%E3%81%9F%E3%82%93%E3%80%90M.A.O.%E3%80%91"

ydl_opts = {
    "format": "best",
    "outtmpl": "data\%(title)s.%(ext)s",
}

with YoutubeDL(ydl_opts) as ydl:
    result = ydl.download([url])
