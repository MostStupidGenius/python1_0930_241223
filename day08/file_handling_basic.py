# 파일 입출력 기본
# 파일을 읽거나 쓰려면 open()함수를 이용해서
# 새로운 파일 객체를 생성해야 한다.
# 대상 파일을 파이썬에서 사용할 수 있는 객체로 담거나
# 새 파일을 만들기 위한 파이썬의 파일 객체를 만드는 것이 선행된다.
# file = open(파일경로가 담긴 문자열, 파일여는방식)
# mode: 'r'(읽기), 'w'(쓰기), 'a'(추가)
file_path = 'test.txt'
def file_write():
    # 'x': 기존에 파일이 있으면 오류
    # 없으면 생성 후 내용 쓰기 모드
    # file = open(file_path, 'x') # 생성 및 쓰기 모드로 파일 객체 생성

    # 'a': 기존 파일이 있으면 기존 내용에
    # 추가로 내용 작성하는 쓰기 모드
    file = open(file_path, 'a')

    # 'w': ★기존에 파일이 있든 없든 생성 혹은 덮어쓰기
    # 기존에 담겨 있던 내용을 없애고 새로 내용을 작성하는 쓰기 모드
    # file = open(file_path, 'w')

    # 쓰기 예제
    file.write("hello, world2\nnewline2\n")

    # 파일을 열었으면 닫아주어야 한다.
    file.close()

def file_read():
    file = open(file_path, 'r') # 읽기 모드

    # 모든 내용을 하나의 문자열에 담아 읽는 방식
    content = file.read() 
    print(f"content:\n{content}")
    file.close() # 닫아주기

def file_read2():
    # 위의 방법으로 내용을 읽고 이어서 읽게 되면
    # 읽을 내용을 못 가져오기 때문에 
    # 읽는 방식에 따라 파일 객체를 새로 생성

    file = open(file_path, 'r') # 읽기 모드

    # 여러 라인을 하나의 리스트에 담아 가져오는 방식
    lines = file.readlines()
    print("readlines:")
    for line in lines: # 각 라인이 요소로 담긴 lines를 반복
        print(line.strip()) # 앞뒤 공백문자, 이 경우 줄바꿈 문자 제거
    file.close() # 닫아주기

if __name__ == "__main__":
    file_read2()
    # file_write()





# 예외처리 

# 파일 입출력 심화(다른 파일)