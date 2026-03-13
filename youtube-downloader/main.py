import yt_dlp
import shutil
import os

def get_urls():# 유튜브 영상 링크 입력받는 함수
  urls = []
  while True:
     url = input("유튜브 동영상 링크(종료는 0을 입력): ")
     if url == "0":
        break
     urls.append(url)
  return urls

# 함수에 갇혀있는 링크 빼주기
urls = get_urls()

print("다운로드 할 영상", len(urls), "개")

# 다운로드 설정
ydl_opts = {
    'ffmpeg_location': r'C:\ffmpeg\bin',
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': 'downloads/%(title)s.%(ext)s'
}

# 다운로드 실행
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)

