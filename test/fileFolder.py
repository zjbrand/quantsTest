import os
#重命名:rename()
#os.rename("C:\PopMusic\Bob Dylan - Blowin' In the Wind.flac","C:\PopMusic\Bob Dylan - Blowin' In the Wind.mp3")
#os.remove('The Devil Is Alive and Well.mp3')
#os.rename('C:\PopMusic\新建文件夹19\*.flac','C:\PopMusic\新建文件夹19\*.mp3')#報錯

#os.mkdir(文件夾名)
#os.mkdir('C:\PopMusic\dd')#如果已經存在則報錯
#os.rmdir('c:\PopMusic\dd')

# fold=os.getcwd()#返回當前目錄的路徑
# print(os.getcwd())
# print(fold)#C:\Users\zj_brand\PycharmProjects\test

#chdir()改變目錄路徑
# os.rmdir("aa")
# os.mkdir('aa')
# os.chdir('aa')
# os.mkdir('bb')

#print(os.listdir())#獲取當前文件夾下的所有文件
# print(os.listdir("aa"))
#
# os.rename('aa','ab')

#改變文件夾内所有文件名：
# f='C:\PopMusic\新建文件夹21\\'
# file_list=os.listdir(f)
# print(file_list)
# for i in file_list:
#     if i.find('flac'):
#         new_name=f+i.replace('flac','mp3')
#         print(new_name)
#         old_name=f+i
#         os.rename(old_name,new_name)
# print(file_list)

flag=2#選擇執行下面哪個程序
file_list1=os.listdir()
for i in file_list1:
    if flag==1:
        new_name='Python_'+i
    elif flag==2:
        num=len('Python_')
        new_name=i[num:]
    os.rename(i,new_name)