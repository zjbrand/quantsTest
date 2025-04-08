def info_print():
    print('請選擇功能-------------')
    print('1.添加學員')
    print('2.刪除學員')
    print('3.修改學員')
    print('4.查詢學員')
    print('5.顯示所有學員')
    print('6.退出系統')
    print('-'*20)

#等待存儲所有學員的信息
info=[]

def add_info():
    """添加學員函數"""
    new_id=input('請輸入學號：')
    new_name=input('請輸入姓名：')
    new_tel=input('請輸入電話：')
    #判斷是否添加這個學員
    global info
    for i in info:
        if new_name==i['name']:
            print('此用戶已經存在')
            return#無返回值，退出程序。

    #如果輸入的姓名不存在，添加數據
    info_dict={}
    info_dict['id']=new_id
    info_dict['name']=new_name
    info_dict['tel']=new_tel
    info.append(info_dict)
    print(info)

def del_info():
    """刪除學員"""
    del_name=input('請輸入刪除學員的姓名：')
    global info
    for i in info:
        if del_name==i['name']:
            info.remove(i)
            break
    else:
        print('該學員不存在')
    print(info)

def modify_info():
    """修改函數"""
    modify_name=input('請輸入要修改的名字：')
    global info
    for i in info:
        if modify_name==i['name']:
            i['tel']=input('請輸入要修改的電話：')
            break
    else:
        print('該學員不存在')
    print(info)

def search_info():
    search_name=input('請輸入要查找的學員姓名：')
    global info
    for i in info:
        if search_name==i['name']:
            print('查找到的學員信息如下：---------')
            print(f"該學員是{i['id']},姓名是{i['name']},手機號是{i['tel']}")
            break
    else:
        print('該學員不存在')

def print_all():
    """顯示所有學院信息"""
    print('學號\t姓名\t手機號')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")

while True:
    info_print()

    user_num=int(input('請輸入功能序號：'))
    if user_num==1:
        # print('添加')
        add_info()

    elif user_num==2:
        #print('刪除')
        del_info()

    elif user_num==3:
       #print('修改')
        modify_info()

    elif user_num==4:
       # print('查詢')
        search_info()

    elif user_num==5:
        #print('顯示所有')
        print_all()
    elif user_num==6:
        #print('退出系統')
        exit_flag=input('確定要退出嗎？(1.yes 2.no)')
        if exit_flag=='1':
            break
    else:
        print('輸入的功能序號有誤')
