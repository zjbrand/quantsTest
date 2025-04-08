#打開：open()，讀寫read()，關閉文件close()
#打開：open(name,mode)  name是文件名，可以加具體路徑。
#mode是訪問模式,主要有只讀r、寫入w、追加a,後面可加b和+,b表示2進制，+表示可讀可寫
#r,w 的文件指針都在文件頭部，a的文件指針在結尾
# f=open('test.txt','w')#w表示write,f就是打開的文件對象,沒有的話會在同級目錄下創建
# f.write('bbb')#會替代原有内容
# # f.write('bbb')
# # f.write('bbb')
# f.close()#Process finished with exit code 0 表明過程結束，生成的文件test.txt中寫入了aaa

#訪問模式對文件的影響，對write的影響，是否可以省略
# f=open('test.txt','r')#如果文件不存在報錯
# #f.write('aa')#報錯，r只讀方式，不支持寫入
# f.close()

f=open('test1.txt','a')#追加如果文件不存在則建立文件
f.write('xyz')#保留原來内容追加新内容
f.close()

#f=open('100.txt')#報錯，如果省略訪問模式，則默認為'r'

f=open('test.txt','r')
#print(f.read())#顯示全部
print(f.read(10))#顯示10個字節，最後有一個\n換行
f.close()

f=open('test.txt')
content=f.readlines()
print(content)#['aaaa\n', 'bbbb\n', 'cccc\n', 'dddd\n', 'eeee']連同回車作爲列表形式返回
f.close()

# f=open('test.txt')
# content=f.readline()
# print(f'第一行内容：{content}')
#
# content=f.readline()
# print(f'第二行内容：{content}')
# f.close()

# # f=open('test.txt','r+')
# # f=open('test.txt','w+')#w下如果不帶write則寫入空，文件内容被清空
# f=open('test.txt','a+')#指針在文件尾部，從文件結尾讀不出數據，也是什麽也不顯示
# con=f.read()
# print(con)
# f.close()

#seek(偏移量，起始位置)用來移動文件指針，起始位置：0文件開頭，1當前位置，2文件結尾
# f=open('test.txt','r+')
# #f.seek(2,0)#前兩個字符因爲偏移而沒有讀
# f.seek(0,2)#因指針在最後，讀不出數據
# con=f.read()
# print(con)
# f.close()

# f=open('test.txt','a+')#因追加的指針在最後，讀不出數據
# con=f.read()
# print(con)
# f.close()

f=open('test.txt','a+')
f.seek(0,0)#因把指針放到最前，可以讀出數據，也可以寫成seek(0)
con=f.read()
print(con)
f.close()

#文件備份，接受文件名
old_name=input('請輸入備份文件名：')

#規劃文件名，（1）提取後綴，名字和後綴分離
index=old_name.rfind('.')
#print(index)
#切片[開始：結束：步長]
# print(old_name[:index])
# print(old_name[index:])

#（2）組織新名字=原名字+[備份]+後綴
if index>0:#防止出現.txt的情況
    postfix=old_name[index:]
#new_name=old_name[:index]+'[備份]'+old_name[index:]
new_name=old_name[:index]+'[備份]'+postfix
print(new_name)

#(3)打開兩個文件，讀取元文件，寫入到新文件中，關閉兩個文件
old_f=open(old_name,'rb')#二進制只讀模式打開
new_f=open(new_name,'wb')
#如果不確定目標文件大小，應該用循環分次讀取，防止一次讀取過大，造成超過内存的情況
while True:
    con=old_f.read(1024)
    if len(con)==0:
        break
    new_f.write(con)
old_f.close()
new_f.close()





