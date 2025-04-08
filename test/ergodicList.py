name_list=['Tom','Lily','Rose']
# i=0
# while i<len(name_list):
#     print(name_list[i])
#     i+=1

# for aa in name_list:#代碼量少於while
#     print(aa)

#列表嵌套
# name_embList=[['小明','小紅','小綠'],['Tom','Lily','Rose'],['張三','李四','王五']]
# print(name_embList)
# print(name_embList[0])#拿子列表序列
# print(name_embList[1][1])#Lily

#案例：八位老師，三個辦公室，隨機分配到三個辦公室
import random
teachers=['aa','bb','cc','dd','ee','ff','gg','hh']
offices=[[],[],[]]

for name in teachers:
    #追加有appand(不會拆開字符，選用) extend insert
    num=random.randint(0,2)
    offices[num].append(name)
#print(offices)
i=1
for room in offices:
    print(f'辦公室{i}的人數是{len(room)}')
    i+=1
    for name in room:
        print(f'{name}')

#tuple數據是不能修改的



