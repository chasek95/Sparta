import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')


songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

rank=0
for song in songs:
    if song is not None:   # 값이 있으면
        singer = song.select_one('td.info > a.artist.ellipsis')
        title = song.select_one('td.info > a.title.ellipsis')
        rank += 1
        print(str(rank)+'위',singer.text.strip() +'-',title.text.strip())
        
       
#순위 따오기 힘들어 for문으로 숫자 +=1 해서 프린트함
#strip()이 프린트에 안찍혀서 고생했지만 검색결과 singer.text.strip()으로 text를 지정해줘야함



#순위
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#가수
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
#제목
##body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis