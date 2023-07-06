# 모듈 호출
import re
import math

# 약수 함수
def divisor(num):
    num = abs(num)
    divisors = []

    for i in range (1, num+1):
        if num%i==0:
            divisors.append(i)
            divisors.append(-i)

    return divisors  
# 근 구하기(근의 공식)
def root2(a,b,c):
    roots=[]
    roots.append(-b+(math.sqrt((b**2)-4*a*c)))
    roots.append(-b-(math.sqrt((b**2)-4*a*c)))
    return roots

# 근 구하기 (조립제법)
def root1(a,b,c,d,e):
    roots=[]
    for i in range (0,len(d),1):
        for j in range (0,len(e),1):
            x=(e[j]/d[i])
            if ((a*(x**2))+(b*x)+c)==0:
                roots.append(x)
    if roots==[]:
        print("이 방정식의 근을 조립제법으로 구할 수 없습니다.\n근의 공식을 사용하여 근을 구합니다.")
        print(root2(a,b,c))
    else:  
        return (roots)  

# (이차방정식) 계수 함수
def extract_coefficients(equation):
    quadratic_regex = r"([+-]?\d*)x\^2"
    linear_regex = r"([+-]?\d+)x(?![\^])"
    constant_regex = r"([+-]?\d+)=0$"
    
    quadratic_coefficient = re.search(quadratic_regex, equation)
    linear_coefficient = re.search(linear_regex, equation)
    constant_term = re.search(constant_regex, equation)
    
    a = int(quadratic_coefficient.group(1).replace('-', '') or '1') if quadratic_coefficient and quadratic_coefficient.group(1) else 1
    b = int(linear_coefficient.group(1).replace('-', '') or '1') if linear_coefficient and linear_coefficient.group(1) else 1
    c = int(constant_term.group(1)) if constant_term and constant_term.group(1) else 0
    
    return (a, b, c)

# 근 판별
def d(a,b,c):
    flag=0
    if ((b**2)-4*a*c)>0:
        print("이 방정식은 두 실근을 갖습니다.")
        flag=flag+1
    elif ((b**2)-4*a*c)==0:
        print("이 방정식은 중근인 실근을 갖습니다.")
        flag=flag+1
    elif ((b**2)-4*a*c)<0:
        print("이 방정식은 두 허근을 갖습니다.")
    return flag  