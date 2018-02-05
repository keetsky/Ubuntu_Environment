
npm install hexo-all-minifier --save

之后执行hexo g就会自动压缩
但这有一个缺点，就是本地运行也就是执行hexo s之后浏览器打开本地项目会很慢，原因是每次点击一个链接它就会重新压缩一次，所以建议本地调试的时候把项目根目录下的package.json中的"hexo-all-minifier": "0.0.14"先删掉再调试,或者改成注释：

"dependencies": {
    .
	.
	.
    "hexo-server": "^0.2.0",
    "hexo-wordcount": "^2.0.1",
    "this-is-compress-plugin": {
      "hexo-all-minifier": "0.0.14"
    }
其实也没必要压缩代码，牺牲了性能，每次生成静态文件都太慢了，得不偿失的感觉
