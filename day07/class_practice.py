# 클래스란
# 값이 빈 데이터와 메서드를 가진 하나의 템플릿, 양식으로써
# 클래스를 통해 구체화될 객체를 미리 정의하는 설계도다.
# ※클래스 이름은 반드시 대문자로 시작해야 한다.
class Student(): # 클래스 선언.
    # 소괄호()는 상속할 부모 클래스를 지정할 때 쓰인다.
    # 생성자:
    # 객체를 구체화할 때(객체화) 객체에 필요한 정보를
    # 받는 입력창 역할을 한다.
    # __init__의 매개변수로 필요한 정보의 이름을 사용하여
    # 입력을 받으면 된다.
    def __init__(self, name, gender, job) -> None:
        # 객체(self)의(.) name에 외부에서 전달받은
        # name의 값을 저장한다.
        self.name = name
        self.gender2 = gender
        self.job2 = job
        # self는 클래스를 객체화한 객체를
        # 통틀어서 가리키기 위한 대명사로 쓰이는
        # 키워드이다.
        print(self.name)
        pass
    pass

# 객체화
if __name__ == "__main__":
    영희 = Student("김영희", False, "개발자")
    print(영희)
    # print(영희.name)
    # print(영희.job2)
    # print(영희.gender2)


