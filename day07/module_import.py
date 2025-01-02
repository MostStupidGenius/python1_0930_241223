# 모듈과 임포트
# from 모듈명 import 변수,함수,객체명 등
# import를 통해 다른 모듈(.py, 모듈로 지정된 폴더)의 정보를
# 가져다가 쓸 수 있다.
# if name main 코드블록을 쓰지 않으면
# 해당 모듈파일에 작성된 모든 코드가 실행되어
# 가져다쓰는 쪽에서 쓸데없는 내용까지 실행, 출력된다.

import class_practice as cp
# 경로를 다루기 위한 라이브러리
import os
import sys

# __file__ 현재 파일 경로를 담고 있는 이미 만들어진 변수
workspace = __file__
while True: # 반복횟수를 알 수 없음
    # 만약 현재 workspace 변수에 담긴 폴더명이
    # workspace라면 반복 중단
    if os.path.basename(workspace) == "workspace":
        break
    else: # 아니라면 상위폴더 경로를 workspace에 담는다.
        workspace = os.path.dirname(workspace)
print(workspace)
sys.path.append(workspace)

from day06.function_adv import *
print(add(3, 5))

# go = cp.Student("고길동", "남자", "회사원")
# go.print_info()
