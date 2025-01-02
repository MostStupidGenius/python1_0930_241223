# 클래스란
# 값이 빈 데이터와 메서드를 가진 하나의 템플릿, 양식으로써
# 클래스를 통해 구체화될 객체를 미리 정의하는 설계도다.
# ※클래스 이름은 반드시 대문자로 시작해야 한다.
class Student(): # 클래스 선언.
    # 소괄호()는 상속할 부모 클래스를 지정할 때 쓰인다.
    
    # 클래스 변수 선언
    # self(객체)를 통해서 접근할 수 없는
    # 클래스에 소속된 변수를 의미하며, 이 변수에 접근할 때에는
    # "클래스명.변수명"과 같이 클래스를 통해서 직접 접근해야 한다.
    # 이러한 클래스 변수는 다른 객체들과 공유되는 변수라고 해서
    # 공유 변수(shared variable)이라고도 부른다.
    amount = 0

    # 생성자:
    # 객체를 구체화할 때(객체화) 객체에 필요한 정보를
    # 받는 입력창 역할을 한다.
    # __init__의 매개변수로 필요한 정보의 이름을 사용하여
    # 입력을 받으면 된다.
    def __init__(self, name="이름없음", gender="남자", job="무직") -> None:
        # 객체(self)의(.) name에 외부에서 전달받은
        # name의 값을 저장한다.
        self.name = name # self.name은 멤버변수, 인스턴스 변수라 불린다.
        self.gender2 = gender
        self.job2 = job
        # self는 클래스를 객체화한 객체를
        # 통틀어서 가리키기 위한 대명사로 쓰이는
        # 키워드이다.
        # print(self.name)

        # 클래스 전역 변수를 사용하려면
        # 클래스이름.변수이름으로 값에 접근해야 한다.
        Student.amount += 1
    
    # 객체의 정보를 합쳐서 출력하는 메서드
    def print_info(self): # 객체의 정보에 접근하는 경우
        # 매개변수로 self를 전달해주어야 한다.
        print(f"{self.name}은(는) {self.gender2}이고 {self.job2} 직업을 가지고 있다.")

    # 지금까지 객체화한 Student 클래스의 객체의 개수를
    # 출력하는 함수
    def print_student_number():
        print(Student.amount)

# 객체화
# if __name__... 코드 블록에 대해서:
# __name__ 현재 실행중인 파일명
# __main__ 직접 실행한 메인 파일의 정보
# -> 현재 파일을 직접 실행한 경우에만 if문의 코드를
# 실행해라-
# 다른 .py파일에서 현재 파일을 import(가져다쓰는) 경우
# 전체 코드를 실행하는 방식으로 코드를 가져다쓰는데,
# 이때 예제코드, 테스트 코드까지 실행하는 것을 방지하기 위해서
if __name__ == "__main__":
    # 예제 코드, 테스트 코드
    영희 = Student(name="김영희", gender=False, job="개발자")
    # print(영희)
    # print(영희.name)
    # print(영희.job2)
    # print(영희.gender2)
    영희.print_info()

    철수 = Student(name="김철수", gender="남자", job="사무직")
    # print(철수.name)
    철수.print_info()

    Student.print_student_number()