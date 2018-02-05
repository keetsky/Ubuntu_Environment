http://ookamiantd.top/2017/build-blog-hexo-advanced/#好玩的样式



打开/themes/next/layout/_partials/head.swig文件，添加如下代码：

<script src="//cdn.bootcss.com/pace/1.0.2/pace.min.js"></script>
<link href="//cdn.bootcss.com/pace/1.0.2/themes/pink/pace-theme-flash.css" rel="stylesheet">

但是，默认的是粉色的，要改变颜色可以在/themes/next/layout/_partials/head.swig文件中添加如下代码（接在刚才link的后面）

<style>
    .pace .pace-progress {
        background: #ff009e; /*进度条颜色*/
        height: 3px;
    }
    .pace .pace-progress-inner {
         box-shadow: 0 0 10px #ff009e, 0 0 5px #ff009e; /*阴影颜色*/
    }
    .pace .pace-activity {
        border-top-color: #ff009e;    /*上边框颜色*/
        border-left-color: #ff009e;    /*左边框颜色*/
    }
</style>
