# 파일 입출력을 예외 처리와 함께 사용하기
file_path = 'test2.txt'

# 파일 읽기('r') -> 파일 존재x -> 에러
def read_file():
    file = None
    try:
        # 파일을 읽는 로직
        file = open(file_path, 'r')
        print(file.read())
    except Exception as e:
        # 오류가 발생했을 때, 어떤 오류인지 출력
        print(e)
    finally:
        # 오류 발생 여부와 무관하게 파일을 닫아주어야 한다.
        # 만약 파일 객체가 담겨 있다면
        if file is not None:
            # 파일을 닫아준다.
            file.close()


# 파일 쓰기('x') -> 파일 존재o -> 에러
def write_file_x():
    file = None
    try:
        file = open(file_path, 'x', encoding="utf-8")
        file.write("내용1")
    except FileExistsError as e:
        # print(e)
        print("x방식으로 파일을 쓸 때에는 파일이 존재해서는 안 됩니다.")
        print("이미 파일이 존재합니다.")
    except Exception as e:
        print(e)
    finally:
        if file: file.close()

if __name__ == "__main__":
    # read_file()
    write_file_x()