if False:
    print('條件成立執行的代碼1')
    print('條件成立執行的代碼2')

print('條件成立執行的代碼3')
#縮進的代碼在if的管理範圍，頂格的代碼不在if管理中

age=int(input('請輸入您的年齡：'))
if age>=18:
    print(f'您輸入的年齡是{age},已經成年，可以上網')
else:
    print(f'您輸入的年齡是{age},小朋友，回家寫作業去！')

print('系統關閉')