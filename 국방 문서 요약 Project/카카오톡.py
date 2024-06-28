import json
import requests
import pandas as pd

# CSV 파일 경로
csv_file_path = r'C:\Users\wjkr0\OneDrive\바탕 화면\국방 문서 요약 Project\뉴스 요약\국방 뉴스 요약.csv'

# CSV 파일 읽어오기
news_list3 = pd.read_csv(csv_file_path)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 사용자 토큰
headers = {
    "Authorization": "Bearer " + "RESET API KEY"
}

# 추후 각 리스트에 들어갈 내용(content) 만들기
contents = []

for i in range(5):
    # 텍스트 템플릿 형식 만들기
    template = {
        "object_type": "text",
        "text": f'제목 : {news_list3["제목"][i]}\n\n요약된 기사 : {news_list3["요약된 기사"][i]}\n\n기사 링크 : {news_list3["링크"][i]}',
        "link": {
            "web_url": news_list3['링크'][i],
            "mobile_web_url": news_list3['링크'][i]
        },
        "button_title": "자세히 보기"
    }

    data = {
        "template_object": json.dumps(template)
    }

    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    if response.json().get('result_code') == 0:
        print(f'메시지 {i + 1}를 성공적으로 보냈습니다.')
    else:
        print(f'메시지 {i + 1}를 성공적으로 보내지 못했습니다. 오류메시지 : {response.json()}')
