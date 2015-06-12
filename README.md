功能部分
========
        * 用户注册、登录、退出功能<br/>
        * 上传和修改头像的功能<br/>
        * 访问头像API的功能，即根据用户名查询头像<br/>
数据库的配置
============
    1.创建好数据库的用户名、密码和数据库名字后，把信息添加到setting.py中.<br/>
    2.执行account.sql脚本文件创建数据库和用户信息表，具体内容为：<br/>
    >CREATE DATABASE netease;
    >CREATE TABLE `account` 
    >>`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
    >>`user` varchar(20) NOT NULL, 
    >>`passwd` varchar(20) NOT NULL,
    >>`photo` varchar(100),
    >>PRIMARY KEY (`id`)
    >>) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    其中：
    id字段为主键；user字段为用户名，且不能为空；passwd字段为密码，也不能为空；<br/>
    photo字段存放的是用户头像在项目中的相对路径，用于浏览器的访问。这里的用户名没有设置为唯一，但是在注册时，通过程序查询该用户名是否存在来给出相应的响应。若已存在，则不予注册。

apache的配置
============
    1.编译并按装wsgi模块，然后添加LoadModule wsgi_module modules/mod_wsgi.so；打开Include conf/extra/httpd-vhosts.conf<br/>
    2.虚拟主机的配置文件为
    <VirtualHost *:80><br/>
    ServerName localhost<br/>

    >DocumentRoot "/home/fangjian/workspace/netease"<br/>
    >ErrorLog "/usr/local/apache/logs/avatar_errors.log"<br/>


    >WSGIScriptAlias /  "/home/fangjian/workspace/netease/avatar.py/"<br/>
    >Alias /static "/home/fangjian/workspace/netease/static/"<br/>
    >AddType text/html .py<br/>

    ><Directory "/home/fangjian/workspace/netease"><br/>
    >>AllowOverride None<br/>
    >>Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch -Indexes<br/>
    >>Require all granted<br/>

    ></Directory><br/>
    >></VirtualHost><br/>
    其中，DocumentRoot需要根据自己项目的位置加以修改<br/>
    3.配置好项目所在目录的权限，比如：session目录和upfile目录要具有写的权限，所有的目录要具有执行权限等	

项目安装
=======
    * 由apache的配置文件可以知道，项目的目录放在/home/fangjian/workspace/netease中，可以根据需要放在不同的位置，但是，apache需要相应的修改配置文件。
    * 为了使apache通过wsgi调用python代码，需要把python文件的权限加上可执行权限。创建好数据库之后，启动apache服务器，即可通过浏览器访问本项目。
代码结构
========
    * setting.py中存放的是项目的配置文件，包括：上传头像存放的路径、数据库的信息、是否是调试阶段、urls映射关系等。
    * avatar.py是项目的启动程序，apache把浏览器访问的根地址重定向到该文件，该文件再根据setting.py中的urls映射，对不同的请求调用相应的处理程序。
    * 所有的hander处理程序都在src文件夹中，其中：<br />
      * base:基类，在构造函数中添加了session验证，所有需要权限验证的类都需要继承该类，包括information、search和upload
      * register：注册，包含了两次密码是否一致以及用户名是否存在的验证
      * login：登录与退出，包含了session的添加与取消
      * db：数据库操作
      * information：显示头像等信息
      * search：访问头像API的功能，即根据用户名查询头像
      * upload：上传、修改用户头像
    * 另外，data文件夹中存放的是session信息，static文件夹中存放的是js、css以及上传的头像，templates文件夹中存放的是html模板文件。
工作流程
=======
    * 项目的入口程序是avatar.py，该文件根据urls中的映射关系，把请求重定向到src.login.Login中，在GET方法中调用login.html模块显示给用户登录。
    * 如果用户进行登录，则调用src.login.Login的POST方法进行验证，并创建一个session信息保存下来；如果选择注册，则调用src.register.Register的GET方法，把register.html模板给用户注册，然后调用其POST方法对注册进行响应，同样创建相应的session信息。
    * 登录或注册成功后，调用src.information.Information进入个人信息页面。在该类中，首先调用base类的__init__方法进行session验证，通过后从数据库读取该用户的头像信息进行显示。在该页面可以通过选择修改和查询按钮对用户的头像进行操作。
    * src.upload.Upload和src.search.Search方法分别用于上传和查询用户头像，这两个类都继承了base类，因此，在进行操作前，都会进行session权限的验证。
    * 在informaion页面中，有一个退出按钮，单击后，会调用src.login.Quit类的GET方法，在该方法中，会删除相应的session信息，并把页面重定向到登录页面。
