import yt_dlp
import shutil
import os
import sys

def link_check(url): # 유튜브링크가 맞는지 확인해주는 함수
  if ("youtube.com/" in url) or ("youtu.be/" in url):
    return True
  else:
    return False
  
def check_p(url): # 플레이리스트인지 확인하는 함수
  if "list=" in url or "/playlist" in url:
    print("!!!##!!! -------------------- 경고 --------------------- !!!##!!!")
    print("!!!##!!! 재생목록을 입력하셨습니다 다운로드 하시겠습니까? !!!##!!!")
    print("!!!##!!! 다운로드가 매우 오래걸리거나 중단될 수 있습니다  !!!##!!!")
    print("!!!##!!! (y/n): ", end="")
    opinion = input("")
    if opinion == 'y' or opinion == 'Y' :
      return True
    elif opinion == 'n' or opinion == 'N' :
      return False
    else: # Y,y 말고 다른건 모두 취소로 하려 했으나 혹시 모르기에 수정함
      return False
  else:
    return 2 # 플레이리스트가 아닐 때

def get_urls():     # 유튜브 영상 링크 입력받는 함수
  check_opts = {
    'quiet': True,
    'logger': None,
    'noplaylist': True,
    }
  urls = []

  while True:
    print("--!(모든 작업 취소 및 프로그램 중단: 0 입력)!--")
    url = input("유튜브 동영상 링크(완료는 1을 입력): ")
    if url == "0":
      q_onof = input("정말 모든 작업을 취소하고 종료하시겠습니까?\n" \
      "(No = 0,Yes = 1) : ")
      if q_onof == "1":
        sys.exit()
      else:
        continue
    # 종료문

    if url == "1":
      break

    print("... 링크 검사 중 ...")

    if link_check(url): # 유튜브 링크인지 아닌지 먼저 확인
      with yt_dlp.YoutubeDL(check_opts) as ydl: #동영상 이름 불러오기
        info = ydl.extract_info(url, download=False)
        print("\n",info['title'], "\n다운로드 예정\n")
        settling = input("위의 영상을 리스트에 추가하시겠습니까?(동의:1, 취소0)")
        if settling == "1":
          print("리스트에 성공적으로 추가되었습니다\n")
        else:
          print("성공적으로 취소 되었습니다\n")
          continue
    else:
      print("**##(오류)유튜브링크가 아닙니다")
      print("**##(오류)링크를 다시 확인해주세요.##**")
      continue

    p_result = check_p(url)

    if p_result == True : # 유튜브 링크 확인 후 플레이리스트인지 확인
      print("다운로드 진행")
    elif p_result == False:
      print("다운로드 취소")
      continue
    elif p_result == 2:
      print("")

    urls.append(url) # 최종 삽입
  return urls

# 함수에 갇혀있는 링크 빼주기
urls = get_urls()

print("다운로드 할 영상/재생목록", len(urls), "개")

# 다운로드 설정
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'quiet': True,
    'logger': None,
}

# 다운로드 실행
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)

if len(urls) > 0:
  print("다운로드 완료")

print("프로그램 종료")
