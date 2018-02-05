
如：
执行hexo new page "guestbook"之后，那怎么在博客中加进去呢？
找到\next\_config.yml下的memu，把guestbook加进去：

menu:
 home: /
 categories: /categories
 #about: /about
 archives: /archives
 tags: /tags
 guestbook: /guestbook

图标网站：http://fontawesome.io/icons/

在/themes/hexo-theme-next/languages/zh-Hans.yml的目录下（这里默认你使用的是简体中文，若是其他语言更改相应的yml就行），在memu下加一句即可：

guestbook: 留言

