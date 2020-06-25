#2020년 1분기 일반의약품 판매순위 3위 까지의 정보를 크롤링 하는것이 목표임
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

# 제일 많이 팔린 2가지 의약품 크롤링
# dnm = drug name/ dnb = drug number
ranks = [{'dnm':'까스활명수', 'dnb':'157XA11A0570A0357'},{'dnm':'비맥스메타정', 'dnb':'157X2019030800004'}]
for rank in ranks:
    base_url = 'https://100.daum.net/encyclopedia/view/'
    plus_url = rank['dnb']
    url = base_url + plus_url

#크롤링 할것: 이름, (제조사), 사진, 효과, 성분, 복용법, 주의사항
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    pre_d_name = soup.select_one('meta[property="og:title"]')
    d_name = pre_d_name['content']

    pre_d_img = soup.select_one('meta[property="og:image"]')
    d_img = pre_d_img['content']

    pre_d_effect = soup.select_one('#mArticle > div > div.info_cont.info_details > div:nth-child(7) > p')
    d_effect =  pre_d_effect.text.replace('/p','')

    pre_d_ingrt = soup.select_one('#mArticle > div > div.info_cont.info_details > div:nth-child(5) > p')
    d_ingrt =  pre_d_ingrt.text.replace('/p','')

    pre_d_inst = soup.select_one('#mArticle > div > div.info_cont.info_details > div:nth-child(7) > p')
    d_inst =  pre_d_inst.text.replace('/p','')

    pre_d_warn = soup.select_one('#mArticle > div > div.info_cont.info_details > div:nth-child(8) > p')
    d_warn =  pre_d_warn.text.replace('/p','')


#mArticle > div > div.info_cont.info_details > div:nth-child(6)