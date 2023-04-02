# 1<=n<=10000
n=int(input('1과 10000사이의 자연수를 입력하시오.'))
for a in range(2,n):
    b=n%a
    if b==0:
        print('소수가 아닙니다.')
        break
    elif a == n-1:
        print('소수입니다.')
        break
    else:
        continue




