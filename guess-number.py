import random
r = random.randint(1, 100)

while True:
    u = int(input('請猜一個1-100的數字: '))
    
    if r == u:
        print('終於猜對了！')
        break
    elif r < u:
        print('比答案大')
    elif r > u:
        print('比答案小')