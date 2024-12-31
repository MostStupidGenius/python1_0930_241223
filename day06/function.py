# 함수(function)
# 전달받은 데이터를 일정한 로직에 따라 처리하여
# 그 결과를 반환하거나 하지 않고 종료하는
# 기능을 묶어놓은 코드 블록이다.
# 모든 함수는 사용할 때에 함수명 뒤에 소괄호를 붙인다.
# 이러한 소괄호 안에 함수가 기능을 수행하는 데
# 필요한 데이터(값)를 입력하여 전달해야 한다.

# 함수 만들기
# 입력x 출력x
def inputXOutputX():
    print("전달되는 값이 없는 함수")
    return # return 키워드를 만나면
    # 함수의 기능이 종료되고 코드 흐름이
    # 외부로 이동한다.
    # return 키워드 아래쪽의 내용은
    # 실행되지 않는다(도달할 수 없다.)
    print("도달할 수 없는 코드")

# 입력x 출력o
def noInput():
    result = "홍길동"
    return result # return 키워드 뒤에 바로 오는
    # 값을 함수를 사용한 외부의 위치로 전달한다.

# 입력o 출력x
def noOutput(name):
    print(f"제 이름은 {name}입니다.")
    return

# 값을 입력받아 결과를 반환하는 함수
# 입력o 출력o
def add(num1, num2):
    result = num1 + num2
    return result

if __name__ == "__main__":
    # inputXOutputX()
    # print(noInput())
    # print(noOutput("홍길동"))
    return_value = add(3, 10)
    print(return_value)
