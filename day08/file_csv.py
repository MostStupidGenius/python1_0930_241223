# csv란
# 쉼표,로 구분된 값들(comma-seperated values)을
# 텍스트 파일 형태로 나타낸 파일을 가리킨다.
# csv 파일을 읽을 때는 기본 라이브러리인
# csv를 import하여 reader나 writer를 객체화 해야 한다.
import csv

file_path = "file.csv"
def write_csv_file():
    with open(file_path, 'w', encoding="utf-8-sig", newline='') as file:
        # csv에 내장된 쓰기 객체를 호출
        writer = csv.writer(file) # 파일 객체를 쓰기 객체에 전달

        # open()함수를 사용할 때, newline=''을 넣는 이유는
        # 새로운 행을 추가할 때마다 줄바꿈이 추가되기 때문에
        # 빈 행이 자꾸 삽입된다.
        writer.writerow(['이름', '나이', '직업'])
        writer.writerow(['홍길동', 30, '개발자'])
        # 데이터를 내보낼 때에는, 작은 따옴표''가 제거되어
        # raw data 형태로 나간다.(30과 '30'은 동일하게 처리된다.)
        writer.writerow(['홍당무', 10, '학생'])
def read_csv_file():
    with open(file_path, 'r', encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        for row in reader:
            # 데이터를 읽어올 때에는
            # 한 행씩 데이터를 읽어오며, 한 행은
            # 리스트에 문자열이 담긴 형태로 가져온다.
            # 이때 담긴 값들은 숫자, 문자 상관없이
            # 모두 문자열로 처리되어 가져오게 된다.
            print(row)

if __name__ == "__main__":
    # write_csv_file()
    read_csv_file()