## 170827 - 170909 [3w4w]Chap3 learning record

### 170827 [3w0d]

* PM 2：00 - 3：00 练习 ["笨办法"学Python](https://book.douban.com/subject/26264642/) ex47 内容，主题为单元测试。
* PM 3：30 - 7： 00 （中间吃饭 30 分钟）浏览 Chap3 卡包，学习基础知识，展开任务预备阶段。

  做法：
  
  1. 练习 ex47, 照着前面 ex46 基本没什么难度，只是简单地看了一些关于 python 测试的文章，还是没理解到底为什么发生！
  2. 学习 Chap3 基础内容，卡包里又涌现出了许多名词，如 MVC、Flask，HTML，HTTP，web Framework，WSGI，CSS……
   
       我先浏览了一些文章，然后梳理一下它们之间的逻辑关系。
       
       
### 170828 [3w1d]

* AM 5：30 - 7：00 浏览网页，学习 HTTP 语言和 WSGI 相关内容。
* PM 6：30 - 9：00 浏览网页，学习 WSGI 和 Flask，练习 [WSGI接口 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432012393132788f71e0edad4676a3f76ac7776f3a16000) 及 [使用Web框架 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432012745805707cb9f00a484d968c72dbb7cfc90b91000) 内容，调用成功。

    感受：Chap3 涉及的知识点比较多，对于从未接触过的我来说都需要从零开始，今天又接触到了几个新的名词，scoket、CGI……
    
    To do list:
    
    1. 弄清楚 web 开发中接触到的名词的抽象关系。
    2. 弄清楚 environment 是什么，有什么内容。（它的类型好像是个字典。）
    3. 在写程序之前，先写一个程序使用说明。
    
### 170829 [3w2d]

* AM 6：00 - 7：10 找一些网页上的实例来了解 Flask。
* PM 4：30 - 8：30 （中间吃饭 30 分钟）从头学习 [Flask Web开发：基于Python的Web应用开发实战](https://book.douban.com/subject/26274202/)，希望对 Flask 能有系统了解。

    ##### 感受：
    
     做前两周任务的时候总是想着先把任务完成，然后再好好学习，但是发现任务完成之后学习的动力不强了。同时由于只顾着完成任务，对代码的理解不够深，若是应用到其他的地方，恐怕不是从零开始也要从零点一开始了。再加上，这周的知识牵连太多，太复杂，因此希望从笨方法开始让自己对于 Web 世界能够破门而入。
     
     ##### 今日收获： 折腾了三个小时之后，再加上昨天的学习，能够自己默写最基本的 Flask 程序。
     
     * 收获清单
     
     1. python「虚拟环境」([Python虚拟环境（pyvenv、virtualenv） – WTF Daily Blog](http://blog.topspeedsnail.com/archives/5618))
     2. 装饰器 ([装饰器 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000))
     3. 复习构造函数 （[Python中的__name__和__main__含义详解 – 在路上](https://www.crifan.com/python_detailed_explain_about___name___and___main__/)）

     * 输出清单
     
     四张图片形式的操作记录
     
     ![](http://wx2.sinaimg.cn/large/6a959c93ly1fj0wgndz7aj20mw0m0to5.jpg)
     
     ![](http://wx4.sinaimg.cn/large/6a959c93ly1fj0wjt2npyj20mw0megxk.jpg)
     
     ![](http://wx4.sinaimg.cn/large/6a959c93ly1fj0wjqyr26j20mw0ot48l.jpg)
     
     ![](http://wx2.sinaimg.cn/large/6a959c93ly1fj0wjrda8fj20lv0k5wt5.jpg)
    
### 170830 [3w3d]

* AM 5：45 - 7：00 学习 [Flask Web开发：基于Python的Web应用开发实战](https://book.douban.com/subject/26274202/) 中Jinja2 模板，了解 Flask-Bootstrap。

### 170830 [3w4d]

* AM 6：00 - 7：00 了解数据库，下载 mySQL。
* PM 7：00 - 9：30 安装 mySQL，并做笔记。

 参考资料：[Mac下安装mysql服务及基于workbench的使用方法 - 孟飞阳](https://my.oschina.net/u/2391658/blog/716741)
 
 [Mac下安装与配置MySQL - 简书](http://www.jianshu.com/p/a8e4068a7a8a)
 
 这篇文章已经写得很详尽了，安装和配置足够用。我来记录一下自己遇到的坑：
 
 1. 安装结束，配置环境变量，为了能够在终端使用命令来操作数据库。
 
             cd~
             vim .bash_profile
        在.bash_profile文件中输入：
        
            export PATH=${PATH}:/usr/local/mysql/bin
            
        用 i 键 INSERT 输入，结束后按 esc 保存，然后在命令行输入 :wq!(冒号、w、q、叹号)。
        
        然后输入
        
            source .bash_profile
            vim ~/.zshrc
            
        在.zshrc文件中输入：export PATH=${PATH}:/usr/local/mysql/bin
        
            source ~/.zshrc 
            
     ![](http://wx2.sinaimg.cn/large/6a959c93ly1fj39gy23oaj20mw0tudzd.jpg)       
            
     ![](http://wx3.sinaimg.cn/large/6a959c93ly1fj39hqw3inj20vq0k40z8.jpg)
     
            
    2. 重设密码
    
        在命令行输入（5.7.6 以后的版本）
        
            ALTER USER ‘root’@’localhost’ IDENTIFIED BY ‘新密码’；
          
        注意要输入分号（;），SQL 语句以分号(;)为结束标识。
        
        设置成功后显示
        
            Query OK, 0 rows affected (0.01 sec)
            
### 170901[3w5d]

* AM 5：30 - 7：00 重新看课程卡包，组织学习要点。
* PM 6：00 - 9：30 重新做[Flask Web开发：基于Python的Web应用开发实战](https://book.douban.com/subject/26274202/)。

  感受： 各个知识点是如何衔接的呢？比如 python 脚本如何做成 Web。
  
### 170902 [3w6d]

* PM 4：00 - 10：00 做[Flask Web开发：基于Python的Web应用开发实战](https://book.douban.com/subject/26274202/)

   感受：学了一堆，但任务没有进展，卡住了不知道如何实现任务。有点儿着急啦
   
### 170903 [4w0d]

因工作，需要出人一天，昨天晚上把要看的内容都存到 kindle 里，内容包括：

1.  HTTP 的 POST 和 GET 方法。
2. flask 对数据的接收和传送。

晚上浏览 [世界是数字的](https://book.douban.com/subject/24749903/) 第 9 章互联网和第 10 章万维网的内容。

然而，还是不知道怎么做任务！！！

### 170904 [4w1d]

* AM 5：30 - 7：00 
* PM 8：00 - 10：50  重新梳理一下知识点，主要是 flask 的工作原理和 WGSI。

感受：稍微有一些思路，明天早晨开始实践。

### 170904 [4w2d]

* AM 5：30 - 7：00 
* PM 4：00 - 9：00  写程序，剩下 history 的部分卡住了。

感受：艰难！

            
      
 
      


   