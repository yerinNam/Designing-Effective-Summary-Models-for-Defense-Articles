# Designing-Effective-Summary-Models-for-Defense-Articles
> 본 연구의 모델은 국방 분야에서의 정보 수집과 이해를 돕기 위해, 뉴스 기사의 효과적인 요약을 통해 빠르고 정확한 의사결정을 지원하는 것을 목표로 한다.
> Jypyter 환경에서 돌렸으며, 온디바이스 환경에서 학습이 가능함을 시사한다.

## 학습 개요도
<img src="https://github.com/yerinNam/Designing-Effective-Summary-Models-for-Defense-Articles/blob/main/img/%EC%A0%84%EC%B2%B4%20%EA%B0%9C%EC%9A%94%EB%8F%84.png?raw=true" width="400" height="100"/>


## 서비스 개요도
<img src="https://github.com/yerinNam/Designing-Effective-Summary-Models-for-Defense-Articles/blob/main/img/%EC%84%9C%EB%B9%84%EC%8A%A4%20%EC%A0%84%EC%B2%B4%20%EA%B0%9C%EC%9A%94%EB%8F%84.png?raw=true" width="400" height="150"/>


## 요약 문장 비교
<img src="https://github.com/yerinNam/Designing-Effective-Summary-Models-for-Defense-Articles/blob/main/img/%EC%9A%94%EC%95%BD%20%EB%AC%B8%EC%9E%A5%20%EB%B9%84%EA%B5%90.png?raw=true" width="850" height="600"/>



## 카카오톡 서비스 예제
<img src="https://github.com/yerinNam/Designing-Effective-Summary-Models-for-Defense-Articles/blob/main/img/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%86%A1%20%EC%84%9C%EB%B9%84%EC%8A%A4.png?raw=true" width="300" height="400"/>


## 사용 예제

```sh
# Encode Input Text
input_text = """
'대한민국 5G 홍보대사\'를 자처한 문재인 대통령은 "넓고, 체증 없는 \'통신 고속도로\'가 5G"라며 "대한민국의 대전환이 이제 막 시작됐다"고 기대감을 높였다.', '문 대통령은 8일 서울 올림픽공원에서 열린 5G플러스 전략발표에 참석해 "5G 시대는 우리가 생각하고, 만들면 그것이 세계 표준이 되는 시대"라며 "5G는 대한민국 혁신성장의 인프라"라고 강조했다.', "산업화 시대에 고속도로가 우리 경제의 '대동맥' 역할을 했듯, 5G가 4차 산업혁명 시대의 고속도로가 돼 새로운 기회를 열어 줄 것이란 설명이다.", '문 대통령은 "5G가 각 분야에 융합되면, 정보통신산업을 넘어 자동차, 드론(무인항공기), 로봇, 지능형 폐쇄회로TV(CCTV)를 비롯한 제조업과 벤처에 이르기까지 우리 산업 전체의 혁신을 통한 동반성장이 가능하다"고 밝혔다.', '세계 최초 상용화에 성공한 5G가 반도체를 이을 우리 경제의 새 먹거리가 될 것이란 관측이다.', '정부는 2026년 세계 5G 시장 규모가 1161조원에 달할 것으로 보고 있다.', '작년 반도체 시장 규모가 529조원인 점을 고려하면 2배 이상 큰 미래 시장이 창출되는 셈이다.', '문 대통령은 아직은 국민에게 다소 낯선 5G 시대의 미래상을 친절히 설명해 눈길을 끌기도 했다.', '문 대통령은 "\'지금 스마트폰으로 충분한데, 5G가 왜 필요하지?\'라고 생각할 수 있다"며 "4세대 이동통신은 \'아직은\' 빠르지만 가까운 미래에는 결코 빠르지 않다"고 했다.', '그러면서 "자동차가 많아질수록 더 넓은 길이 필요한 것처럼 사물과 사물을 연결하고, 데이터를 주고받는 이동통신망도 더 넓고 빠른 길이 필요하다"고 덧붙였다.', '문 대통령은 세계 최초 상용화에 성공한 우리 5G 기술을 널리 알리는 홍보대사를 자처하기도 했다.', '5G 시장을 선점하기 위한 각국의 경쟁이 뜨겁게 달아오른 만큼 정부 차원에서 적극 지원하겠다는 방침이다.', '문 대통령은 "평창동계올림픽 360도 중계, 작년 4·27 남북한 정상회담 때 프레스센터에서 사용된 스마트월처럼 기회가 생기면 대통령부터 나서서 우리의 앞선 기술을 홍보하겠다"고 말했다.
"""
input_ids = tokenizer.encode(input_text, return_tensors="pt")
model.to("cpu")
input_ids.to("cpu")

summary_text_ids = model.generate(
    input_ids=input_ids,
    length_penalty=2.0,
    max_length=80,
    min_length=10,
    num_beams=8,
    repetition_penalty=1.5,
    no_repeat_ngram_size=1
)

# Decoding Text
print(tokenizer.decode(summary_text_ids[0], skip_special_tokens=True))
```


## 정보

MIT 라이센스를 준수하며 ``LICENSE``에서 자세한 정보를 확인할 수 있습니다.


인용글
> 인용글[1](https://wonhwa.tistory.com/11#google_vignette)
