一、功能部分
1. 用户注册、登录、退出功能
2. 上传和修改头像的功能
3. 访问头像API的功能，即根据用户名查询头像

二、数据库的配置

三、apache的配置
1.添加模块LoadModule wsgi_module modules/mod_wsgi.so，并打开Include conf/extra/httpd-vhosts.conf
2.虚拟主机的配置文件为
<VirtualHost *:80>
    ServerName localhost

    DocumentRoot "/home/fangjian/workspace/netease"
    ErrorLog "/usr/local/apache/logs/avatar_errors.log"


    WSGIScriptAlias /  "/home/fangjian/workspace/netease/avatar.py/"
    Alias /static "/home/fangjian/workspace/netease/static/"
    AddType text/html .py

    <Directory "/home/fangjian/workspace/netease">
        AllowOverride None
        Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch -Indexes
        Require all granted

    </Directory>

</VirtualHost>
3.配置好项目所在目录的权限，比如：session目录和upfile目录要具有写的权限，其它的目录要具有执行权限等	
