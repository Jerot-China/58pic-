#############项目功能
基于scrapy框架，爬取58pic网站的图片地址和名称

#############准备工作
安装scrapy最新版本
python3.6+
安装Mysql数据库
新建数据库picsp
新建表pic,建表语句如下
create table pic(id int not null auto_increment primary key,name char(100),url char(255))

根目录下指令输入 scrapy crawl picspd 运行程序