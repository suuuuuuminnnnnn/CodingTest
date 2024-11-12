# 첫 숫자는 몇번 할 껀지
# 그러고 각 테스트 케이스에 대해 마지막 데이터가 처리되는 컴퓨터 번호 출력
''' 예제 입력   예제 출력
5               1
1 6             7
3 7             6
6 2             1
7 100           9
9 635
'''

'''

n = int(input())

l = [5]
for i in range(n):
    a, b = map(int, input().split())
    if a > 10:
        a = a % 10
    if b > 10:
        b = b % 10
    if a > b:
        l[i] = a
    else:
        l[i] = b

for i in range(5):
    print(l[i])
'''

n = int(input())  # 테스트 케이스의 수 입력

for _ in range(n):
    a, b = map(int, input().split())
    a = a % 10 if a % 10 != 0 else 10  # 10으로 나눈 나머지가 0이면 10으로 처리
    result = pow(a, b, 10)  # a^b의 마지막 자릿수 구하기
    print(result if result != 0 else 10)  # 0이면 10번 컴퓨터로 처리
