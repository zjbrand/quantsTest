import re

fruit=["apple","banana","orange","pear","watermelon"]

for value in fruit:
    result=re.match("apple|pear",value)
    if result:
        info=result.group()
        print("这是我想吃的：",info)
    else:
        print("这个不想吃")

s="ijijijyuhbnu567362276$^^*(%$$&jk"

# 找出字符串中的数字
result=re.findall(r"\d", s) #r表示让\的转义失效，是普通字符的意思
print(result)

# 找出字符串中的特殊字符
result1=re.findall(r"\W", s)
print(result1)

# 找出其中的英文字母
result2=re.findall(r"[a-zA-Z]", s)
print(result2)


