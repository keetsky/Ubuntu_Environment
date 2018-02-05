安装插件:$ npm install --save hexo-generator-feed

blog 的config.yml修改：
# Extensions
## Plugins: http://hexo.io/plugins/
plugins: hexo-generate-feed


主题的config.yml修改：

 rss: /atom.xml



配置完之后运行：

$ hexo g
重新生成一次，你会在./public 文件夹中看到 atom.xml 文件。然后启动服务器查看是否有效，之后再部署到 Github 中。


