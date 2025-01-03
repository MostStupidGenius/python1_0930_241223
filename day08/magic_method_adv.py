# 매직 메서드 심화
# __add__와 __eq__ 매직 메서드 구현
# 입력되는 other 객체(연산 대상 객체)를 타입 검사하는
# 예제 진행

# x좌표와 y좌표를 보유한 클래스 객체로
# Point 클래스 간의 더하기, == 연산자 연산 구현
class Point():
    def __init__(self, x: int, y: int):
        self.x = x # x좌표
        self.y = y # y좌표
    
    def __eq__(self, value):
        # 만약 value가 Point클래스로 만든 인스턴스(객체)라면
        if isinstance(value, Point):
            # 비교 주체인 self의 x와 비교 대상인 value의 x가
            # 같은지 비교
            eq_x = self.x == value.x
            # y좌표도 마찬가지
            eq_y = self.y == value.y
            # 두 좌표가 모두 같으면 True 반환
            return eq_x and eq_y
        # 전달받은 value가 tuple이라면
        elif isinstance(value, tuple):
            if len(value) == 2: # 튜플의 길이가 2라면
                eq_x = self.x == value[0] # 0번째 값과 x를 비교
                eq_y = self.y == value[1] # 1번째 값과 y를 비교
                # 두 값이 같은지 여부를 반환
                return eq_x and eq_y
            # 튜플의 길이가 2가 아니라면
            # 좌표와 비교할 수 없으므로 False 반환
            else:
                return False
        else:
            print("잘못된 객체와 비교 중입니다.")
            return False
    
    def __add__(self, value):
        # Point 타입인지 확인
        if isinstance(value, Point):
            new_x = self.x + value.x
            new_y = self.y + value.y
            return Point(new_x, new_y)

    # print()나 str()함수에 전달되었을 때
    # 문자열 표현 방법
    def __str__(self) -> str:
        expression = f"Point({self.x}, {self.y})"
        return expression

    # x, y 좌표를 튜플 형태로 반환하는 메서드
    def get_coord(self) -> tuple:
        return (self.x, self.y)
    
if __name__ == "__main__":
    # p1 = Point(1, 3)
    # p2 = Point(1, 3)
    # print("Point끼리 비교:\t", p1 == p2)
    # print("숫자와 잘못 비교:\t", p1 == 3)
    # # 포인트와 튜플의 비교
    # print("튜플과 비교:\t",p1 == (1, 3))

    # 더하기 연산 테스트
    p1 = Point(10, 31)
    p2 = Point(3, 1)
    p3 = p1 + p2
    # print(p3.x, p3.y)
    # print(p3)
    x, y = p3.get_coord()
    print(x, y)