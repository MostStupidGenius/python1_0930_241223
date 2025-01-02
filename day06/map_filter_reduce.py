# 함수형 프로그래밍
# 순수함수를 이용하여 쉽게 많은 데이터를 다룰 수 있다.
# map(), filter(), reduce()
def map_pratice():
    # map
    # 전달된 이터러블 객체의 요소마다
    # 전달한 함수를 수행하게끔하여
    # 그 결과값을 새로운 이터러블 객체의 요소로 구성하여
    # 반환하는 함수다.
    numbers = [1, 2, 3, 4, 5]
    # numbers의 모든 요소에 2를 곱한 새로운 map 객체 생성
    doubled = map(lambda x: x*2, numbers)
    print(tuple(doubled))

def filter_practice():
    # filter
    # 전달한 조건식이 반환되는 함수의 결과가
    # 참인 요소들만 모아서 새로운 이터러블 객체로
    # 반환한다.
    # 3의 배수인 요소만 새로운 객체의 요소로 추출
    numbers = [1, 2, 3, 4, 5, 6, 7]
    filtered = filter(lambda x: x % 3 == 0, numbers)
    print(list(filtered))

def reduce_practice():
    # reduce
    # 전달된 이터러블 객체의 요소를 하나씩 소모하여
    # 두 개의 변수 a, b 중 a에 이전 함수의 결과를 담고
    # 이를 반복하여 최종 결과 값을 하나만 도출해내는
    # 함수이다.
    # reduce는 functools에서 reduce를 임포트하여 사용할 수 있다.
    from functools import reduce

    # 전달된 리스트의 모든 수를 곱한 결과를 반환하는 코드
    numbers = [1, 2, 3, 4, 5]
    reduced = reduce(lambda x1, x2: x1 * x2, numbers)
    print((reduced))