# 모듈 호출
import sys
import functions 
import numpy as np
import matplotlib.pyplot as plt

# 파이썬을 이용한 방정식의 해결
print("SFR: Subject-Fusion Research for School")
print("자동 조립제법 계산기")
print(
    """
[1] 이차방정식
[2] 이차함수 그리기
[3] 나가기
    """
)

while True: 
      try:
            check=int(input("원하는 항목을 입력하세요. : "))
            if check==1 or check==2:
                  break
            elif check==3:
                  print("프로그램을 종료합니다.")
                  sys.exit()
            elif not (1<=check<=3):
                  print("값이 올바르지 않습니다. 다시 시도해 주세요.")
      except ValueError:
            print("Error: ValueError\n다시 시도해 주세요.")

# 이차방정식 해결
if check==1:
      print("이차방정식을 입력해 주세요. (승수 입력: x^n, 계수와 미지수를 띄우지 마십시오)")
      equation = input("이차방정식을 입력하세요 : ")
      a,b,c = functions.extract_coefficients(equation)
      print(a,b,c)
      if functions.d(a,b,c)==0:
            print("조립제법이 불가합니다.")
            sys.exit()
      ad = functions.divisor(a)
      cd = functions.divisor(c)
      print(functions.root1(a,b,c,ad,cd))

if check==2:
      print("이차함수 식을 입력해 주세요. (승수 입력: x^n, 계수와 미지수를 띄우지 마십시오.)")
      function = input("이차함수 식을 입력하세요 :")
      a,b,c = functions.extract_coefficients(function)
      x=np.linspace(-10,10,100)
      y=(a*(x**2))+(b*x)+c
      plt.plot(x,y,color='darkviolet',)
      plt.xlabel('x')
      plt.ylabel('y')
      plt.title('Quadratic Function')
      plt.grid(True, which='both')
      plt.show()