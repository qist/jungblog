# jungblog

🌍
* [简体中文](README.md)*

基于`python3.8`和`Django4.0`的博客。   

## 主要功能：
- 文章，页面，分类目录，标签的添加，删除，编辑等。文章、评论及页面支持`Markdown`，支持代码高亮。
- 支持文章全文搜索。
- 完整的评论功能，包括发表回复评论，以及评论的邮件提醒，支持`Markdown`。
- 侧边栏功能，最新文章，最多阅读，标签云等。
- 支持Oauth登陆，现已有Google,GitHub,facebook,微博,QQ登录。
- 支持`Redis`缓存，支持缓存自动刷新。
- 简单的SEO功能，新建文章等会自动通知Google和百度。
- 集成了简单的图床功能。
- 集成`django-compressor`，自动压缩`css`，`js`。
- 网站异常邮件提醒，若有未捕捉到的异常会自动发送提醒邮件。
- 集成了微信公众号功能，现在可以使用微信公众号来管理你的vps了。

## 安装

## python env 环境初始化

```
python3 -m venv /apps/python/jungblog_env
# 进入虚拟环境
source /apps/python/jungblog_env/bin/activate
```
## 拉取代码

```
git clone https://github.com/qist/jungblog.git
```
mysql客户端从`pymysql`修改成了`mysqlclient`，具体请参考 [pypi](https://pypi.org/project/mysqlclient/) 查看安装前的准备。

使用pip安装： `pip install -Ur requirements.txt`

如果你没有pip，使用如下方式安装：
- OS X / Linux 电脑，终端下执行: 

    ```
    curl http://peak.telecommunity.com/dist/ez_setup.py | python
    curl https://bootstrap.pypa.io/get-pip.py | python
    ```

- Windows电脑：

    下载 http://peak.telecommunity.com/dist/ez_setup.py 和 https://raw.github.com/pypa/pip/master/contrib/get-pip.py 这两个文件，双击运行。 



## 运行

 修改`jungblog/setting.py` 修改数据库配置，如下所示：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jungblog',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'host',
        'PORT': 3306,
    }
}
```
### 创建连接数据库账号

```
mysql -uroot -p #进入mysql终端
CREATE USER 'jungblog'@'localhost' IDENTIFIED BY 'JuNgBlOg123!@#';
FLUSH PRIVILEGES;
exit #退出
```

### 创建数据库
mysql数据库中执行:
```sql
CREATE DATABASE `jungblog` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
GRANT all ON jungblog.* TO 'jungblog'@'localhost';
FLUSH PRIVILEGES;
exit #退出
```

然后终端下执行:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 创建超级用户

 终端下执行:
```bash
python manage.py createsuperuser
```

### 创建测试数据
终端下执行:
```bash
python manage.py create_testdata
```

### 收集静态文件
终端下执行:  
```bash
python manage.py collectstatic --noinput
python manage.py compress --force
```

### 开始运行：
执行： `python manage.py runserver`


浏览器打开: http://127.0.0.1:8000/  就可以看到效果了。  

## 服务器部署

本地安装部署请参考 [jungblog部署教程](https://www.tycng.com/article/2019/8/5/58.html)
有详细的部署介绍.    

本项目已经支持使用docker来部署，如果你有docker环境那么可以使用docker来部署，具体请参考:[docker部署](/docs/docker.md)



## 更多配置:
[更多配置介绍](/docs/config.md)  
[集成elasticsearch](/docs/es.md)
