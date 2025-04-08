import time
import threading


# def sing():
#     while True:
#         print("我在唱歌，啦啦啦....")
#         time.sleep(1)
#
# def dance():
#     while True:
#         print("我在跳舞，哒哒哒....")
#         time.sleep(1)
#
# if __name__=='__main__':
#     sing_thread=threading.Thread(target=sing)
#     dance_thread=threading.Thread(target=dance)
#
#     sing_thread.start()
#     dance_thread.start()

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__=='__main__':
    # 以元组形式传递参数
    sing_thread=threading.Thread(target=sing,args=("我在唱歌，啦啦啦....",))
    # 以字典形式传递参数
    dance_thread=threading.Thread(target=dance,kwargs={"msg":"我在跳舞，哒哒哒...."})

    sing_thread.start()
    dance_thread.start()

