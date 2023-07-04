# 모듈 호출
import sys
import re

# 파이썬을 이용한 방정식의 해결
print("SFR: Subject-Fusion Research for School")
print("이 프로그램은 계수가 정수인 2~4차 방정식만 해결이 가능합니다.")
print(
    """
[1] 이차방정식
[2] 삼차방정식
[3] 사차방정식
[4] 도움말
[5] 나가기
    """
)

while True: 
      try:
            check=int(input("원하는 항목을 입력하세요. : "))
            if check>=1 and check<=4:
                  break
            elif check==5:
                  print("프로그램을 종료합니다.")
                  sys.exit()
            elif not (1<=check<=5):
                  print("값이 올바르지 않습니다. 다시 시도해 주세요.")
      except ValueError:
            print("Error: ValueError\n다시 시도해 주세요.")
# 이차방정식 해결함수
def extract_coefficients(equation):
    # 이차방정식에서 각 항의 계수를 추출하는 함수
    # 예시: 2x^2 + 3x - 5 = 0 -> (2, 3, -5)
    
    # 이차항, 일차항, 상수항에 해당하는 정규표현식
    quadratic_regex = r"([+-]?\d*)x\^2"
    linear_regex = r"([+-]?\d*)x(?![\^])"
    constant_regex = r"([+-]?\d+)$"
    
    quadratic_coefficient = re.search(quadratic_regex, equation)
    linear_coefficient = re.search(linear_regex, equation)
    constant_term = re.search(constant_regex, equation)
    
    a = int(quadratic_coefficient.group(1)) if quadratic_coefficient and quadratic_coefficient.group(1) else 1
    b = int(linear_coefficient.group(1)) if linear_coefficient and linear_coefficient.group(1) else 1
    c = int(constant_term.group(1)) if constant_term and constant_term.group(1) else 0
    
    return (a, b, c)

# 이차방정식 해결
if check==1:
      print("이차방정식을 입력해 주세요. (승수 입력: x^n, 계수와 미지수를 띄우지 마십시오)")
      equation = input("이차방정식을 입력하세요 : ")
      equation = equation.replace("^2")
      equation = equation.replace("=", "+0=")
      coefficients = extract_coefficients(equation)
      print("각 항의 계수:", coefficients)

# 삼차방정식 해결
elif check==2:
      print("삼차방정식을 입력해 주세요. (승수 입력: x^n, 계수와 미지수를 띄우지 마십시오)")
      equation=input("방정식 입력...")
# 사차방정식 해결
elif check==3:
      print("사차방정식을 입력해 주세요. (승수 입력: x^n, 계수와 미지수를 띄우지 마십시오)")
      equation=input("방정식 입력...")
# 도움말
elif check==4:
      print(
            """
- 방정식을 입력하실 때 계수가 0인 항이 있더라도 생략하지 마십시오.
- 방정식을 입력하실 때 (equation)=0 의 형태로 작성하십시오.
- 각 항의 미지수가 다를 경우 올바른 결과가 도출되지 않습니다.
            """
      )
