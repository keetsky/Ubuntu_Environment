背景的几何线条是采用的nest效果，一个基于html5 canvas绘制的网页背景效果，非常赞！来自github的开源项目canvas-nest

特性

不依赖任何框架或者内库，比如不依赖jQuery，使用原生的javascript。
非常小，只有1.66kb，如果开启gzip，可以更小。
非常容易实现，配置简单，即使你不是web开发者，也能简单搞定。
使用非常简单

color: 线条颜色, 默认: ‘0,0,0’ ；三个数字分别为(R,G,B)，注意用,分割
opacity: 线条透明度（0~1）, 默认: 0.5
count: 线条的总数量, 默认: 150
zIndex: 背景的z-index属性，css属性用于控制所在层的位置, 默认: -1
eg :


<script type="text/javascript" color="255,132,0" opacity='0.6' zIndex="-2" count="99" src="//cdn.bootcss.com/canvas-nest.js/1.0.1/canvas-nest.min.js"></script>

不足: CPU占用过高

打开next/layout/_layout.swig，在</body>之前添加如下代码：

{% if theme.canvas_nest %}
<script type="text/javascript" src="//cdn.bootcss.com/canvas-nest.js/1.0.0/canvas-nest.min.js"></script>
{% endif %}


修改主题配置文件

打开/next/_config.yml，修改以下代码：

# --------------------------------------------------------------
# background settings
# --------------------------------------------------------------
# add canvas-nest effect
# see detail from https://github.com/hustcc/canvas-nest.js
canvas_nest: true
