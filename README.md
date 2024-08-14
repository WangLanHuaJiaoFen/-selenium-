## 前言
西安电子科技大学大二下学期有一门课叫做思想政治理论实践课，这门课要求学生收集至少**800份**问卷星问卷(ノへ￣、)，诗人握持(￣_,￣ )
本着之前学过一点selenium，并且发现问卷星问卷只不过是一个网页，并且问卷可以设置每个人可以填无数份，于是就想着用selenium写一个刷问卷星脚本。

## 注意
该脚本只针对**只有多选**的问卷，如果有其他需求，请直接在github向我提issue[王兰花椒粉](https://github.com/WangLanHuaJiaoFen)

## 环境要求
Python                    3.11.8
urllib3                   2.2.2
selenium                  4.23.1
pyinstaller               6.10.0

可以直接用pip/conda进行安装对应版本的包。

## Get Started
- [点击进入仓库]()
- 获取你问卷的url：微信扫码打开你们的问卷，右上角三个点选择在浏览器打开，打开后复制问卷链接。
- ![Alt text](image.png)
  在代码这一行的引号中写入你问卷的url
- 然后直接运行即可(如果没有谷歌的webdriver，可以在网上找个教程配一下，注意安装对应版本的chromedriver)。

## 关于实现自动化运行
由于不理解问卷星反爬机制，网上的反爬教程也是老到掉毛了，所以这里只介绍一种实现自动化运行的方法。
- windows
  - 安装pyinstaller，在命令行对应环境中输入`pip install pyinstaller`
  - 安装好后在代码文件夹中运行
    ```bash
        pyinstaller -F -w 文件名.py
    ```
  - 最后生成的可执行文件在dist文件夹中，直接运行即可。
- linux
  - 基本步骤和windows一致，不过参数方面有些许不同，可自行查找资料。

## 设置定时任务
- windows
  - win+r打开运行，输入`taskschd.msc`，回车。
  - ![Alt text](image-1.png)点击创建任务
  - ![Alt text](image-2.png)输入名称，选择最高权限运行
  - ![Alt text](image-3.png)新建触发器
  - ![Alt text](image-4.png)按照图示勾选
  - ![Alt text](image-5.png)新建操作
  - ![Alt text](image-6.png)在这里点击浏览，选择你生成的可执行文件
  - 最后点击确定即可。

- linux
  - linux下设置定时任务比较简单，直接在命令行中输入`crontab -e`，然后按照提示操作即可。
  - ![Alt text](image-7.png)这里给出我设置的定时任务，*/2表示每两分钟执行一次。/home/rongrong/PycharmProjects/pc_wjx/dist/p1c即为可执行文件的路径，p1c为我的可执行文件。后面的表示输入日志文件，可自行修改或者不写即可。
  - 设置完后在终端输入
    ```bash
    crontab -l # 查看定时任务列表
    sudo systemctl start cron # 开始执行定时任务
    sudo systemctl enable cron # 设置开机自动启动定时任务
    ```

## 结语
如果这篇文章对你有帮助，欢迎star/fork(๑•̀ㅂ•́)و✧
如果有其他需求或者发现bug，欢迎issue/prヽ(✿ﾟ▽ﾟ)ノ
如果懒得动手，你可以在issue中给我问卷url和联系方式，我把可执行文件直接发给你♪(^∇^*)
