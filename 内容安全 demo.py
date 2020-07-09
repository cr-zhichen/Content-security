#!/usr/bin/env python
# coding=utf-8

import re

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkimageaudit.request.v20191230.ScanImageRequest import ScanImageRequest

#############################################################
# 请输入阿里云accessKeyId & accessSecret

accessKeyId = 'accessKeyId'
accessSecret = 'accessSecret'

if accessKeyId == accessKeyId or accessSecret == accessSecret:
    print('请输入AccessKeyId')
    accessKeyId = input("")

    print('请输入AccessSecret')
    accessSecret = input("")


#############################################################

print('请输入所需判断图片安全性的链接')
ImageURL = input("")

#############################################################
# 调用阿里云API判断

try:
    client = AcsClient(accessKeyId,
                       accessSecret,
                       'cn-shanghai')

    request = ScanImageRequest()
    request.set_accept_format('json')

    request.set_Scenes(["porn"])
    request.set_Tasks([
        {
            "ImageURL": ImageURL
        }
    ])

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    # print(str(response, encoding='utf-8'))

    strReponse = (str(response, encoding='utf-8'))

    # print("\n"+strReponse)

except:
    strReponse = "请输入正确的链接"
    print("\n"+strReponse)


#############################################################
# 定义切片位置

S1 = 0
S2 = 0

R1 = 0
R2 = 0

#############################################################
# 函数查找切片位置


def Xiabiao(str, int):
    n = strReponse.find(str)

    i = 1  # 设置一个计数值

    # 当find查找到要统计下标的字符时，返回字符所在下标，直到统计没有这个字符时，返回的下标为-1。
    while n != -1:

        # print("第", i, "个str的下标为", n)

        int = n

        # 计数累加
        i = i+1

        # 从上一次统计到的下标+1的位置开始，继续统计的下标
        n = strReponse.find(str, n+1)
    return int

#############################################################
# 替换文字以及输出


S1 = Xiabiao("\"Suggestion", S1)
S2 = Xiabiao(",\"Rate", S2)

R1 = Xiabiao("\"Rate", R1)
R2 = Xiabiao(",\"Label", R2)


print('---------------------------------------------'+'\n'+'检测结果：')

newstr = strReponse[S1:S2]+"\n"+strReponse[R1:R2]+"%"

newstr = newstr.replace('\"Suggestion\"', '内容安全性')
newstr = newstr.replace('\"pass\"', '安全')
newstr = newstr.replace('\"review\"', '不确定')
newstr = newstr.replace('\"block\"', '违规')

newstr = newstr.replace('\"Rate\"', '概率')

if len(newstr) <= 2:
    newstr = "Erro"+"\n"+"若链接与阿里云AccessKey输入正确请尝试重试"

print(newstr+'\n---------------------------------------------')
