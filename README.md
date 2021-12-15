# freshStudyTime
全自动刷学习时长工具

适用于aq.fhmooc.com


# 使用方法
1、下载源码，或者下载release中我已经编译好的二进制版本，记得要一并下载config.txt配置文件，将两个文件放在同一目录下。
<br/>2、访问https://aq.fhmooc.com/home 登录自己的账号
<br/>3、访问https://aq.fhmooc.com/knowStudy/amifawcspkfh3ziyldznq 点击下面任意一项课程，进入学习界面
<br/>4、按f12打开开发者工具，选择网络选项卡，如果没有内容就刷新下学习页面
<br/>5、找到方法为POST，文件名为statStuProcessCellLogAndTimeLong的一项查看详细信息，在请求头中找到cookie和referer，复制以上所述参数后面的内容到config.txt中对应的位置。
<br/>6、运行工具后稍等片刻，访问https://aq.fhmooc.com/stu/myStudy 进入个人中心检查累计学习时长。
