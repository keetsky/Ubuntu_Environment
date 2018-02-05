每个项目下一般都有一个 README.md 文件，但是使用 hexo 部署到仓库后，项目下是没有 README.md 文件的。

在 Hexo 目录下的 source 根目录下添加一个 README.md 文件，修改站点配置文件 _config.yml，将 skip_render 参数的值设置为

skip_render: README.md
保存退出即可。再次使用 hexo d 命令部署博客的时候就不会在渲染 README.md 这个文件了。

作者：Moorez
链接：http://www.jianshu.com/p/f054333ac9e6
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
