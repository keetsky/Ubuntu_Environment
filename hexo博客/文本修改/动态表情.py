在这个表情横行的时代，使用emoji似乎已经是日常。之前一直搜索相关插件，安装了很多，但都失败了。后来发现直接Copy，Paste就能用😆，可以去https://www.emojicopy.com/   拷贝

1.首先编辑~/blog/themes/next/source/css/_custom/custom.styl，往里面加入：

// 自定义emoji样式
img#github-emoji {
    margin: 0;
    padding: 0;
    display: inline !important;
    vertical-align: bottom;
    border: none;
    cursor: text;
    box-shadow: none;
}
// 文章超链接样式（为emoji特设）
// color的值可以改成你博客自己的！
.post-body a {
    color: rgb(5, 147, 211);
    border-bottom: none;
    text-decoration: underline;
}
.post-body a:hover {
    color: rgb(255, 118, 0);
    border-bottom: none;
    text-decoration: underline;
}
// 标签云页面超链接样式（为emoji特设）
.tag-cloud a {
    color: rgb(5, 147, 211);
    border-bottom: 1px solid rgb(5, 147, 211);
    text-decoration: none;
}
.tag-cloud a:hover {
    color: rgb(255, 118, 0);
    border-bottom: 1px solid rgb(255, 118, 0);
    text-decoration: none;
}
// 阅读更多按钮样式（为emoji特设）
.post-button .btn {
    text-decoration: none;
    border: 1.5px solid rgb(255, 118, 0);
}
.post-button .btn:hover {
    text-decoration: none;
    border: 1.5px solid rgb(255, 118, 0);
}









####
2.然后在文章中引用：
<img id="github-emoji" src="https://assets-cdn.github.com/images/icons/emoji/unicode/1f602.png" height="20" width="20">



有点麻烦的就是找到这个emoji的图片名：

输入法输入想用的emoji直接Google到其名字，或者打开https://www.webpagefx.com/tools/emoji-cheat-sheet/ 找到emoji的名字。
然后打开https://api.github.com/emojis 快捷键搜索（Ctrl + F），输入emoji的名字，即可找到emoji的图片名。
方法是我看一个Hexo插件的https://github.com/crimx/hexo-filter-github-emojis自己摸索出来的，当然用途不止于emoji。手机里的各种表情包，传到自己的云存储，然后改下URL，看情况改下height和width的值即可啦，GIF也可以哦～

当然，还有颜文字(ﾉ*･ω･)ﾉ。








