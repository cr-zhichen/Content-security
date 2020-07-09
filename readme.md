# 利用阿里云API完成的鉴黄服务

## 程序说明

调用阿里云内容安全API实现图片的鉴黄功能  
需要开通阿里云`阿里云图片智能鉴黄`功能  
[阿里图片智能鉴黄](https://vision.aliyun.com/experience/detail?spm=a211p3.14471183.J_7240705510.24.1f501aa1cnSEa6&tagName=imageaudit&children=IdentifyPorn)  

![阿里图片智能鉴黄](https://www.chengrui.xyz/images/2020/07/09/Snipaste_2020-07-09_13-45-31.png)

## 运行版本

Python 3.7.4 64-bit  

## 所需库

```(python)
pip install aliyun-python-sdk-core
pip install aliyun-python-sdk-imageaudit
```

## 运行注意

请将`accessKeyId，accessSecret`变量赋值为你的阿里云AccessKey  
![变量赋值](https://www.chengrui.xyz/images/2020/07/09/Snipaste_2020-07-09_13-53-30.png)  
请确保开通`阿里云图片智能鉴黄`功能  
**暂时不支持本地路径图片上传鉴黄**  
**注意:请勿在任何地方透露你的阿里云AccessKey**  

## 运行截图

![运行截图](https://www.chengrui.xyz/images/2020/07/09/Snipaste_2020-07-09_13-50-31.png)
