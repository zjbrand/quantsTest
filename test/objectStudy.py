#1.建立一個類，函數在其中能實現一定功能，此時叫做對象方法（實例方法），必須由此類中的對象來調用
# class Washer():
#     def wash(self):#self的地址和調用對象的地址是一樣的，self就是接收對象地址
#         print('能洗衣服')
#         print(self)
#
#
# #2.創建對象
# haier1=Washer()
# haier2=Washer()
#
# #3.調用類方法
# haier1.wash()
# haier2.wash()#打印地址不同，説明self接受的是對象地址，不同對象不同地址
#
# #在類的外面，添加對象屬性
# haier1.width=500
# haier1.height=800
#
# print(f'haier1洗衣機的寬度是{haier1.width}')
# print(f'haier1洗衣機的寬度是{haier1.height}')


# class Washer1():
#     def wash_print(self):
#         # 類裏面獲取實例屬性
#         print(f'洗衣機的寬度是{self.width}')
#         print(f'洗衣機的高度是{self.height}')
#
# xiaomi=Washer1()
#
# xiaomi.width=600
# xiaomi.height=900
#
# xiaomi.wash_print()

#魔法方法：__xx__()的函數方法
#__init__()方法的作用：初始化對象

# class Washer():
#     def __init__(self):#類中定義屬性
#         self.width=500
#         self.height=800
#     def print_info(self):
#         print(f'洗衣機的寬度是{self.width},高度是{self.height}')
#
# haier3=Washer()
# haier3.print_info()

class Wacher():
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def print_info(self):
        print(f'洗衣機的寬度是{self.width},高度是{self.height}')

haier4=Wacher(500,800)
haier4.print_info()

haier5=Wacher(700,900)
haier5.print_info()


