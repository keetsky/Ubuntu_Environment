
https://www.cnblogs.com/penglei-it/p/hexo_domain_name.html

http://www.jianshu.com/p/bfba2b7120fe
#####################
上https://wanwang.aliyun.com/购买域名
(注意：购买.top域名之后，大概6个小时之内就会生效，5之内必须对域名进行认证，超过5天没有认证域名将会被锁定。)
域名配置：
购买后进入域名与网址选项点击控制台找到云解析DNS
点击对应域名的"解析"
点击添加解析，记录类型选A或CNAME，A记录的记录值就是ip地址，github(官方文档)提供了两个IP地址，192.30.252.153和192.30.252.154，这两个IP地址为github的服务器地址，两个都要填上，解析记录设置两个www和@，线路就默认就行了，CNAME记录值填你的github博客网址。如我的是keetsky.github.io。

CNAME www 默认 keetsky.github.io    ....
CNAME @ 默认 keetsky.github.io    ....
A @ 默认 192.30.252.153    ....
A @ 默认 192.30.252.154    ....

这些全部设置完成后，此时你并不能要申请的域名访问你的博客。接着你需要做的是在hexo根目录的source文件夹里创建CNAME文件，不带任何后缀，里面添加你的域名信息，如：keetsky.com。实践证明如果此时你填写的是www.keetsky.top那么以后你只能用www.keetsky.top访问，而如果你填写的是keetsky.top。那么用www.keetsky.top和keetsky.top访问都是可以的。重新清理hexo,并发布即可用新的域名访问。
或者
直接在github博客项目中setting->Custom domain 中填入keetsky.top

修改站点配置文件，把站点地址更新成新的绑定的域名即可
url: http://keetsky.top
#####################
搭建完成访问出现404 可能的原因是：

绑定了个人域名，但是域名解析错误。
域名解析正确但你的域名是通过国内注册商注册的，你的域名因没有实名制而无法访问。
你认为配置没有问题，那么可能只是你的浏览器在捣鬼，可尝试清除浏览器缓存再访问或者换个浏览器访问。
也有可能是你的路由器缓存导致的错觉，所以也可以尝试换个局域网访问你的网站。
最有可能的原因是你下载的hexo有问题，导致所有的东西都上传到了github,而导致index页面在主域名的下一级目录。你可以尝试查看上传的内容，找到index页面，在域名后面添加下一级目录。若能访问index页面（此时样式可能是乱的），则证明是hexo安装有问题，笔者当时遇到的就是这个问题。可卸载重新安装。
注：1，2默认你的CNAME文件配置没有问题，如果没有绑定个人域名，则不需要CNAME文件。
