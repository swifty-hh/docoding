from random import *
users = range(1,21) # 1부터 20까지의 숫자를 생성
users = list(users)
shuffle(users)

Champions = sample(users, 4) # 4명 당첨

print("{}".format(Champions[0])) # 1명 뽑기
print("{}".format(Champions[1:])) # 3명 뽑기
