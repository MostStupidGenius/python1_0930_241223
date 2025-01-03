# json파일 형식으로 내보내고 받아오기
# json파일이란, dict와 동일한 형태의 텍스트로
# 데이터를 전송하는 파일 형식이다.
# 주로 웹상에서 데이터를 주고 받을 때 사용하며
# dict와 같은 형태이기 때문에 파이썬에서는
# 비교적으로 다루기 쉽다.
import json

json_data = {
    "name": "홍길동",
    "age": 30,
    "score": {
        "math": 90,
        "kor": 80,
        "eng": 70
    }
}
file_path = 'info.json'

# json 파일 쓰기
with open(file_path, 'w', encoding='utf-8') as file:
    # .dump()에 데이터와 파일 객체, 기타 설정 등을 입력하여
    # 데이터를 json 형태로 내보낼 수 있다.
    json.dump(json_data, file,
              ensure_ascii=False, # 아스키 코드 형식으로 내보낼지 여부
            #   False로 안하면 한글이 깨진다.
              indent=4 # 들여쓰기를 얼마나 할지 정하는 것으로
            #   indent 옵션을 주지 않으면 모든 데이터가 한 줄로 표현된다(용량압축)
              )

# json 파일 읽어오기
with open(file_path, 'r', encoding='utf-8') as file:
    # .load로 file 객체를 전달하면
    # json의 데이터를 dict 형태로 반환한다.
    data = json.load(file)
    print(data)
