# 파일을 open()함수로 열 때,
# .close()를 매번 해주어야 했다.
# with open() as f: 구문을 사용하면
# 닫는 것을 자동으로 해준다.
# as f로 하면 f라는 파일 객체를 담은 임시 변수를
# 사용하여 파일 입출력을 진행할 수 있다.
file_path = 'test3.txt'
def with_open():
    with open(file_path, 'a') as file:
        file.write("asdsd")

with_open()
