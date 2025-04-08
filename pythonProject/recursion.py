import os

def test_os():
    # 列出文件夹下的内容
    print(os.listdir("C:/baidunetdiskdownload/test"))
    # 判断是不是文件夹
    print(os.path.isdir("C:/baidunetdiskdownload/test/aaa"))
    # 判断路径是否存在
    print(os.path.exists("C:/baidunetdiskdownload/test"))


def get_files_recursion_from_dir(path):

    print(f"当前判断的是:{path}")
    file_list=[]
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path=path+"/"+f
            if os.path.isdir(new_path):
                file_list +=get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录{path},不存在")
        return []

    return file_list




if __name__=="__main__":
    print(get_files_recursion_from_dir("C:/baidunetdiskdownload/test"))