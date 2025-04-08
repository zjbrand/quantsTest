"""
age=int(input('請輸入您的年齡：'))

if age<18:
    print(f'您輸入的年齡是{age},童工。')
elif 18<=age<=60:
#elif (age>=18) and (age<=60):
    print(f'您輸入的年齡是{age},合法。')
elif age>60:
    print(f'您輸入的年齡是{age},退休。')
"""

import random

player=int(input('請出拳：0--石頭；1--剪刀；2--手帕：'))

#computer=1
computer=random.randint(0,2)
if((player==0) and (computer==1)) or ((player==1) and (computer==2))or ((player==2) and (computer==0)):
    print('玩家獲勝，哈哈哈')
elif player==computer:
    print('平局，別走，再來一把')
else:
    print('不好意思，電腦獲勝')