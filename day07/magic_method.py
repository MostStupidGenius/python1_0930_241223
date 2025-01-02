# 매직 메서드란
# 클래스에서 정의하는 일반적인 기능이 아닌
# 파이썬과 직접적으로 연관이 있는
# 연산, 객체 생성/삭제,... 등을 정의하는
# 특수한 목적으로 만들어진 메서드를 통칭한다.
# 매직 메서드의 특징은 언더바(_) 두 개가 앞뒤로
# 감싸인 형태를 가지며,
# 이러한 메서드는 직접 호출하는 것을 권장하지 않는다.

class Student():
    def __init__(self, name):
        self.name = name
        print("init")

    # init 메서드보다 먼저 호출되어
    # 전달된 객체를 주소값에 할당하는 동작을 한다.
    # ※ 잘 모르면 new 매직 메서드는 재정의하지 말자.
    # def __new__(cls): # new 매직 메서드를 잘못 정의하면
    #     # __init__ 메서드에 정의된 내용이 무시당한다.
    #     print(cls) # cls 변수는 type(객체)를 넣었을 때
    #     # 나오는 값이 담겨있다.

    #     # print("new")
    #     # cls.__init__(cls, ) # 생성자를 호출해주어야 한다.
    #     return cls
    # 해당 객체를 문자열로 바꾸었을 때
    # 호출될 값을 정의하는 매직 메서드
    def __str__(self):
        return "학생입니다."
    # 문자열로 표현하는 매직 메서드2
    # repr 메서드는 repr() 함수에 객체를 전달했을 때
    # 어떻게 표현할 것인가를 정의하는
    # 매직 메서드다.
    # __str__ 메서드가 정의되어 있다면
    # print() 함수로 객체가 호출될 때
    # __str__ 메서드의 내용이 먼저 호출된다.
    def __repr__(self):
        return "repr 매직 메서드입니다."

if __name__ == "__main__":
    obj = Student("")
    # print(str(obj))
    # print(repr(obj))
    print(obj.name)